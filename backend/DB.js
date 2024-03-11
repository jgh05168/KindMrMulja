const mysql = require("mysql2/promise");

const dbConfig = {
  host: "stg-yswa-kr-practice-db-master.mariadb.database.azure.com",
  port: 3306,
  user: "S10P22C109@stg-yswa-kr-practice-db-master.mariadb.database.azure.com",
  password: "ze4rrqSoI0",
  database: "s10p22c109",
};

const pool = mysql.createPool(dbConfig);

module.exports = pool;
