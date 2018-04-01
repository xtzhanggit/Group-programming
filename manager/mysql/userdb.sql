-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: userdb
-- ------------------------------------------------------
-- Server version	5.7.17

/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;
/*!40103 SET @OLD_TIME_ZONE=@@TIME_ZONE */;
/*!40103 SET TIME_ZONE='+00:00' */;
/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;

--
-- Table structure for table `user_equip_db`
--

DROP TABLE IF EXISTS `user_equip_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_equip_db` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `PARAMS` varchar(30) NOT NULL,
  `UUIDS` varchar(10) NOT NULL,
  `VAL` tinyint(4) DEFAULT '0',
  `NOTES` text,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_equip_db`
--

LOCK TABLES `user_equip_db` WRITE;
/*!40000 ALTER TABLE `user_equip_db` DISABLE KEYS */;
INSERT INTO `user_equip_db` VALUES (1,'equip_bracelet','0000-00001',0,'test');
/*!40000 ALTER TABLE `user_equip_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_info_db`
--

DROP TABLE IF EXISTS `user_info_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_info_db` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `PARAMS` varchar(30) NOT NULL,
  `VAL` char(8) NOT NULL,
  `NOTES` text,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=8 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_info_db`
--

LOCK TABLES `user_info_db` WRITE;
/*!40000 ALTER TABLE `user_info_db` DISABLE KEYS */;
INSERT INTO `user_info_db` VALUES (1,'user_name','joliu','test'),(2,'user_age','23','test'),(3,'user_weight','65','test'),(4,'user_height','165','test'),(5,'user_blood_sugar','165','test'),(6,'user_blood_pressure','120/60','test');
/*!40000 ALTER TABLE `user_info_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `user_monitor_db`
--

DROP TABLE IF EXISTS `user_monitor_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `user_monitor_db` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `PARAMS` varchar(30) NOT NULL,
  `VAL` char(8) NOT NULL,
  `NOTES` text,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `user_monitor_db`
--

LOCK TABLES `user_monitor_db` WRITE;
/*!40000 ALTER TABLE `user_monitor_db` DISABLE KEYS */;
INSERT INTO `user_monitor_db` VALUES (1,'body_body_temperature','37.5','test'),(2,'body_humidity','37.5','test'),(3,'body_heart_rate','64','test'),(4,'bed_pressure','64','test');
/*!40000 ALTER TABLE `user_monitor_db` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-02  5:58:49

