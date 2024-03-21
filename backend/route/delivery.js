const express = require("express");
const moment = require("moment");
const delivery = express.Router();
const pool = require("../DB.js");

// 배송지 추가하기 api
delivery.post("/delivery-address/add", async (req, res) => {
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
delivery.get("/delivery-address/list/:user_id", async (req, res) => {
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

// 기본 배송지로 선택하기
delivery.patch("/delivery-address/default-address", async (req, res) => {
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

module.exports = delivery;
