const socketIO = require("socket.io");

var location_data1 = null;
var location_data2 = null;
var location_data3 = null;

const initializeSocketLoc = (server) => {
  const io = socketIO(server);

  io.on("connection", (socket) => {
    // ros에서 받은 메세지
    socket.on("sendTime", (data) => {
      console.log("수신한 메시지:", data);
    });

    //////////////// Turtlebot 1 \\\\\\\\\\\\\\\\\\
    // ros에서 받은 위치 정보 1
    socket.on("sendLocation1", (data) => {
      // console.log("수신한 메시지:", data);
      location_data1 = data;
      // console.log(raw_data["x"]);
    });

    //////////////// Turtlebot 2 \\\\\\\\\\\\\\\\\\
    // ros에서 받은 위치 정보 2
    socket.on("sendLocation2", (data) => {
      // console.log("수신한 메시지:", data);
      location_data2 = data;
      // console.log(raw_data["x"]);
    });

    //////////////// Turtlebot 3 \\\\\\\\\\\\\\\\\\
    // ros에서 받은 위치 정보 3
    socket.on("sendLocation3", (data) => {
      // console.log("수신한 메시지:", data);
      location_data3 = data;
      // console.log(raw_data["x"]);
    });

    const sendDataToClient = async () => {
      // console.log(raw_data);

      //// turtlebot 1
      if (location_data1 !== null) {
        io.emit("sendToFrontLoc1", location_data1);
      }

      //// turtlebot 2
      if (location_data2 !== null) {
        io.emit("sendToFrontLoc2", location_data2);
      }

      //// turtlebot 3
      if (location_data3 !== null) {
        io.emit("sendToFrontLoc3", location_data3);
      }
    };

    setInterval(sendDataToClient, 300);
  });
};

module.exports = initializeSocketLoc;
