// socket.js

const socketIO = require("socket.io");

const initializeSocket = (server) => {
  const io = socketIO(server);

  io.on("connection", (socket) => {
    console.log("새로운 사용자가 연결되었습니다.");

    // ros에서 받은 메세지
    socket.on("sendTime", (data) => {
      console.log("수신한 메시지:", data);
    });

    socket.on("tutleStatus", (data) => {
      console.log("수신한 메시지:", data);
    });

    
    socket.on("socketStatus", (data) => {
      console.log("수신한 메시지:", data);
    });

    // ros로 보내는 메세지 (msgName, data)
    const jsonData = {
        tutle_id:1,
        order_detail_id:1,
        product_x: -43.591,
        product_y:-38.4146,
        moving_zone: 3,
    };
    io.emit("order", JSON.stringify(jsonData));
  });
};

module.exports = initializeSocket;
