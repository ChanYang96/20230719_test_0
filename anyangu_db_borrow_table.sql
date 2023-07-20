-- MySQL dump 10.13  Distrib 8.0.32, for Win64 (x86_64)
--
-- Host: localhost    Database: anyangu_db
-- ------------------------------------------------------
-- Server version	8.0.32

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!50503 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `borrow_table`
--

DROP TABLE IF EXISTS `borrow_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `borrow_table` (
  `B_name` varchar(20) NOT NULL,
  `quantity` int NOT NULL,
  `C_name` varchar(20) NOT NULL,
  `U_name` varchar(20) NOT NULL,
  `borrow_date` date NOT NULL,
  `deadline_date` date NOT NULL,
  `borrow_check` varchar(20) NOT NULL,
  KEY `B_name` (`B_name`),
  KEY `C_name` (`C_name`),
  KEY `U_name` (`U_name`),
  CONSTRAINT `borrow_table_ibfk_1` FOREIGN KEY (`B_name`) REFERENCES `book_table` (`B_name`) ON DELETE CASCADE,
  CONSTRAINT `borrow_table_ibfk_2` FOREIGN KEY (`C_name`) REFERENCES `card_table` (`C_name`) ON DELETE CASCADE,
  CONSTRAINT `borrow_table_ibfk_3` FOREIGN KEY (`U_name`) REFERENCES `card_table` (`U_name`) ON DELETE CASCADE
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `borrow_table`
--

LOCK TABLES `borrow_table` WRITE;
/*!40000 ALTER TABLE `borrow_table` DISABLE KEYS */;
INSERT INTO `borrow_table` VALUES ('역도학개론',5,'4903','장미란','2023-05-11','2023-05-25','반납'),('이제는 제대로 화내고 싶다',1,'5318','차범근','2023-06-02','2023-06-16','반납'),('혼자 공부하는 SQL',1,'4903','장미란','2023-05-30','2023-06-13','미반납'),('스포츠심리학 플러스',1,'9755','손흥민','2023-05-30','2023-06-13','미반납');
/*!40000 ALTER TABLE `borrow_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2023-05-31  3:09:43
