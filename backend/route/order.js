const express = require("express");
const moment = require("moment");
const order = express.Router();
const pool = require("../DB.js");

// 주문 내역 업로드 api
order.post("", async (req, res) => {
  const { user_id, address_id, order_type } = req.body;
  const selected_cart_id = req.body.selected_cart_id;
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
    console.log(selected_cart_id);

    for (let i = 0; i < selected_cart_id.length; i++) {
      const query2 = `SELECT product_id, product_quentity FROM shopping_cart WHERE cart_id = ?`;
      const results = await pool.query(query2, selected_cart_id[i]);
      console.log(results);
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

    for (let i = 0; i < selected_cart_id.length; i++) {
      const query = `DELETE FROM shopping_cart WHERE cart_id = ?`;
      await pool.query(query, [selected_cart_id[i]]);
    }

    return res.json({ result: true }); // 성공적인 응답을 반환
  } catch (error) {
    console.error("에러 발생:", error);
    return res
      .status(500)
      .json({ error: "요청 처리 중에 오류가 발생했습니다." }); // 오류 응답을 반환
  }
});

// 주문 목록 전체 보기
order.get("/order-list/:user_id", async (req, res) => {
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

// 주문 목록 디테일 보기
order.get("/order-list-detail/:user_id", async (req, res) => {
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
    return res.json(results[0]);
  } catch (error) {
    console.log(error);
  }
});

module.exports = order;
