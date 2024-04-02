const express = require("express");
const moment = require("moment");
const product = express.Router();
const pool = require("../DB.js");
product.get("/hihi", (req, res) => {
  res.send("hello");
});

// 홈화면 상품리스트 전체 불러오기 api
product.get("/product-list", async (req, res) => {
  try {
    const query = `
      SELECT 
          p.product_id,
          p.product_name,
          p.product_price,
          p.product_category,
          p.product_stock,
          COUNT(w.product_id) AS wish_count

      FROM 
          product_list p
      LEFT JOIN 
          wishlist w ON p.product_id = w.product_id
      GROUP BY 
          p.product_id, p.product_name, p.product_price, p.product_category, p.product_stock
    `;
    const results = await pool.query(query);
    return res.json(results[0]);
  } catch (error) {
    console.error(error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 개별 상품 페이지 관련 api
product.get("/product-detail/:product_id", async (req, res) => {
  const product_id = req.params.product_id;
  try {
    const query = `SELECT product_name, summary, product_price, product_stock, description, width, length, height FROM product_list WHERE product_id = ?`;
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
product.post("/add-shopping-cart", async (req, res) => {
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
product.get("/check-wish-product/:user_id/:product_id", async (req, res) => {
  const user_id = parseInt(req.params.user_id);
  const product_id = req.params.product_id;

  try {
    // 해당 유저와 제품에 대한 위시리스트 항목이 이미 존재하는지 확인하는 쿼리
    const query = `SELECT * FROM wishlist WHERE user_id = ? AND product_id = ?`;
    const result = await pool.query(query, [user_id, product_id]);
    return res.json({ result: result[0].length > 0 });
  } catch (error) {
    console.error("Error executing SQL query:", error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 찜 버튼을 눌렀을때 찜 상태를 바꾸는 api
product.post("/wishlist-toggle", async (req, res) => {
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

      const decreaseWishcountQuery = `UPDATE product_list SET wishcount = wishcount - 1 WHERE product_id = ?`;
      await pool.query(decreaseWishcountQuery, [product_id]);

      return res.json({ result: false });
    } else {
      // 위시리스트에 해당 제품이 없으면 새로운 row를 추가하는 쿼리
      const insertQuery = `INSERT INTO wishlist (user_id, product_id) VALUES (?, ?)`;
      await pool.query(insertQuery, [user_id, product_id]);

      const increaseWishcountQuery = `UPDATE product_list SET wishcount = wishcount + 1 WHERE product_id = ?`;
      await pool.query(increaseWishcountQuery, [product_id]);

      return res.json({ result: true });
    }
  } catch (error) {
    console.error("Error executing SQL query:", error);
  }
});

module.exports = product;
