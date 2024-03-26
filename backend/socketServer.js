// socket.js

const socketIO = require("socket.io");
const pool = require("./DB.js");
const initializeSocket = (server) => {
  const io = socketIO(server);

  io.on("connection", (socket) => {
    console.log("새로운 사용자가 연결되었습니다.");

    // ros에서 받은 메세지
    socket.on("sendTime", (data) => {
      console.log("수신한 메시지:", data);
    });

    setInterval(() => {
      const query = `SELECT odl.order_detail_id, odl.order_quentity, odl.order_progress FROM order_detail_list odl JOIN order_list ol ON odl.order_id = ol.order_id WHERE odl.is_progress = 0 LIMIT 1`;

      pool
        .query(query)
        .then((results) => {
          console.log(results[0]);

          // ros로 보내는 메세지 (msgName, data)
          const jsonData = {
            order_detail_id: results[0].order_detail_id,
            grid: {
              x: 12,
              y: 13,
            },
          };
          io.emit("order", JSON.stringify(jsonData));
        })
        .catch((error) => {
          console.error("데이터베이스 쿼리 오류:", error);
        });
    }, 5000); // 5초마다 실행
  });
};

module.exports = initializeSocket;
