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
        부울경: "부울경",
      };

      // 주소의 첫 두 글자를 추출
      const addressPrefix = address.substr(1, 2);
      console.log(addressPrefix);
      // cityMapping에 있는지 확인하고 있다면 해당 값 반환
      if (cityMapping[addressPrefix]) {
        return cityMapping[addressPrefix];
      }

      // 추가 규칙 적용
      switch (addressPrefix) {
        case "경기":
        case "인천":
        case "강원":
          return "서울"; // 경기, 인천, 강원은 서울로 분류
        case "충남":
        case "충북":
        case "세종":
          return "대전"; // 충남, 충북, 세종은 대전으로 분류
        case "전북":
        case "전남":
          return "광주"; // 전북, 전남은 광주로 분류
        case "경북":
          return "구미"; // 경북은 구미로 분류
        case "경남":
        case "제주":
          return "부울경"; // 경남, 제주는 부울경으로 분류
        default:
          return "기타"; // 그 외 지역은 기타로 분류
      }
    };

    const getDataAndEmit = async () => {
      try {
        const query1 = `SELECT odl.order_detail_id, odl.order_quentity, odl.order_progress, ol.address 
        FROM order_detail_list odl 
        JOIN order_list ol ON odl.order_id = ol.order_id 
        WHERE odl.is_progress = 0 
        ORDER BY ol.order_type DESC 
        LIMIT 1;`;
        const results = await pool.query(query1);
        console.log(results);
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
