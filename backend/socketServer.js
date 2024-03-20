const express = require("express");

var app = express();

// 로직 1. WebSocket 서버, WebClient 통신 규약 정의
const server = require("http").createServer(app);
const io = require("socket.io")(server);

const roomName = "team";

// socket 연결
io.on("connection", (socket) => {
  console.log("새로운 사용자가 연결되었습니다.");
  // room socket을 사용하는 경우 room에 참여할 때 join 사용. room은 참여한 socket들에 대해 한번에 여러 이벤트를 emit할 수 있다.
  // socket.join(receviedTitle);

  //ros에서 받은 메세지
  socket.on("sendTime", (data) => {
    console.log("수신한 메시지:", data);
  });

  //ros로 보내는 메세지 (msgName, data)
  io.emit("order", { product_id: "A001", user_id: "1" });
});

// 로직 2. 포트번호 지정
const port = process.env.port || 12001;
server.listen(port, () => {
  // 연결 port 모니터링 console
  console.log(`listening on *:${port}`);
});
