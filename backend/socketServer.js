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

    const getRegion = (address) => {
      // 각 도시의 대표값 설정
      const cityMapping = {
        서울: "서울",
        대전: "대전",
        광주: "광주",
        구미: "구미",
        부산: "부울경",
      };

      const addressPrefix = address.substr(0, 2);
      console.log(addressPrefix);
      return cityMapping[addressPrefix];
    };

    const getDataAndEmit = async () => {
      try {
        const query1 = `SELECT odl.order_detail_id, odl.order_quentity, odl.order_progress, ol.address FROM order_detail_list odl JOIN order_list ol ON odl.order_id = ol.order_id WHERE odl.is_progress = 0 LIMIT 1`;
        const results = await pool.query(query1);
        const region = getRegion(results[0][0].address);
        const jsonData = {
          order_detail_id: results[0][0].order_detail_id,
          order_quentity: results[0][0].order_quentity,
          order_progress: results[0][0].order_progress,
          order_region: region,
        };
        io.emit("order", JSON.stringify(jsonData));
      } catch (error) {
        console.error("데이터베이스 쿼리 오류:", error);
      }
    };

    // 5초마다 데이터 조회 및 전송
    setInterval(getDataAndEmit, 5000);
  });
};

module.exports = initializeSocket;
