const express = require("express");
const app = express();
const cors = require("cors");
const pool = require("./DB.js");
const PORT = 3000;

app.use(express.json());
app.use(cors());

app.get("/", (req, res) => {
  res.send("You need to request API");
});

app.get("/test", (req,res) => {
    res.send("HIHI");
    const query = `
    INSERT INTO test (name, age) VALUES (1, 1)`;
    pool.query(query);
});
app.listen(PORT, () => console.log(`${PORT} 서버 기동중`));
