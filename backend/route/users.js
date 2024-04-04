const express = require("express");
const moment = require("moment");
const user = express.Router();
const pool = require("../DB.js");

user.get("/hihi", (req, res) => {
  res.send("hello");
});

// 회원가입 api
user.post("/signup", async (req, res) => {

  const name = req.body.name;
  const email = req.body.email;
  const password = req.body.password;
  const alarm = req.body.alarm;
  try {
    const query = `
      INSERT INTO user (user_name, user_email, user_password) VALUES (?, ?, ?);`;
    const results = await pool.query(query, [name, email, password]);
    return res.json({ result: true });
  } catch (error) {
    console.log(error);
    return res.status(500).json({ error: "Internal Server Error" });
  }
});

// 이메일 중복확인 api
user.post("/email-duplicate-check", async (req, res) => {
  const email = req.body.email;

  try {
    const query = `SELECT * FROM user WHERE user_email = ?`;
    const results = await pool.query(query, [email]);
    if (results[0].length > 0) {
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
user.post("/signin", async (req, res) => {
  const email = req.body.email;
  const password = req.body.password;

  try {
    const query = `
            SELECT user_id, user_name, is_admin FROM user
            WHERE user_email = ? AND user_password = ?
          `;

    const result = await pool.query(query, [email, password]);
    if (result[0].length > 0) {
      return res.json({
        user_info: {
          user_id: result[0][0].user_id,
          user_name: result[0][0].user_name,
          is_admin: result[0][0].is_admin,
        },
        result: true,
      });
    } else {
      return res.json({ result: false });
    }
  } catch (error) {
    console.error(error);
    return res
      .status(500)
      .json({ result: false, error: "Internal Server Error" });
  }
});

// 로그아웃 api

module.exports = user;
