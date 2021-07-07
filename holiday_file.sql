-- MariaDB dump 10.17  Distrib 10.4.8-MariaDB, for debian-linux-gnu (x86_64)
--
-- Host: localhost    Database: holidays
-- ------------------------------------------------------
-- Server version	10.4.8-MariaDB-1:10.4.8+maria~bionic-log

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `holiday_table`
--

DROP TABLE IF EXISTS `holiday_table`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `holiday_table` (
  `holiday` text DEFAULT NULL,
  `start_date` text DEFAULT NULL,
  `end_date` text DEFAULT NULL
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `holiday_table`
--

LOCK TABLES `holiday_table` WRITE;
/*!40000 ALTER TABLE `holiday_table` DISABLE KEYS */;
INSERT INTO `holiday_table` VALUES ('Martin Luther King Jr. Day','2022-01-17','2022-01-18'),('Daylight Saving Time starts','2022-03-13','2022-03-14'),('Independence Day','2022-07-04','2022-07-05'),('Halloween','2022-11-01','2022-10-31'),('Election Day (General Election)','2020-11-03','2020-11-04'),('Easter Sunday','2022-04-18','2022-04-17'),('Thanksgiving Day','2022-11-24','2022-11-25'),('New Year\'s Eve','2023-01-01','2022-12-31'),('Tax Day','2021-05-17','2021-05-18'),('Veterans Day','2021-11-12','2021-11-11'),('Presidents\' Day','2021-02-15','2021-02-16'),('Cinco de Mayo','2022-05-06','2022-05-05'),('Memorial Day','2022-05-31','2022-05-30'),('Labor Day','2022-09-05','2022-09-06'),('Christmas Day','2022-12-26','2022-12-25'),('New Year\'s Day','2020-01-01','2020-01-02'),('Juneteenth','2022-06-19','2022-06-20'),('Independence Day observed','2020-07-03','2020-07-04'),('Columbus Day','2022-10-11','2022-10-10'),('Daylight Saving Time ends','2020-11-01','2020-11-02'),('Christmas Eve','2020-12-25','2020-12-24'),('Day off for Christmas Day','2022-12-27','2022-12-26'),('First Day of Women\'s History Month','2020-03-01','2020-03-02'),('St. Patrick\'s Day','2020-03-18','2020-03-17'),('Father\'s Day','2021-06-21','2021-06-20'),('First Day of Hispanic Heritage Month','2021-09-15','2021-09-16'),('Native American Heritage Day','2020-11-28','2020-11-27'),('First Day of Black History Month','2020-02-01','2020-02-02'),('Inauguration Day (regional holiday)','2021-01-20','2021-01-21'),('Easter Monday','2020-04-14','2020-04-13'),('Mother\'s Day','2020-05-10','2020-05-11'),('Indigenous Peoples\' Day','2020-10-13','2020-10-12'),('Super Tuesday (regional holiday)','2020-03-04','2020-03-03'),('Valentine\'s Day','2022-02-14','2022-02-15'),('Election Day','2022-11-08','2022-11-09'),('Day off for New Year\'s Day','2021-12-31','2022-01-01'),('First Day of Asian Pacific American Heritage Month','2022-05-02','2022-05-01'),('First Day of LGBTQ+ Pride Month','2022-06-02','2022-06-01'),('First Day of American Indian Heritage Month','2022-11-02','2022-11-01');
/*!40000 ALTER TABLE `holiday_table` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-07-07 19:53:46
