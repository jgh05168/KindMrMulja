const express = require("express");
const app = express();
const cors = require("cors");
const pool = require("./DB.js");
const PORT = 3000;

app.use(express.json());
app.use(cors());

app.get("/", (req, res) => {
  res.send("You need to request API");
});

// 회원가입 api
app.post("/api/users/signup", async (req, res) => {
  console.log(req.body);

  const name = req.body.name;
  const email = req.body.email;
  const password = req.body.password;

  try {
    const query = `
    INSERT INTO user (user_name, user_email, user_password) VALUES (?, ?, ?);`;
    const results = await pool.query(query, [name, email, password]);
    return res.json({ result: true });
    // console.log(result);
  } catch (error) {
    // console.log(error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 이메일 중복확인 api
app.post("/api/users/email-duplicate-check", async (req, res) => {
  console.log(req.body);
  const email = req.body.email;

  try {
    const query = `SELECT * FROM user WHERE user_email = ?`;
    const results = await pool.query(query, [email]);
    console.log(results);
    if (results.length > 0) {
      return res.json({ result: false });
    } else {
      return res.json({ result: true });
    }
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 로그인 api
app.post("/api/users/signin", async (req, res) => {
  const email = req.body.email;
  const password = req.body.password;

  try {
    const query = `
          SELECT user_id FROM user
          WHERE user_email = ? AND user_password = ?
        `;

    const result = await pool.query(query, [email, password]);
    console.log(result[0]);
    if (result[0].length > 0) {
      const user_id = result[0].user_id;
      return res.json({ user_id: user_id, result: true });
    } else {
      return res.json({ user_id: null, result: false });
    }
  } catch (error) {
    console.error(error);
    return res
      .status(500)
      .json({ result: false, error: "Internal Server Error" });
  }
});

// 홈화면 상품리스트 전체 불러오기 api
app.get("/api/product/product-list", async (req, res) => {
  try {
    const query = `SELECT product_id, product_name, product_price, product_category FROM product_list`;
    const results = await pool.query(query);
    console.log(results[0]);
    return res.json(results[0]);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 개별 상품 페이지 관련 api
app.get("/api/product/product-detail/:product_id", async (req, res) => {
  const product_id = req.params.product_id;
  try {
    const query = `SELECT product_name, product_price, description FROM product_list WHERE product_id = ?`;
    const results = await pool.query(query, [product_id]);
    if (results[0].length > 0) {
      return res.json(results[0][0]);
    } else {
      return res.status(404).json({ error: "Product Not Found" });
    }
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 장바구니에 추가 요청 api
app.post("/api/product/add-shopping-cart", async (req, res) => {
  const user_id = parseInt(req.body.user_id);
  const product_id = req.body.product_id;
  const cart_quentity = parseInt(req.body.cart_quentity);

  try {
    const query1 = `SELECT * FROM shopping_cart WHERE user_id = ? AND product_id = ?`;
    const checkResult = await pool.query(query1, [user_id, product_id]);
    if (checkResult[0].length > 0) {
      // 이미 장바구니에 해당 제품이 있으면 cart_quentity를 증가시키는 쿼리
      const updateQuery = `UPDATE shopping_cart SET cart_quentity = cart_quentity + ? WHERE user_id = ? AND product_id = ?`;
      await pool.query(updateQuery, [cart_quentity, user_id, product_id]);
    } else {
      // 장바구니에 해당 제품이 없으면 새로운 row를 추가하는 쿼리
      const insertQuery = `INSERT INTO shopping_cart (user_id, product_id, cart_quentity) VALUES (?,?,?)`;
      await pool.query(insertQuery, [user_id, product_id, cart_quentity]);
    }
    return res.json({ result: true });
  } catch (error) {
    console.error("Error executing SQL query:", error);
    return res.json({ result: false });
  }
});

// 상세 페이지에서 현재 찜 상태를 확인하는 api
app.get(
  "/api/product/check-wish-product/:user_id/:product_id",
  async (req, res) => {
    const user_id = parseInt(req.params.user_id);
    const product_id = req.params.product_id;

    try {
      // 해당 유저와 제품에 대한 위시리스트 항목이 이미 존재하는지 확인하는 쿼리
      const query = `SELECT * FROM wishlist WHERE user_id = ? AND product_id = ?`;
      const result = await pool.query(query, [user_id, product_id]);
      if (result[0].length > 0) {
        return res.json({ result: true });
      } else {
        return res.json({ result: false });
      }
    } catch (error) {
      console.error("Error executing SQL query:", error);
      return res.status(500).json({ error: "Internal Server Error" });
    }
  }
);

// 찜 버튼을 눌렀을때 찜 상태를 바꾸는 api
app.post("/api/product/wishlist-toggle", async (req, res) => {
  const user_id = parseInt(req.body.user_id);
  const product_id = req.body.product_id;

  try {
    // 해당 유저와 제품에 대한 위시리스트 항목이 이미 존재하는지 확인하는 쿼리
    const checkQuery = `SELECT * FROM wishlist WHERE user_id = ? AND product_id = ?`;
    const checkResult = await pool.query(checkQuery, [user_id, product_id]);
    console.log(checkResult[0]);
    if (checkResult[0].length > 0) {
      // 이미 위시리스트에 해당 제품이 있으면 삭제하는 쿼리
      const deleteQuery = `DELETE FROM wishlist WHERE user_id = ? AND product_id = ?`;
      await pool.query(deleteQuery, [user_id, product_id]);
    } else {
      // 위시리스트에 해당 제품이 없으면 새로운 row를 추가하는 쿼리
      const insertQuery = `INSERT INTO wishlist (user_id, product_id) VALUES (?, ?)`;
      await pool.query(insertQuery, [user_id, product_id]);
    }

    return res.json({ result: true });
  } catch (error) {
    console.error("Error executing SQL query:", error);
    return res.json({ result: false });
  }
});

// 사용자 찜목록 불러오기
app.get("/api/product/wish-list/:user_id", async (req, res) => {
  const user_id = req.params.user_id;
  try {
    const query = `
      SELECT wl.wishlist_id, wl.product_id, pl.product_name, pl.product_price
      FROM wishlist wl
      JOIN product_list pl ON wl.product_id = pl.product_id
      WHERE wl.user_id = ?;
    `;
    const results = await pool.query(query, user_id);
    console.log(results[0]);
    return res.json(results[0]);
  } catch (error) {
    console.error("Error retrieving wishlist:", error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 찜목록 삭제 api
app.delete("/api/product/wish-list-delete/:wishlist_id", async (req, res) => {
  const wishlist_id = req.params.wishlist_id;
  try {
    const query = `
    DELETE FROM wishlist WHERE wishlist_id = ?`;
    const result = await pool.query(query, wishlist_id);
    console.log(result[0]);
    if (result[0].affectedRows > 0) {
      return res.json({ result: true });
    } else {
      return res.json({ result: false });
    }
  } catch (error) {
    console.error("Error delete wishlist:", error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});
app.listen(PORT, () => console.log(`${PORT} 서버 기동중`));
