const express = require("express");
const moment = require("moment");
const user = express.Router();
const pool = require("../DB.js");
user.get("/hihi", (req, res) => {
  res.send("hello");
});

// 회원가입 api
user.post("/signup", async (req, res) => {
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
user.post("/email-duplicate-check", async (req, res) => {
  console.log(req.body);
  const email = req.body.email;

  try {
    const query = `SELECT * FROM user WHERE user_email = ?`;
    const results = await pool.query(query, [email]);
    console.log(results[0]);
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
            SELECT user_id FROM user
            WHERE user_email = ? AND user_password = ?
          `;

    const result = await pool.query(query, [email, password]);
    console.log(result[0]);
    if (result[0].length > 0) {
      return res.json({ user_id: result[0][0].user_id, result: true });
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
