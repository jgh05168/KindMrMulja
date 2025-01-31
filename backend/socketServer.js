const socketIO = require("socket.io");
const pool = require("./DB.js");
const { json } = require("express");

const initializeSocket = (server) => {
  const io = socketIO(server);
  let isEmitting = true; // Emit 상태를 제어하는 변수
  let processedMessages = {};

  io.on("connection", (socket) => {
    console.log("새로운 사용자가 연결되었습니다.");

    socket.on("sendTime", async (data) => {
      console.log(data);
    });

    socket.on("turtleStatus", async (data) => {
      isEmitting = false; // Emit을 중지
      const parsedData = JSON.parse(data);
      const turtle_id = parsedData.turtle_id;
      const order_detail_id = parsedData.order_detail_id;
      const work_status = parsedData.work_status;
      const messageKey = `${turtle_id}_${order_detail_id}`;
      const currentTime = new Date().getTime();
      if (
        processedMessages[messageKey] &&
        processedMessages[messageKey] === work_status &&
        currentTime - processedMessages[messageKey].timestamp < 20
      ) {
        return;
      }
      processedMessages[messageKey] = {
        status: work_status,
        timestamp: currentTime,
      };

      const query1 = `UPDATE order_detail_list SET order_progress = order_progress + 1 WHERE order_detail_id = ? `;
      const query2 = `UPDATE turtlebot SET turtlebot_status = ?, progress_detail_id = ? WHERE turtle_id = ?`;
      const query3 = `UPDATE order_list
        SET order_state = order_state + 1
        WHERE order_id IN (
            SELECT order_id
            FROM order_detail_list
            WHERE order_detail_id = ?
        );`;
      const query4 = `UPDATE order_detail_list SET is_progress = is_progress + 1 WHERE order_detail_id = ? `;
      if (work_status === "start") {
        await Promise.all([
          pool.query(query1, [order_detail_id]),
          pool.query(query2, [1, order_detail_id, turtle_id]),
        ]);
      } else if (work_status === "done") {
        await Promise.all([
          pool.query(query2, [0, 0, turtle_id]),
          pool.query(query3, [order_detail_id]),
          pool.query(query4, [order_detail_id]),
        ]);
      }
      isEmitting = true; // Emit을 다시 시작
    });

    const getRegion = (address) => {
      // 각 도시의 대표값 설정
      const cityMapping = {
        서울: 1,
        대전: 2,
        광주: 3,
        구미: 4,
        부울경: 5,
      };

      // 픽업 주소의 대표값 설정
      const pickupMapping = {
        픽업1: 6,
        픽업2: 7,
        픽업3: 8,
      };

      // 주소의 첫 두 글자를 추출
      const addressPrefix = address.substr(1, 2);
      // 픽업 주소인지 확인
      if (addressPrefix === "픽업") {
        const pickupKey = address.substr(1, 3); // 픽업 문자열과 뒤에 오는 글자 추출
        if (pickupMapping[pickupKey]) {
          return pickupMapping[pickupKey];
        }
      }

      // cityMapping에 있는지 확인하고 있다면 해당 값 반환
      if (cityMapping[addressPrefix]) {
        return cityMapping[addressPrefix];
      }

      // 추가 규칙 적용
      switch (addressPrefix) {
        case "경기":
        case "강원":
        case "인천":
          return 1; // 경기, 인천, 강원은 서울(1)로 분류
        case "충남":
        case "충북":
        case "세종":
          return 2; // 충남, 충북, 세종은 대전(2)으로 분류
        case "전북":
        case "전남":
          return 3; // 전북, 전남은 광주(3)로 분류
        case "경북":
        case "대구":
          return 4; // 경북은 구미(4)로 분류
        case "경남":
        case "제주":
        case "부산":
        case "울산":
          return 5; // 경남, 제주, 부산, 울산은 부울경(5)으로 분류
        default:
          return "기타"; // 그 외 지역은 기타로 분류
      }
    };

    const getDataAndEmit = async () => {
      try {
        if (isEmitting) {
          // Emit을 제어하는 변수를 확인하여 Emit을 수행
          const query1 = `SELECT odl.order_detail_id, odl.order_quentity, odl.order_progress, odl.product_id, ol.address 
          FROM order_detail_list odl 
          JOIN order_list ol ON odl.order_id = ol.order_id 
          WHERE odl.order_quentity > odl.order_progress
          ORDER BY ol.order_type DESC , odl.order_detail_id ASC
          LIMIT 1;`;
          const results = await pool.query(query1);
          const turtlequery = `SELECT turtle_id, turtlebot_status FROM turtlebot WHERE turtlebot_status = ? LIMIT 1`;
          const query2 = `SELECT pos_x, pos_y FROM product_list WHERE product_id = ? `;
          const turtle = await pool.query(turtlequery, 0);
          const position = await pool.query(query2, [results[0][0].product_id]);
          const region = getRegion(results[0][0].address);
          const jsonData = {
            turtle_id: turtle[0][0].turtle_id,
            // turtle_id: 2,
            order_detail_id: results[0][0].order_detail_id,
            product_x: position[0][0].pos_x,
            product_y: position[0][0].pos_y,
            moving_zone: region,
          };
          io.emit("order", JSON.stringify(jsonData));
        }
      } catch (error) {}

      // 다음 호출 예약
      setTimeout(getDataAndEmit, 8000);
    };

    getDataAndEmit(); // 처음 호출
  });
};

module.exports = initializeSocket;
