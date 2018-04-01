-- MySQL dump 10.13  Distrib 5.7.17, for Linux (x86_64)
--
-- Host: localhost    Database: iot_db
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
-- Table structure for table `equip_to_db`
--

DROP TABLE IF EXISTS `equip_to_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equip_to_db` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `USERDB` varchar(30) NOT NULL,
  `UUIDS` varchar(10) NOT NULL,
  `NOTES` text,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equip_to_db`
--

LOCK TABLES `equip_to_db` WRITE;
/*!40000 ALTER TABLE `equip_to_db` DISABLE KEYS */;
INSERT INTO `equip_to_db` VALUES (1,'joliu_db','0000-00001','test');
/*!40000 ALTER TABLE `equip_to_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iot_equip_db`
--

DROP TABLE IF EXISTS `iot_equip_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `iot_equip_db` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `PARAMS` varchar(30) NOT NULL,
  `UUIDS` varchar(10) NOT NULL,
  `VAL` tinyint(2) DEFAULT '0',
  `NOTES` text,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iot_equip_db`
--

LOCK TABLES `iot_equip_db` WRITE;
/*!40000 ALTER TABLE `iot_equip_db` DISABLE KEYS */;
INSERT INTO `iot_equip_db` VALUES (1,'equip_temperature','0000-00001',0,'test');
/*!40000 ALTER TABLE `iot_equip_db` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `iot_monitor_db`
--

DROP TABLE IF EXISTS `iot_monitor_db`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `iot_monitor_db` (
  `ID` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `PARAMS` varchar(30) NOT NULL,
  `VAL` varchar(20) DEFAULT '0',
  `NOTES` text,
  PRIMARY KEY (`ID`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `iot_monitor_db`
--

LOCK TABLES `iot_monitor_db` WRITE;
/*!40000 ALTER TABLE `iot_monitor_db` DISABLE KEYS */;
INSERT INTO `iot_monitor_db` VALUES (1,'room_temperature','24','test'),(2,'room_humidity','24','test'),(3,'room_alarm','0','test'),(4,'door_entrance_guard','0','test');
/*!40000 ALTER TABLE `iot_monitor_db` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-04-02  6:38:20

