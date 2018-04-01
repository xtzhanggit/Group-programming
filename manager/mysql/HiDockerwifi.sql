-- MySQL dump 10.13  Distrib 5.7.19, for Linux (x86_64)
--
-- Host: 127.0.0.1    Database: HiDockerwifi
-- ------------------------------------------------------
-- Server version	5.7.19

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
-- Table structure for table `equipdb`
--

DROP TABLE IF EXISTS `equipdb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `equipdb` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `equip` char(10) NOT NULL,
  `status` tinyint(3) unsigned NOT NULL,
  `signintime` varchar(30) NOT NULL,
  `dockername` varchar(30) DEFAULT NULL,
  `ipaddress` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `equipdb`
--

LOCK TABLES `equipdb` WRITE;
/*!40000 ALTER TABLE `equipdb` DISABLE KEYS */;
/*!40000 ALTER TABLE `equipdb` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `portdb`
--

DROP TABLE IF EXISTS `portdb`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!40101 SET character_set_client = utf8 */;
CREATE TABLE `portdb` (
  `id` int(10) unsigned NOT NULL AUTO_INCREMENT,
  `port` int(8) NOT NULL,
  `status` int(11) DEFAULT '0',
  `equip` varchar(30) DEFAULT NULL,
  `ipaddress` varchar(40) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=21 DEFAULT CHARSET=utf8;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `portdb`
--

LOCK TABLES `portdb` WRITE;
/*!40000 ALTER TABLE `portdb` DISABLE KEYS */;
INSERT INTO `portdb` VALUES (1,33333,0,NULL,NULL),(2,33334,0,NULL,NULL),(3,33335,0,NULL,NULL),(4,33336,0,NULL,NULL),(5,33337,0,NULL,NULL),(6,33338,0,NULL,NULL),(7,33339,0,NULL,NULL),(8,33340,0,NULL,NULL),(9,33341,0,NULL,NULL),(10,33342,0,NULL,NULL),(11,33343,0,NULL,NULL),(12,33344,0,NULL,NULL),(13,33345,0,NULL,NULL),(14,33346,0,NULL,NULL),(15,33347,0,NULL,NULL),(16,33348,0,NULL,NULL),(17,33349,0,NULL,NULL),(18,33350,0,NULL,NULL),(19,33351,0,NULL,NULL),(20,33352,0,NULL,NULL);
/*!40000 ALTER TABLE `portdb` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2017-08-14 10:49:02
