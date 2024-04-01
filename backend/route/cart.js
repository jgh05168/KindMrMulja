const express = require("express");
const moment = require("moment");
const cart = express.Router();
const pool = require("../DB.js");
// 사용자 장바구니 목록 불러오기
cart.get("/:user_id", async (req, res) => {
  const user_id = req.params.user_id;
  try {
    const query = `
            SELECT sc.cart_id, sc.product_id, pl.product_name, pl.product_price, sc.product_quentity, pl.product_stock
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
cart.patch("/cart-update", async (req, res) => {
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

cart.delete("/:cart_id", async (req, res) => {
  const cart_id = req.params.cart_id;

  try {
    const query = `DELETE FROM shopping_cart WHERE cart_id = ?`;
    const result = await pool.query(query, cart_id);
    if (result[0].affectedRows > 0) {
      return res.json({ result: true });
    } else {
      return res.json({ result: false });
    }
  } catch (error) {}
});

module.exports = cart;
