
export class Utils {
static numberWithCommas(x) {
    return x.toString().replace(/\B(?=(\d{3})+(?!\d))/g, ',')
  }

static splitStringByComma(sentence) {
    // 쉼표를 기준으로 문장을 잘라서 배열에 넣기
    return sentence.split(',');
}


static pushNotification() {
  var title = 'Simple Title' // 푸쉬 알람 제목
  var options = { 
    icon : '../../public/icons/icon-192.png', // 푸시에 표시될 앱 아이콘 >> 안드로이드에서 실행할 경우 최소 64dp = 192px
    badge : '../../public/icons/icon-192.png', // 모바일에서, 상단 상태 바에 알람 표시 = 어디서 알람 왔는 지 알 수 있는 아이콘
    body: 'Simple piece of body text.\nSecond line of body text :)' , // 알람 본문에 표시될 내용
    image: '' , // 알림 창 안에 이미지 표시
    actions : [ // 특정 동작 수행
    {
      action: 'coffee-action',
      title: 'Coffee',
      icon: ''
    },
    ],
    tag: 'message-group-1', // 새로운 알림 뜰 때 이전 알림의 태그 값 참고하여 이전 알림 지우고 새로운 알림 띄우게 함
    vibrate : [500,110,500,110,450,110,200,110,170,40,450,110,200,110,170,40,500], // 알람시 진동패턴
    sound: '/demos/notification-examples/audio/notification-sound.mp3', //알람시 소리
  };

  registration.showNotification(title, options);
}

}

export default Utils
