const express = require("express");
const app = express();
const cors = require("cors");
const pool = require("./DB.js");
const PORT = 3000;
const userRouter = require("./route/users.js");
const productRouter = require("./route/product.js");
const wishlistRouter = require("./route/wishlist.js");
const cartRouter = require("./route/cart.js");
const orderRouter = require("./route/order.js");
const deliveryRouter = require("./route/delivery.js");
const server = require("http").createServer(app);
const io = require("socket.io")(server);
const initializeSocket = require("./socketServer.js");
const payRouter = require("./route/payments.router.js");
const initializeSocketLoc = require("./socketServerLoc.js");

//

app.use(express.json());
app.use(express.urlencoded({ extended: true }));
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
app.use("/sandbox-dev/api/v1/payments", payRouter);

// 물류 목적지 좌표 통신
const socketServerPort1 = process.env.SOCKET_SERVER_PORT || 12001;
initializeSocket(socketServerPort1);

// 로봇 좌표 받기
//const socketServerPort2 = process.env.SOCKET_SERVER_PORT_LOC || 12002;
//initializeSocketLoc(socketServerPort2);

app.listen(PORT, () => console.log(`${PORT} 서버 기동중`));
