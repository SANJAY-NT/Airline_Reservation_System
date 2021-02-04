-- MySQL dump 10.13  Distrib 8.0.22, for Win64 (x86_64)
--
-- Host: localhost    Database: airline
-- ------------------------------------------------------
-- Server version	8.0.22

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
-- Table structure for table `booking`
--

DROP TABLE IF EXISTS `booking`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `booking` (
  `booking_id` int NOT NULL AUTO_INCREMENT,
  `booking_date` date NOT NULL,
  `booking_user_name` varchar(45) NOT NULL,
  `route_id` int NOT NULL,
  `seat_type` varchar(45) NOT NULL,
  `card_name` varchar(45) NOT NULL,
  `card_no` varchar(50) NOT NULL,
  `count` int DEFAULT NULL,
  PRIMARY KEY (`booking_id`),
  KEY `route_id_idx` (`route_id`),
  CONSTRAINT `route_id` FOREIGN KEY (`route_id`) REFERENCES `route` (`route_id`) ON DELETE CASCADE
) ENGINE=InnoDB AUTO_INCREMENT=61 DEFAULT CHARSET=utf8mb4 COLLATE=utf8mb4_0900_ai_ci;
/*!40101 SET character_set_client = @saved_cs_client */;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `booking_AFTER_INSERT` AFTER INSERT ON `booking` FOR EACH ROW BEGIN
declare x decimal(10,2);
declare y int;
declare z int;
if new.card_no then
	if new.booking_date >='20210201' then
		if new.seat_type = 'Economy' then
			set x = new.count*((select economy_cost from route r where r.route_id = new.route_id) * 0.18 + (select r.economy_cost from route r where r.route_id = new.route_id));
			insert into payment (booking_id,Total_cost) values (new.booking_id , x);
            set  y = (select c.economy_count from count c,route r where c.airline_id = r.airline_id and r.route_id = new.route_id) - new.count;
            set z = (select airline_id from route where route_id = new.route_id);
            update count set economy_count = y where count.airline_id = z;
		else
			set x = new.count*((select business_cost from route r where r.route_id = new.route_id) * 0.18 + (select r.business_cost from route r where r.route_id = new.route_id));
			insert into payment (booking_id,Total_cost) values (new.booking_id , x);
            set  y = (select c.business_count from count c,route r where c.airline_id = r.airline_id and r.route_id = new.route_id) - new.count;
            set z = (select airline_id from route where route_id = new.route_id);
            update count set business_count = y where count.airline_id = z;
		end if;
	end if;
    end if; 
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!50003 SET @saved_cs_client      = @@character_set_client */ ;
/*!50003 SET @saved_cs_results     = @@character_set_results */ ;
/*!50003 SET @saved_col_connection = @@collation_connection */ ;
/*!50003 SET character_set_client  = utf8mb4 */ ;
/*!50003 SET character_set_results = utf8mb4 */ ;
/*!50003 SET collation_connection  = utf8mb4_0900_ai_ci */ ;
/*!50003 SET @saved_sql_mode       = @@sql_mode */ ;
/*!50003 SET sql_mode              = 'STRICT_TRANS_TABLES,NO_ENGINE_SUBSTITUTION' */ ;
DELIMITER ;;
/*!50003 CREATE*/ /*!50017 DEFINER=`root`@`localhost`*/ /*!50003 TRIGGER `booking_BEFORE_DELETE` BEFORE DELETE ON `booking` FOR EACH ROW BEGIN
declare y int;
declare z int;
if old.booking_date >='20210201' then
	if old.seat_type = 'Economy' then
		set  y = (select c.economy_count from count c,route r where c.airline_id = r.airline_id and r.route_id = old.route_id) + old.count;
		set z = (select airline_id from route where route_id = old.route_id);
		update count set economy_count = y where count.airline_id = z;
	else
		set  y = (select c.business_count from count c,route r where c.airline_id = r.airline_id and r.route_id = old.route_id) + old.count;
		set z = (select airline_id from route where route_id = old.route_id);
		update count set business_count = y where count.airline_id = z;
	end if;
end if;
END */;;
DELIMITER ;
/*!50003 SET sql_mode              = @saved_sql_mode */ ;
/*!50003 SET character_set_client  = @saved_cs_client */ ;
/*!50003 SET character_set_results = @saved_cs_results */ ;
/*!50003 SET collation_connection  = @saved_col_connection */ ;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2021-02-04 19:31:54
