const socketIO = require("socket.io");

var location_data = null;
var camera_data = null;

const initializeSocketLoc = (server) => {
  const io = socketIO(server);

  io.on("connection", (socket) => {
    // ros에서 받은 메세지
    socket.on("sendTime", (data) => {
      console.log("수신한 메시지:", data);
    });

    // ros에서 받은 위치 정보
    socket.on("sendLocation", (data) => {
      // console.log("수신한 메시지:", data);
      location_data = data;
      // console.log(raw_data["x"]);
    });

    // ros에서 받은 카메라 정보
    socket.on("sendImage", (data) => {
      // console.log("수신한 메시지:", data);
      camera_data = data;
      // console.log(raw_data["x"]);
    });

    const sendDataToClient = async () => {
      // console.log(raw_data);
      // loc data
      if (location_data !== null) {
        io.emit("sendToFrontLoc", location_data);
      }

      // cam data
      if (camera_data !== null) {
        io.emit("sendToFrontImage", camera_data);
      }
    };

    setInterval(sendDataToClient, 200);
  });
};

module.exports = initializeSocketLoc;
