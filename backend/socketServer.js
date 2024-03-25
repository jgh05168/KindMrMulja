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

    // ros로 보내는 메세지 (msgName, data)
    const jsonData = {
        local_num: 1,
        target_grid: {
            x: -44.0,
            y: -39.0
        }
    };
    io.emit("order", JSON.stringify(jsonData));
  });
};

module.exports = initializeSocket;
