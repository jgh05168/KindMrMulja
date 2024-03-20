const express = require("express");
const app = express();
const cors = require("cors");
const PORT = 3000;
const pool = require("./DB.js");
const userRouter = require("./route/users.js");
const productRouter = require("./route/product.js");
const wishlistRouter = require("./route/wishlist.js");
const cartRouter = require("./route/cart.js");
const orderRouter = require("./route/order.js");
const deliveryRouter = require("./route/delivery.js");
const server = require("http").createServer(app);
const io = require("socket.io")(server);

app.use(express.json());
app.use(cors());

app.get("/", (req, res) => {
  res.send("You need to request API");
});

app.use("/user", userRouter);
app.use("/product", productRouter);
app.use("/wishlist", wishlistRouter);
app.use("/cart", cartRouter);
app.use("/order", orderRouter);
app.use("/delivery", deliveryRouter);

io.on("connection", async (socket) => {
  console.log("새로운 사용자가 연결되었습니다.");

  const query = `SELECT * FROM order_detail_list WHERE order_id = ?`;
  const results = await pool.query(query, 56);
  console.log(results);
  io.emit("order", results);
  // 연결 종료 이벤트 핸들러에서 타이머를 정리하여 메모리 누수를 방지합니다.
  socket.on("disconnect", () => {
    console.log("사용자 연결이 해제되었습니다.");
    clearInterval(interval);
  });
});

// 로직 2. 포트번호 지정
const port = process.env.port || 12001;
server.listen(port, () => {
  // 연결 port 모니터링 console
  console.log(`listening on *:${port}`);
});

app.listen(PORT, () => console.log(`${PORT} 서버 기동중`));
