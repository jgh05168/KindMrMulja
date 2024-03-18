const express = require("express");
const moment = require("moment");
const wishlist = express.Router();
const pool = require("../DB.js");

// 사용자 찜목록 불러오기
wishlist.get("/:user_id", async (req, res) => {
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
wishlist.delete("/:wishlist_id", async (req, res) => {
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

module.exports = wishlist;
