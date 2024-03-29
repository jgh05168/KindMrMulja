const socketIO = require("socket.io");

var raw_data = null;

const initializeSocketLoc2 = (server) => {
  const io = socketIO(server);

  io.on("connection", (socket) => {
    console.log("새로운 사용자가 연결되었습니다 hi.");

    // ros에서 받은 메세지
    socket.on("sendTime", (data) => {
      console.log("수신한 메시지:", data);
    });

    // ros에서 받은 위치 정보
    socket.on('sendImage', (data) => {
    //   console.log("수신한 메시지:", data);
      raw_data = data;
      // console.log(raw_data["x"]);
    });

    const sendDataToClientImage = async () => {
      console.log(raw_data);
      io.emit("sendToFrontImage", raw_data);
    };

    setInterval(sendDataToClientImage, 1000);
  });
};

module.exports = initializeSocketLoc2;
