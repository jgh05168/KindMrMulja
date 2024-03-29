const express = require("express");
const moment = require("moment");
const wishlist = express.Router();
const pool = require("./DB.js");

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
    // wishlist에서 해당 wishlist_id에 해당하는 제품의 product_id 가져오기
    const selectQuery = `SELECT product_id FROM wishlist WHERE wishlist_id = ?`;
    const selectResult = await pool.query(selectQuery, wishlist_id);
    if (selectResult.length > 0) {
      const product_id = selectResult[0][0].product_id;

      // 찜리스트에서 해당 항목 삭제
      const deleteQuery = `DELETE FROM wishlist WHERE wishlist_id = ?`;
      const deleteResult = await pool.query(deleteQuery, wishlist_id);

      if (deleteResult[0].affectedRows > 0) {
        // 제품의 찜 횟수를 업데이트
        const updateQuery = `UPDATE product_list SET wishcount = wishcount - 1 WHERE product_id = ?`;
        const updateResult = await pool.query(updateQuery, product_id);
        console.log(updateResult[0]);
        if (updateResult[0].affectedRows > 0) {
          // 제품의 찜 횟수가 성공적으로 업데이트되었을 경우
          return res.json({ result: true });
        } else {
          // 제품의 찜 횟수 업데이트에 실패한 경우
          return res.json({
            result: false,
            message: "Failed to update product wishlist count",
          });
        }
      } else {
        // 찜리스트에서 삭제된 항목이 없는 경우
        return res.json({ result: false, message: "Wishlist item not found" });
      }
    } else {
      // 해당 wishlist_id에 해당하는 제품이 없는 경우
      return res.json({
        result: false,
        message: "Product not found in wishlist",
      });
    }
  } catch (error) {
    // 오류 처리
    console.error("Error delete wishlist:", error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

module.exports = wishlist;
