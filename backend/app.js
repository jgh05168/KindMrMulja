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
const initializeSocket = require("./socketServer.js");
const payRouter = require("./route/payments.router.js");

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

const socketServerPort = process.env.SOCKET_SERVER_PORT || 12001;
initializeSocket(socketServerPort);
app.listen(PORT, () => console.log(`${PORT} 서버 기동중`));
