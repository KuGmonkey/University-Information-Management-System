/*
 Navicat Premium Data Transfer

 Source Server         : project
 Source Server Type    : MySQL
 Source Server Version : 80028
 Source Host           : localhost:3306
 Source Schema         : school

 Target Server Type    : MySQL
 Target Server Version : 80028
 File Encoding         : 65001

 Date: 29/05/2022 00:34:10
*/

SET NAMES utf8mb4;
SET FOREIGN_KEY_CHECKS = 0;

-- ----------------------------
-- Table structure for admin_login
-- ----------------------------
DROP TABLE IF EXISTS `admin_login`;
CREATE TABLE `admin_login`  (
  `admin_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `admin_pwd` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`admin_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of admin_login
-- ----------------------------
INSERT INTO `admin_login` VALUES ('admin01', '123456');
INSERT INTO `admin_login` VALUES ('admin02', '654321');

-- ----------------------------
-- Table structure for college
-- ----------------------------
DROP TABLE IF EXISTS `college`;
CREATE TABLE `college`  (
  `col_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `pre_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`col_name`) USING BTREE,
  INDEX `manged_by`(`pre_id`) USING BTREE,
  CONSTRAINT `manged_by` FOREIGN KEY (`pre_id`) REFERENCES `teacher` (`tea_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of college
-- ----------------------------
INSERT INTO `college` VALUES ('人工智能学院', '01015');
INSERT INTO `college` VALUES ('电子信息与光学工程学院', '02003');
INSERT INTO `college` VALUES ('网络空间安全学院', '03008');
INSERT INTO `college` VALUES ('计算机学院', '04011');
INSERT INTO `college` VALUES ('软件学院', '05014');

-- ----------------------------
-- Table structure for graduatestudent
-- ----------------------------
DROP TABLE IF EXISTS `graduatestudent`;
CREATE TABLE `graduatestudent`  (
  `stu_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_gender` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_adm_time` date NOT NULL,
  `stu_college` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tea_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `study` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`stu_id`) USING BTREE,
  INDEX `gs_in_col`(`stu_college`) USING BTREE,
  INDEX `teached_by`(`tea_id`) USING BTREE,
  INDEX `gs_in_stuname`(`stu_name`) USING BTREE,
  INDEX `gs_in_stuadm`(`stu_adm_time`) USING BTREE,
  CONSTRAINT `gs_in_col` FOREIGN KEY (`stu_college`) REFERENCES `college` (`col_name`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `gs_in_stuadm` FOREIGN KEY (`stu_adm_time`) REFERENCES `student` (`stu_adm_time`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `gs_in_stuid` FOREIGN KEY (`stu_id`) REFERENCES `student` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `gs_in_stuname` FOREIGN KEY (`stu_name`) REFERENCES `student` (`stu_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `teached_by` FOREIGN KEY (`tea_id`) REFERENCES `teacher` (`tea_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of graduatestudent
-- ----------------------------
INSERT INTO `graduatestudent` VALUES ('00001', '张三', '男', '2020-09-11', '网络空间安全学院', '03008', '计算机病毒');
INSERT INTO `graduatestudent` VALUES ('00002', '李凤', '女', '2020-09-11', '软件学院', '05014', '软件工程');
INSERT INTO `graduatestudent` VALUES ('00005', '王麻', '男', '2021-09-13', '电子信息与光学工程学院', '02003', '光导纤维');

-- ----------------------------
-- Table structure for learn
-- ----------------------------
DROP TABLE IF EXISTS `learn`;
CREATE TABLE `learn`  (
  `stu_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `lesson_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `score` float(255, 0) NULL DEFAULT NULL,
  `class_number` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`stu_id`, `lesson_id`) USING BTREE,
  INDEX `lesson`(`lesson_id`) USING BTREE,
  CONSTRAINT `lesson` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`lesson_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `stu` FOREIGN KEY (`stu_id`) REFERENCES `student` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of learn
-- ----------------------------
INSERT INTO `learn` VALUES ('00001', '001', 96, 'C126/A304');
INSERT INTO `learn` VALUES ('00001', '002', 92, 'B202/A308');
INSERT INTO `learn` VALUES ('00001', '003', 95, 'C420');
INSERT INTO `learn` VALUES ('00001', '009', NULL, NULL);
INSERT INTO `learn` VALUES ('00002', '004', 99, 'B420/A205');
INSERT INTO `learn` VALUES ('00003', '005', 88, 'B402/A203');
INSERT INTO `learn` VALUES ('00003', '009', 94, 'E201');
INSERT INTO `learn` VALUES ('00004', '006', 87, 'B502/A205');
INSERT INTO `learn` VALUES ('00005', '007', 91, '羽毛球馆');
INSERT INTO `learn` VALUES ('98725', '008', 98, 'B531/A315');
INSERT INTO `learn` VALUES ('98725', '015', 77, 'A34');

-- ----------------------------
-- Table structure for lesson
-- ----------------------------
DROP TABLE IF EXISTS `lesson`;
CREATE TABLE `lesson`  (
  `lesson_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `lesson_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `credit` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `class_hour` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`lesson_id`) USING BTREE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of lesson
-- ----------------------------
INSERT INTO `lesson` VALUES ('001', '数据库系统', '3', '17');
INSERT INTO `lesson` VALUES ('002', '计算机组成原理', '3', '17');
INSERT INTO `lesson` VALUES ('003', '计算方法', '2', '17');
INSERT INTO `lesson` VALUES ('004', '嵌入式系统', '3.5', '17');
INSERT INTO `lesson` VALUES ('005', '人工智能导论', '2', '17');
INSERT INTO `lesson` VALUES ('006', '算法导论', '3.5', '17');
INSERT INTO `lesson` VALUES ('007', '羽毛球初级', '2', '16');
INSERT INTO `lesson` VALUES ('008', '软件安全', '3', '17');
INSERT INTO `lesson` VALUES ('009', '高级英语', '2', '17');
INSERT INTO `lesson` VALUES ('010', '信息安全数学基础', '3', '17');
INSERT INTO `lesson` VALUES ('011', '毛概', '3', '17');
INSERT INTO `lesson` VALUES ('012', '揭开基因的奥秘', '2', '9');
INSERT INTO `lesson` VALUES ('014', '爱情社会学', '1', '9');
INSERT INTO `lesson` VALUES ('015', '吉他鉴赏与演奏', '1', '9');

-- ----------------------------
-- Table structure for major
-- ----------------------------
DROP TABLE IF EXISTS `major`;
CREATE TABLE `major`  (
  `maj_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `maj_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `train_way` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `col_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`maj_id`) USING BTREE,
  INDEX `maj_in_col`(`col_name`) USING BTREE,
  CONSTRAINT `maj_in_col` FOREIGN KEY (`col_name`) REFERENCES `college` (`col_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of major
-- ----------------------------
INSERT INTO `major` VALUES ('08001K', '信息安全', '学习计算机病毒', '网络空间安全学院');
INSERT INTO `major` VALUES ('08002K', '软件工程', '学习软件工程', '软件学院');
INSERT INTO `major` VALUES ('08003K', '计算机科学与技术', '学习电脑', '计算机学院');
INSERT INTO `major` VALUES ('08004K', '电子科学与技术', '学习芯片', '电子信息与光学工程学院');
INSERT INTO `major` VALUES ('08005K', '自动化', '学习机器人', '人工智能学院');
INSERT INTO `major` VALUES ('08006K', '物联网工程', '学习物联网', '网络空间安全学院');
INSERT INTO `major` VALUES ('08007K', '软件安全', '学习软件防护', '软件学院');
INSERT INTO `major` VALUES ('08008K', '通信工程', '学习通信', '电子信息与光学工程学院');
INSERT INTO `major` VALUES ('08009K', '智能科学', '学习智能科学与技术', '人工智能学院');

-- ----------------------------
-- Table structure for student
-- ----------------------------
DROP TABLE IF EXISTS `student`;
CREATE TABLE `student`  (
  `stu_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_gender` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_adm_time` date NULL DEFAULT NULL,
  `stu_college` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`stu_id`) USING BTREE,
  UNIQUE INDEX `id_index`(`stu_id`) USING BTREE,
  INDEX `stu_in_col`(`stu_college`) USING BTREE,
  INDEX `stu_name`(`stu_name`) USING BTREE,
  INDEX `stu_adm_time`(`stu_adm_time`) USING BTREE,
  CONSTRAINT `stu_in_col` FOREIGN KEY (`stu_college`) REFERENCES `college` (`col_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student
-- ----------------------------
INSERT INTO `student` VALUES ('00001', '张三', '男', '2020-09-11', '网络空间安全学院');
INSERT INTO `student` VALUES ('00002', '李凤', '女', '2020-09-11', '软件学院');
INSERT INTO `student` VALUES ('00003', '刘二', '男', '2021-09-13', '计算机学院');
INSERT INTO `student` VALUES ('00004', '赵四', '女', '2021-09-13', '人工智能学院');
INSERT INTO `student` VALUES ('00005', '王麻', '男', '2021-09-13', '电子信息与光学工程学院');
INSERT INTO `student` VALUES ('98725', '张蛋', '男', '2019-09-10', '网络空间安全学院');

-- ----------------------------
-- Table structure for student_login
-- ----------------------------
DROP TABLE IF EXISTS `student_login`;
CREATE TABLE `student_login`  (
  `stu_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_pwd` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`stu_id`) USING BTREE,
  CONSTRAINT `stu_login` FOREIGN KEY (`stu_id`) REFERENCES `student` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of student_login
-- ----------------------------
INSERT INTO `student_login` VALUES ('00001', '123456');
INSERT INTO `student_login` VALUES ('00002', '123456');
INSERT INTO `student_login` VALUES ('00003', '123456');
INSERT INTO `student_login` VALUES ('00004', '123456');
INSERT INTO `student_login` VALUES ('00005', '123456');
INSERT INTO `student_login` VALUES ('98725', '123456');

-- ----------------------------
-- Table structure for teach
-- ----------------------------
DROP TABLE IF EXISTS `teach`;
CREATE TABLE `teach`  (
  `tea_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `lesson_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `end_way` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `class` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`tea_id`, `lesson_id`) USING BTREE,
  INDEX `les`(`lesson_id`) USING BTREE,
  CONSTRAINT `les` FOREIGN KEY (`lesson_id`) REFERENCES `lesson` (`lesson_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `tea` FOREIGN KEY (`tea_id`) REFERENCES `teacher` (`tea_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teach
-- ----------------------------
INSERT INTO `teach` VALUES ('01001', '001', '闭卷', 'A1');
INSERT INTO `teach` VALUES ('01001', '012', '闭卷', 'A1');
INSERT INTO `teach` VALUES ('01002', '002', '闭卷', 'B2');
INSERT INTO `teach` VALUES ('01015', '003', '闭卷', 'C3');
INSERT INTO `teach` VALUES ('02003', '004', '开卷', 'A2');
INSERT INTO `teach` VALUES ('02003', '008', '开卷', 'A2');
INSERT INTO `teach` VALUES ('02003', '010', '无期末考试', 'A2');
INSERT INTO `teach` VALUES ('02004', '006', '论文', 'C3');
INSERT INTO `teach` VALUES ('02005', '005', '展示', 'Q1');
INSERT INTO `teach` VALUES ('03006', '007', '闭卷', 'W2');
INSERT INTO `teach` VALUES ('03007', '008', '开卷', 'E3');
INSERT INTO `teach` VALUES ('03008', '009', '通过制', 'S2');
INSERT INTO `teach` VALUES ('04009', '010', '开卷', 'T5');
INSERT INTO `teach` VALUES ('04010', '011', '闭卷', 'X3');
INSERT INTO `teach` VALUES ('04011', '012', '论文', 'I2');
INSERT INTO `teach` VALUES ('05013', '015', '平时成绩', 'P0');

-- ----------------------------
-- Table structure for teacher
-- ----------------------------
DROP TABLE IF EXISTS `teacher`;
CREATE TABLE `teacher`  (
  `tea_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tea_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tea_title` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `tea_salary` int(0) NOT NULL,
  `tea_college` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  PRIMARY KEY (`tea_id`) USING BTREE,
  INDEX `tea_in_col`(`tea_college`) USING BTREE,
  CONSTRAINT `tea_in_col` FOREIGN KEY (`tea_college`) REFERENCES `college` (`col_name`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher
-- ----------------------------
INSERT INTO `teacher` VALUES ('01001', '冯浩', '讲师', 10000, '人工智能学院');
INSERT INTO `teacher` VALUES ('01002', '李布林', '教授', 30001, '人工智能学院');
INSERT INTO `teacher` VALUES ('01015', '鲁智深', '辅导员', 20000, '人工智能学院');
INSERT INTO `teacher` VALUES ('02003', '马超', '副教授', 20000, '电子信息与光学工程学院');
INSERT INTO `teacher` VALUES ('02004', '杜珂', '讲师', 10000, '电子信息与光学工程学院');
INSERT INTO `teacher` VALUES ('02005', '刘备', '实验师', 15000, '电子信息与光学工程学院');
INSERT INTO `teacher` VALUES ('03006', '赵云', '讲师', 10000, '网络空间安全学院');
INSERT INTO `teacher` VALUES ('03007', '关羽', '实验员', 10000, '网络空间安全学院');
INSERT INTO `teacher` VALUES ('03008', '公孙离', '教授', 30000, '网络空间安全学院');
INSERT INTO `teacher` VALUES ('04009', '崔不理', '讲师', 10000, '计算机学院');
INSERT INTO `teacher` VALUES ('04010', '司徒全蛋', '操作员', 15000, '计算机学院');
INSERT INTO `teacher` VALUES ('04011', '姜维', '教授', 30000, '计算机学院');
INSERT INTO `teacher` VALUES ('05012', '董卓', '讲师', 10000, '软件学院');
INSERT INTO `teacher` VALUES ('05013', '貂蝉', '秘书长', 20000, '软件学院');
INSERT INTO `teacher` VALUES ('05014', '林冲', '教授', 30000, '软件学院');

-- ----------------------------
-- Table structure for teacher_login
-- ----------------------------
DROP TABLE IF EXISTS `teacher_login`;
CREATE TABLE `teacher_login`  (
  `tea_id` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `tea_pwd` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`tea_id`) USING BTREE,
  CONSTRAINT `tea_login` FOREIGN KEY (`tea_id`) REFERENCES `teacher` (`tea_id`) ON DELETE CASCADE ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of teacher_login
-- ----------------------------
INSERT INTO `teacher_login` VALUES ('01001', '123456');
INSERT INTO `teacher_login` VALUES ('01002', '123456');
INSERT INTO `teacher_login` VALUES ('01015', '123456');
INSERT INTO `teacher_login` VALUES ('02003', '123456');
INSERT INTO `teacher_login` VALUES ('02004', '123456');
INSERT INTO `teacher_login` VALUES ('02005', '123456');
INSERT INTO `teacher_login` VALUES ('03006', '123456');
INSERT INTO `teacher_login` VALUES ('03007', '123456');
INSERT INTO `teacher_login` VALUES ('03008', '123456');
INSERT INTO `teacher_login` VALUES ('04009', '123456');
INSERT INTO `teacher_login` VALUES ('04010', '123456');
INSERT INTO `teacher_login` VALUES ('04011', '123456');
INSERT INTO `teacher_login` VALUES ('05012', '123456');
INSERT INTO `teacher_login` VALUES ('05013', '123456');
INSERT INTO `teacher_login` VALUES ('05014', '123456');

-- ----------------------------
-- Table structure for undergraduate
-- ----------------------------
DROP TABLE IF EXISTS `undergraduate`;
CREATE TABLE `undergraduate`  (
  `stu_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_name` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_gender` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  `stu_adm_time` date NOT NULL,
  `stu_college` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `major_id` varchar(20) CHARACTER SET utf8 COLLATE utf8_general_ci NULL DEFAULT NULL,
  `class` varchar(255) CHARACTER SET utf8 COLLATE utf8_general_ci NOT NULL,
  PRIMARY KEY (`stu_id`) USING BTREE,
  INDEX `ug_in_col`(`stu_college`) USING BTREE,
  INDEX `ug_learn_maj`(`major_id`) USING BTREE,
  INDEX `ug_in_stuname`(`stu_name`) USING BTREE,
  INDEX `ug_in_stuadm`(`stu_adm_time`) USING BTREE,
  CONSTRAINT `ug_in_col` FOREIGN KEY (`stu_college`) REFERENCES `college` (`col_name`) ON DELETE SET NULL ON UPDATE CASCADE,
  CONSTRAINT `ug_in_stuadm` FOREIGN KEY (`stu_adm_time`) REFERENCES `student` (`stu_adm_time`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ug_in_stuid` FOREIGN KEY (`stu_id`) REFERENCES `student` (`stu_id`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ug_in_stuname` FOREIGN KEY (`stu_name`) REFERENCES `student` (`stu_name`) ON DELETE CASCADE ON UPDATE CASCADE,
  CONSTRAINT `ug_learn_maj` FOREIGN KEY (`major_id`) REFERENCES `major` (`maj_id`) ON DELETE SET NULL ON UPDATE CASCADE
) ENGINE = InnoDB CHARACTER SET = utf8 COLLATE = utf8_general_ci ROW_FORMAT = Dynamic;

-- ----------------------------
-- Records of undergraduate
-- ----------------------------
INSERT INTO `undergraduate` VALUES ('00003', '刘二', '男', '2021-09-13', '计算机学院', '08003K', '1');
INSERT INTO `undergraduate` VALUES ('00004', '赵四', '女', '2021-09-13', '人工智能学院', '08009K', '3');
INSERT INTO `undergraduate` VALUES ('98725', '张蛋', '男', '2019-09-10', '网络空间安全学院', '08001K', '5');

-- ----------------------------
-- View structure for stu_les
-- ----------------------------
DROP VIEW IF EXISTS `stu_les`;
CREATE ALGORITHM = UNDEFINED SQL SECURITY DEFINER VIEW `stu_les` AS select `student`.`stu_id` AS `stu_id`,`student`.`stu_name` AS `stu_name`,`learn`.`lesson_id` AS `lesson_id`,`learn`.`score` AS `score` from (`student` join `learn`) where (`student`.`stu_id` = `learn`.`stu_id`);

-- ----------------------------
-- Procedure structure for updata_tea1
-- ----------------------------
DROP PROCEDURE IF EXISTS `updata_tea1`;
delimiter ;;
CREATE PROCEDURE `updata_tea1`(in n varchar(255), in t varchar(255), in s INT, in i varchar(20))
BEGIN
IF s < 5000 
THEN
    SIGNAL SQLSTATE '45000';
ELSE 
    UPDATE teacher SET tea_name = n, tea_title = t, tea_salary = s WHERE tea_id = i;
END IF;
END
;;
delimiter ;

-- ----------------------------
-- Procedure structure for updata_teach
-- ----------------------------
DROP PROCEDURE IF EXISTS `updata_teach`;
delimiter ;;
CREATE PROCEDURE `updata_teach`(in l varchar(20), in e varchar(255), in c varchar(255), in i varchar(20), in le varchar(20))
BEGIN
    UPDATE lesson SET lesson_id = l WHERE lesson_id = le;
    UPDATE teach SET end_way = e, class = c WHERE tea_id = i;
END
;;
delimiter ;

SET FOREIGN_KEY_CHECKS = 1;
