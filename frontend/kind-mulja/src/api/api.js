import axios from 'axios'
//여기 사이트에 json 데이터 파일 있음
const api_url = 'http://localhost:3000'
// const api_url = 'https://j10c109.p.ssafy.io/api'
export class Service {
  static SignIn(email, password) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'post',
        url: api_url + '/user/signin',
        data: {
          email: email,
          password: password
        }
      })
        .then((res) => {
          const data = res.data
          // 만약 로그인이 완료 되면 회원 정보 local 에 저장
          console.log('회원 로그인 성공 여부 : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`로그인에 실패했습니다.: ${error.message}`))
        })
    })
  }

  static SignUp(account) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'post',
        url: api_url + '/user/signup',
        data: {
          name: account.name,
          email: account.email,
          password: account.password
        },
        // `headers`는 사용자 지정 헤더입니다.
        withCredentials: false // 기본값
      })
        .then((res) => {
          console.log('회원가입 요청', res.data)
          // 결과값 result
          resolve(res.data)
        })
        .catch((error) => {
          reject(new Error(`회원가입에 실패하였습니다.: ${error.message}`))
        })
    })
  }

  static email_duplicate_check(email) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'post',
        url: api_url + '/user/email-duplicate-check',
        data: {
          email: email
        }
      })
        .then((res) => {
          const data = res.data
          // 이메일 중복 여부에 따라 반환해주기
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`중복 체크에 실패 했습니다.: ${error.message}`))
        })
    })
  }

  static getProductList() {
    return new Promise((resolve, reject) => {
      axios({
        method: 'get',
        url: api_url + '/product/product-list'
      })
        .then((res) => {
          // "product_id" : string,"product_name" : string,"product_price" : int,"product_category” : string
          const data = res.data
          // console.log('상품 전체 리스트 : ',data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`상품 전체 리스트 실패: ${error.message}`))
        })
    })
  }

  static getProduct(id) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'get',
        url: api_url + `/product/product-detail/${id}`
      })
        .then((res) => {
          // "product_name" : string,"product_price" : int,"description” : string
          const data = res.data
          console.log('상품 단일 데이터 : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`상품 단일 데이터 실패: ${error.message}`))
        })
    })
  }

  static checkProductWish(user_id, product_id) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'get',
        url: api_url + `/product/check-wish-product/${user_id}/${product_id}`
      })
        .then((res) => {
          const data = res.data
          // console.log('상품 찜 여부 : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`상품 찜 여부 확인: ${error.message}`))
        })
    })
  }

  static toggleWish(user_id, product_id) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'post',
        url: api_url + `/product/wishlist-toggle`,
        data: {
          user_id: user_id,
          product_id: product_id
        }
      })
        .then((res) => {
          const data = res.data
          console.log('상품 찜 토글 : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`상품 찜 토글 실패: ${error.message}`))
        })
    })
  }

  static getWishList(user_id) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'get',
        url: api_url + `/wishlist/${user_id}`
      })
        .then((res) => {
          const data = res.data
          console.log('상품 찜 목록 조회 : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`상품 목록 조회 실패: ${error.message}`))
        })
    })
  }

  static deleteWish(wishlist_id) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'delete',
        url: api_url + `/wishlist/${wishlist_id}`
      })
        .then((res) => {
          const data = res.data
          console.log('위시리스트에서 삭제 여부 : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`위시리스트에서 삭제 실패: ${error.message}`))
        })
    })
  }

  static addToCart(user_id, product_id, product_quentity) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'post',
        url: api_url + '/product/add-shopping-cart',
        data: {
          user_id: user_id,
          product_id: product_id,
          product_quentity: product_quentity
        }
      })
        .then((res) => {
          const data = res.data
          console.log('장바구니 담기 : ', data)
          resolve(data.result)
        })
        .catch((error) => {
          reject(new Error(`장바구니 담기 실패: ${error.message}`))
        })
    })
  }

  static cartList(user_id) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'get',
        url: api_url + `/cart/${user_id}`
      })
        .then((res) => {
          const data = res.data
          console.log('장바구니 목록 : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`장바구니 목록 불러오기 실패: ${error.message}`))
        })
    })
  }

  static cartUpdate(cart_id, product_quentity) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'patch',
        url: api_url + `/cart/cart-update`,
        data: {
          cart_id: cart_id,
          product_quentity: product_quentity
        }
      })
        .then((res) => {
          const data = res.data
          console.log('장바구니 업데이트 : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`장바구니 업데이트 실패: ${error.message}`))
        })
    })
  }

  static cartDelete(cart_id) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'delete',
        url: api_url + `/cart/${cart_id}`
      })
        .then((res) => {
          const data = res.data
          console.log('장바구니 에서 상품 삭제 : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`장바구니 상품 삭제 실패: ${error.message}`))
        })
    })
  }

  static addDelivery(info) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'post',
        url: api_url + '/delivery/delivery-address/add',
        data: {
          user_id: info.user_id,
          address_name: info.address_name,
          user_name: info.user_name,
          address_normal: info.address_normal,
          address_detail: info.address_detail,
          phone_number: info.phone_number,
          is_default: info.is_default
        }
      })
        .then((res) => {
          const data = res.data
          console.log('배송지 추가 : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`배송지 추가 실패: ${error.message}`))
        })
    })
  }

  static getAddress(user_id) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'get',
        url: api_url + `/delivery/delivery-address/list/${user_id}`
      })
        .then((res) => {
          const data = res.data
          console.log('배송지 목록 : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`배송지 목록 조회: ${error.message}`))
        })
    })
  }

  static setDefaultAddress(user_id, address_id) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'patch',
        url: api_url + `/delivery/delivery-address/default-address`,
        data: {
          user_id: user_id,
          address_id: address_id
        }
      })
        .then((res) => {
          const data = res.data
          console.log('기본 배송지 성공? : ', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`기본 배송지 설정 실패: ${error.message}`))
        })
    })
  }

  static createOrder(order_info) {
    return new Promise((resolve, reject) => {
      axios({
        method: 'post',
        url: api_url + '/order',
        data: {
          user_id: order_info.user_id,
          address_content: order_info.address_content,
          order_type: order_info.order_type,
          selected_cart_id: order_info.selected_cart_id
        }
      })
        .then((res) => {
          const data = res.data
          console.log('주문', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`주문 실패: ${error.message}`))
        })
    })
  }

  static getOrderList(user_id) {
    // {
    //   "order_id": int,
    //   "user_id": int,
    //   "address_id": int,
    //   "order_type": int,
    //   "order_date": string,
    //   "order_state": int,
    //   "total_quentity": int,
    //   "total_price": int
    //   }
    return new Promise((resolve, reject) => {
      axios({
        method: 'get',
        url: api_url + `/order/order-list/${user_id}`
      })
        .then((res) => {
          const data = res.data
          console.log('주문목록 묶음 리스트', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`주문목록 묶음 리스트 조회 실패: ${error.message}`))
        })
    })
  }

  static getOrderDetailList(order_id) {
    // {
    //   "order_detail_id": int,
    //   "order_id": int,
    //   "order_quentity": int,
    //   "order_progress": int,
    //   "product_id": string,
    //   "product_name": string,
    //   "product_price": int
    //   }
    return new Promise((resolve, reject) => {
      axios({
        method: 'get',
        url: api_url + `/order/order-list-detail/${order_id}`
      })
        .then((res) => {
          const data = res.data
          console.log('주문목록 묶음 상세 리스트', data)
          resolve(data)
        })
        .catch((error) => {
          reject(new Error(`주문목록 묶음 상세 리스트 조회 실패: ${error.message}`))
        })
    })
  }
}

export default Service
