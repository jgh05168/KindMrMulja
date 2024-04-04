-- --------------------------------------------------------
-- 호스트:                          43.201.59.121
-- 서버 버전:                        11.3.2-MariaDB-1:11.3.2+maria~ubu2204 - mariadb.org binary distribution
-- 서버 OS:                        debian-linux-gnu
-- HeidiSQL 버전:                  12.6.0.6765
-- --------------------------------------------------------

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET NAMES utf8 */;
/*!50503 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;


-- s10p22c109 데이터베이스 구조 내보내기
CREATE DATABASE IF NOT EXISTS `s10p22c109` /*!40100 DEFAULT CHARACTER SET utf8mb4 COLLATE utf8mb4_bin */;
USE `s10p22c109`;

-- 테이블 s10p22c109.address_information 구조 내보내기
CREATE TABLE IF NOT EXISTS `address_information` (
  `address_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `address_name` varchar(255) DEFAULT NULL,
  `user_name` varchar(255) DEFAULT NULL,
  `address_normal` varchar(255) DEFAULT NULL,
  `address_detail` varchar(255) DEFAULT NULL,
  `is_default` tinyint(4) DEFAULT NULL,
  `phone_number` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`address_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `address_information_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=126 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- 테이블 데이터 s10p22c109.address_information:~24 rows (대략적) 내보내기
INSERT INTO `address_information` (`address_id`, `user_id`, `address_name`, `user_name`, `address_normal`, `address_detail`, `is_default`, `phone_number`) VALUES
	(95, 38, '집', '민규', '경기 의왕시 보식골로 1', ' (오전동)', 0, '01012341234'),
	(96, 39, '집', '송아람', '광주 광산구 목련로 293', ' (신가동)', 1, '01066689811'),
	(97, 40, 'ㅊㅊㅊ', '아아', '경기 성남시 분당구 금곡로 233', ' (금곡동, 청솔마을)', 1, '01065911141'),
	(98, 31, '광주', '유명렬', '광주 광산구 풍영로229번안길 2-14', ' (장덕동)', 1, '01029117634'),
	(101, 42, '전남대', '김민영', '광주 북구 용봉로 33', ' (용봉동)', 1, '01096560913'),
	(102, 6, '1', '1', '광주 광산구 장덕동 1336', '1', 0, '01012312341'),
	(104, 2, 'SSAFY 광주캠퍼스', '이싸피', '광주 광산구 하남산단6번로 107', ' (오선동) ', 1, '01012341234'),
	(105, 2, 'SSAFY 서울캠퍼스', '이싸피', '서울 강남구 테헤란로 212', ' (역삼동)', 0, '01012341234'),
	(106, 2, 'SSAFY 부울경캠퍼스', '이싸피', '부산 강서구 녹산산업중로 333', ' (송정동)', 0, '01012341234'),
	(107, 2, 'SSAFY 대전캠퍼스', '이싸피', '대전 유성구 동서대로 98-39', ' (덕명동)', 0, '01012341234'),
	(108, 2, 'SSAFY 구미캠퍼스', '이싸피', '경북 구미시 3공단3로 302', ' (임수동)', 0, '01012341234'),
	(110, 3, 'SSAFY 광주캠퍼스', '이싸피', '광주 광산구 하남산단6번로 107', ' (오선동) ', 1, '01012341234'),
	(111, 6, 'SSAFY 광주캠퍼스', '이싸피', '광주 광산구 하남산단6번로 107', ' (오선동) ', 1, '01012341234'),
	(112, 3, 'SSAFY 서울캠퍼스', '이싸피', '서울 강남구 테헤란로 212', ' (역삼동)', 0, '01012341234'),
	(113, 6, 'SSAFY 서울캠퍼스', '이싸피', '서울 강남구 테헤란로 212', ' (역삼동)', 0, '01012341234'),
	(114, 3, 'SSAFY 부울경캠퍼스', '이싸피', '부산 강서구 녹산산업중로 333', ' (송정동)', 0, '01012341234'),
	(115, 6, 'SSAFY 부울경캠퍼스', '이싸피', '부산 강서구 녹산산업중로 333', ' (송정동)', 0, '01012341234'),
	(116, 3, 'SSAFY 대전캠퍼스', '이싸피', '대전 유성구 동서대로 98-39', ' (덕명동)', 0, '01012341234'),
	(117, 6, 'SSAFY 대전캠퍼스', '이싸피', '대전 유성구 동서대로 98-39', ' (덕명동)', 0, '01012341234'),
	(118, 3, 'SSAFY 구미캠퍼스', '이싸피', '경북 구미시 3공단3로 302', ' (임수동)', 0, '01012341234'),
	(119, 6, 'SSAFY 구미캠퍼스', '이싸피', '경북 구미시 3공단3로 302', ' (임수동)', 0, '01012341234'),
	(123, 2, '123', '구구거ㅓㄱ거ㅓㄱ가가ㅏ다닫다ㅏ다다다ㅏ다다다ㅏ다닫다ㅏ다다ㅏ다다ㅏ', '경북 안동시 예안면 굼곡길 12', 'ㄷ다다ㅏ', 0, '01065911141'),
	(124, 46, '싸피', '김싸피', '경남 밀양시 하남읍 하남산단로 170', 'SSFAY', 1, '01012345678'),
	(125, 42, '집', '김민영', '광주 광산구 풍영로229번안길 2', ' (장덕동)', 0, '01096560913');

-- 테이블 s10p22c109.order_detail_list 구조 내보내기
CREATE TABLE IF NOT EXISTS `order_detail_list` (
  `order_detail_id` int(11) NOT NULL AUTO_INCREMENT,
  `order_id` int(11) DEFAULT NULL,
  `product_id` varchar(50) DEFAULT NULL,
  `order_quentity` int(11) DEFAULT NULL,
  `order_progress` int(11) DEFAULT NULL,
  `moving_zone` varchar(50) DEFAULT NULL,
  `is_progress` int(11) DEFAULT NULL,
  PRIMARY KEY (`order_detail_id`),
  KEY `order_id` (`order_id`),
  KEY `product_id` (`product_id`) USING BTREE,
  CONSTRAINT `FK_order_detail_list_product_list` FOREIGN KEY (`product_id`) REFERENCES `product_list` (`product_id`),
  CONSTRAINT `order_detail_list_ibfk_2` FOREIGN KEY (`order_id`) REFERENCES `order_list` (`order_id`)
) ENGINE=InnoDB AUTO_INCREMENT=260 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- 테이블 데이터 s10p22c109.order_detail_list:~3 rows (대략적) 내보내기
INSERT INTO `order_detail_list` (`order_detail_id`, `order_id`, `product_id`, `order_quentity`, `order_progress`, `moving_zone`, `is_progress`) VALUES
	(257, 298, 'B001', 1, 1, '부산', 1),
	(258, 299, 'C003', 1, 1, '픽업2', 1),
	(259, 300, 'E002', 1, 1, '광주', 0);

-- 테이블 s10p22c109.order_list 구조 내보내기
CREATE TABLE IF NOT EXISTS `order_list` (
  `order_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `address` varchar(255) DEFAULT NULL,
  `order_type` int(11) DEFAULT NULL,
  `order_date` varchar(50) DEFAULT NULL,
  `order_state` int(11) DEFAULT NULL,
  `total_quentity` int(11) DEFAULT NULL,
  `total_price` int(11) DEFAULT NULL,
  PRIMARY KEY (`order_id`),
  KEY `user_id` (`user_id`),
  CONSTRAINT `order_list_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=301 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- 테이블 데이터 s10p22c109.order_list:~3 rows (대략적) 내보내기
INSERT INTO `order_list` (`order_id`, `user_id`, `address`, `order_type`, `order_date`, `order_state`, `total_quentity`, `total_price`) VALUES
	(298, 2, '"부산 강서구 녹산산업중로 333 (송정동)"', 0, '2024-04-04 09:31:09', 1, 1, 749000),
	(299, 31, '"픽업2"', 1, '2024-04-04 09:31:30', 1, 1, 179000),
	(300, 2, '"광주 광산구 하남산단6번로 107 (오선동) "', 0, '2024-04-04 09:33:03', 0, 1, 99900);

-- 테이블 s10p22c109.product_list 구조 내보내기
CREATE TABLE IF NOT EXISTS `product_list` (
  `product_id` varchar(255) NOT NULL,
  `product_name` varchar(255) DEFAULT NULL,
  `summary` varchar(1000) DEFAULT NULL,
  `product_price` int(11) DEFAULT NULL,
  `product_category` varchar(255) DEFAULT NULL,
  `product_stock` int(11) DEFAULT NULL,
  `description` varchar(1000) DEFAULT NULL,
  `pos_x` float DEFAULT NULL,
  `pos_y` float DEFAULT NULL,
  `width` float DEFAULT NULL,
  `length` float DEFAULT NULL,
  `height` float DEFAULT NULL,
  `size` varchar(50) DEFAULT NULL,
  `wishcount` int(11) DEFAULT NULL,
  PRIMARY KEY (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- 테이블 데이터 s10p22c109.product_list:~23 rows (대략적) 내보내기
INSERT INTO `product_list` (`product_id`, `product_name`, `summary`, `product_price`, `product_category`, `product_stock`, `description`, `pos_x`, `pos_y`, `width`, `length`, `height`, `size`, `wishcount`) VALUES
	('A001', 'RAKKESTAD 라케스타드', '슬라이딩도어옷장, 블랙브라운, 117x176 cm', 229000, 'closet', 0, '간편하고 스마트하죠! 기본 기능에 충실한 옷장이 필요할 때 사용하기 좋아요. 수납이 여전히 부족하다면 RAKKESTAD 라케스타드 시리즈의 다른 옷장을 추가해보세요.', NULL, NULL, 117, 55, 176, '59*20*180', 4),
	('A002', 'OMAR 오마르', '선반유닛+옷걸이봉, 아연도금, 186x50x201 cm', 298000, 'closet', 0, 'OMAR 오마르 선반유닛은 집안 어디에서나 사용할 수 있습니다. 옷걸이봉이 있어 현관이나 침실, 심지어 세탁실에서도 유용하죠. 옷을 걸거나 접어서 보관해보세요. 같은 시리즈의 수납공간을 추가하면 더욱 완벽해집니다.', 0, 0, 186, 50, 201, '64*52*13', 2),
	('A003', 'KLEPPSTAD 클렙스타드', '슬라이딩도어옷장, 화이트, 117x176 cm', 199000, 'closet', 0, '간편하고 스마트하죠! 기본 기능에 충실한 옷장이 필요할 때 사용하기 좋아요. 수납이 여전히 부족하다면 KLEPPSTAD 클렙스타드 시리즈의 다른 옷장을 추가해보세요.', NULL, NULL, 117, 55, 176, '59*15*180', 2),
	('A004', 'NORDKISA 노르드키사', '오픈형 옷장+미닫이도어, 대나무, 120x186 cm', 279000, 'closet', 9, '이 옷장은 클래식 스칸디나비아 가구 디자인에서 영감을 받아 라인이 깔끔하고 산뜻한 느낌이 특징이에요. 옷과 소지품을 위한 수납공간으로 사용할 수 있고 집에 개성을 더해주는 아이템이에요.', -59.7882, -57.945, 120, 47, 186, '64*18*169', 6),
	('A005', 'VUKU 부쿠', '옷장, 화이트, 74x51x149 cm', 20000, 'closet', 0, '텐트 재질 특유의 장점에서 영향을 받아서 만든 옷장입니다. 실제 텐트 제조업체와 함께 개발했죠. 계절이 지난 옷을 보관하거나 이동이 편리한 옷장이 필요할 때 유용합니다. 싹 말아서 들고가기만 하면 되니까요.', NULL, NULL, 74, 51, 149, '12*7*75', 0),
	('A006', 'VILHATTEN 빌하텐', '옷장+도어2/서랍2, 참나무무늬', 259000, 'closet', 0, '옷을 걸어 둘지 혹은 개어 둘지 선택할 필요가 없어요. 컴팩트한 VILHATTEN 빌하텐 옷장에는 두 가지 공간이 모두 있으니까요. 바닥 공간은 조금만 차지하기 때문에 현관과 침실에 두기에 아주 좋아요.', NULL, NULL, 98, 57, 190, '56*20*193', 1),
	('B001', 'SÖDERHAMN 쇠데르함', '3인용섹션, 비아르프 베이지/브라운', 749000, 'sofa', 5, '스타일리시하고 산뜻한 느낌이 좋다면 시트가 깊고 넓은 소파는 어떨까요? 개성을 살려 맞춤 구성한 SÖDERHAMN 쇠데르함 소파에 혼자 또는 가족 모두와 함께 앉아 편안한 휴식을 즐겨보세요.', -62.9639, -64.2941, 186, 99, 83, '97*40*193', 4),
	('B002', 'ANGERSBY 앙에르스뷔', '2인용소파, 크니사 라이트그레이', 199000, 'sofa', 0, '마음에 드신다면 지금 바로 구매해서 집으로 가져가세요. ANGERSBY 앙에르스뷔 소파는 차에 실어서 집까지 편하게 운반할 수 있도록 만들어졌습니다. 측면에 수납할 수 있는 포켓이 있어 더욱 편리합니다.', NULL, NULL, 137, 84, 89, '62*47*87', 1),
	('B003', 'KLIPPAN 클리판', '2인용소파, 비슬레 그레이', 299000, 'sofa', 0, 'IKEA는 1980년대에 KLIPPAN/클리판 소파를 출시했으며 지금까지 인기를 끌고 있습니다. 이 소파는 편안하고 거의 모든 곳에서 사용할 수 있으며 수많은 커버를 선택할 수 있는 옵션이 있습니다. 모던하며 유행을 타지 않는 클래식한 스타일입니다!', NULL, NULL, 180, 88, 66, '88*43*182', 0),
	('B004', 'PÄRUP 페루프', '2인용 소파베드, 군나레드 다크그레이', 629000, 'sofa', 0, '빠르고 간편하게 소파를 넓은 침대로 변신시켜보세요. 커버는 폴리에스테르 소재의 GUNNARED 군나레드 원착 패브릭으로 만들었어요. 울과 같은 느낌을 지닌 내구성이 우수한 패브릭으로, 따스한 분위기와 투톤의 멜란지 효과가 특징입니다. 커버는 분리하여 물세탁이 가능하기 때문에 오랫동안 깨끗하게 사용할 수 있습니다.', NULL, NULL, 166, 83, 86, '86*74*146', 0),
	('B005', 'SMEDSTORP 스메스토르프', '2인용소파, 유파르프 다크그린블루/자작나무', 899000, 'sofa', 0, '옛 시절의 부드러운 모양을 좋아하고 현대적인 편안함도 원하는 이들을 위한 소파예요. 탄성폼 쿠션과 편안한 팔걸이, 레트로 감성이 느껴지는 원뿔 모양의 다리는 오래 쓸 수 있어요.', NULL, NULL, 165, 94, 88, '80*46*185', 1),
	('B006', 'KIVIK 쉬비크', '1인용 소파베드, 티블레뷔 베이지/그레이', 449000, 'sofa', 0, 'KIVIK 쉬비크 소파는 IKEA의 클래식 제품 중 하나로, 특히 이 제품은 편안한 침대로 쉽게 변신할 수 있는 컴팩트한 1인용 소파베드예요. 공간을 스마트하게 사용할 수 있고 아무리 작은 공간이라도 하룻밤 자고 가는 손님을 위해 유용하게 쓸 수 있어요.', NULL, NULL, 90, 97, 86, '89*68*95', 0),
	('C001', 'LINNMON 린몬 / ADILS 아딜스', '테이블, 화이트, 100x60cm', 45000, 'desk', 0, '테이블 상판과 다리를 취향대로 조합하거나 사전 구성된 콤비네이션을 사용해 보세요. 튼튼하고 가벼우며, 원자재를 덜 사용하는 기술로 제작되어 환경에 미치는 영향도 줄여줍니다.', NULL, NULL, 100, 60, 74, '60*6*100', 0),
	('C002', 'SANDSBERG 산스베리', '테이블, 블랙, 110x67 cm', 50000, 'desk', 0, 'SANDSBERG 산스베리 의자와 완벽하게 어우러지도록 디자인되었어요. ADDE 아데 및 ÖSTANÖ 외스타뇌 의자와도 잘 어울려 남다른 스타일로 연출하기 좋아요.', NULL, NULL, 110, 67, 75, '72*5*148', 1),
	('C003', 'UTESPELARE 우테스펠라레', '게이밍 책상, 블랙, 160x80 cm', 179000, 'desk', 5, '크고 견고한 UTESPELARE 우테스펠라레 게이밍 책상의 높이를 가장 적합한 높이로 올릴 수 있어요. 테이블 상판 뒤쪽의 메탈판에 구멍이 나 있어 통풍이 잘되므로 게임이 후끈 달아오를 때 PC가 과열되지 않도록 유지해 줍니다.', -56.9534, -60.5666, 160, 80, 66.78, '79*9*165', 4),
	('C004', 'TROTTEN 트로텐', '높이조절책상, 화이트, 160x80 cm', 299000, 'desk', 0, '앉아만 있기보다 일어서기도 하고 자세를 달리하는 것이 건강에 좋아요. 높이조절 핸들을 조절하여 몸을 움직여보세요. 기분도 상쾌해지고 업무 능률도 향상됩니다.', NULL, NULL, 160, 80, 72, '85*10*167', 0),
	('C005', 'MÖCKELBY 뫼켈뷔', '테이블, 참나무, 235x100 cm', 999000, 'desk', 0, '널빤지 모양은 오크 상단으로 제작되어 공예품 및 농가의 느낌을 부각시킵니다. 모든 테이블은 다양한 나뭇결 패턴과 자연스러운 색상 변화로 독특함을 자아냅니다. 견고한 테이블은 손님 초대용으로 바로 사용할 수 있습니다.', NULL, NULL, 235, 100, 74, '53*20*242', 0),
	('C006', 'LAGKAPTEN 락캅텐 / ALEX 알렉스', '책상, 그레이터쿼이즈/블랙, 120x60 cm', 131900, 'desk', 0, '간단한 방법으로 취향과 공간을 모두 만족시키는 책상을 꾸며보세요. 원하는 테이블상판과 다리를 조합하거나 이 추천 콤비네이션을 선택해 보세요. 깔끔한 라인의 상판이 마음에 쏙 들 거예요.', NULL, NULL, 120, 60, 73, '67*10*120', 0),
	('D001', 'VALEVÅG 발레보그', '포켓스프링매트리스, 매우 단단함/라이트블루, 150x200 cm', 329000, 'mattress', 0, '편안함과 지지력이 좋은 컴포트존과 포켓스프링이 결합해 편안한 숙면을 보장합니다.', NULL, NULL, 150, 200, 24, '40*40*163', 0),
	('D002', 'ÅBYGDA 오뷔그다', '폼매트리스, 단단함/화이트, 120x200 cm', 249000, 'mattress', 0, '16cm 높이의 2단, 단단한 폼 매트리스입니다. 메모리폼 상단 레이어가 몸에 가해지는 압력을 덜어주고, 컴포트 존이 몸 전체를 편안하게 받쳐주며, 부드러운 커버는 세탁이 가능합니다.', NULL, NULL, 120, 200, 16, '32*32*130', 0),
	('D003', 'VATNESTRÖM 바트네스트룀', '포켓스프링매트리스, 매우 단단함/내추럴, 180x200 cm', 1090000, 'mattress', 0, '매트리스의 천연소재가 안정된 수면 환경을 조성하고 온도를 조절하여 다소 덥거나 쌀쌀한 밤에도 곤히 숙면을 취할 수 있도록 도와줍니다.', NULL, NULL, 180, 200, 26, '183*201*27', 0),
	('D004', 'MAUSUND 마우순드', '천연 라텍스 매트리스, 푹신함 내추럴, 120x200 cm', 799000, 'mattress', 10, '편안한 잠자리만큼은 조금 욕심내도 괜찮아요. 천연 라텍스, 면, 울처럼 천연소재를 사용해서 잘 때 몸을 편안하게 감싸주고 땀 흡수도 잘되는 매트리스입니다. 수면 온도가 일정하게 유지되어 매우 쾌적하죠.', -55.506, -72.518, 120, 200, 20, '122*202*22', 2),
	('D005', 'TUSSÖY 투쇠위', '매트리스 토퍼, 화이트, 90x200 cm', 149000, 'mattress', 0, '메모리폼 소재의 매트리스 패드가 엉덩이와 어깨에 가해지는 압력을 줄여줍니다. 체형에 따라 매트리스가 부드럽게 몸을 감싸 주므로 차분하게 자는 사람은 아주 편안하게 잠을 잘 수 있습니다. 세탁기로 커버를 세탁할 수 있어 깨끗하게 관리하기 쉬워요.', NULL, NULL, 90, 200, 8, '31*31*100', 0),
	('D006', 'ÅKREHAMN 오크레함', '폼매트리스, 단단함/화이트, 150x200 cm', 399000, 'mattress', 0, '신중하게 엄선한 3단 폼 층이 결합되어 안정적이고 편안합니다.', NULL, NULL, 150, 200, 20, '40*40*158', 0),
	('E001', 'MALM 말름', '4칸서랍장, 화이트스테인 참나무 무늬목, 80x100 cm', 229000, 'drawer', 0, '심플하고 깔끔한 디자인 덕분에 어디에나 잘 어울립니다. 부드럽게 열고 닫히는 서랍입니다. 원하는 마감재를 선택할 수 있습니다. 벽에 단단히 고정해주세요.', NULL, NULL, 80, 48, 100, '49*102*11', 0),
	('E002', 'ALEX 알렉스', '서랍유닛, 그레이터쿼이즈, 36x70 cm', 99900, 'drawer', 6, '다른 스타일과도 잘 어울려 누구나 좋아할 수밖에 없는 간결한 디자인의 수납장입니다. 책상과 함께 혹은 단독으로 사용해도 근사해요. 바로 뒷면도 마감 처리가 되어 있어서 방 한가운데 놓아도 멋져요.', -56.9534, -65.5741, 36, 58, 70, '59*82*11', 2),
	('E003', 'GURSKEN 구르스켄', '3칸서랍장, 라이트베이지, 69x67 cm', 59900, 'drawer', 0, '간결하고 깔끔한 디자인이 멋스러운 GURSKEN 구르스켄 서랍장은 아파트나 게스트룸을 빠르고 쉽게 꾸미기 좋은 가구입니다. 같은 시리즈의 침대협탁, 침대, 옷장과 아주 잘 어울려요!', NULL, NULL, 69, 38, 67, '42*75*11', 0),
	('E004', 'HEMNES 헴네스', '8칸서랍장, 화이트 스테인, 160x96 cm', 459000, 'drawer', 0, '클래식한 대형 원목 서랍장으로 고전적인 멋과 현대적 기능을 모두 누릴 수 있습니다. 조용하고 부드럽게 여닫히는 서랍 안에 물건을 정리해 보세요. 기억해 두세요! 서랍장은 벽에 단단히 고정해야 합니다.', NULL, NULL, 160, 96, 50, '51*146*6', 0),
	('E005', 'KOPPANG 코팡', '5칸서랍장, 화이트, 90x114 cm', 179000, 'drawer', 0, '침실뿐 아니라 어디에 두어도 모든 장식과 잘 어울리는 심플함과 기능성을 갖춘 서랍장입니다. 좋아하는 옷과 여분의 침구를 모두 수납할 수 있는 넉넉한 공간의 제품입니다. 참! 꼭 벽에 고정하세요.', NULL, NULL, 90, 44, 114, '63*116*7', 0),
	('E006', 'SONGESAND 송에산드', '4칸서랍장, 화이트, 82x104 cm', 199000, 'drawer', 0, '서랍앞판 패널의 클래식한 디자인은 시간이 흘러도 근사하게 느껴질 거예요. 기억해 두세요! 서랍장은 벽에 단단히 고정해야 합니다.', NULL, NULL, 82, 50, 104, '51*107*11', 1);

-- 테이블 s10p22c109.receiving_product 구조 내보내기
CREATE TABLE IF NOT EXISTS `receiving_product` (
  `receiving_id` int(11) NOT NULL AUTO_INCREMENT,
  `product_id` varchar(255) DEFAULT NULL,
  `receiving_count` int(11) DEFAULT NULL,
  PRIMARY KEY (`receiving_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `receiving_product_ibfk_1` FOREIGN KEY (`product_id`) REFERENCES `product_list` (`product_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- 테이블 데이터 s10p22c109.receiving_product:~0 rows (대략적) 내보내기

-- 테이블 s10p22c109.shopping_cart 구조 내보내기
CREATE TABLE IF NOT EXISTS `shopping_cart` (
  `cart_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `product_id` varchar(255) DEFAULT NULL,
  `product_quentity` int(11) DEFAULT NULL,
  PRIMARY KEY (`cart_id`),
  KEY `user_id` (`user_id`),
  KEY `FK_shopping_cart_product_list` (`product_id`),
  CONSTRAINT `FK_shopping_cart_product_list` FOREIGN KEY (`product_id`) REFERENCES `product_list` (`product_id`),
  CONSTRAINT `shopping_cart_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=300 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- 테이블 데이터 s10p22c109.shopping_cart:~2 rows (대략적) 내보내기
INSERT INTO `shopping_cart` (`cart_id`, `user_id`, `product_id`, `product_quentity`) VALUES
	(261, 32, 'A004', 1),
	(294, 42, 'E002', 1);

-- 테이블 s10p22c109.turtlebot 구조 내보내기
CREATE TABLE IF NOT EXISTS `turtlebot` (
  `turtle_id` int(11) NOT NULL AUTO_INCREMENT,
  `pos_x` float DEFAULT NULL,
  `pos_y` float DEFAULT NULL,
  `turtlebot_status` int(11) DEFAULT NULL,
  `progress_detail_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`turtle_id`) USING BTREE
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- 테이블 데이터 s10p22c109.turtlebot:~3 rows (대략적) 내보내기
INSERT INTO `turtlebot` (`turtle_id`, `pos_x`, `pos_y`, `turtlebot_status`, `progress_detail_id`) VALUES
	(1, NULL, NULL, 1, 259),
	(2, NULL, NULL, 0, 0),
	(3, NULL, NULL, 0, 0);

-- 테이블 s10p22c109.user 구조 내보내기
CREATE TABLE IF NOT EXISTS `user` (
  `user_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_name` varchar(255) DEFAULT NULL,
  `user_email` varchar(255) DEFAULT NULL,
  `user_password` varchar(255) DEFAULT NULL,
  `is_admin` tinyint(4) DEFAULT NULL,
  PRIMARY KEY (`user_id`)
) ENGINE=InnoDB AUTO_INCREMENT=47 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- 테이블 데이터 s10p22c109.user:~20 rows (대략적) 내보내기
INSERT INTO `user` (`user_id`, `user_name`, `user_email`, `user_password`, `is_admin`) VALUES
	(1, 'ssafy_1', 'ssafy1@ssafy.com', 'ssafy109@', 1),
	(2, 'test_1', 'test1@ssafy.com', 'ssafy109@', NULL),
	(3, 'test_2', 'test2@ssafy.com', 'ssafy109@', NULL),
	(4, 'ssafy_2', 'ssafy2@ssafy.com', 'ssafy109@', 1),
	(5, 'ssafy_3', 'ssafy3@ssafy.com', 'ssafy109@', 1),
	(6, 'test_3', 'test3@ssafy.com', 'ssafy109@', NULL),
	(31, '유명렬', 'dlek567@gmail.com', 'qwerty1!', 0),
	(32, '이윤형', 'yun0730@gmail.com', '12qwaszx@', 0),
	(33, '이윤형', 'yun0730@naver.com', '12qwaszx@', NULL),
	(34, '이윤형', 'yun0730@masl.com', '12qwaszx@', NULL),
	(35, '이윤형', 'yun0730@daum.com', '12qwaszx@', NULL),
	(36, '유명렬', 'dlek567@naver.com', 'qwerty1!', NULL),
	(37, '광현', 'rhkdgus3573@naver.com', 'rhrhkdguS1!', NULL),
	(38, '이민규', 'test@test.com', 'asdf1234!', NULL),
	(39, '송아람', 'son9aram@test.com', 'qwer1234!', NULL),
	(40, '이윤형', 'yun0730@ssafy.com', '12qwaszx@', NULL),
	(42, 'minzero', 'minzero@gmail.com', 'minzero1234!', NULL),
	(44, 'gogwang', 'gogwang@gogwangland.com', 'ssafy109@', NULL),
	(45, '송아람', 'son9aram@gmail.com', 'qwer1234!', NULL),
	(46, '고고고', 'gogogo@go.go', '12345678a!', NULL);

-- 테이블 s10p22c109.wishlist 구조 내보내기
CREATE TABLE IF NOT EXISTS `wishlist` (
  `wishlist_id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) DEFAULT NULL,
  `product_id` varchar(255) DEFAULT NULL,
  PRIMARY KEY (`wishlist_id`),
  KEY `user_id` (`user_id`),
  KEY `product_id` (`product_id`),
  CONSTRAINT `wishlist_ibfk_1` FOREIGN KEY (`user_id`) REFERENCES `user` (`user_id`),
  CONSTRAINT `wishlist_ibfk_2` FOREIGN KEY (`product_id`) REFERENCES `product_list` (`product_id`)
) ENGINE=InnoDB AUTO_INCREMENT=703 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_bin;

-- 테이블 데이터 s10p22c109.wishlist:~18 rows (대략적) 내보내기
INSERT INTO `wishlist` (`wishlist_id`, `user_id`, `product_id`) VALUES
	(576, 32, 'A001'),
	(577, 32, 'A002'),
	(578, 32, 'C003'),
	(589, 32, 'A004'),
	(590, 32, 'B001'),
	(591, 32, 'D004'),
	(592, 32, 'E002'),
	(593, 32, 'A003'),
	(595, 44, 'B001'),
	(596, 44, 'A004'),
	(597, 44, 'C003'),
	(599, 44, 'A003'),
	(600, 44, 'D004'),
	(601, 44, 'A001'),
	(602, 45, 'C003'),
	(603, 3, 'E006'),
	(604, 3, 'E002'),
	(618, 46, 'A004');

/*!40103 SET TIME_ZONE=IFNULL(@OLD_TIME_ZONE, 'system') */;
/*!40101 SET SQL_MODE=IFNULL(@OLD_SQL_MODE, '') */;
/*!40014 SET FOREIGN_KEY_CHECKS=IFNULL(@OLD_FOREIGN_KEY_CHECKS, 1) */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40111 SET SQL_NOTES=IFNULL(@OLD_SQL_NOTES, 1) */;
