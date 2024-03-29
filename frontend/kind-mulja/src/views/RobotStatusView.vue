<template>
  <div>hi</div>
</template>

<script setup>
  socket1.on("sendToFrontImage", (data) => {
    // 이미지 데이터를 Base64로 인코딩
    const imageData = btoa(String.fromCharCode.apply(null, new Uint8Array(data)));
    
    // 이미지를 표시할 img 태그 선택
    const imgElement = image1.value; // 수정

    // 이미지 데이터를 img 태그의 src 속성에 할당하여 표시
    imgElement.src = "data:image/jpeg;base64," + imageData;
  });

  // 에러가 발생했을 때의 처리
  socket1.on('error', (error) => {
    console.error('웹소켓 에러:', error)
  })
});
</script>

<style scoped></style>
