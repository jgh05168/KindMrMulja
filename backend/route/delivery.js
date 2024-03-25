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
  const phone_number = req.body.phone_number;
  const is_default = req.body.is_default;
  try {
    const query3 = `SELECT address_id FROM address_information WHERE is_default = 1 and user_id = ?`;
    const result2 = await pool.query(query3, user_id);
    const query = `INSERT INTO address_information (user_id, address_name, user_name, address_normal, address_detail, phone_number, is_default) VALUES (?,?,?,?,?,?,?)`;
    const result = await pool.query(query, [
      user_id,
      address_name,
      user_name,
      address_normal,
      address_detail,
      phone_number,
      is_default,
    ]);

    if (result[0].affectedRows > 0) {
      const query2 = `UPDATE address_information SET is_default = 0 WHERE address_id = ?`;
      if (is_default === true) {
        await pool.query(query2, result2[0][0].address_id);
      }
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

// 배송지 목록에서 삭제
delivery.delete("/delivery-address/:address_id", async (req, res) => {
  const address_id = req.params.address_id;
  try {
    const query = `DELETE FROM address_information WHERE address_id = ?`;
    const result = await pool.query(query, [address_id]);
    console.log(result[0]);
    return res.json({ result: result[0].affectedRows > 0 });
  } catch (error) {
    console.log(error);
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
