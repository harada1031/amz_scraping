/*
 Navicat Premium Data Transfer

 Source Server         : mysql
 Source Server Type    : MySQL
 Source Server Version : 100424 (10.4.24-MariaDB)
 Source Host           : 127.0.0.1:3306
 Source Schema         : amz

 Target Server Type    : MySQL
 Target Server Version : 100424 (10.4.24-MariaDB)
 File Encoding         : 65001

 Date: 07/11/2023 11:22:41
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for detailed_seller_info
-- ----------------------------
DROP TABLE IF EXISTS `detailed_seller_info`;
CREATE TABLE `detailed_seller_info`  (
  `id` int UNSIGNED NOT NULL AUTO_INCREMENT,
  `seller_id` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NOT NULL,
  `business_name` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `store_name` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `review` varchar(300) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `business_type` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `trade_register_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `vat_number` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `business_address` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL,
  `customer_service_address` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL,
  `email` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `email_2` varchar(100) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `phone_number` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `telephone_2` varchar(30) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `notes` text CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL,
  `seller_page_link` varchar(800) CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci NULL DEFAULT NULL,
  `created` timestamp NOT NULL DEFAULT current_timestamp ON UPDATE CURRENT_TIMESTAMP,
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_unicode_ci ROW_FORMAT = DYNAMIC;

-- ----------------------------
-- Table structure for links
-- ----------------------------
DROP TABLE IF EXISTS `links`;
CREATE TABLE `links`  (
  `id` int NOT NULL AUTO_INCREMENT,
  `link` varchar(800) CHARACTER SET utf8mb4 COLLATE utf8mb4_general_ci NOT NULL,
  `is_used` bit(1) NOT NULL DEFAULT b'0',
  PRIMARY KEY (`id`) USING BTREE
) ENGINE = InnoDB AUTO_INCREMENT = 1 CHARACTER SET = utf8mb4 COLLATE = utf8mb4_general_ci ROW_FORMAT = DYNAMIC;

SET FOREIGN_KEY_CHECKS = 1;
