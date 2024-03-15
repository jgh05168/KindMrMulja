const express = require("express");
const app = express();
const cors = require("cors");
const pool = require("./DB.js");
const moment = require("moment");
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
    console.log(error);
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
  const product_quentity = parseInt(req.body.product_quentity);

  try {
    const query1 = `SELECT * FROM shopping_cart WHERE user_id = ? AND product_id = ?`;
    const checkResult = await pool.query(query1, [user_id, product_id]);
    if (checkResult[0].length > 0) {
      // 이미 장바구니에 해당 제품이 있으면 product_quentity를 증가시키는 쿼리
      const updateQuery = `UPDATE shopping_cart SET product_quentity = product_quentity + ? WHERE user_id = ? AND product_id = ?`;
      await pool.query(updateQuery, [product_quentity, user_id, product_id]);
    } else {
      // 장바구니에 해당 제품이 없으면 새로운 row를 추가하는 쿼리
      const insertQuery = `INSERT INTO shopping_cart (user_id, product_id, product_quentity) VALUES (?,?,?)`;
      await pool.query(insertQuery, [user_id, product_id, product_quentity]);
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

// 사용자 장바구니 목록 불러오기
app.get("/api/product/shopping-cart/:user_id", async (req, res) => {
  const user_id = req.params.user_id;
  try {
    const query = `
      SELECT sc.cart_id, sc.product_id, pl.product_name, pl.product_price, sc.product_quentity
      FROM shopping_cart sc
      JOIN product_list pl ON sc.product_id = pl.product_id
      WHERE sc.user_id = ?;
    `;
    const results = await pool.query(query, user_id);
    console.log(results[0]);
    return res.json(results[0]);
  } catch (error) {
    console.error("Error recieving shopping-cart:", error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 장바구니에서 물품 수량 변경 api
app.patch("/api/product/shopping-cart-update", async (req, res) => {
  const cart_id = req.body.cart_id;
  const product_quentity = req.body.product_quentity;

  try {
    const query = `UPDATE shopping_cart SET product_quentity = ? WHERE cart_id = ?`;
    const result = await pool.query(query, [product_quentity, cart_id]);
    console.log(result[0]);
    if (result[0].affectedRows > 0) {
      return res.json({ result: true });
    } else {
      return res.json({ result: false });
    }
  } catch (error) {
    console.error("Error updating shopping-cart:", error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 배송지 추가하기 api
app.post("/api/delivery-address/add", async (req, res) => {
  const user_id = req.body.user_id;
  const address_name = req.body.address_name;
  const user_name = req.body.user_name;
  const address_normal = req.body.address_normal;
  const address_detail = req.body.address_detail;

  try {
    const query = `INSERT INTO address_information (user_id, address_name, user_name, address_normal, address_detail, is_default) VALUES (?,?,?,?,?,?)`;
    const result = await pool.query(query, [
      user_id,
      address_name,
      user_name,
      address_normal,
      address_detail,
      0,
    ]);

    if (result[0].affectedRows > 0) {
      return res.json({ result: true });
    } else {
      return res.json({ result: false });
    }
  } catch (error) {
    console.error("Error adding delivery address:", error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 배송지 목록 불러오기
app.get("/api/delivery-address/list/:user_id", async (req, res) => {
  const user_id = req.params.user_id;
  try {
    const query = `SELECT * FROM address_information WHERE user_id = ?`;
    const results = await pool.query(query, [user_id]);
    console.log(results);
    return res.json(results[0]);
  } catch (error) {
    console.error("Error retrieving address list:", error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 배송지로 선택하기
app.patch("/api/delivery-address/default-address", async (req, res) => {
  const user_id = req.body.user_id;
  const address_id = req.body.address_id;
  try {
    const query = `SELECT address_id FROM address_information WHERE user_id = ? AND is_default = 1`;
    const result = await pool.query(query, [user_id]);
    if (result[0].length > 0) {
      const updateQuerry = `UPDATE address_information SET is_default = 0 WHERE address_id = ?`;
      await pool.query(updateQuerry, result[0][0].address_id);
    }
    const setDefaultQuerry = `UPDATE address_information SET is_default = 1 WHERE address_id = ?`;
    await pool.query(setDefaultQuerry, [address_id]);
    return res.json({ result: true });
  } catch (error) {
    console.error("Error setting default address:", error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 주문 내역 업로드 api
app.post("/api/product/order", async (req, res) => {
  const { user_id, address_id, order_type, selected_cart_id } = req.body;
  try {
    const order_date = moment().format("YYYY-MM-DD");
    const order_time = moment().format("HH:mm:ss");
    const order_datetime = `${order_date} ${order_time}`;

    const query = `INSERT INTO order_list (user_id, address_id, order_type, order_date, order_state) VALUES (?,?,?,?,?)`;
    await pool.query(query, [
      user_id,
      address_id,
      order_type,
      order_datetime,
      0,
    ]);

    const order_id = await pool.query("SELECT LAST_INSERT_ID() AS order_id");

    let total_price = 0;
    let total_quentity = 0;

    for (let i = 0; i < selected_cart_id.length; i++) {
      const query2 = `SELECT product_id, product_quentity FROM shopping_cart WHERE cart_id = ?`;
      const results = await pool.query(query2, selected_cart_id[i]);
      console.log(results[0][0].product_id);
      const query3 = `INSERT INTO order_detail_list (order_id, product_id, order_quentity, order_progress, moving_zone) VALUES (?,?,?,?,?)`;
      await pool.query(query3, [
        order_id[0][0].order_id,
        results[0][0].product_id,
        results[0][0].product_quentity,
        0,
        0,
      ]);

      const query4 = `SELECT product_price FROM product_list WHERE product_id = ?`;
      const price_result = await pool.query(query4, [results[0][0].product_id]);
      console.log(price_result[0]);
      total_quentity += results[0][0].product_quentity;
      total_price +=
        results[0][0].product_quentity * price_result[0][0].product_price;

      console.log(total_price);
      console.log(total_quentity);
    }
    console.log(order_id);
    const query5 = `UPDATE order_list SET total_price = ?, total_quentity = ? WHERE order_id = ?`;
    await pool.query(query5, [
      total_price,
      total_quentity,
      order_id[0][0].order_id,
    ]);

    // for (let i = 0; i < selected_cart_id.length; i++) {
    //   const query = `DELETE FROM shopping_cart WHERE cart_id = ?`;
    //   await pool.query(query, [selected_cart_id[i]]);
    // }

    return res.json({ result: true }); // 성공적인 응답을 반환
  } catch (error) {
    console.error("에러 발생:", error);
    return res
      .status(500)
      .json({ error: "요청 처리 중에 오류가 발생했습니다." }); // 오류 응답을 반환
  }
});

// 주문 목록 전체 보기
app.get("/api/product/order-list/:user_id", async (req, res) => {
  const user_id = req.params.user_id;
  try {
    const query = `SELECT * FROM order_list WHERE user_id = ?`;
    const results = await pool.query(query, [user_id]);
    console.log(results[0]);
    return res.json(results[0]);
  } catch (error) {
    console.error("에러 발생:", error);
    return res
      .status(500)
      .json({ error: "요청 처리 중에 오류가 발생했습니다." }); // 오류 응답을 반환
  }
});

app.get("/api/product/order-list-detail/:user_id", async (req, res) => {
  const user_id = req.params.user_id;
  try {
    const query = `SELECT odl.order_detail_id, odl.order_id, odl.order_quentity, odl.order_progress, odl.product_id
    FROM order_detail_list odl 
    JOIN order_list ol ON ol.order_id = odl.order_id 
    WHERE ol.user_id = '1'`;
    const results = await pool.query(query, user_id);

    for (let i = 0; i < results[0].length; i++) {
      const product_id = results[0][i].product_id;
      const query2 = `SELECT product_name, product_price FROM product_list WHERE product_id = ?`;
      const results2 = await pool.query(query2, product_id);

      // product_name 및 product_price 정보를 결과에 추가
      results[0][i].product_name = results2[0][0].product_name;
      results[0][i].product_price = results2[0][0].product_price;
    }
    console.log(results[0]);
  } catch (error) {
    console.log(error);
  }
});
app.listen(PORT, () => console.log(`${PORT} 서버 기동중`));
