const mysql = require("mysql2/promise");
require('dotenv').config(); // .env 파일의 환경 변수 로드

const dbConfig = {
  host: process.env.DB_HOST,
  port: process.env.DB_PORT,
  user: process.env.DB_USER,
  password: process.env.DB_PASSWORD,
  database: process.env.DB_DATABASE,
};

const pool = mysql.createPool(dbConfig);

module.exports = pool;
