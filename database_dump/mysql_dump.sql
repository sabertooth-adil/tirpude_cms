-- MySQL dump 10.13  Distrib 8.0.18, for Win64 (x86_64)
--
-- Host: 15.206.60.193    Database: tirpude_cms
-- ------------------------------------------------------
-- Server version	5.7.28-0ubuntu0.16.04.2

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
-- Table structure for table `auth_group`
--

DROP TABLE IF EXISTS `auth_group`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(150) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_group_permissions`
--

DROP TABLE IF EXISTS `auth_group_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_group_permissions_group_id_permission_id_0cd325b0_uniq` (`group_id`,`permission_id`),
  KEY `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_group_permissio_permission_id_84c5c92e_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permissions_group_id_b120cbf9_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_permission`
--

DROP TABLE IF EXISTS `auth_permission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_permission_content_type_id_codename_01ab375a_uniq` (`content_type_id`,`codename`),
  CONSTRAINT `auth_permission_content_type_id_2f476e4b_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=173 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can view log entry',1,'view_logentry'),(5,'Can add permission',2,'add_permission'),(6,'Can change permission',2,'change_permission'),(7,'Can delete permission',2,'delete_permission'),(8,'Can view permission',2,'view_permission'),(9,'Can add group',3,'add_group'),(10,'Can change group',3,'change_group'),(11,'Can delete group',3,'delete_group'),(12,'Can view group',3,'view_group'),(13,'Can add user',4,'add_user'),(14,'Can change user',4,'change_user'),(15,'Can delete user',4,'delete_user'),(16,'Can view user',4,'view_user'),(17,'Can add content type',5,'add_contenttype'),(18,'Can change content type',5,'change_contenttype'),(19,'Can delete content type',5,'delete_contenttype'),(20,'Can view content type',5,'view_contenttype'),(21,'Can add session',6,'add_session'),(22,'Can change session',6,'change_session'),(23,'Can delete session',6,'delete_session'),(24,'Can view session',6,'view_session'),(25,'Can add academic session',7,'add_academicsession'),(26,'Can change academic session',7,'change_academicsession'),(27,'Can delete academic session',7,'delete_academicsession'),(28,'Can view academic session',7,'view_academicsession'),(29,'Can add applying concession',8,'add_applyingconcession'),(30,'Can change applying concession',8,'change_applyingconcession'),(31,'Can delete applying concession',8,'delete_applyingconcession'),(32,'Can view applying concession',8,'view_applyingconcession'),(33,'Can add blood group',9,'add_bloodgroup'),(34,'Can change blood group',9,'change_bloodgroup'),(35,'Can delete blood group',9,'delete_bloodgroup'),(36,'Can view blood group',9,'view_bloodgroup'),(37,'Can add cast',10,'add_cast'),(38,'Can change cast',10,'change_cast'),(39,'Can delete cast',10,'delete_cast'),(40,'Can view cast',10,'view_cast'),(41,'Can add category',11,'add_category'),(42,'Can change category',11,'change_category'),(43,'Can delete category',11,'delete_category'),(44,'Can view category',11,'view_category'),(45,'Can add city',12,'add_city'),(46,'Can change city',12,'change_city'),(47,'Can delete city',12,'delete_city'),(48,'Can view city',12,'view_city'),(49,'Can add course',13,'add_course'),(50,'Can change course',13,'change_course'),(51,'Can delete course',13,'delete_course'),(52,'Can view course',13,'view_course'),(53,'Can add day',14,'add_day'),(54,'Can change day',14,'change_day'),(55,'Can delete day',14,'delete_day'),(56,'Can view day',14,'view_day'),(57,'Can add degree',15,'add_degree'),(58,'Can change degree',15,'change_degree'),(59,'Can delete degree',15,'delete_degree'),(60,'Can view degree',15,'view_degree'),(61,'Can add gender',16,'add_gender'),(62,'Can change gender',16,'change_gender'),(63,'Can delete gender',16,'delete_gender'),(64,'Can view gender',16,'view_gender'),(65,'Can add lecture',17,'add_lecture'),(66,'Can change lecture',17,'change_lecture'),(67,'Can delete lecture',17,'delete_lecture'),(68,'Can view lecture',17,'view_lecture'),(69,'Can add module',18,'add_module'),(70,'Can change module',18,'change_module'),(71,'Can delete module',18,'delete_module'),(72,'Can view module',18,'view_module'),(73,'Can add mother tongue',19,'add_mothertongue'),(74,'Can change mother tongue',19,'change_mothertongue'),(75,'Can delete mother tongue',19,'delete_mothertongue'),(76,'Can view mother tongue',19,'view_mothertongue'),(77,'Can add nationality',20,'add_nationality'),(78,'Can change nationality',20,'change_nationality'),(79,'Can delete nationality',20,'delete_nationality'),(80,'Can view nationality',20,'view_nationality'),(81,'Can add physically challenged',21,'add_physicallychallenged'),(82,'Can change physically challenged',21,'change_physicallychallenged'),(83,'Can delete physically challenged',21,'delete_physicallychallenged'),(84,'Can view physically challenged',21,'view_physicallychallenged'),(85,'Can add religion',22,'add_religion'),(86,'Can change religion',22,'change_religion'),(87,'Can delete religion',22,'delete_religion'),(88,'Can view religion',22,'view_religion'),(89,'Can add reserved',23,'add_reserved'),(90,'Can change reserved',23,'change_reserved'),(91,'Can delete reserved',23,'delete_reserved'),(92,'Can view reserved',23,'view_reserved'),(93,'Can add screen',24,'add_screen'),(94,'Can change screen',24,'change_screen'),(95,'Can delete screen',24,'delete_screen'),(96,'Can view screen',24,'view_screen'),(97,'Can add section',25,'add_section'),(98,'Can change section',25,'change_section'),(99,'Can delete section',25,'delete_section'),(100,'Can view section',25,'view_section'),(101,'Can add semester',26,'add_semester'),(102,'Can change semester',26,'change_semester'),(103,'Can delete semester',26,'delete_semester'),(104,'Can view semester',26,'view_semester'),(105,'Can add state',27,'add_state'),(106,'Can change state',27,'change_state'),(107,'Can delete state',27,'delete_state'),(108,'Can view state',27,'view_state'),(109,'Can add time',28,'add_time'),(110,'Can change time',28,'change_time'),(111,'Can delete time',28,'delete_time'),(112,'Can view time',28,'view_time'),(113,'Can add twelveth or diploma',29,'add_twelvethordiploma'),(114,'Can change twelveth or diploma',29,'change_twelvethordiploma'),(115,'Can delete twelveth or diploma',29,'delete_twelvethordiploma'),(116,'Can view twelveth or diploma',29,'view_twelvethordiploma'),(117,'Can add user role',30,'add_userrole'),(118,'Can change user role',30,'change_userrole'),(119,'Can delete user role',30,'delete_userrole'),(120,'Can view user role',30,'view_userrole'),(121,'Can add user type',31,'add_usertype'),(122,'Can change user type',31,'change_usertype'),(123,'Can delete user type',31,'delete_usertype'),(124,'Can view user type',31,'view_usertype'),(125,'Can add year of admission',32,'add_yearofadmission'),(126,'Can change year of admission',32,'change_yearofadmission'),(127,'Can delete year of admission',32,'delete_yearofadmission'),(128,'Can view year of admission',32,'view_yearofadmission'),(129,'Can add user operation',33,'add_useroperation'),(130,'Can change user operation',33,'change_useroperation'),(131,'Can delete user operation',33,'delete_useroperation'),(132,'Can view user operation',33,'view_useroperation'),(133,'Can add tehsil',34,'add_tehsil'),(134,'Can change tehsil',34,'change_tehsil'),(135,'Can delete tehsil',34,'delete_tehsil'),(136,'Can view tehsil',34,'view_tehsil'),(137,'Can add subject',35,'add_subject'),(138,'Can change subject',35,'change_subject'),(139,'Can delete subject',35,'delete_subject'),(140,'Can view subject',35,'view_subject'),(141,'Can add sub cast',36,'add_subcast'),(142,'Can change sub cast',36,'change_subcast'),(143,'Can delete sub cast',36,'delete_subcast'),(144,'Can view sub cast',36,'view_subcast'),(145,'Can add stream or field',37,'add_streamorfield'),(146,'Can change stream or field',37,'change_streamorfield'),(147,'Can delete stream or field',37,'delete_streamorfield'),(148,'Can view stream or field',37,'view_streamorfield'),(149,'Can add postal code',38,'add_postalcode'),(150,'Can change postal code',38,'change_postalcode'),(151,'Can delete postal code',38,'delete_postalcode'),(152,'Can view postal code',38,'view_postalcode'),(153,'Can add district',39,'add_district'),(154,'Can change district',39,'change_district'),(155,'Can delete district',39,'delete_district'),(156,'Can view district',39,'view_district'),(157,'Can add degree stream or field',40,'add_degreestreamorfield'),(158,'Can change degree stream or field',40,'change_degreestreamorfield'),(159,'Can delete degree stream or field',40,'delete_degreestreamorfield'),(160,'Can view degree stream or field',40,'view_degreestreamorfield'),(161,'Can add user info',41,'add_userinfo'),(162,'Can change user info',41,'change_userinfo'),(163,'Can delete user info',41,'delete_userinfo'),(164,'Can view user info',41,'view_userinfo'),(165,'Can add address detail',42,'add_addressdetail'),(166,'Can change address detail',42,'change_addressdetail'),(167,'Can delete address detail',42,'delete_addressdetail'),(168,'Can view address detail',42,'view_addressdetail'),(169,'Can add academic info',43,'add_academicinfo'),(170,'Can change academic info',43,'change_academicinfo'),(171,'Can delete academic info',43,'delete_academicinfo'),(172,'Can view academic info',43,'view_academicinfo');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user`
--

DROP TABLE IF EXISTS `auth_user`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime(6) DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(150) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(150) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime(6) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$180000$TJJS4de32oOc$En4W62WxRizwms517572EAgvPrSaek9Vuoc4tPxgaPo=','2020-01-06 06:13:28.900351',1,'Admin','','','',1,1,'2020-01-03 07:35:22.853986');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_groups`
--

DROP TABLE IF EXISTS `auth_user_groups`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_groups_user_id_group_id_94350c0c_uniq` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_97559544_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_97559544_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_6a12ed8b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `auth_user_user_permissions`
--

DROP TABLE IF EXISTS `auth_user_user_permissions`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `auth_user_user_permissions_user_id_permission_id_14a6b632_uniq` (`user_id`,`permission_id`),
  KEY `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` (`permission_id`),
  CONSTRAINT `auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentication_academicinfo`
--

DROP TABLE IF EXISTS `authentication_academicinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentication_academicinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `roll_no` int(11) DEFAULT NULL,
  `school_name` varchar(100) DEFAULT NULL,
  `school_board` varchar(30) DEFAULT NULL,
  `school_place` varchar(30) DEFAULT NULL,
  `tenth_year_of_passing` date DEFAULT NULL,
  `tenth_marks` int(11) DEFAULT NULL,
  `tenth_out_of` int(11) DEFAULT NULL,
  `school_percentage` varchar(10) DEFAULT NULL,
  `college_name` varchar(100) DEFAULT NULL,
  `college_board_or_university` varchar(30) DEFAULT NULL,
  `college_place` varchar(30) DEFAULT NULL,
  `college_date_of_passing` date DEFAULT NULL,
  `college_total_marks` int(11) DEFAULT NULL,
  `college_marks_out_of` int(11) DEFAULT NULL,
  `college_percentage` varchar(30) DEFAULT NULL,
  `degree_college_name` varchar(100) DEFAULT NULL,
  `degree_college_board_or_university` varchar(100) DEFAULT NULL,
  `degree_college_place` varchar(100) DEFAULT NULL,
  `degree_college_date_of_passing` date DEFAULT NULL,
  `degree_college_total_marks` int(11) DEFAULT NULL,
  `degree_college_marks_out_of` int(11) DEFAULT NULL,
  `degree_college_percentage` int(11) DEFAULT NULL,
  `guardian_name` varchar(30) DEFAULT NULL,
  `occupation_of_guardian` varchar(30) DEFAULT NULL,
  `annual_income_of_guardian` varchar(30) DEFAULT NULL,
  `relationship_with_guardian` varchar(30) DEFAULT NULL,
  `guardian_mobile_no` varchar(30) DEFAULT NULL,
  `resume` varchar(100) DEFAULT NULL,
  `fk_academic_session_id` int(11) DEFAULT NULL,
  `fk_applying_concession_id` int(11) DEFAULT NULL,
  `fk_cast_id` int(11) DEFAULT NULL,
  `fk_category_id` int(11) DEFAULT NULL,
  `fk_course_id` int(11) DEFAULT NULL,
  `fk_degree_id` int(11) DEFAULT NULL,
  `fk_degree_stream_or_field_id` int(11) DEFAULT NULL,
  `fk_domicile_of_state_id` int(11) DEFAULT NULL,
  `fk_physically_challenged_id` int(11) DEFAULT NULL,
  `fk_reserved_id` int(11) DEFAULT NULL,
  `fk_sections_id` int(11) DEFAULT NULL,
  `fk_semesters_id` int(11) DEFAULT NULL,
  `fk_stream_or_field_id` int(11) DEFAULT NULL,
  `fk_sub_cast_id` int(11) DEFAULT NULL,
  `fk_twelveth_or_diploma_id` int(11) DEFAULT NULL,
  `fk_user_info_id` int(11) DEFAULT NULL,
  `fk_year_of_admission_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `authentication_acade_fk_academic_session__fd1af0e1_fk_master_fo` (`fk_academic_session_id`),
  KEY `authentication_acade_fk_applying_concessi_da7202db_fk_master_fo` (`fk_applying_concession_id`),
  KEY `authentication_acade_fk_cast_id_fe958616_fk_master_fo` (`fk_cast_id`),
  KEY `authentication_acade_fk_category_id_dc1a67c3_fk_master_fo` (`fk_category_id`),
  KEY `authentication_acade_fk_course_id_25c01a39_fk_master_fo` (`fk_course_id`),
  KEY `authentication_acade_fk_degree_id_4209d586_fk_master_fo` (`fk_degree_id`),
  KEY `authentication_acade_fk_degree_stream_or__e8d30a93_fk_master_fo` (`fk_degree_stream_or_field_id`),
  KEY `authentication_acade_fk_domicile_of_state_86d24356_fk_master_fo` (`fk_domicile_of_state_id`),
  KEY `authentication_acade_fk_physically_challe_8024a55a_fk_master_fo` (`fk_physically_challenged_id`),
  KEY `authentication_acade_fk_reserved_id_1edfd67d_fk_master_fo` (`fk_reserved_id`),
  KEY `authentication_acade_fk_sections_id_f11220d0_fk_master_fo` (`fk_sections_id`),
  KEY `authentication_acade_fk_semesters_id_38657f3f_fk_master_fo` (`fk_semesters_id`),
  KEY `authentication_acade_fk_stream_or_field_i_fc34a117_fk_master_fo` (`fk_stream_or_field_id`),
  KEY `authentication_acade_fk_sub_cast_id_94bc6ca1_fk_master_fo` (`fk_sub_cast_id`),
  KEY `authentication_acade_fk_twelveth_or_diplo_4bac71b5_fk_master_fo` (`fk_twelveth_or_diploma_id`),
  KEY `authentication_acade_fk_user_info_id_81f771e6_fk_authentic` (`fk_user_info_id`),
  KEY `authentication_acade_fk_year_of_admission_9d80b293_fk_master_fo` (`fk_year_of_admission_id`),
  CONSTRAINT `authentication_acade_fk_academic_session__fd1af0e1_fk_master_fo` FOREIGN KEY (`fk_academic_session_id`) REFERENCES `master_forms_academicsession` (`id`),
  CONSTRAINT `authentication_acade_fk_applying_concessi_da7202db_fk_master_fo` FOREIGN KEY (`fk_applying_concession_id`) REFERENCES `master_forms_applyingconcession` (`id`),
  CONSTRAINT `authentication_acade_fk_cast_id_fe958616_fk_master_fo` FOREIGN KEY (`fk_cast_id`) REFERENCES `master_forms_cast` (`id`),
  CONSTRAINT `authentication_acade_fk_category_id_dc1a67c3_fk_master_fo` FOREIGN KEY (`fk_category_id`) REFERENCES `master_forms_category` (`id`),
  CONSTRAINT `authentication_acade_fk_course_id_25c01a39_fk_master_fo` FOREIGN KEY (`fk_course_id`) REFERENCES `master_forms_course` (`id`),
  CONSTRAINT `authentication_acade_fk_degree_id_4209d586_fk_master_fo` FOREIGN KEY (`fk_degree_id`) REFERENCES `master_forms_degree` (`id`),
  CONSTRAINT `authentication_acade_fk_degree_stream_or__e8d30a93_fk_master_fo` FOREIGN KEY (`fk_degree_stream_or_field_id`) REFERENCES `master_forms_degreestreamorfield` (`id`),
  CONSTRAINT `authentication_acade_fk_domicile_of_state_86d24356_fk_master_fo` FOREIGN KEY (`fk_domicile_of_state_id`) REFERENCES `master_forms_state` (`id`),
  CONSTRAINT `authentication_acade_fk_physically_challe_8024a55a_fk_master_fo` FOREIGN KEY (`fk_physically_challenged_id`) REFERENCES `master_forms_physicallychallenged` (`id`),
  CONSTRAINT `authentication_acade_fk_reserved_id_1edfd67d_fk_master_fo` FOREIGN KEY (`fk_reserved_id`) REFERENCES `master_forms_reserved` (`id`),
  CONSTRAINT `authentication_acade_fk_sections_id_f11220d0_fk_master_fo` FOREIGN KEY (`fk_sections_id`) REFERENCES `master_forms_section` (`id`),
  CONSTRAINT `authentication_acade_fk_semesters_id_38657f3f_fk_master_fo` FOREIGN KEY (`fk_semesters_id`) REFERENCES `master_forms_semester` (`id`),
  CONSTRAINT `authentication_acade_fk_stream_or_field_i_fc34a117_fk_master_fo` FOREIGN KEY (`fk_stream_or_field_id`) REFERENCES `master_forms_streamorfield` (`id`),
  CONSTRAINT `authentication_acade_fk_sub_cast_id_94bc6ca1_fk_master_fo` FOREIGN KEY (`fk_sub_cast_id`) REFERENCES `master_forms_subcast` (`id`),
  CONSTRAINT `authentication_acade_fk_twelveth_or_diplo_4bac71b5_fk_master_fo` FOREIGN KEY (`fk_twelveth_or_diploma_id`) REFERENCES `master_forms_twelvethordiploma` (`id`),
  CONSTRAINT `authentication_acade_fk_user_info_id_81f771e6_fk_authentic` FOREIGN KEY (`fk_user_info_id`) REFERENCES `authentication_userinfo` (`id`),
  CONSTRAINT `authentication_acade_fk_year_of_admission_9d80b293_fk_master_fo` FOREIGN KEY (`fk_year_of_admission_id`) REFERENCES `master_forms_yearofadmission` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentication_academicinfo`
--

LOCK TABLES `authentication_academicinfo` WRITE;
/*!40000 ALTER TABLE `authentication_academicinfo` DISABLE KEYS */;
INSERT INTO `authentication_academicinfo` VALUES (1,NULL,'a','a','a','2020-01-01',100,100,'100','z','z','z','2020-01-01',100,100,'100','1','1','1','2020-01-01',100,100,100,'Adil Warsi','fsdf','3145','645645','8983291651','',NULL,1,1,2,1,1,1,1,1,2,1,1,1,1,1,1,3);
/*!40000 ALTER TABLE `authentication_academicinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentication_addressdetail`
--

DROP TABLE IF EXISTS `authentication_addressdetail`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentication_addressdetail` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `address` varchar(200) NOT NULL,
  `tehsil` varchar(100) NOT NULL,
  `pin_code` varchar(20) NOT NULL,
  `correspondence_address` varchar(200) DEFAULT NULL,
  `correspondence_tehsil` varchar(100) NOT NULL,
  `correspondence_pin_code` varchar(20) DEFAULT NULL,
  `fk_city_id` int(11) DEFAULT NULL,
  `fk_correspondence_city_id` int(11) DEFAULT NULL,
  `fk_correspondence_district_id` int(11) DEFAULT NULL,
  `fk_correspondence_state_id` int(11) DEFAULT NULL,
  `fk_district_id` int(11) DEFAULT NULL,
  `fk_state_id` int(11) DEFAULT NULL,
  `fk_user_info_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `authentication_addre_fk_city_id_ab97229d_fk_master_fo` (`fk_city_id`),
  KEY `authentication_addre_fk_correspondence_ci_8aa6ba16_fk_master_fo` (`fk_correspondence_city_id`),
  KEY `authentication_addre_fk_correspondence_di_cf943b01_fk_master_fo` (`fk_correspondence_district_id`),
  KEY `authentication_addre_fk_correspondence_st_d868895c_fk_master_fo` (`fk_correspondence_state_id`),
  KEY `authentication_addre_fk_district_id_c8622f21_fk_master_fo` (`fk_district_id`),
  KEY `authentication_addre_fk_state_id_b67b6c3e_fk_master_fo` (`fk_state_id`),
  KEY `authentication_addre_fk_user_info_id_51a17f71_fk_authentic` (`fk_user_info_id`),
  CONSTRAINT `authentication_addre_fk_city_id_ab97229d_fk_master_fo` FOREIGN KEY (`fk_city_id`) REFERENCES `master_forms_city` (`id`),
  CONSTRAINT `authentication_addre_fk_correspondence_ci_8aa6ba16_fk_master_fo` FOREIGN KEY (`fk_correspondence_city_id`) REFERENCES `master_forms_city` (`id`),
  CONSTRAINT `authentication_addre_fk_correspondence_di_cf943b01_fk_master_fo` FOREIGN KEY (`fk_correspondence_district_id`) REFERENCES `master_forms_district` (`id`),
  CONSTRAINT `authentication_addre_fk_correspondence_st_d868895c_fk_master_fo` FOREIGN KEY (`fk_correspondence_state_id`) REFERENCES `master_forms_state` (`id`),
  CONSTRAINT `authentication_addre_fk_district_id_c8622f21_fk_master_fo` FOREIGN KEY (`fk_district_id`) REFERENCES `master_forms_district` (`id`),
  CONSTRAINT `authentication_addre_fk_state_id_b67b6c3e_fk_master_fo` FOREIGN KEY (`fk_state_id`) REFERENCES `master_forms_state` (`id`),
  CONSTRAINT `authentication_addre_fk_user_info_id_51a17f71_fk_authentic` FOREIGN KEY (`fk_user_info_id`) REFERENCES `authentication_userinfo` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentication_addressdetail`
--

LOCK TABLES `authentication_addressdetail` WRITE;
/*!40000 ALTER TABLE `authentication_addressdetail` DISABLE KEYS */;
INSERT INTO `authentication_addressdetail` VALUES (1,'Ramdeo Baba HIll top','Aali','440013','Ramdeo Baba HIll top','Aali','440013',4166,1364,718,7,439,3,1),(2,'Ramdeo Baba HIll top','Anantnag','440013','Ramdeo Baba HIll top','Akola','440013',2048,10,327,27,196,2,2);
/*!40000 ALTER TABLE `authentication_addressdetail` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `authentication_userinfo`
--

DROP TABLE IF EXISTS `authentication_userinfo`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `authentication_userinfo` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(50) DEFAULT NULL,
  `first_name` varchar(30) DEFAULT NULL,
  `middle_name` varchar(30) DEFAULT NULL,
  `last_name` varchar(50) DEFAULT NULL,
  `profile_image` varchar(100) DEFAULT NULL,
  `email` varchar(50) DEFAULT NULL,
  `dob` date DEFAULT NULL,
  `phone_no` varchar(20) DEFAULT NULL,
  `phone_no2` varchar(20) DEFAULT NULL,
  `aadhar_no` varchar(20) DEFAULT NULL,
  `password` varchar(20) DEFAULT NULL,
  `registration_date` date DEFAULT NULL,
  `fk_blood_group_id` int(11) DEFAULT NULL,
  `fk_gender_id` int(11) DEFAULT NULL,
  `fk_mother_tongue_id` int(11) DEFAULT NULL,
  `fk_nationality_id` int(11) DEFAULT NULL,
  `fk_religion_id` int(11) DEFAULT NULL,
  `fk_user_role_id` int(11) DEFAULT NULL,
  `fk_user_type_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `authentication_useri_fk_blood_group_id_bf35815f_fk_master_fo` (`fk_blood_group_id`),
  KEY `authentication_useri_fk_gender_id_97e7f794_fk_master_fo` (`fk_gender_id`),
  KEY `authentication_useri_fk_mother_tongue_id_1771fc60_fk_master_fo` (`fk_mother_tongue_id`),
  KEY `authentication_useri_fk_nationality_id_8b0f3fa9_fk_master_fo` (`fk_nationality_id`),
  KEY `authentication_useri_fk_religion_id_dee8c85b_fk_master_fo` (`fk_religion_id`),
  KEY `authentication_useri_fk_user_role_id_3274c597_fk_master_fo` (`fk_user_role_id`),
  KEY `authentication_useri_fk_user_type_id_8cb2406e_fk_master_fo` (`fk_user_type_id`),
  CONSTRAINT `authentication_useri_fk_blood_group_id_bf35815f_fk_master_fo` FOREIGN KEY (`fk_blood_group_id`) REFERENCES `master_forms_bloodgroup` (`id`),
  CONSTRAINT `authentication_useri_fk_gender_id_97e7f794_fk_master_fo` FOREIGN KEY (`fk_gender_id`) REFERENCES `master_forms_gender` (`id`),
  CONSTRAINT `authentication_useri_fk_mother_tongue_id_1771fc60_fk_master_fo` FOREIGN KEY (`fk_mother_tongue_id`) REFERENCES `master_forms_mothertongue` (`id`),
  CONSTRAINT `authentication_useri_fk_nationality_id_8b0f3fa9_fk_master_fo` FOREIGN KEY (`fk_nationality_id`) REFERENCES `master_forms_nationality` (`id`),
  CONSTRAINT `authentication_useri_fk_religion_id_dee8c85b_fk_master_fo` FOREIGN KEY (`fk_religion_id`) REFERENCES `master_forms_religion` (`id`),
  CONSTRAINT `authentication_useri_fk_user_role_id_3274c597_fk_master_fo` FOREIGN KEY (`fk_user_role_id`) REFERENCES `master_forms_userrole` (`id`),
  CONSTRAINT `authentication_useri_fk_user_type_id_8cb2406e_fk_master_fo` FOREIGN KEY (`fk_user_type_id`) REFERENCES `master_forms_usertype` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `authentication_userinfo`
--

LOCK TABLES `authentication_userinfo` WRITE;
/*!40000 ALTER TABLE `authentication_userinfo` DISABLE KEYS */;
INSERT INTO `authentication_userinfo` VALUES (1,'Active','Shubham',NULL,'Paliwal','profile_images/Profile_2020-01-03_15_05_16.jpg','student@gmail.com','1995-10-30','8983291651',NULL,'333333333333','A@a12345','2020-01-03',1,1,NULL,1,NULL,NULL,1),(2,'Active','Adil','fdsfg','Warsi','profile_images/Profile_2020-01-03_15_14_55.jpg','faculty@gmail.com','1995-10-30','8983291651','21313123','444444444444','A@a12345','2020-01-03',1,1,NULL,1,NULL,1,2);
/*!40000 ALTER TABLE `authentication_userinfo` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_admin_log`
--

DROP TABLE IF EXISTS `django_admin_log`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime(6) NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_content_type_id_c4bce8eb_fk_django_co` (`content_type_id`),
  KEY `django_admin_log_user_id_c564eba6_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_content_type_id_c4bce8eb_fk_django_co` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  CONSTRAINT `django_admin_log_user_id_c564eba6_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=82 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
INSERT INTO `django_admin_log` VALUES (1,'2020-01-03 09:10:55.624654','1','Student',1,'[{\"added\": {}}]',31,1),(2,'2020-01-03 09:10:59.122104','2','Faculty',1,'[{\"added\": {}}]',31,1),(3,'2020-01-03 09:11:32.503304','1','Male',1,'[{\"added\": {}}]',16,1),(4,'2020-01-03 09:11:35.568906','2','Female',1,'[{\"added\": {}}]',16,1),(5,'2020-01-03 09:11:38.385611','3','Transgender',1,'[{\"added\": {}}]',16,1),(6,'2020-01-03 09:13:20.930775','1','MBA',1,'[{\"added\": {}}]',13,1),(7,'2020-01-03 09:13:23.655238','2','BBA',1,'[{\"added\": {}}]',13,1),(8,'2020-01-03 09:13:27.872619','3','BCCA',1,'[{\"added\": {}}]',13,1),(9,'2020-01-03 09:13:41.136609','1','I',1,'[{\"added\": {}}]',26,1),(10,'2020-01-03 09:13:48.285288','2','II',1,'[{\"added\": {}}]',26,1),(11,'2020-01-03 09:13:51.008099','3','III',1,'[{\"added\": {}}]',26,1),(12,'2020-01-03 09:13:54.493230','4','IV',1,'[{\"added\": {}}]',26,1),(13,'2020-01-03 09:13:57.511954','5','V',1,'[{\"added\": {}}]',26,1),(14,'2020-01-03 09:14:00.387651','6','VI',1,'[{\"added\": {}}]',26,1),(15,'2020-01-03 09:14:25.457455','1','A',1,'[{\"added\": {}}]',25,1),(16,'2020-01-03 09:14:28.237193','2','B',1,'[{\"added\": {}}]',25,1),(17,'2020-01-03 09:14:31.157639','3','C',1,'[{\"added\": {}}]',25,1),(18,'2020-01-03 09:15:21.520997','1','2017',1,'[{\"added\": {}}]',32,1),(19,'2020-01-03 09:15:24.339229','2','2018',1,'[{\"added\": {}}]',32,1),(20,'2020-01-03 09:15:27.265704','3','2019',1,'[{\"added\": {}}]',32,1),(21,'2020-01-03 09:26:50.558371','1','Adil-Warsi',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',41,1),(22,'2020-01-03 09:32:54.950274','1','Indian',1,'[{\"added\": {}}]',20,1),(23,'2020-01-03 09:32:57.817703','2','Other',1,'[{\"added\": {}}]',20,1),(24,'2020-01-03 09:33:13.077681','1','A-',1,'[{\"added\": {}}]',9,1),(25,'2020-01-03 09:33:16.580828','2','A+',1,'[{\"added\": {}}]',9,1),(26,'2020-01-03 09:33:20.072476','3','B-',1,'[{\"added\": {}}]',9,1),(27,'2020-01-03 09:33:23.358816','4','B+',1,'[{\"added\": {}}]',9,1),(28,'2020-01-03 09:33:26.224114','5','AB-',1,'[{\"added\": {}}]',9,1),(29,'2020-01-03 09:33:29.479176','6','AB+',1,'[{\"added\": {}}]',9,1),(30,'2020-01-03 09:35:42.255113','1','Open',1,'[{\"added\": {}}]',11,1),(31,'2020-01-03 09:35:45.175352','2','Reserved',1,'[{\"added\": {}}]',11,1),(32,'2020-01-03 09:35:55.443968','1','SC',1,'[{\"added\": {}}]',23,1),(33,'2020-01-03 09:35:58.062648','2','ST',1,'[{\"added\": {}}]',23,1),(34,'2020-01-03 09:36:04.080778','3','DT(A)',1,'[{\"added\": {}}]',23,1),(35,'2020-01-03 09:36:06.618215','4','NT(B)',1,'[{\"added\": {}}]',23,1),(36,'2020-01-03 09:36:09.143262','5','NT(C)',1,'[{\"added\": {}}]',23,1),(37,'2020-01-03 09:36:11.792067','6','NT(D)',1,'[{\"added\": {}}]',23,1),(38,'2020-01-03 09:36:23.531312','1','ST',1,'[{\"added\": {}}]',8,1),(39,'2020-01-03 09:36:26.006374','2','EBC',1,'[{\"added\": {}}]',8,1),(40,'2020-01-03 09:36:28.524099','3','SC',1,'[{\"added\": {}}]',8,1),(41,'2020-01-03 09:36:42.685928','1','MARATHA',1,'[{\"added\": {}}]',10,1),(42,'2020-01-03 09:36:45.318415','2','(HINDU ) SUTAR',1,'[{\"added\": {}}]',10,1),(43,'2020-01-03 09:36:47.863571','3','Hindi',1,'[{\"added\": {}}]',10,1),(44,'2020-01-03 09:36:50.783368','4','ADIWASI GOND',1,'[{\"added\": {}}]',10,1),(45,'2020-01-03 09:38:20.279835','1','A',1,'[{\"added\": {}}]',36,1),(46,'2020-01-03 09:38:23.914305','2','B',1,'[{\"added\": {}}]',36,1),(47,'2020-01-03 09:38:27.447938','3','A',1,'[{\"added\": {}}]',36,1),(48,'2020-01-03 09:38:31.244641','4','B',1,'[{\"added\": {}}]',36,1),(49,'2020-01-03 09:38:37.513841','5','A',1,'[{\"added\": {}}]',36,1),(50,'2020-01-03 09:38:41.541002','6','B',1,'[{\"added\": {}}]',36,1),(51,'2020-01-03 09:38:45.188281','7','A',1,'[{\"added\": {}}]',36,1),(52,'2020-01-03 09:38:49.282718','8','B',1,'[{\"added\": {}}]',36,1),(53,'2020-01-03 09:38:59.771099','1','A',1,'[{\"added\": {}}]',21,1),(54,'2020-01-03 09:39:03.020161','2','B',1,'[{\"added\": {}}]',21,1),(55,'2020-01-03 09:39:05.819378','3','C',1,'[{\"added\": {}}]',21,1),(56,'2020-01-03 09:39:47.975642','1','Diploma',1,'[{\"added\": {}}]',29,1),(57,'2020-01-03 09:39:50.738172','2','Twelveth',1,'[{\"added\": {}}]',29,1),(58,'2020-01-03 09:40:03.333552','1','Computer Technology',1,'[{\"added\": {}}]',37,1),(59,'2020-01-03 09:40:07.097496','2','Informaction Science & Engineering',1,'[{\"added\": {}}]',37,1),(60,'2020-01-03 09:40:10.626625','3','Mechanical Engineering',1,'[{\"added\": {}}]',37,1),(61,'2020-01-03 09:40:14.688369','4','Electrical & Electronics Engineering',1,'[{\"added\": {}}]',37,1),(62,'2020-01-03 09:40:22.315282','5','Arts',1,'[{\"added\": {}}]',37,1),(63,'2020-01-03 09:40:28.567918','6','Science',1,'[{\"added\": {}}]',37,1),(64,'2020-01-03 09:40:35.605798','1','B.E.',1,'[{\"added\": {}}]',15,1),(65,'2020-01-03 09:40:38.013808','2','B.Sc',1,'[{\"added\": {}}]',15,1),(66,'2020-01-03 09:40:40.514765','3','B.A.',1,'[{\"added\": {}}]',15,1),(67,'2020-01-03 09:40:42.994776','4','BBA',1,'[{\"added\": {}}]',15,1),(68,'2020-01-03 09:40:45.449126','5','B.Com',1,'[{\"added\": {}}]',15,1),(69,'2020-01-03 09:40:56.209492','1','Computer Technology',1,'[{\"added\": {}}]',40,1),(70,'2020-01-03 09:41:00.484329','2','Informaction Science & Engineering',1,'[{\"added\": {}}]',40,1),(71,'2020-01-03 09:41:04.692900','3','Mechanical Engineering',1,'[{\"added\": {}}]',40,1),(72,'2020-01-03 09:43:28.904587','2','Adil-Warsi',2,'[{\"changed\": {\"fields\": [\"Status\"]}}]',41,1),(73,'2020-01-03 09:43:40.074190','1','Faculty',1,'[{\"added\": {}}]',30,1),(74,'2020-01-03 09:43:49.643585','2','Adil-Warsi',2,'[{\"changed\": {\"fields\": [\"Fk user role\"]}}]',41,1),(75,'2020-01-06 06:16:57.948338','1','Shubham-Paliwal',2,'[{\"changed\": {\"fields\": [\"First name\", \"Last name\"]}}]',41,1),(76,'2020-01-06 06:18:37.167212','1','Monday',1,'[{\"added\": {}}]',14,1),(77,'2020-01-06 06:18:46.969619','2','Tuesday',1,'[{\"added\": {}}]',14,1),(78,'2020-01-06 06:18:52.588881','3','Wednesday',1,'[{\"added\": {}}]',14,1),(79,'2020-01-06 06:18:58.290927','4','Thursday',1,'[{\"added\": {}}]',14,1),(80,'2020-01-06 06:19:03.371660','5','Friday',1,'[{\"added\": {}}]',14,1),(81,'2020-01-06 06:19:06.976234','6','Saturday',1,'[{\"added\": {}}]',14,1);
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_content_type`
--

DROP TABLE IF EXISTS `django_content_type`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_model_76bd3d3b_uniq` (`app_label`,`model`)
) ENGINE=InnoDB AUTO_INCREMENT=44 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(43,'authentication','academicinfo'),(42,'authentication','addressdetail'),(41,'authentication','userinfo'),(5,'contenttypes','contenttype'),(7,'master_forms','academicsession'),(8,'master_forms','applyingconcession'),(9,'master_forms','bloodgroup'),(10,'master_forms','cast'),(11,'master_forms','category'),(12,'master_forms','city'),(13,'master_forms','course'),(14,'master_forms','day'),(15,'master_forms','degree'),(40,'master_forms','degreestreamorfield'),(39,'master_forms','district'),(16,'master_forms','gender'),(17,'master_forms','lecture'),(18,'master_forms','module'),(19,'master_forms','mothertongue'),(20,'master_forms','nationality'),(21,'master_forms','physicallychallenged'),(38,'master_forms','postalcode'),(22,'master_forms','religion'),(23,'master_forms','reserved'),(24,'master_forms','screen'),(25,'master_forms','section'),(26,'master_forms','semester'),(27,'master_forms','state'),(37,'master_forms','streamorfield'),(36,'master_forms','subcast'),(35,'master_forms','subject'),(34,'master_forms','tehsil'),(28,'master_forms','time'),(29,'master_forms','twelvethordiploma'),(33,'master_forms','useroperation'),(30,'master_forms','userrole'),(31,'master_forms','usertype'),(32,'master_forms','yearofadmission'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_migrations`
--

DROP TABLE IF EXISTS `django_migrations`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime(6) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=20 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'master_forms','0001_initial','2020-01-03 07:34:29.941930'),(2,'contenttypes','0001_initial','2020-01-03 07:34:38.897586'),(3,'auth','0001_initial','2020-01-03 07:34:39.977291'),(4,'admin','0001_initial','2020-01-03 07:34:41.897512'),(5,'admin','0002_logentry_remove_auto_add','2020-01-03 07:34:42.351019'),(6,'admin','0003_logentry_add_action_flag_choices','2020-01-03 07:34:42.417984'),(7,'contenttypes','0002_remove_content_type_name','2020-01-03 07:34:42.862521'),(8,'auth','0002_alter_permission_name_max_length','2020-01-03 07:34:42.949515'),(9,'auth','0003_alter_user_email_max_length','2020-01-03 07:34:43.050494'),(10,'auth','0004_alter_user_username_opts','2020-01-03 07:34:43.096495'),(11,'auth','0005_alter_user_last_login_null','2020-01-03 07:34:43.278537'),(12,'auth','0006_require_contenttypes_0002','2020-01-03 07:34:43.318562'),(13,'auth','0007_alter_validators_add_error_messages','2020-01-03 07:34:43.383506'),(14,'auth','0008_alter_user_username_max_length','2020-01-03 07:34:43.478866'),(15,'auth','0009_alter_user_last_name_max_length','2020-01-03 07:34:43.567196'),(16,'auth','0010_alter_group_name_max_length','2020-01-03 07:34:43.657254'),(17,'auth','0011_update_proxy_permissions','2020-01-03 07:34:43.788490'),(18,'sessions','0001_initial','2020-01-03 07:34:43.977794'),(19,'authentication','0001_initial','2020-01-03 07:43:47.960865');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `django_session`
--

DROP TABLE IF EXISTS `django_session`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime(6) NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_expire_date_a5c62663` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
INSERT INTO `django_session` VALUES ('7ysv5thn7o4ouq3y6aczubkhhrqlx3nm','NzYyZjJhOTEyNDc3MzE3ZDZjZDA5Zjc1M2ZkYmQzYWI2ZGQxYzg0Mjp7InVzZXJfaWQiOjJ9','2020-01-17 11:54:39.807251'),('ag6l31zd3brpztjp757xy7ervy5lrli4','NTA4NmU5N2VlN2ViMDg2YjFlYWIxYWMyNjg1M2I2ZGMwZmNhZWUxYTp7InVzZXJfaWQiOjJ9','2020-01-20 06:28:55.612394'),('dbc0y96qvja4goxpa9y8cb4ddirk470j','NTA4NmU5N2VlN2ViMDg2YjFlYWIxYWMyNjg1M2I2ZGMwZmNhZWUxYTp7InVzZXJfaWQiOjJ9','2020-01-20 06:29:02.424175'),('g3670vobt1grhccfi94p0dzzhn41e7ch','NzkwMzc5ZTE4OTI3NDIyODYwM2Q3NTEwNTY4OWE4N2IzOGE4ZWQ2Yzp7Il9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZjVjOWY1OWQ3ZmIwNDk3MDc4Y2Q4NTBlNTMyMzdlNTVmYTlhMWNmIiwidXNlcl9pZCI6MX0=','2020-01-17 11:33:24.902845'),('tnmi0aj00ze2arxyfow9pxcrt43yjvkj','NTA4NmU5N2VlN2ViMDg2YjFlYWIxYWMyNjg1M2I2ZGMwZmNhZWUxYTp7InVzZXJfaWQiOjJ9','2020-01-20 06:38:36.173848'),('w7ai2giicep3olko0di0zwd2z7mte9cc','NTIyNDFkY2VkMTdmZTZiMjVkMGYzMWM1MTAzNzAwYTJkNDg5NDg4ZTp7InVzZXJfaWQiOjIsIl9hdXRoX3VzZXJfaWQiOiIxIiwiX2F1dGhfdXNlcl9iYWNrZW5kIjoiZGphbmdvLmNvbnRyaWIuYXV0aC5iYWNrZW5kcy5Nb2RlbEJhY2tlbmQiLCJfYXV0aF91c2VyX2hhc2giOiIzZjVjOWY1OWQ3ZmIwNDk3MDc4Y2Q4NTBlNTMyMzdlNTVmYTlhMWNmIn0=','2020-01-20 06:13:28.921719'),('znatst33rcyex0s9due22duzbr73a3k8','NzYyZjJhOTEyNDc3MzE3ZDZjZDA5Zjc1M2ZkYmQzYWI2ZGQxYzg0Mjp7InVzZXJfaWQiOjJ9','2020-01-17 12:29:13.917567');
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_academicsession`
--

DROP TABLE IF EXISTS `master_forms_academicsession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_academicsession` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `start_date` date DEFAULT NULL,
  `end_date` date DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_academicsession`
--

LOCK TABLES `master_forms_academicsession` WRITE;
/*!40000 ALTER TABLE `master_forms_academicsession` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_forms_academicsession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_applyingconcession`
--

DROP TABLE IF EXISTS `master_forms_applyingconcession`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_applyingconcession` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `applying_concession` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_applyingconcession`
--

LOCK TABLES `master_forms_applyingconcession` WRITE;
/*!40000 ALTER TABLE `master_forms_applyingconcession` DISABLE KEYS */;
INSERT INTO `master_forms_applyingconcession` VALUES (1,'ST'),(2,'EBC'),(3,'SC');
/*!40000 ALTER TABLE `master_forms_applyingconcession` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_bloodgroup`
--

DROP TABLE IF EXISTS `master_forms_bloodgroup`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_bloodgroup` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `blood_group` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_bloodgroup`
--

LOCK TABLES `master_forms_bloodgroup` WRITE;
/*!40000 ALTER TABLE `master_forms_bloodgroup` DISABLE KEYS */;
INSERT INTO `master_forms_bloodgroup` VALUES (1,'A-'),(2,'A+'),(3,'B-'),(4,'B+'),(5,'AB-'),(6,'AB+');
/*!40000 ALTER TABLE `master_forms_bloodgroup` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_cast`
--

DROP TABLE IF EXISTS `master_forms_cast`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_cast` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `cast` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=5 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_cast`
--

LOCK TABLES `master_forms_cast` WRITE;
/*!40000 ALTER TABLE `master_forms_cast` DISABLE KEYS */;
INSERT INTO `master_forms_cast` VALUES (1,'MARATHA'),(2,'(HINDU ) SUTAR'),(3,'Hindi'),(4,'ADIWASI GOND');
/*!40000 ALTER TABLE `master_forms_cast` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_category`
--

DROP TABLE IF EXISTS `master_forms_category`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_category` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `category` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_category`
--

LOCK TABLES `master_forms_category` WRITE;
/*!40000 ALTER TABLE `master_forms_category` DISABLE KEYS */;
INSERT INTO `master_forms_category` VALUES (1,'Open'),(2,'Reserved');
/*!40000 ALTER TABLE `master_forms_category` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_city`
--

DROP TABLE IF EXISTS `master_forms_city`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_city` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `city` varchar(30) DEFAULT NULL,
  `fk_state_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `master_forms_city_fk_state_id_4128d03c_fk_master_forms_state_id` (`fk_state_id`),
  CONSTRAINT `master_forms_city_fk_state_id_4128d03c_fk_master_forms_state_id` FOREIGN KEY (`fk_state_id`) REFERENCES `master_forms_state` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7881 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_city`
--

LOCK TABLES `master_forms_city` WRITE;
/*!40000 ALTER TABLE `master_forms_city` DISABLE KEYS */;
INSERT INTO `master_forms_city` VALUES (1,'Achalpur',27),(2,'Aheri',27),(3,'Ahmadnagar (Ahmednagar)',27),(4,'Ahmadnagar Cantonment',27),(5,'Ahmadpur (Ahmedpur)',27),(6,'Ajra',27),(7,'Akkalkot',27),(8,'Akkalkuwa',27),(9,'Akluj',27),(10,'Akola',27),(11,'Akot',27),(12,'Alandi',27),(13,'Alibag',27),(14,'Amalner',27),(15,'Ambad',27),(16,'Ambarnath',27),(17,'Ambejogai (Ambajogai)',27),(18,'Ambepur',27),(19,'Amgaon bk.',27),(20,'Amgaon kh.',27),(21,'Amravati',27),(22,'Anantpur',27),(23,'Anjangaon',27),(24,'Arvi',27),(25,'Arvi',27),(26,'Asangaon',27),(27,'Ashta',27),(28,'Ashti',27),(29,'Ashti',27),(30,'Aurangabad [Aurangabad]',27),(31,'Aurangabad Cantonment',27),(32,'Ausa',27),(33,'Awadhan',27),(34,'Awalpur',27),(35,'Badlapur',27),(36,'Balapur',27),(37,'Balirampur',27),(38,'Ballarpur',27),(39,'Bamhni',27),(40,'Banda',27),(41,'Baramati',27),(42,'Barshi',27),(43,'Basmath',27),(44,'Bela',27),(45,'Bhadgaon',27),(46,'Bhadravati',27),(47,'Bhagur',27),(48,'Bhandara',27),(49,'Bhiwandi Nizampur',27),(50,'Bhokar',27),(51,'Bhokara',27),(52,'Bhokardan',27),(53,'Bhor',27),(54,'Bhum',27),(55,'Bhusawal',27),(56,'Bhuwaneshwar',27),(57,'Bid (Beed)',27),(58,'Bid Rural',27),(59,'Biloli',27),(60,'Birwadi',27),(61,'Boisar',27),(62,'Borgaon (Meghe)',27),(63,'Bori',27),(64,'Borivali Tarf Rahur',27),(65,'Borkhedi',27),(66,'Borli Panchtan',27),(67,'Brahmapuri (Bramhapuri)',27),(68,'Budhgaon',27),(69,'Buldana (Buldhana)',27),(70,'Burhanagar',27),(71,'Chakan',27),(72,'Chalisgaon',27),(73,'Chandkapur',27),(74,'Chandrapada',27),(75,'Chandrapur',27),(76,'Chandur',27),(77,'Chandurbazar',27),(78,'Chandur Railway',27),(79,'Chandvad (Chandwad)',27),(80,'Chanje',27),(81,'Chendhare',27),(82,'Chicholi',27),(83,'Chikhala',27),(84,'Chikhaldara',27),(85,'Chikhli',27),(86,'Chinchani',27),(87,'Chiplun',27),(88,'Chitegaon',27),(89,'Chopda',27),(90,'Dabhol',27),(91,'Dadar',27),(92,'Dahanu',27),(93,'Dandi',27),(94,'Dapoli Camp',27),(95,'Darewadi',27),(96,'Darwha',27),(97,'Daryapur (Banosa)',27),(98,'Dattapur Dhamangaon',27),(99,'Daund',27),(100,'Daund',27),(101,'Davlameti',27),(102,'Deglur',27),(103,'Dehu',27),(104,'Dehu Road',27),(105,'Deogiri',27),(106,'Deolali Cantonment',27),(107,'Deolali Pravara',27),(108,'Deoli',27),(109,'Deori',27),(110,'Desaiganj',27),(111,'Deulgaon Raja',27),(112,'Devrukh',27),(113,'Dhanegaon',27),(114,'Dharangaon',27),(115,'Dharmabad',27),(116,'Dharni',27),(117,'Dharur',27),(118,'Dhatau',27),(119,'Dhopatala',27),(120,'Dhule',27),(121,'Digdoh',27),(122,'Digras',27),(123,'Dondaicha-Warwade',27),(124,'Dudhani',27),(125,'Durgapur',27),(126,'Dyane',27),(127,'Eklahare',27),(128,'Erandol',27),(129,'Faizpur',27),(130,'Fulchur',27),(131,'Gadchiroli',27),(132,'Gadhinglaj',27),(133,'Gandhinagar',27),(134,'Ganeshpur',27),(135,'Gangakhed',27),(136,'Gangapur',27),(137,'Georai (Gevrai)',27),(138,'Ghatanji',27),(139,'Ghoti Budruk',27),(140,'Ghugus',27),(141,'Ghulewadi',27),(142,'Gimhavane',27),(143,'Godoli',27),(144,'Gokul Shirgaon',27),(145,'Gokunda',27),(146,'Gondiya (Gondia)',27),(147,'Gondpipri',27),(148,'Goregaon',27),(149,'Gotheghar',27),(150,'Greater Mumbai [Bombay]',27),(151,'Hadgaon',27),(152,'Hajarmachi',27),(153,'Harsul',27),(154,'Hinganghat',27),(155,'Hingoli',27),(156,'Hinjavadi',27),(157,'Hudkeshwar bk.',27),(158,'Hupari',27),(159,'Ichalkaranji',27),(160,'Igatpuri',27),(161,'Indapur',27),(162,'Isasani',27),(163,'Jalgaon',27),(164,'Jalgaon',27),(165,'Jalgaon Jamod',27),(166,'Jalna',27),(167,'Jalochi',27),(168,'Jamkhed',27),(169,'Jamner',27),(170,'Jasai',27),(171,'Jawhar',27),(172,'Jaysingpur',27),(173,'Jejuri',27),(174,'Jintur',27),(175,'Junnar',27),(176,'Kabnur',27),(177,'Kagal',27),(178,'Kaij',27),(179,'Kalamb',27),(180,'Kalambe Turf Thane',27),(181,'Kalameshwar',27),(182,'Kalamnuri',27),(183,'Kalher',27),(184,'Kalmath',27),(185,'Kalundre',27),(186,'Kambe (in: Kalyan subdistrict)',27),(187,'Kamptee',27),(188,'Kamptee Cantonment',27),(189,'Kandari',27),(190,'Kandhar',27),(191,'Kanhan (Pipri)',27),(192,'Kankavli',27),(193,'Kannad',27),(194,'Karad',27),(195,'Karad Rural',27),(196,'Karanja (Karanja Lad)',27),(197,'Karivali',27),(198,'Karjat',27),(199,'Karjat',27),(200,'Karle',27),(201,'Karmala',27),(202,'Kasara Budruk',27),(203,'Katai',27),(204,'Katangi Kala',27),(205,'Katkar',27),(206,'Katol',27),(207,'Kegaon',27),(208,'Khadkale',27),(209,'Khadki Bk',27),(210,'Khaira',27),(211,'Khamari',27),(212,'Khamgaon',27),(213,'Khandbara',27),(214,'Khapa',27),(215,'Khapar',27),(216,'Kharabwadi',27),(217,'Kharbav',27),(218,'Khardi',27),(219,'Kharghar',27),(220,'Khed',27),(221,'Khed',27),(222,'Kherdi',27),(223,'Khoni',27),(224,'Khopoli',27),(225,'Khuldabad',27),(226,'Kinwat',27),(227,'Kirkee Cantonment (Khadki)',27),(228,'Kodoli',27),(229,'Kolhapur',27),(230,'Kolki',27),(231,'Kon',27),(232,'Kondumal',27),(233,'Kopargaon',27),(234,'Koradi',27),(235,'Koregaon',27),(236,'Koregaon Bhima',27),(237,'Korochi',27),(238,'Kudal',27),(239,'Kudus',27),(240,'Kudwa',27),(241,'Kundalwadi',27),(242,'Kurduvadi',27),(243,'Kurkheda',27),(244,'Kurul',27),(245,'Kurundvad (Kuruntwad)',27),(246,'Kusgaon Budruk',27),(247,'Kuwarbav',27),(248,'Lanja',27),(249,'Lasalgaon',27),(250,'Latur',27),(251,'Loha',27),(252,'Lohara',27),(253,'Lonand',27),(254,'Lonar',27),(255,'Lonavala (Lonavla)',27),(256,'Madhavnagar',27),(257,'Mahabaleshwar',27),(258,'Mahad',27),(259,'Mahadula',27),(260,'Mahapoli',27),(261,'Mahindale',27),(262,'Maindargi',27),(263,'Majgaon',27),(264,'Makranifali',27),(265,'Maldhe',27),(266,'Malegaon',27),(267,'Malkapur',27),(268,'Malkapur',27),(269,'Malkapur',27),(270,'Malkapur',27),(271,'Malwan',27),(272,'Manchar',27),(273,'Mangalvedhe (Mangalwedha)',27),(274,'Mangrulpir',27),(275,'Manjlegaon',27),(276,'Manmad',27),(277,'Manor',27),(278,'Manwath',27),(279,'Masala',27),(280,'Matheran',27),(281,'Medankarwadi',27),(282,'Medha',27),(283,'Mehkar',27),(284,'Mharal Bk',27),(285,'Mhasla',27),(286,'Mhaswad',27),(287,'Mira-Bhayandar',27),(288,'Mohpa',27),(289,'Mohpada (Wasambe)',27),(290,'Morewadi',27),(291,'Morshi',27),(292,'Mouda',27),(293,'Mouje Anjanvel',27),(294,'Mowad',27),(295,'Mudkhed',27),(296,'Mukhed',27),(297,'Mul',27),(298,'Murbad',27),(299,'Murgud',27),(300,'Murmadi',27),(301,'Murtijapur (Murtajapur)',27),(302,'Murud Janjira',27),(303,'Murum',27),(304,'Nachane',27),(305,'Nadgaon Tarf Birwadi',27),(306,'Nagalwadi',27),(307,'Nagapur',27),(308,'Nagardeole',27),(309,'Nagothane (Nagothana)',27),(310,'Nagpur',27),(311,'Nakoda',27),(312,'Naldurg',27),(313,'Nalwadi',27),(314,'Nanda',27),(315,'Nanded Waghala',27),(316,'Nandgaon',27),(317,'Nandgaon Pode',27),(318,'Nandura',27),(319,'Nandurbar',27),(320,'Nanekarwadi',27),(321,'Narkhed',27),(322,'Narsala',27),(323,'Nashik [Nasik]',27),(324,'Natepute',27),(325,'Navghar',27),(326,'Navi Mumbai',27),(327,'Navi Mumbai Panvel Raigarh',27),(328,'Nawapur (Navapur)',27),(329,'Ner',27),(330,'Neral',27),(331,'Nideban',27),(332,'Nijampur',27),(333,'Nilanga',27),(334,'Nildoh',27),(335,'Nimbhore Budruk',27),(336,'Osmanabad',27),(337,'Owle',27),(338,'Ozar',27),(339,'Pachgaon',27),(340,'Pachora',27),(341,'Pachora Rural',27),(342,'Padagha',27),(343,'Padoli',27),(344,'Paithan',27),(345,'Palghar',27),(346,'Pali',27),(347,'Palidevad',27),(348,'Panchgani',27),(349,'Pandharkaoda',27),(350,'Pandharpur',27),(351,'Pandharpur',27),(352,'Panhala',27),(353,'Panvel',27),(354,'Paranda',27),(355,'Parbhani',27),(356,'Parli',27),(357,'Parola',27),(358,'Partur',27),(359,'Pasthal',27),(360,'Patan',27),(361,'Pathardi',27),(362,'Pathri',27),(363,'Patur',27),(364,'Pauni',27),(365,'Pen',27),(366,'Peth Umri',27),(367,'Phaltan',27),(368,'Pimpalgaon',27),(369,'Pimpalgaon Najik',27),(370,'Pimpri Chinchwad',27),(371,'Pipri',27),(372,'Pirangut',27),(373,'Poladpur',27),(374,'Pulgaon',27),(375,'Pune (Poona) [Poona]',27),(376,'Pune Cantonment (Pune Camp)',27),(377,'Purna',27),(378,'Purne',27),(379,'Pusad',27),(380,'Rahanal',27),(381,'Rahimatpur',27),(382,'Rahta Pimplas',27),(383,'Rahuri',27),(384,'Rajapur',27),(385,'Rajgurunagar (Khed)',27),(386,'Rajur',27),(387,'Rajur',27),(388,'Rajura',27),(389,'Ramtek',27),(390,'Ranjangaon S',27),(391,'Ratnagiri',27),(392,'Raver',27),(393,'Rees',27),(394,'Risama',27),(395,'Risod',27),(396,'Roha Ashtami',27),(397,'Saidapur',27),(398,'Sailu',27),(399,'Sakoli',27),(400,'Sakri',27),(401,'Salwad',27),(402,'Samangaon',27),(403,'Sanaswadi',27),(404,'Sangameshwar',27),(405,'Sangamner',27),(406,'Sangli Miraj Kupwad',27),(407,'Sangole',27),(408,'Sangramnagar',27),(409,'Sansari',27),(410,'Saravali',27),(411,'Sasti',27),(412,'Sasvad (Saswad)',27),(413,'Satana',27),(414,'Satara',27),(415,'Satara',27),(416,'Savda',27),(417,'Savner (Saoner)',27),(418,'Sawangi (Meghe)',27),(419,'Sawantwadi',27),(420,'Sawari Jawharnagar',27),(421,'Shahade (Shahada)',27),(422,'Shahapur',27),(423,'Shahapur',27),(424,'Shegaon',27),(425,'Shelar',27),(426,'Shendurjana',27),(427,'Shirdi',27),(428,'Shirgaon',27),(429,'Shirpur-Warwade',27),(430,'Shirur',27),(431,'Shivaji Nagar',27),(432,'Shivani',27),(433,'Shivar',27),(434,'Shivatkar (Nira)',27),(435,'Shrigonda',27),(436,'Shrirampur',27),(437,'Shrirampur',27),(438,'Shrivardhan',27),(439,'Sillewada',27),(440,'Sillod',27),(441,'Sindi',27),(442,'Sindi Turf Hindnagar',27),(443,'Sindkhed Raja',27),(444,'Sinnar',27),(445,'Sironcha Ry.',27),(446,'Solapur [Sholapur]',27),(447,'Sonegaon (Nipani)',27),(448,'Songirwadi Rural',27),(449,'Sonpeth',27),(450,'Soyagaon',27),(451,'Sundarkhed',27),(452,'Surgana',27),(453,'Tadali',27),(454,'Takalghat',27),(455,'Takali Pr. Chalisgaon',27),(456,'Talegaon Dabhade',27),(457,'Talode',27),(458,'Tamgaon',27),(459,'Tarapur',27),(460,'Tasgaon',27),(461,'Tekadi',27),(462,'Telhara',27),(463,'Thana',27),(464,'Thane',27),(465,'Tirora',27),(466,'Trimbak',27),(467,'Tuljapur',27),(468,'Tumsar',27),(469,'Uchgaon',27),(470,'Udgir',27),(471,'Ujalaiwadi',27),(472,'Ulhasnagar',27),(473,'Umarga',27),(474,'Umari Pr. Akola',27),(475,'Umarkhed',27),(476,'Umarsara',27),(477,'Umbar Pada Nandade',27),(478,'Umred',27),(479,'Umri Pragane Balapur',27),(480,'Uran',27),(481,'Uran Islampur',27),(482,'Urjanagar',27),(483,'Utekhol',27),(484,'Vada',27),(485,'Vadfalya',27),(486,'Vadgaon Kasba (Peth Vadgaon)',27),(487,'Vadghar',27),(488,'Vaijapur',27),(489,'Vangani',27),(490,'Varangaon',27),(491,'Vasai-Virar City',27),(492,'Vashind',27),(493,'Vengurla',27),(494,'Vikramgad',27),(495,'Vilholi',27),(496,'Visapur',27),(497,'Vita',27),(498,'Wadagaon (Vadgaon)',27),(499,'Waddhamana',27),(500,'Wadgaon Kolhati',27),(501,'Wadgaon Road',27),(502,'Wadi',27),(503,'Wadi Ratnagiri',27),(504,'Waghapur',27),(505,'Waghoda',27),(506,'Wagholi',27),(507,'Wai',27),(508,'Wajegaon',27),(509,'Walani',27),(510,'Waluj Bk.',27),(511,'Walwadi',27),(512,'Wanadongri',27),(513,'Wani',27),(514,'Wardha',27),(515,'Warora',27),(516,'Warthi',27),(517,'Warud',27),(518,'Warud',27),(519,'Washim',27),(520,'Yavatmal',27),(521,'Yavatmal R',27),(522,'Yawal',27),(523,'Yerkheda',27),(524,'Yevla (Yeola)',27),(525,'Yewalewadi',27),(526,'Zadgaon',27),(527,'Zotirpada',27),(528,'Bakultala',35),(529,'Bambooflat (Bombooflat)',35),(530,'Garacharma',35),(531,'Port Blair',35),(532,'Prothrapur',35),(533,'Adoni',28),(534,'Akkarampalle',28),(535,'Amadalavalasa (Amudalavalasa)',28),(536,'Amalapuram',28),(537,'Anakapalle',28),(538,'Anantapur',28),(539,'Anantapur',28),(540,'Arempudi',28),(541,'Avilala',28),(542,'Badvel',28),(543,'Balaga',28),(544,'Banaganapalle (Banganapalle)',28),(545,'Bandarulanka',28),(546,'Banumukkala',28),(547,'Bapatla',28),(548,'Bethamcherla',28),(549,'Bheemunipatnam',28),(550,'Bhimavaram',28),(551,'Bobbili',28),(552,'Bowluvada',28),(553,'Buja Buja Nellore',28),(554,'Cheepurupalle (Cheepurupalli)',28),(555,'Chennamukkapalle',28),(556,'Cherlopalle',28),(557,'Chidiga',28),(558,'Chilakaluripet',28),(559,'Chintalavalasa',28),(560,'Chintapalle',28),(561,'Chirala',28),(562,'Chirala',28),(563,'Chittoor',28),(564,'Chodavaram',28),(565,'Cumbum',28),(566,'Dharmavaram',28),(567,'Dhone (Dronachalam)',28),(568,'Dommara Nandyala',28),(569,'Dowleswaram',28),(570,'Dwarakatirumala',28),(571,'Eluru',28),(572,'Gajapathinagaram',28),(573,'Gavaravaram',28),(574,'Giddaluru',28),(575,'Gooty',28),(576,'Gopavaram',28),(577,'Gudivada',28),(578,'Gudivada',28),(579,'Gudur',28),(580,'Guntakal',28),(581,'Guntupalle',28),(582,'Guntur',28),(583,'Hindupur',28),(584,'Hiramandalam',28),(585,'Hukumpeta',28),(586,'Ibrahimpatnam',28),(587,'Ichchapuram',28),(588,'Jaggaiahpet (Jaggayyapeta)',28),(589,'Jammalamadugu',28),(590,'Jarjapupeta',28),(591,'Kadapa (Cuddapah)',28),(592,'Kadiri',28),(593,'Kakinada',28),(594,'Kakkalapalle',28),(595,'Kalyandurg',28),(596,'Kanapaka',28),(597,'Kandukur',28),(598,'Kanigiri U',28),(599,'Kankipadu',28),(600,'Kantabamsuguda',28),(601,'Kanuru',28),(602,'Katheru',28),(603,'Kavali',28),(604,'Kondapalle (Kondapalli)',28),(605,'Kothavalasa',28),(606,'Kovvur',28),(607,'Kuppam',28),(608,'Kurnool (incl. Kallur)',28),(609,'L.A.Sagaram',28),(610,'Macherla',28),(611,'Machilipatnam',28),(612,'Madanapalle',28),(613,'Malicherla',28),(614,'Mamidalapadu',28),(615,'Mandapeta',28),(616,'Mangalagiri',28),(617,'Mangalam',28),(618,'Mangampeta',28),(619,'Mangasamudram',28),(620,'Markapur',28),(621,'Modameedipalle',28),(622,'Moragudi',28),(623,'Morampudi',28),(624,'Muddanur',28),(625,'Mulaguntapadu',28),(626,'Mulakuddu',28),(627,'Murakambattu',28),(628,'Nadim Tiruvuru',28),(629,'Nagari',28),(630,'Nagireddipalle',28),(631,'Nakkapalle',28),(632,'Nandyal',28),(633,'Narasannapeta',28),(634,'Narasapur',28),(635,'Narasaraopet',28),(636,'Narayanapuram',28),(637,'Narayanavanam',28),(638,'Narsipatnam',28),(639,'Nellimarla',28),(640,'Nellore',28),(641,'Nidadavole (Nidadavolu)',28),(642,'Nuzvid',28),(643,'Ongole',28),(644,'Palacole (Palakollu)',28),(645,'Palakonda',28),(646,'Palamaner',28),(647,'Palasa Kasibugga',28),(648,'Pamur',28),(649,'Papampeta',28),(650,'Parvathipuram',28),(651,'Payakaraopeta',28),(652,'Peda Boddepalle',28),(653,'Pedana',28),(654,'Peddapuram',28),(655,'Perur',28),(656,'Piduguralla',28),(657,'Pileru',28),(658,'Pithapuram',28),(659,'Podili',28),(660,'Ponduru',28),(661,'Ponnur',28),(662,'Poranki',28),(663,'Prasadampadu',28),(664,'Proddatur',28),(665,'Pulivendla (Pulivendula)',28),(666,'Punganur',28),(667,'Puttur',28),(668,'Rajahmundry',28),(669,'Rajam',28),(670,'Rajampet',28),(671,'Ramachandrapuram',28),(672,'Ramanayyapeta',28),(673,'Ramapuram',28),(674,'Ramavarappadu',28),(675,'Rameswaram',28),(676,'Rampachodavaram',28),(677,'Rayachoti',28),(678,'Rayadurg',28),(679,'Renigunta',28),(680,'Repalle',28),(681,'Salur',28),(682,'Samalkot',28),(683,'Sanivarapupeta',28),(684,'Satrampadu',28),(685,'Sattenapalle',28),(686,'Singarayakonda',28),(687,'Somandepalle',28),(688,'Sompeta',28),(689,'Srikakulam',28),(690,'Srikalahasti',28),(691,'Sriramnagar',28),(692,'Sulluru (Sullurpeta)',28),(693,'Suryaraopeta',28),(694,'Tada Khandrika',28),(695,'Tadepalle',28),(696,'Tadepalligudem',28),(697,'Tadigadapa',28),(698,'Tadpatri (Tadipatri)',28),(699,'Tangellamudi',28),(700,'Tanuku',28),(701,'Tekkali',28),(702,'Tenali',28),(703,'Thummalamenta',28),(704,'Tiruchanur',28),(705,'Tirumala',28),(706,'Tirupati',28),(707,'Tirupati NMA',28),(708,'Tummikapalle',28),(709,'Tuni',28),(710,'Upper Sileru Project Site Camp',28),(711,'Uravakonda',28),(712,'Vaddeswaram',28),(713,'Venkatagiri',28),(714,'Veparala',28),(715,'Vetapalem',28),(716,'Vijayawada',28),(717,'Vinnamala',28),(718,'Vinukonda',28),(719,'Visakhapatnam [Vishakhapatnam]',28),(720,'Vizianagaram',28),(721,'Yelamanchili',28),(722,'Yemmiganur',28),(723,'Yenamalakuduru',28),(724,'Yenumalapalle',28),(725,'Yerrabalem',28),(726,'Yerraguntla',28),(727,'Aalo (Along)',12),(728,'Anini',12),(729,'Basar',12),(730,'Boleng',12),(731,'Bomdila',12),(732,'Changlang',12),(733,'Daporijo',12),(734,'Deomali',12),(735,'Dirang',12),(736,'Hawai',12),(737,'Itanagar',12),(738,'Jairampur',12),(739,'Khonsa',12),(740,'Koloriang',12),(741,'Longding',12),(742,'Miao',12),(743,'Naharlagun',12),(744,'Namsai',12),(745,'Pasighat',12),(746,'Roing',12),(747,'Rupa',12),(748,'Sagalee',12),(749,'Seppa',12),(750,'Tawang',12),(751,'Tezu',12),(752,'Yingkiong',12),(753,'Ziro',12),(754,'Abhayapuri',18),(755,'Ambicapur Pt VI',18),(756,'Ambicapur Pt VIII',18),(757,'Ambikapur Part-X',18),(758,'Amguri',18),(759,'Amin Gaon',18),(760,'Anand Nagar',18),(761,'Asudubi',18),(762,'Azara',18),(763,'Badarpur',18),(764,'Badarpur Railway Town',18),(765,'Bahbari Gaon',18),(766,'Bali Koria',18),(767,'Bamun Sualkuchi',18),(768,'Bangaon',18),(769,'Barbari (AMC Area)',18),(770,'Barika Chuburi',18),(771,'Barpathar',18),(772,'Barpeta',18),(773,'Barpeta Road',18),(774,'Barua Bari Gaon',18),(775,'Basugaon',18),(776,'Batarashi',18),(777,'Belsor',18),(778,'Bhalukdubi',18),(779,'Bhuragaon Rev. Town',18),(780,'Bihpuria',18),(781,'Bijni',18),(782,'Bilasipara',18),(783,'Biswanath Chariali',18),(784,'Bohari',18),(785,'Bokajan',18),(786,'Bokakhat',18),(787,'Bongaigaon',18),(788,'Borgolai Grant No.11',18),(789,'Borpukhuri',18),(790,'Chabua',18),(791,'Chalantapara Pt IV',18),(792,'Changsari',18),(793,'Chapakhowa Town',18),(794,'Chapar',18),(795,'Chapra',18),(796,'Charingia Gaon',18),(797,'Chatibor Gaon',18),(798,'Chekonidhara',18),(799,'Chota Haibor (Choto Haibor)',18),(800,'Dahali',18),(801,'Damara Patpara',18),(802,'Dergaon',18),(803,'Dhakuakhana',18),(804,'Dharapur',18),(805,'Dhekiajuli',18),(806,'Dhekorgorha',18),(807,'Dhemaji',18),(808,'Dhing',18),(809,'Dhubri',18),(810,'Dibrugarh',18),(811,'Digaru Gaon (Digarubar Gaon)',18),(812,'Digboi',18),(813,'Digboi Oil Town',18),(814,'Digheli',18),(815,'Dimaruguri',18),(816,'Diphu',18),(817,'Doboka (Dabaka)',18),(818,'Dokmoka',18),(819,'Donkamokam',18),(820,'Doom Dooma',18),(821,'Dudhpatil Pt V',18),(822,'Dudhpatil Pt VI',18),(823,'Duliajan Oil Town',18),(824,'Durga Nagar Part-V',18),(825,'Forest Village Lakhipathar',18),(826,'Garal',18),(827,'Gauripur',18),(828,'Gerimari Chapori',18),(829,'Goalpara',18),(830,'Gobindapur',18),(831,'Gohpur',18),(832,'Golaghat',18),(833,'Golaghatia Basti',18),(834,'Golokganj',18),(835,'Gossaigaon',18),(836,'Gutlong Gaon',18),(837,'Guwahati [Gauhati]',18),(838,'Haflong',18),(839,'Hailakandi',18),(840,'Hamren',18),(841,'Hojai',18),(842,'Howli (Howly)',18),(843,'Howraghat',18),(844,'Irongmara',18),(845,'Jagiroad',18),(846,'Jalah',18),(847,'Jamunamukh',18),(848,'Jhagra Pt.III',18),(849,'Jonai Bazar',18),(850,'Jorhat',18),(851,'Kachujan Gaon',18),(852,'Kahi Kuchi',18),(853,'Kakaya',18),(854,'Kalaigaon (Town Part)',18),(855,'Kamalabaria N.C.',18),(856,'Kampur Town',18),(857,'Kanakpur I',18),(858,'Kanakpur Part-II',18),(859,'Kanisail Pt I',18),(860,'Karimganj',18),(861,'Katirail T.E.',18),(862,'Khaira Bari',18),(863,'Kharijapikon',18),(864,'Kharupatia (Kharupetia)',18),(865,'Kochpara',18),(866,'Kokrajhar',18),(867,'Kumar Kaibarta Gaon',18),(868,'Laharijan Natun Bosti',18),(869,'Lakhi Nepali',18),(870,'Lakhipur',18),(871,'Lakhipur',18),(872,'Lala',18),(873,'Lanka',18),(874,'Lido Tikok',18),(875,'Lido Town',18),(876,'Lumding',18),(877,'Lumding Railway Colony',18),(878,'Mahur',18),(879,'Maibong (Maibang)',18),(880,'Mairabari Town',18),(881,'Majarkuri',18),(882,'Majgaon',18),(883,'Majir Gaon',18),(884,'Makum',18),(885,'Mangaldoi',18),(886,'Mankachar',18),(887,'Margherita',18),(888,'Mariani',18),(889,'Marigaon (Morigaon)',18),(890,'Marowa',18),(891,'Mohmaiki',18),(892,'Moranhat',18),(893,'Moran Town',18),(894,'Morongial',18),(895,'Mosli Pt I',18),(896,'Nagaon',18),(897,'Naharkatiya',18),(898,'Nahira',18),(899,'Nakhula Grant',18),(900,'Nalbari',18),(901,'Namrup',18),(902,'Narayanpur',18),(903,'Naubaisa Goan',18),(904,'Nazira',18),(905,'New Bongaigaon Railway Colony',18),(906,'Nidanpur Pt-II',18),(907,'Niz-Bahjani',18),(908,'Niz-Hajo',18),(909,'Niz Katigorah Pt III',18),(910,'Niz - Mankata',18),(911,'No.2 Goreswar',18),(912,'North Guwahati',18),(913,'North Lakhimpur',18),(914,'Nowsolia Gaon',18),(915,'Numaligarh Refinery Township',18),(916,'Padmabil',18),(917,'Palasbari',18),(918,'Parlli Part',18),(919,'Pathsala',18),(920,'Pipalibari',18),(921,'Pub - Dhaniram Pather',18),(922,'Raha',18),(923,'Rangapara',18),(924,'Rangia (Rangiya)',18),(925,'Rupahi Town',18),(926,'Rupiabathan',18),(927,'Salakati',18),(928,'Salpara Molandubi Pt.-I',18),(929,'Sanpara',18),(930,'Sapatgram',18),(931,'Sarbhog',18),(932,'Sarpara',18),(933,'Sarthebari',18),(934,'Sarupathar',18),(935,'Sarupathar Bengali',18),(936,'Sepon',18),(937,'Silapathar',18),(938,'Silchar',18),(939,'Silchar Part-X',18),(940,'Simaluguri',18),(941,'Sivasagar',18),(942,'Sonapur Gaon',18),(943,'Sonari',18),(944,'Sualkuchi',18),(945,'Takhlibilar Pathar',18),(946,'Tangla',18),(947,'Tarapur Pt VI',18),(948,'Tarapur VII',18),(949,'Tegheria',18),(950,'Teok',18),(951,'Tezpur',18),(952,'Thekashu Pt-I',18),(953,'Thekashu Pt.-II',18),(954,'Tihu',18),(955,'Tinsukia',18),(956,'Titabor Town',18),(957,'Tupkhana Pt I',18),(958,'Udalguri (Odalguri)',18),(959,'Udiana',18),(960,'Umrangso',18),(961,'Upar Hali',18),(962,'Uttar Athiabari',18),(963,'Uttar Krishnapur Part-I',18),(964,'Uttar Krishnapur Pt III',18),(965,'Amarpur',10),(966,'Anwari',10),(967,'Araria',10),(968,'Areraj',10),(969,'Arrah',10),(970,'Arwal',10),(971,'Asarganj',10),(972,'Aurangabad',10),(973,'Bagaha',10),(974,'Bahadurganj',10),(975,'Bahadurpur',10),(976,'Bairgania',10),(977,'Bakhri',10),(978,'Bakhtiarpur',10),(979,'Balia',10),(980,'Banka',10),(981,'Banmankhi Bazar',10),(982,'Bara',10),(983,'Barahiya',10),(984,'Barauli',10),(985,'Barauni',10),(986,'Barbigha',10),(987,'Barh',10),(988,'Begusarai',10),(989,'Behea',10),(990,'Belsand',10),(991,'Benipur',10),(992,'Bettiah',10),(993,'Bhabua',10),(994,'Bhadauni',10),(995,'Bhagalpur',10),(996,'Bhagirathpur',10),(997,'Bhardua',10),(998,'Bhuindhara',10),(999,'Bihar Sharif',10),(1000,'Bihat',10),(1001,'Bihta',10),(1002,'Bikram',10),(1003,'Bikramganj',10),(1004,'Birpur',10),(1005,'Bodh Gaya',10),(1006,'Buxar',10),(1007,'Chakia',10),(1008,'Chanari',10),(1009,'Chanpatia',10),(1010,'Chapra (Chhapra)',10),(1011,'Colgong (Kahalgaon)',10),(1012,'Colgong',10),(1013,'Dalsinghsarai',10),(1014,'Damodarpur',10),(1015,'Darbhanga',10),(1016,'Dariapur',10),(1017,'Daudnagar',10),(1018,'Dehri',10),(1019,'Dhaka',10),(1020,'Dharampur',10),(1021,'Dighwara',10),(1022,'Dinapur Cantonment',10),(1023,'Dinapur Nizamat',10),(1024,'Dumra',10),(1025,'Dumraon',10),(1026,'Ekangar Sarai',10),(1027,'Fatwah (Fatuha)',10),(1028,'Forbesganj',10),(1029,'Gaya',10),(1030,'Gazipur',10),(1031,'Ghoghardiha',10),(1032,'Gogri Jamalpur',10),(1033,'Gopalganj',10),(1034,'Habibpur',10),(1035,'Hajipur',10),(1036,'Hanspura',10),(1037,'Hathua',10),(1038,'Hat Saraiya',10),(1039,'Hilsa',10),(1040,'Hisua',10),(1041,'Islampur',10),(1042,'Jagdishpur (Jagdispur)',10),(1043,'Jainagar',10),(1044,'Jamalpur',10),(1045,'Jamui',10),(1046,'Janakpur Road',10),(1047,'Janpur',10),(1048,'Jehanabad',10),(1049,'Jhajha',10),(1050,'Jhanjharpur',10),(1051,'Jogabani (Jogbani)',10),(1052,'Kanti',10),(1053,'Kargahia Purab',10),(1054,'Kasba',10),(1055,'Kataiya',10),(1056,'Katihar',10),(1057,'Kesaria',10),(1058,'Khagaria',10),(1059,'Khagaul',10),(1060,'Kharagpur',10),(1061,'Khusrupur',10),(1062,'Kishanganj',10),(1063,'Koath',10),(1064,'Koilwar',10),(1065,'Kurthaur',10),(1066,'Lakhisarai',10),(1067,'Lalganj',10),(1068,'Laruara',10),(1069,'Madhepura',10),(1070,'Madhuban',10),(1071,'Madhubani',10),(1072,'Madhubani',10),(1073,'Maharajganj',10),(1074,'Mahnar Bazar',10),(1075,'Mairwa',10),(1076,'Majhauli Khetal',10),(1077,'Makhdumpur',10),(1078,'Malhipur',10),(1079,'Maner',10),(1080,'Manihari',10),(1081,'Mansur Chak',10),(1082,'Marhaura',10),(1083,'Masaurhi',10),(1084,'Mathurapur',10),(1085,'Mehsi',10),(1086,'Mirganj',10),(1087,'Mohanpur',10),(1088,'Mokameh (Mokama)',10),(1089,'Motihari',10),(1090,'Motipur',10),(1091,'Munger',10),(1092,'Murliganj',10),(1093,'Muzaffarpur',10),(1094,'Nabinagar',10),(1095,'Narkatiaganj',10),(1096,'Nasriganj',10),(1097,'Naubatpur',10),(1098,'Naugachhia (Naugachia)',10),(1099,'Nawada',10),(1100,'Nirmali',10),(1101,'Nohsa',10),(1102,'Nokha',10),(1103,'Nurpur',10),(1104,'Nurpur',10),(1105,'Obra',10),(1106,'Padri',10),(1107,'Paharpur',10),(1108,'Pakri Dayal',10),(1109,'Pareo',10),(1110,'Paria',10),(1111,'Pataliputra Housing Colony',10),(1112,'Patna',10),(1113,'Phulwari Sharif',10),(1114,'Piro',10),(1115,'Puraini',10),(1116,'Purnia',10),(1117,'Rafiganj',10),(1118,'Raghunathpur',10),(1119,'Rajauli',10),(1120,'Rajgir',10),(1121,'Rajopatti urf Kota Bazar',10),(1122,'Ramgarh',10),(1123,'Ramnagar',10),(1124,'Raxaul Bazar',10),(1125,'Revelganj',10),(1126,'Rosera',10),(1127,'Sabour',10),(1128,'Saharsa',10),(1129,'Sahebganj',10),(1130,'Saidpura',10),(1131,'Samastipur',10),(1132,'Sanrha',10),(1133,'Saraiya',10),(1134,'Sarimpur',10),(1135,'Sasaram',10),(1136,'Satghara',10),(1137,'Shahjangi',10),(1138,'Shahpur',10),(1139,'Sheikhpura',10),(1140,'Shekhpura',10),(1141,'Sheohar',10),(1142,'Sherghati',10),(1143,'Silao',10),(1144,'Singhesar Asthan',10),(1145,'Sitamarhi',10),(1146,'Siwan',10),(1147,'Sonepur (Sonpur)',10),(1148,'Sugauli',10),(1149,'Sultanganj',10),(1150,'Supaul',10),(1151,'Talkhapur Dumra',10),(1152,'Tarapur',10),(1153,'Teghra',10),(1154,'Telkap',10),(1155,'Thakurganj',10),(1156,'Tikari',10),(1157,'Tola Baliadih',10),(1158,'Tola Chain',10),(1159,'Tola Mansaraut',10),(1160,'Tola Pairamatihana',10),(1161,'Warisaliganj',10),(1162,'Yehiapur',10),(1163,'Behlana',4),(1164,'Chandigarh',4),(1165,'Daria',4),(1166,'Khuda Alisher',4),(1167,'Mauli Jagran',4),(1168,'Aamadi',22),(1169,'Abhanpur',22),(1170,'Adbhar',22),(1171,'Ahiwara',22),(1172,'Akaltara',22),(1173,'Ambagarh Chowki',22),(1174,'Ambikapur',22),(1175,'Antagarh',22),(1176,'Arang',22),(1177,'Arjunda',22),(1178,'Bade Bacheli',22),(1179,'Bagbahara',22),(1180,'Bagicha',22),(1181,'Baikunthpur',22),(1182,'Balod',22),(1183,'Baloda',22),(1184,'Baloda Bazar',22),(1185,'Balrampur',22),(1186,'Baramkela',22),(1187,'Barsur',22),(1188,'Basna',22),(1189,'Bastar',22),(1190,'Bemetara (Bemetra)',22),(1191,'Berla',22),(1192,'Bhairamgarh',22),(1193,'Bhakhara',22),(1194,'Bhanupratappur',22),(1195,'Bhatapara',22),(1196,'Bhatgaon',22),(1197,'Bhatgaon',22),(1198,'Bhilai Charoda',22),(1199,'Bhilai Nagar (Bhilai)',22),(1200,'Bhopalpattanam (Bhopalpatnam)',22),(1201,'Bijapur',22),(1202,'Bilaigarh',22),(1203,'Bilaspur',22),(1204,'Bilha',22),(1205,'Birgaon',22),(1206,'Bishrampur',22),(1207,'Bodla',22),(1208,'Bodri',22),(1209,'Champa',22),(1210,'Chandrapur',22),(1211,'Charama',22),(1212,'Chhuikhadan',22),(1213,'Chhura',22),(1214,'Chhurikala',22),(1215,'Chhuriya',22),(1216,'Chikhalakasa',22),(1217,'Chirmiri',22),(1218,'Dabhra',22),(1219,'Dalli-Rajhara',22),(1220,'Dantewada',22),(1221,'Daundi Lohara',22),(1222,'Deori',22),(1223,'Devkar',22),(1224,'Dhamdha',22),(1225,'Dhamtari',22),(1226,'Dharamjaigarh',22),(1227,'Dipka',22),(1228,'Dongargaon',22),(1229,'Dongargarh',22),(1230,'Dornapal',22),(1231,'Doundi',22),(1232,'Durena',22),(1233,'Durg',22),(1234,'Farasgaon',22),(1235,'Fingeshwar',22),(1236,'Gandai',22),(1237,'Gariyaband (Gariaband)',22),(1238,'Gaurella',22),(1239,'Geedam',22),(1240,'Gharghoda',22),(1241,'Gobra Nawapara',22),(1242,'Govindpur',22),(1243,'Gunderdehi',22),(1244,'Gurur',22),(1245,'Hirmi',22),(1246,'Jagdalpur',22),(1247,'Jaijepur',22),(1248,'Jamul',22),(1249,'Jarhi',22),(1250,'Jashpurnagar',22),(1251,'Jhagrakhand',22),(1252,'Kanker',22),(1253,'Kasdol',22),(1254,'Katghora',22),(1255,'Katkona',22),(1256,'Kawardha',22),(1257,'Keskal',22),(1258,'Khairagarh',22),(1259,'Kharod',22),(1260,'Kharora',22),(1261,'Kharsia',22),(1262,'Khongapani',22),(1263,'Kirandul',22),(1264,'Kirodimalnagar',22),(1265,'Kondagaon',22),(1266,'Koni',22),(1267,'Konta',22),(1268,'Koora',22),(1269,'Korba',22),(1270,'Kota',22),(1271,'Kotba',22),(1272,'Kumhari',22),(1273,'Kunkuri',22),(1274,'Kurud',22),(1275,'Kusmi',22),(1276,'Lailunga',22),(1277,'Lakhanpur',22),(1278,'Lawan',22),(1279,'Lingiyadih',22),(1280,'Lormi',22),(1281,'Magarlod',22),(1282,'Mahasamund',22),(1283,'Malhar',22),(1284,'Mana-Camp',22),(1285,'Mandir Hasaud',22),(1286,'Manendragarh',22),(1287,'Maro',22),(1288,'Mehmand',22),(1289,'Mungeli',22),(1290,'Nagari',22),(1291,'Naila-Janjgir',22),(1292,'Nai-Ledri',22),(1293,'Narayanpur',22),(1294,'Narharpur',22),(1295,'Nawagarh',22),(1296,'Nawagarh',22),(1297,'Naya Baradwar',22),(1298,'Pakhanjur',22),(1299,'Palari',22),(1300,'Pali',22),(1301,'Pandariya',22),(1302,'Pandatarai',22),(1303,'Parpondi',22),(1304,'Patan',22),(1305,'Pathalgaon',22),(1306,'Pathariya',22),(1307,'Pendra',22),(1308,'Pipariya',22),(1309,'Pithora',22),(1310,'Pratappur',22),(1311,'Premnagar',22),(1312,'Pusaur',22),(1313,'Rahaud',22),(1314,'Raigarh',22),(1315,'Raipur',22),(1316,'Rajgamar',22),(1317,'Rajim',22),(1318,'Rajnandgaon',22),(1319,'Rajpur',22),(1320,'Ramanujganj',22),(1321,'Ratanpur',22),(1322,'Rawan',22),(1323,'Sahaspur-Lohara',22),(1324,'Saja',22),(1325,'Sakari',22),(1326,'Sakti',22),(1327,'Saragaon',22),(1328,'Saraipali',22),(1329,'Sarangarh',22),(1330,'Sargaon',22),(1331,'Sariya',22),(1332,'Shivnandanpur (Omkarbahara)',22),(1333,'Shivpur Charcha',22),(1334,'Shivrinarayan',22),(1335,'Siltara',22),(1336,'Simga',22),(1337,'Sirgitti (Sirgiti)',22),(1338,'Sitapur',22),(1339,'Sukma',22),(1340,'Surajpur',22),(1341,'Takhatpur',22),(1342,'Than-Khamharia',22),(1343,'Tifra',22),(1344,'Tilda Newra',22),(1345,'Tumgaon',22),(1346,'Tundra',22),(1347,'Utai',22),(1348,'Visrampuree',22),(1349,'Wadrafnagar',22),(1350,'Dadra',26),(1351,'Masat',26),(1352,'Naroli',26),(1353,'Rakholi',26),(1354,'Samarvarni',26),(1355,'Silvassa (incl. Amli)',26),(1356,'Bhimpore',25),(1357,'Dadhel',25),(1358,'Daman',25),(1359,'Diu',25),(1360,'Dunetha',25),(1361,'Kachigam',25),(1362,'Kadaiya',25),(1363,'Marwad',25),(1364,'Aali',7),(1365,'Ali Pur',7),(1366,'Asola',7),(1367,'Aya Nagar',7),(1368,'Babar Pur',7),(1369,'Bakhtawar Pur',7),(1370,'Bakkar Wala',7),(1371,'Bankauli',7),(1372,'Bankner',7),(1373,'Bapraula',7),(1374,'Baqiabad',7),(1375,'Barwala',7),(1376,'Bawana',7),(1377,'Begum Pur',7),(1378,'Bhalswa Jahangir Pur',7),(1379,'Bhati',7),(1380,'Bhor Garh',7),(1381,'Burari',7),(1382,'Chandan Hola',7),(1383,'Chattar Pur',7),(1384,'Chhawala (Chhawla)',7),(1385,'Chilla Saroda Bangar',7),(1386,'Chilla Saroda Khadar',7),(1387,'Dallo Pura',7),(1388,'Darya Pur Kalan',7),(1389,'Dayal Pur',7),(1390,'Delhi',7),(1391,'Delhi Cantonment',7),(1392,'Deoli',7),(1393,'Dera Mandi',7),(1394,'Dindar Pur',7),(1395,'Fateh Pur Beri',7),(1396,'Gharoli',7),(1397,'Gheora',7),(1398,'Ghitorni',7),(1399,'Gokal Pur',7),(1400,'Hastsal',7),(1401,'Ibrahim Pur',7),(1402,'Jaffar Pur Kalan',7),(1403,'Jaffrabad',7),(1404,'Jait Pur',7),(1405,'Jharoda Kalan',7),(1406,'Jharoda Majra Burari',7),(1407,'Jiwan Pur (Johri Pur)',7),(1408,'Jona Pur',7),(1409,'Kair',7),(1410,'Kamal Pur Majra Burari',7),(1411,'Kanjhawala',7),(1412,'Kapas Hera',7),(1413,'Karala',7),(1414,'Karawal Nagar',7),(1415,'Khajoori Khas',7),(1416,'Khan Pur Dhani',7),(1417,'Khera',7),(1418,'Khera Kalan',7),(1419,'Khera Khurd',7),(1420,'Kirari Suleman Nagar',7),(1421,'Kondli',7),(1422,'Kotla Mahigiran',7),(1423,'Kusum Pur',7),(1424,'Lad Pur',7),(1425,'Libas Pur',7),(1426,'Maidan Garhi',7),(1427,'Malik Pur Kohi (Rang Puri)',7),(1428,'Mandoli',7),(1429,'Mir Pur Turk',7),(1430,'Mithe Pur',7),(1431,'Mitraon',7),(1432,'Mohammad Pur Majri',7),(1433,'Molar Band',7),(1434,'Moradabad Pahari',7),(1435,'Mubarak Pur Dabas',7),(1436,'Mukand Pur',7),(1437,'Mukhmel Pur',7),(1438,'Mundka',7),(1439,'Mustafabad',7),(1440,'Nangli Sakrawati',7),(1441,'Nangloi Jat',7),(1442,'Neb Sarai',7),(1443,'New Delhi',7),(1444,'Nilothi',7),(1445,'Nithari',7),(1446,'Pehlad Pur Bangar',7),(1447,'Pooth Kalan',7),(1448,'Pooth Khurd',7),(1449,'Pul Pehlad',7),(1450,'Qadi Pur',7),(1451,'Quammruddin Nagar',7),(1452,'Qutab Garh',7),(1453,'Raja Pur Khurd',7),(1454,'Rajokri',7),(1455,'Raj Pur Khurd',7),(1456,'Rani Khera',7),(1457,'Roshan Pura (Dichaon Khurd)',7),(1458,'Sadat Pur Gujran',7),(1459,'Sahibabad Daulat Pur',7),(1460,'Saidabad',7),(1461,'Saidul Azaib',7),(1462,'Sambhalka',7),(1463,'Shafi Pur Ranhola',7),(1464,'Shakar Pur Baramad',7),(1465,'Siras Pur',7),(1466,'Sultan Pur',7),(1467,'Sultan Pur Majra',7),(1468,'Taj Pul',7),(1469,'Tigri',7),(1470,'Tikri Kalan',7),(1471,'Tikri Khurd',7),(1472,'Tilang Pur Kotla',7),(1473,'Tukhmir Pur',7),(1474,'Ujwa',7),(1475,'Ziauddin Pur',7),(1476,'Aldona',30),(1477,'Anjuna',30),(1478,'Aquem',30),(1479,'Arambol',30),(1480,'Bambolim',30),(1481,'Bandora',30),(1482,'Benaulim',30),(1483,'Bicholim',30),(1484,'Borim',30),(1485,'Calangute',30),(1486,'Calapor',30),(1487,'Canacona',30),(1488,'Candola',30),(1489,'Candolim',30),(1490,'Carapur',30),(1491,'Chicalim',30),(1492,'Chimbel',30),(1493,'Chinchinim',30),(1494,'Colvale',30),(1495,'Corlim',30),(1496,'Cortalim',30),(1497,'Cumbarjua',30),(1498,'Cuncolim',30),(1499,'Curchorem-Cacora',30),(1500,'Curti',30),(1501,'Curtorim',30),(1502,'Davorlim',30),(1503,'Goa Velha',30),(1504,'Guirim',30),(1505,'Jua',30),(1506,'Mandrem',30),(1507,'Mapusa (M?puca)',30),(1508,'Marcaim',30),(1510,'Mercurim',30),(1511,'Moira',30),(1512,'Morjim',30),(1513,'Murda',30),(1514,'Navelim',30),(1515,'Nerul',30),(1516,'Nuvem',30),(1517,'Onda',30),(1518,'Orgao',30),(1519,'Pale',30),(1520,'Panaji (Panjim, Pangim)',30),(1521,'Parcem',30),(1522,'Penha de França',30),(1523,'Pernem',30),(1524,'Pilerne',30),(1525,'Ponda',30),(1526,'Priol',30),(1527,'Quela',30),(1528,'Quepem',30),(1529,'Raia',30),(1530,'Reis Magos',30),(1531,'Saligao',30),(1532,'Salvador do Mundo',30),(1533,'Sancoale',30),(1534,'Sanguem',30),(1535,'Sanquelim',30),(1536,'Sanvordem',30),(1538,'Siolim',30),(1539,'Socorro (Serula)',30),(1540,'Usgao',30),(1541,'Valpoi',30),(1542,'Varca',30),(1543,'Verna',30),(1544,'Xeldem',30),(1545,'Adalaj',24),(1546,'Ahmadabad Cantonment',24),(1547,'Ahwa',24),(1548,'Alang',24),(1549,'Alang-Sosiya',24),(1550,'Alikherva',24),(1551,'Amardad',24),(1552,'Ambaji',24),(1553,'Ambaliyasan',24),(1554,'Amboli',24),(1555,'Amod',24),(1556,'Amreli',24),(1557,'Anand',24),(1558,'Anandpar',24),(1559,'Andada',24),(1560,'Anjar',24),(1561,'Anklav',24),(1562,'Anklesvar (Ankleshwar)',24),(1563,'Anklesvar INA',24),(1564,'Antaliya',24),(1565,'Antarjal',24),(1566,'Arsodiya',24),(1567,'Atul',24),(1568,'Baben',24),(1569,'Babra',24),(1570,'Bagasara',24),(1571,'Bajwa',24),(1572,'Balasinor',24),(1573,'Balitha',24),(1574,'Baliyasan',24),(1575,'Bansda (Vansda)',24),(1576,'Bantwa (Bantva)',24),(1577,'Bardoli',24),(1578,'Bareja',24),(1579,'Barwala',24),(1580,'Bavla',24),(1581,'Bayad',24),(1582,'Bechar (Becharaji)',24),(1583,'Bhabhar',24),(1584,'Bhachau',24),(1585,'Bhadkodara',24),(1586,'Bhagal (Jagana)',24),(1587,'Bhagdawada',24),(1588,'Bhalpara',24),(1589,'Bhanvad',24),(1590,'Bharthana Kosad',24),(1591,'Bharuch',24),(1592,'Bharuch INA',24),(1593,'Bhat',24),(1594,'Bhavnagar',24),(1595,'Bhayavadar',24),(1596,'Bhilad',24),(1597,'Bhiloda',24),(1598,'Bholav',24),(1599,'Bhuj',24),(1600,'Bhurivel',24),(1601,'Bilimora',24),(1602,'Bilimora (Talodh)',24),(1603,'Bodeli',24),(1604,'Bopal',24),(1605,'Boriavi',24),(1606,'Borsad',24),(1607,'Botad',24),(1608,'Chaklasi',24),(1609,'Chalala',24),(1610,'Chalthan',24),(1611,'Chanasma',24),(1612,'Chandrapur',24),(1613,'Chanod',24),(1614,'Chhapi',24),(1615,'Chhapra',24),(1616,'Chhatral',24),(1617,'Chhatral INA',24),(1618,'Chhaya',24),(1619,'Chhiri',24),(1620,'Chhota Udaipur',24),(1621,'Chikhli',24),(1622,'Chiloda (Naroda)',24),(1623,'Chorvad',24),(1624,'Chotila',24),(1625,'Dabhoi',24),(1626,'Daheli',24),(1627,'Dakor',24),(1628,'Damnagar',24),(1629,'Dediapada',24),(1630,'Deesa',24),(1631,'Dehari',24),(1632,'Dehgam (Dahegam)',24),(1633,'Deodar',24),(1634,'Devgadbaria (Devgadh Baria)',24),(1635,'Devsar',24),(1636,'Dhandhuka',24),(1637,'Dhanera',24),(1638,'Dharampur',24),(1639,'Dhasa Vishi',24),(1640,'Dhola',24),(1641,'Dholka',24),(1642,'Dhoraji',24),(1643,'Dhrangadhra',24),(1644,'Dhrol',24),(1645,'Digvijaygram',24),(1646,'Dohad (Dahod)',24),(1647,'Dungarpur',24),(1648,'Dwarka',24),(1649,'Freelandgunj',24),(1650,'Gadhada',24),(1651,'Gadkhol',24),(1652,'Galpadar',24),(1653,'Gamdi',24),(1654,'Gandevi',24),(1655,'Gandhidham',24),(1656,'Gandhinagar',24),(1657,'Gariadhar',24),(1658,'Ghanteshvar',24),(1659,'Ghogha',24),(1660,'Godhra',24),(1661,'Gondal',24),(1662,'GSFC (Motikhavdi Sikka)',24),(1663,'GSFC Complex INA',24),(1664,'Hadgood',24),(1665,'Hajira INA',24),(1666,'Halol',24),(1667,'Halvad',24),(1668,'Harij',24),(1669,'Himatnagar',24),(1670,'Ichchhapor',24),(1671,'Idar',24),(1672,'Jafrabad',24),(1673,'Jafrabad',24),(1674,'Jambusar',24),(1675,'Jamjodhpur',24),(1676,'Jamnagar',24),(1677,'Jarod',24),(1678,'Jasdan',24),(1679,'Jetalsar',24),(1680,'Jetpur',24),(1681,'Jetpur Navagadh',24),(1682,'Jhadeshwar',24),(1683,'Jhalod',24),(1684,'Junagadh',24),(1685,'Kabilpor',24),(1686,'Kadi',24),(1687,'Kadodara',24),(1688,'Kakoshi',24),(1689,'Kalavad',24),(1690,'Kaliawadi',24),(1691,'Kalol',24),(1692,'Kalol',24),(1693,'Kalol INA',24),(1694,'Kalol INA',24),(1695,'Kandla',24),(1696,'Kanjari',24),(1697,'Kanodar',24),(1698,'Kansad',24),(1699,'Kapadvanj',24),(1700,'Karachiya',24),(1701,'Karamsad',24),(1702,'Karjan',24),(1703,'Karvad',24),(1704,'Kathlal',24),(1705,'Katpar',24),(1706,'Kavant',24),(1707,'Keshod',24),(1708,'Kevadiya',24),(1709,'Khambhalia (Jamkhambhaliya)',24),(1710,'Khambhat',24),(1711,'Khapat',24),(1712,'Kharach',24),(1713,'Kharaghoda',24),(1714,'Kheda',24),(1715,'Khedbrahma',24),(1716,'Kheralu',24),(1717,'Kim',24),(1718,'Kodinar',24),(1719,'Kosamba',24),(1720,'Kotharia',24),(1721,'Kutiyana',24),(1722,'Lathi',24),(1723,'Lavachha',24),(1724,'Lilia',24),(1725,'Limbdi',24),(1726,'Limkheda',24),(1727,'Limla',24),(1728,'Lodhika',24),(1729,'Lunawada (Lunavada)',24),(1730,'Madhapar',24),(1731,'Magdalla',24),(1732,'Mahendranagar',24),(1733,'Mahesana (Mehsana)',24),(1734,'Mahudha',24),(1735,'Mahuva',24),(1736,'Mahuvar',24),(1737,'Maktampur',24),(1738,'Malanka',24),(1739,'Maliya',24),(1740,'Malpur',24),(1741,'Manavadar',24),(1742,'Mandvi',24),(1743,'Mandvi',24),(1744,'Mangrol',24),(1745,'Mankuva',24),(1746,'Mansa',24),(1747,'Meghraj',24),(1748,'Mehmedabad',24),(1749,'Mirjhapar',24),(1750,'Mithapur',24),(1751,'Modasa',24),(1752,'Mora',24),(1753,'Morvi (Morbi)',24),(1754,'Mundra',24),(1755,'Nadiad',24),(1756,'Nanakwada (Nanakvada)',24),(1757,'Nandej',24),(1758,'Nandelav',24),(1759,'Nandesari',24),(1760,'Nandesari INA',24),(1761,'Nari',24),(1762,'Nasvadi',24),(1763,'Nava Bhildi',24),(1764,'Navsari',24),(1765,'Ode',24),(1766,'Okha',24),(1767,'Orvad',24),(1768,'Paddhari',24),(1769,'Padra',24),(1770,'Palaj',24),(1771,'Palanpur',24),(1772,'Palej',24),(1773,'Palitana',24),(1774,'Panoli',24),(1775,'Parabada',24),(1776,'Pardi',24),(1777,'Pardi Kanade',24),(1778,'Pardi Parnera',24),(1779,'Pardi Sondhpur',24),(1780,'Parnera',24),(1781,'Patan',24),(1782,'Patdi',24),(1783,'Pethapur',24),(1784,'Petlad',24),(1785,'Petro-Chemical Complex INA',24),(1786,'Porbandar',24),(1787,'Por-Ramangamdi',24),(1788,'Prantij',24),(1789,'Radhanpur',24),(1790,'Rajkot',24),(1791,'Rajpipla',24),(1792,'Rajula',24),(1793,'Ranavav',24),(1794,'Ranoli',24),(1795,'Ranpur',24),(1796,'Rapar',24),(1797,'Raval',24),(1798,'Ravapara',24),(1799,'Reliance Complex',24),(1800,'Sachin',24),(1801,'Sachin INA',24),(1802,'Sagbara',24),(1803,'Saij',24),(1804,'Saktasanala',24),(1805,'Salaya',24),(1806,'Salvav',24),(1807,'Sanand',24),(1808,'Sanjali',24),(1809,'Sanjan',24),(1810,'Sanjeli',24),(1811,'Santrampur',24),(1812,'Saputara',24),(1813,'Sarangpore',24),(1814,'Sarigam',24),(1815,'Sarigam INA',24),(1816,'Sathamba',24),(1817,'Savarkundla',24),(1818,'Savgadh',24),(1819,'Savli',24),(1820,'Sayan',24),(1821,'Selamba',24),(1822,'Shaktinagar',24),(1823,'Shapur',24),(1824,'Shehera',24),(1825,'Sherpura',24),(1826,'Sidhpur',24),(1827,'Sidsar',24),(1828,'Sihor',24),(1829,'Sikka',24),(1830,'Singarva',24),(1831,'Sojitra',24),(1832,'Solsumba',24),(1833,'Songadh',24),(1834,'Songadh',24),(1835,'Sukhpar',24),(1836,'Surat',24),(1837,'Sutrapada',24),(1838,'Talaja',24),(1839,'Talala',24),(1840,'Talod',24),(1841,'Tarsadi',24),(1842,'Tarsali',24),(1843,'Thangadh',24),(1844,'Thara',24),(1845,'Tharad',24),(1846,'Thasra',24),(1847,'Trajpar',24),(1848,'Ukai',24),(1849,'Umbergaon',24),(1850,'Umbergaon INA',24),(1851,'Umrala',24),(1852,'Umreth',24),(1853,'Una',24),(1854,'Undera',24),(1855,'Unjha',24),(1856,'Upleta',24),(1857,'Vadali',24),(1858,'Vadnagar',24),(1859,'Vadodara',24),(1860,'Vaghodia (Waghodia)',24),(1861,'Vaghodia INA',24),(1862,'Valia-Naldhari',24),(1863,'Vallabhipur (Vallabhi)',24),(1864,'Valsad',24),(1865,'Valsad INA',24),(1866,'Vanthali',24),(1867,'Vapi',24),(1868,'Vapi INA',24),(1869,'Vareli',24),(1870,'Vartej',24),(1871,'Vasna Borsad INA',24),(1872,'Vavdi Bujarg',24),(1873,'Vavol',24),(1874,'Veraval',24),(1875,'Veraval',24),(1876,'Vijalpor',24),(1877,'Vijapur',24),(1878,'Vijaynagar',24),(1879,'Viramgam',24),(1880,'Virpur',24),(1881,'Visavadar',24),(1882,'Visnagar',24),(1883,'Vithal Udyognagar INA',24),(1884,'Vyara',24),(1885,'Wadhwan',24),(1886,'Waghai',24),(1887,'Wankaner',24),(1888,'Aakera',6),(1889,'Adampur',6),(1890,'Ambala',6),(1891,'Ambala Cantonment',6),(1892,'Ambala Sadar',6),(1893,'Asan Khurd',6),(1894,'Assandh',6),(1895,'Ateli',6),(1896,'Babiyal',6),(1897,'Badhi Majra',6),(1898,'Badh Malak',6),(1899,'Badshahpur',6),(1900,'Baghola',6),(1901,'Bahadurgarh',6),(1902,'Barara',6),(1903,'Barwala',6),(1904,'Bawal',6),(1905,'Bawani Khera',6),(1906,'Bayyanpur',6),(1907,'Beri',6),(1908,'Bhakali',6),(1909,'Bhiwani',6),(1910,'Bhondsi',6),(1911,'Bhuran',6),(1912,'Bilaspur',6),(1913,'Bir Ghaghar',6),(1914,'Boh',6),(1915,'Buria',6),(1916,'Chandi Mandir',6),(1917,'Charkhi Dadri',6),(1918,'Cheeka',6),(1919,'Chhachhrauli',6),(1920,'Dharuhera',6),(1921,'Ellenabad',6),(1922,'Faizabad',6),(1923,'Farakhpur',6),(1924,'Faridabad',6),(1925,'Farrukhnagar',6),(1926,'Fatehabad',6),(1927,'Fazalpur',6),(1928,'Ferozepur Jhirka',6),(1929,'Ganaur',6),(1930,'Gangwa',6),(1931,'Garhi Harsaru',6),(1932,'Gharaunda',6),(1933,'Ghatal Mahaniawas',6),(1934,'Gohana',6),(1935,'Gurgaon',6),(1936,'Hailey Mandi',6),(1937,'Hansi',6),(1938,'Hassan Pur',6),(1939,'Hathin',6),(1940,'Hisar',6),(1941,'HMT Pinjore',6),(1942,'Hodal',6),(1943,'Indri',6),(1944,'Ismailabad',6),(1945,'Jagadhri',6),(1946,'Jandli',6),(1947,'Jhajjar',6),(1948,'Jhakal Mandi (Jakhal Mandi)',6),(1949,'Jind',6),(1950,'Julana',6),(1951,'Kabri',6),(1952,'Kachrauli',6),(1953,'Kaithal',6),(1954,'Kakar Majra',6),(1955,'Kalanaur',6),(1956,'Kalanwali',6),(1957,'Kalayat',6),(1958,'Kalka',6),(1959,'Kanina',6),(1960,'Kansepur',6),(1961,'Kanwla',6),(1962,'Kardhan',6),(1963,'Karnal',6),(1964,'Kharkhoda',6),(1965,'Kheri Nangal',6),(1966,'Khori Kalan',6),(1967,'Kundli',6),(1968,'Ladrawan',6),(1969,'Ladwa',6),(1970,'Loharu',6),(1971,'Maham',6),(1972,'Maheshari',6),(1973,'Majra',6),(1974,'Mandi Dabwali',6),(1975,'Manendragarh',6),(1976,'Manesar',6),(1977,'Manethi',6),(1978,'Mayyer',6),(1979,'Mustafabad',6),(1980,'Nagina',6),(1981,'Nanhera',6),(1982,'Naraingarh',6),(1983,'Narnaul',6),(1984,'Narnaund',6),(1985,'Narwana',6),(1986,'Nilokheri',6),(1987,'Nissing',6),(1988,'Nuh',6),(1989,'Palwal',6),(1990,'Palwal Rural',6),(1991,'Panchkula (Urban Estate)',6),(1992,'Panipat',6),(1993,'Panipat Taraf Ansar',6),(1994,'Panipat Taraf Makhdum Zadgan',6),(1995,'Panipat Taraf Rajputan',6),(1996,'Pataudi',6),(1997,'Pehowa',6),(1998,'Piala',6),(1999,'Pingwan',6),(2000,'Pinjore',6),(2001,'Punahana',6),(2002,'Pundri',6),(2003,'Radaur',6),(2004,'Raipur Rani',6),(2005,'Ram Garh',6),(2006,'Rampura',6),(2007,'Rania',6),(2008,'Ratia',6),(2009,'Rewari',6),(2010,'Rohtak',6),(2011,'Sadaura',6),(2012,'Safidon',6),(2013,'Saha',6),(2014,'Salamba',6),(2015,'Samalkha',6),(2016,'Sampla',6),(2017,'Sasauli',6),(2018,'Satrod Kalan',6),(2019,'Satrod Khas',6),(2020,'Satrod Khurd',6),(2021,'Sector 11 & Sector 12 Part II',6),(2022,'Shahbad (Shahabad Markanda)',6),(2023,'Sikanderpur',6),(2024,'Sirsa',6),(2025,'Siwani',6),(2026,'Sohna',6),(2027,'Sonipat',6),(2028,'Sunari Kalan',6),(2029,'Taoru',6),(2030,'Taraori',6),(2031,'Thanesar',6),(2032,'Tilpat',6),(2033,'Tohana',6),(2034,'Tosham',6),(2035,'Tundla',6),(2036,'Uchana',6),(2037,'Ugra Kheri',6),(2038,'Uklana Mandi',6),(2039,'Uncha Siwana',6),(2040,'Yamunanagar',6),(2041,'Arki',2),(2042,'Baddi',2),(2043,'Bakloh Cantonment',2),(2044,'Banjar',2),(2045,'Bhota',2),(2046,'Bhuntar',2),(2047,'Bilaspur',2),(2048,'Chamba',2),(2049,'Chaupal',2),(2050,'Chuari Khas',2),(2051,'Dagshai Cantonment',2),(2052,'Dalhousie',2),(2053,'Dalhousie Cantonment',2),(2054,'Daulatpur',2),(2055,'Dera Gopipur',2),(2056,'Dharmsala (Dharamshala)',2),(2057,'Gagret',2),(2058,'Ghumarwin',2),(2059,'Hamirpur',2),(2060,'Indora',2),(2061,'Jawalamukhi',2),(2062,'Jhakhri',2),(2063,'Jogindarnagar (Jogindernagar)',2),(2064,'Jubbal',2),(2065,'Jutogh Cantonment',2),(2066,'Kangra',2),(2067,'Kasauli Cantonment',2),(2068,'Kotkhai',2),(2069,'Kullu',2),(2070,'Manali',2),(2071,'Mandi',2),(2072,'Mehatpur Basdehra',2),(2073,'Nadaun',2),(2074,'Nagrota Bagwan',2),(2075,'Nahan',2),(2076,'Naina Devi',2),(2077,'Nalagarh',2),(2078,'Narkanda',2),(2079,'Nurpur',2),(2080,'Palampur',2),(2081,'Paonta Sahib',2),(2082,'Parwanoo',2),(2083,'Rajgarh',2),(2084,'Rampur',2),(2085,'Rawalsar (Rewalsar)',2),(2086,'Rohru',2),(2087,'Sabathu Cantonment',2),(2088,'Santokhgarh',2),(2089,'Sarkaghat',2),(2090,'Seoni',2),(2091,'Shamshi',2),(2092,'Shimla',2),(2093,'Solan',2),(2094,'Sundarnagar',2),(2095,'Talai',2),(2096,'Theog',2),(2097,'Tira Sujanpur',2),(2098,'Una',2),(2099,'Yol Cantonment',2),(2100,'Achhabal',1),(2101,'Aishmuquam',1),(2102,'Akhnoor',1),(2103,'Anantnag',1),(2104,'Arnia',1),(2105,'Arwani',1),(2106,'Ashmuji Khalsa',1),(2107,'Awantipora',1),(2108,'Badami Bagh',1),(2109,'Badgam (Budgam)',1),(2110,'Bandipore (Bandipora)',1),(2111,'Banihal',1),(2112,'Baramula (Baramulla)',1),(2113,'Bari Brahamana (Bari Brahmana)',1),(2114,'Bashohli (Basholi)',1),(2115,'Batote',1),(2116,'Beerwah',1),(2117,'Bhaderwah',1),(2118,'Bhalwal',1),(2119,'Bhore',1),(2120,'Bijbehara',1),(2121,'Billawar',1),(2122,'Birpur',1),(2123,'Bishna',1),(2124,'Chadura',1),(2125,'Chak Kalu',1),(2126,'Chak Ratnu',1),(2127,'Charar-i-Sharief',1),(2128,'Chenani',1),(2129,'Chhatha',1),(2130,'Chuglamsar',1),(2131,'Dara Pora',1),(2132,'Devsar',1),(2133,'Dhande Kalan',1),(2134,'Doda',1),(2135,'Drug Mulla',1),(2136,'Duru Verinag',1),(2137,'Frisal',1),(2138,'Ganderbal',1),(2139,'Ghomanhasan',1),(2140,'Gorah Salathian',1),(2141,'Gulmarg',1),(2142,'Hajan',1),(2143,'Handwara',1),(2144,'Heri',1),(2145,'Hiranagar',1),(2146,'Ichgam',1),(2147,'Jammu',1),(2148,'Jammu Cantonment',1),(2149,'Jourian',1),(2150,'Kargil',1),(2151,'Kathua',1),(2152,'Katra',1),(2153,'Khansahib',1),(2154,'Khonmoh',1),(2155,'Khore (Khour)',1),(2156,'Khrew',1),(2157,'Kishtwar',1),(2158,'Koker Nag',1),(2159,'Kral Pora',1),(2160,'Kral Pora',1),(2161,'Kud',1),(2162,'Kulgam',1),(2163,'Kunzer',1),(2164,'Kupwara',1),(2165,'Lakhanpur',1),(2166,'Lasjan',1),(2167,'Leh (Ladakh)',1),(2168,'Magam',1),(2169,'Maralia',1),(2170,'Marhi',1),(2171,'Mattan',1),(2172,'Mehmood Pora',1),(2173,'Nagam',1),(2174,'Nagrota',1),(2175,'Naka Majiari',1),(2176,'Nihalpur Simbal',1),(2177,'Nowangabra',1),(2178,'Now Gam',1),(2179,'Nowshehra',1),(2180,'Pahalgam',1),(2181,'Pampora',1),(2182,'Parole',1),(2183,'Pattan',1),(2184,'Pulwama',1),(2185,'Punch (Poonch)',1),(2186,'Purana Daroorh',1),(2187,'Qazi Gund',1),(2188,'Quimoh',1),(2189,'Raipur Domana',1),(2190,'Rajauri',1),(2191,'Rakh Gadi Garh',1),(2192,'Ramban',1),(2193,'Ramgarh',1),(2194,'Ram Nagar',1),(2195,'Rathian',1),(2196,'Reasi',1),(2197,'Rehambal',1),(2198,'R.S. Pora',1),(2199,'Safa Pora',1),(2200,'Samba',1),(2201,'Seer Hamdan',1),(2202,'Shangus',1),(2203,'Shupiyan',1),(2204,'Sool Koot',1),(2205,'Sopore',1),(2206,'Spituk',1),(2207,'Srinagar',1),(2208,'Sumbal',1),(2209,'Sunderbani',1),(2210,'Surankote',1),(2211,'Talwara',1),(2212,'Tangdhar',1),(2213,'Thanamandi',1),(2214,'Tral',1),(2215,'Trehgam',1),(2216,'Udhampur',1),(2217,'Uri',1),(2218,'Vijay Pur',1),(2219,'Wail',1),(2220,'Watra Gam',1),(2221,'Yari Pora',1),(2222,'Adityapur',20),(2223,'Akdoni Khurd',20),(2224,'Alagdiha',20),(2225,'Alaudia',20),(2226,'Amlabad',20),(2227,'Ara',20),(2228,'Ara',20),(2229,'Aralgoria',20),(2230,'Arsande',20),(2231,'Bachra',20),(2232,'Bagbera',20),(2233,'Baliapur',20),(2234,'Balkundra',20),(2235,'Bandh Dih',20),(2236,'Bandhgora',20),(2237,'Barajamda',20),(2238,'Baratola',20),(2239,'Bardubhi',20),(2240,'Bargarwa',20),(2241,'Barharwa',20),(2242,'Barhi',20),(2243,'Barkakana',20),(2244,'Barki Saraiya',20),(2245,'Barora',20),(2246,'Barughutu',20),(2247,'Barwadih',20),(2248,'Basukinath',20),(2249,'Baua Kalan',20),(2250,'Bekobar',20),(2251,'Berhait Bazar',20),(2252,'Berhait Santali',20),(2253,'Bermo',20),(2254,'Bhamal',20),(2255,'Bhandra',20),(2256,'Bhim Kanari',20),(2257,'Bhojudih',20),(2258,'Bishnugarh',20),(2259,'Bishrampur',20),(2260,'Bishrampur',20),(2261,'Bokaro',20),(2262,'Bokaro Steel City',20),(2263,'Bongabar',20),(2264,'Borio',20),(2265,'Bundu',20),(2266,'Bursera',20),(2267,'Chaibasa',20),(2268,'Chain Pur',20),(2269,'Chakardharpur (Chakradharpur)',20),(2270,'Chakulia',20),(2271,'Chandil',20),(2272,'Chandrapura',20),(2273,'Chandwa',20),(2274,'Charhi',20),(2275,'Chas',20),(2276,'Chatra',20),(2277,'Chauparan',20),(2278,'Cherra',20),(2279,'Chhota Gobindpur',20),(2280,'Chirkunda',20),(2281,'Chitar Pur',20),(2282,'Chota Gamahria',20),(2283,'Churi',20),(2284,'Dandidih',20),(2285,'Danguwapasi',20),(2286,'Dari',20),(2287,'Deoghar',20),(2288,'Dhanbad',20),(2289,'Dhanwar',20),(2290,'Domchanch',20),(2291,'Dudhani',20),(2292,'Dugda',20),(2293,'Dumarkunda',20),(2294,'Dumka',20),(2295,'Dumra',20),(2296,'Egarkunr',20),(2297,'Gadhra',20),(2298,'Garhwa',20),(2299,'Ghagra',20),(2300,'Ghatshila',20),(2301,'Ghorabandha',20),(2302,'Gidi',20),(2303,'Giridih',20),(2304,'Gobindpur',20),(2305,'Godda',20),(2306,'Gomoh',20),(2307,'Gua',20),(2308,'Gumia (Gomia)',20),(2309,'Gumla',20),(2310,'Gunghasa',20),(2311,'Haludbani',20),(2312,'Haludpukhur',20),(2313,'Hariharpur',20),(2314,'Harina',20),(2315,'Hasir',20),(2316,'Hazaribag',20),(2317,'Hesla',20),(2318,'Hussainabad',20),(2319,'Irba',20),(2320,'Isri',20),(2321,'Jadugora',20),(2322,'Jagannathpur',20),(2323,'Jai Nagar',20),(2324,'Jamshedpur',20),(2325,'Jamtara',20),(2326,'Jamtara',20),(2327,'Jangalpur',20),(2328,'Jaridih Bazar',20),(2329,'Jena',20),(2330,'Jhinghipahari',20),(2331,'Jhinkpani',20),(2332,'Jugsalai',20),(2333,'Kadma No-II',20),(2334,'Kandra',20),(2335,'Kanke',20),(2336,'Karma',20),(2337,'Karmatanr',20),(2338,'Karma Tanr',20),(2339,'Kedla',20),(2340,'Kharkhari',20),(2341,'Khelari',20),(2342,'Khunti',20),(2343,'Kiriburu',20),(2344,'Kodarma',20),(2345,'Konra',20),(2346,'Kopali',20),(2347,'Kuju',20),(2348,'Kumarpur',20),(2349,'Kurpania',20),(2350,'Lalpania',20),(2351,'Lapanga',20),(2352,'Latehar',20),(2353,'Lohardaga',20),(2354,'Madhuban',20),(2355,'Madhupur',20),(2356,'Mahagma (Mahagama)',20),(2357,'Mahesh Mundi',20),(2358,'Mahlidih',20),(2359,'Mahuda',20),(2360,'Maithon',20),(2361,'Majhion',20),(2362,'Malkera',20),(2363,'Mandu',20),(2364,'Mango',20),(2365,'Manohar Pur',20),(2366,'Marai Kalan',20),(2367,'Marar',20),(2368,'Marma',20),(2369,'Masratu',20),(2370,'Matigara',20),(2371,'Medininagar (Daltonganj)',20),(2372,'Meghahatuburu Forest Village',20),(2373,'Mera',20),(2374,'Meru',20),(2375,'Mihijam',20),(2376,'Muraidih',20),(2377,'Muri',20),(2378,'Musabani',20),(2379,'Nagri Kalan',20),(2380,'Nandkharki',20),(2381,'Narra',20),(2382,'Nirsa',20),(2383,'Noamundi',20),(2384,'Okani-II (Okni)',20),(2385,'Orla',20),(2386,'Pakaur (Pakur)',20),(2387,'Palawa',20),(2388,'Panchet',20),(2389,'Panchmahali',20),(2390,'Panrra',20),(2391,'Paratdih',20),(2392,'Patra',20),(2393,'Patratu',20),(2394,'Pertodih',20),(2395,'Phulwartanr',20),(2396,'Phusro',20),(2397,'Pondarkanali',20),(2398,'Purana Dumka',20),(2399,'Purihasa',20),(2400,'Raghunandanpur',20),(2401,'Rajbhita (Rajganj)',20),(2402,'Rajmahal',20),(2403,'Ramgarh Cantonment',20),(2404,'Ranchi',20),(2405,'Rasikpur',20),(2406,'Ratu',20),(2407,'Ray',20),(2408,'Religara (Pachhiari)',20),(2409,'Rerma',20),(2410,'Sagarmpur',20),(2411,'Sahibganj (Sahebganj)',20),(2412,'Sahnidih',20),(2413,'Sanri (Tilaiya)',20),(2414,'Sansikhara',20),(2415,'Saram',20),(2416,'Sarauni',20),(2417,'Sarjamda',20),(2418,'Satgawan (Hariharganj)',20),(2419,'Saunda',20),(2420,'Seota',20),(2421,'Seraikela (Saraikela)',20),(2422,'Sewai',20),(2423,'Shah Pur',20),(2424,'Sialgudri',20),(2425,'Sijhua',20),(2426,'Simdega',20),(2427,'Sinduria',20),(2428,'Sini',20),(2429,'Sirka',20),(2430,'Sirsia',20),(2431,'Siuliban',20),(2432,'Sundna',20),(2433,'Suranga',20),(2434,'Tanr Balidih',20),(2435,'Taping',20),(2436,'Tati',20),(2437,'Telo',20),(2438,'Telodih',20),(2439,'Tenu',20),(2440,'Tenu Dam-Cum-Kathhara',20),(2441,'Termi',20),(2442,'Tin Pahar',20),(2443,'Topa',20),(2444,'Topchanchi',20),(2445,'Torpa',20),(2446,'Toto',20),(2447,'Tundiul',20),(2448,'Urimari',20),(2449,'52 Heroor',29),(2450,'Addur',29),(2451,'Adityapatna',29),(2452,'Adyar',29),(2453,'Afzalpur',29),(2454,'Aland',29),(2455,'Alevoor',29),(2456,'Allipura',29),(2457,'Alnavar',29),(2458,'Alur',29),(2459,'Amaravathi',29),(2460,'Ambikanagara (Ambikanagar)',29),(2461,'Aminagad',29),(2462,'Anekal',29),(2463,'Ankola',29),(2464,'Annigeri',29),(2465,'Arasinakunte',29),(2466,'Arkalgud',29),(2467,'Arkula',29),(2468,'Arsikere',29),(2469,'Athni (Athani)',29),(2470,'Attibele',29),(2471,'Aurad',29),(2472,'Aversa',29),(2473,'Bada',29),(2474,'Badagabettu No.80',29),(2475,'Badagaulipady',29),(2476,'Badami',29),(2477,'Bagalkot',29),(2478,'Bagepalli',29),(2479,'Bail Hongal (Bailhongal)',29),(2480,'Bajpe',29),(2481,'Bangalore [Bangalore]',29),(2482,'Bangarapet',29),(2483,'Bankapura',29),(2484,'Bannur',29),(2485,'Bantval (Bantwal)',29),(2486,'Basavakalyan',29),(2487,'Basettihalli',29),(2488,'Belgaum',29),(2489,'Belgaum Cantonment',29),(2490,'Bellary',29),(2491,'Belma',29),(2492,'Beltangadi (Belthangady)',29),(2493,'Belur',29),(2494,'Belvata',29),(2495,'Benakanahalli',29),(2496,'Bethamangala',29),(2497,'Bhadravati',29),(2498,'Bhalki',29),(2499,'Bhatkal',29),(2500,'Bhimarayanagudi',29),(2501,'Bhogadi',29),(2502,'Bidadi',29),(2503,'Bidar',29),(2504,'Bijapur',29),(2505,'Bilgi',29),(2506,'Birur',29),(2507,'Bobruwada',29),(2508,'Bommasandra',29),(2509,'Bondathila',29),(2510,'Byadgi (Byadagi)',29),(2511,'Byrapura',29),(2512,'Challakere',29),(2513,'Chamarajanagar',29),(2514,'Channagiri',29),(2515,'Channapatna',29),(2516,'Channarayapatna',29),(2517,'Chelur',29),(2518,'Chikkabanavara',29),(2519,'Chikkabidarakallu',29),(2520,'Chikkajajur (Chikjajur)',29),(2521,'Chikmagalur',29),(2522,'Chikodi',29),(2523,'Chincholi',29),(2524,'Chintamani',29),(2525,'Chitapur',29),(2526,'Chitgoppa',29),(2527,'Chitradurga',29),(2528,'Dandeli',29),(2529,'Davanagere (Davangere)',29),(2530,'Devadurga',29),(2531,'Devanahalli',29),(2532,'Dod Ballapur (Doddaballapura)',29),(2533,'Dommasandra',29),(2534,'Donimalai Township',29),(2535,'Elwala',29),(2536,'Gajendragarh',29),(2537,'Gangawati (Gangavati)',29),(2538,'Gargeswari',29),(2539,'Gauribidanur',29),(2540,'Gogipeth',29),(2541,'Gokak',29),(2542,'Gokak Falls',29),(2543,'Gonikoppal',29),(2544,'Gubbi',29),(2545,'Gudibanda',29),(2546,'Gudur',29),(2547,'Gulbarga',29),(2548,'Guledgudda',29),(2549,'Gundlupet',29),(2550,'Gurmatkal',29),(2551,'Haliyal',29),(2552,'Hangal',29),(2553,'Hanur',29),(2554,'Haralahalli',29),(2555,'Haralapura',29),(2556,'Harapanahalli (Harpanahalli)',29),(2557,'Harekala',29),(2558,'Harihar',29),(2559,'Hassan',29),(2560,'Hatti',29),(2561,'Hatti Gold Mines',29),(2562,'Haveri',29),(2563,'Hebbagodi',29),(2564,'Heggadadevankote',29),(2565,'Hindalgi',29),(2566,'Hinkal',29),(2567,'Hirekerur',29),(2568,'Hiriyur',29),(2569,'Holalkere',29),(2570,'Hole Narsipur (Holenarasipura)',29),(2571,'Homnabad (Humnabad)',29),(2572,'Honavar (Honnavar)',29),(2573,'Hongalli',29),(2574,'Honnali',29),(2575,'Hosakote (Hoskote)',29),(2576,'Hosanagara',29),(2577,'Hosdurga (Hosadurga)',29),(2578,'Hospet',29),(2579,'Hubli-Dharwad (Hubli)',29),(2580,'Hukeri',29),(2581,'Huliyar',29),(2582,'Hunasamaranahalli',29),(2583,'Hungund (Hunagunda)',29),(2584,'Hunsur',29),(2585,'Hutagalli',29),(2586,'Ilkal',29),(2587,'Indi',29),(2588,'Jagalur',29),(2589,'Jali',29),(2590,'Jamkhandi (Jamakhandi)',29),(2591,'Jevargi',29),(2592,'Jigani',29),(2593,'Jog Kargal (Jog Falls)',29),(2594,'Kadakola',29),(2595,'Kadigenahalli',29),(2596,'Kadur',29),(2597,'Kadwad',29),(2598,'Kairangala',29),(2599,'Kakati',29),(2600,'Kalghatgi (Kalaghatagi)',29),(2601,'Kamalapuram (Kamalapura)',29),(2602,'Kamalnagar',29),(2603,'Kamatgi (Kamatagi)',29),(2604,'Kampli',29),(2605,'Kanakapura',29),(2606,'Kangrali (BK)',29),(2607,'Kangrali (KH)',29),(2608,'Kariyangala',29),(2609,'Karkal',29),(2610,'Karwar',29),(2611,'Kawalettu',29),(2612,'Kenjar',29),(2613,'Kerur',29),(2614,'Khanapur',29),(2615,'Kodiyal',29),(2616,'Kolambe',29),(2617,'Kolar',29),(2618,'Kollegal',29),(2619,'Konaje',29),(2620,'Konappana Agrahara',29),(2621,'Konnur',29),(2622,'Koorgalli',29),(2623,'Koppa',29),(2624,'Koppal',29),(2625,'Korangrapady',29),(2626,'Koratagere',29),(2627,'Kotekara',29),(2628,'Koteshwar',29),(2629,'Kotturu',29),(2630,'Krishnarajanagara',29),(2631,'Krishnarajpet',29),(2632,'Kudchi (Kudachi)',29),(2633,'Kudligi',29),(2634,'Kudremukh',29),(2635,'Kudur',29),(2636,'Kumbalagodu',29),(2637,'Kumta',29),(2638,'Kundapura (Kundapur)',29),(2639,'Kundgol',29),(2640,'Kunigal',29),(2641,'Kurekuppa',29),(2642,'Kurgunta',29),(2643,'Kushalnagar (Kushalanagar)',29),(2644,'Kushtagi',29),(2645,'Kuvettu',29),(2646,'Lakshmeshwar',29),(2647,'Lingsugur (Lingasugur)',29),(2648,'Londa',29),(2649,'Machche',29),(2650,'Madanaiyakanahalli',29),(2651,'Maddur',29),(2652,'Madhugiri',29),(2653,'Madikeri',29),(2654,'Magadi',29),(2655,'Mahalingpur',29),(2656,'Malavalli',29),(2657,'Mallar',29),(2658,'Malur',29),(2659,'Mandya',29),(2660,'Mangalore',29),(2661,'Manipura',29),(2662,'Manjanady',29),(2663,'Manvi',29),(2664,'Maragondahalli',29),(2665,'Matadakurubarahatti',29),(2666,'Mellahalli',29),(2667,'Molakalmuru',29),(2668,'Moodabettu',29),(2669,'Mouje Nandgad',29),(2670,'Mudalgi',29),(2671,'Mudbidri (Moodabidri)',29),(2672,'Muddebihal',29),(2673,'Mudgal',29),(2674,'Mudhol',29),(2675,'Mudigere',29),(2676,'Muduperar',29),(2677,'Mudushedde',29),(2678,'Mulbagal',29),(2679,'Mulgund',29),(2680,'Mulki',29),(2681,'Mulur',29),(2682,'Mundargi',29),(2683,'Mundgod',29),(2684,'Munirabad Project Area',29),(2685,'Munnur',29),(2686,'Munnuru',29),(2687,'Mutga',29),(2688,'Mysore',29),(2689,'Nadsal',29),(2690,'Nagamangala',29),(2691,'Nanjangud',29),(2692,'Narasimharajapura',29),(2693,'Naregal',29),(2694,'Nargund',29),(2695,'Narikombu',29),(2696,'Navalgund',29),(2697,'Navoor',29),(2698,'Neermarga',29),(2699,'Nelamangala',29),(2700,'Nipani',29),(2701,'Pandavapura',29),(2702,'Pavagada',29),(2703,'Peeranwadi',29),(2704,'Piriyapatna',29),(2705,'Pudu',29),(2706,'Puttur',29),(2707,'Rabkavi Banhatti',29),(2708,'Raichur',29),(2709,'Ramanagara',29),(2710,'Ramdurg',29),(2711,'Ranibennur (Ranebennuru)',29),(2712,'Raybag',29),(2713,'Robertson Pet',29),(2714,'Ron',29),(2715,'Sadalgi (Sadalga)',29),(2716,'Sagar',29),(2717,'Saidapur',29),(2718,'Sajipanadu',29),(2719,'Sakleshpur',29),(2720,'Saligram',29),(2721,'Sambra',29),(2722,'Sandur',29),(2723,'Sankeshwar',29),(2724,'Sanoor',29),(2725,'Saragur (Sargur)',29),(2726,'Sarjapura',29),(2727,'Satyamangala',29),(2728,'Saundatti-Yellamma (Saundatti)',29),(2729,'Savanur',29),(2730,'Sedam',29),(2731,'Shahabad',29),(2732,'Shahabad ACC',29),(2733,'Shahpur',29),(2734,'Shaktinagar',29),(2735,'Shiggaon',29),(2736,'Shikarpur (Shikaripur)',29),(2737,'Shimoga',29),(2738,'Shirhatti (Shirahatti)',29),(2739,'Shorapur',29),(2740,'Siddapur',29),(2741,'Sidlaghatta',29),(2742,'Sindgi (Sindagi)',29),(2743,'Sindhnur (Sindhanur)',29),(2744,'Sira',29),(2745,'Siralkoppa',29),(2746,'Sirsi',29),(2747,'Siruguppa',29),(2748,'Someshwar',29),(2749,'Somvarpet (Somwarpet)',29),(2750,'Sorab',29),(2751,'Sringeri',29),(2752,'Srinivaspur',29),(2753,'Srirampura',29),(2754,'Sulebhavi',29),(2755,'Sulya (Sullia)',29),(2756,'Talapady',29),(2757,'Talikota',29),(2758,'Talipady',29),(2759,'Tarikere',29),(2760,'Tattilli (Mundgod)',29),(2761,'Tekkalakote',29),(2762,'Tenkanidyoor',29),(2763,'Terdal',29),(2764,'Thokur-62',29),(2765,'Thumbe',29),(2766,'Tiptur',29),(2767,'Tirthahalli (Thirthahalli)',29),(2768,'Tirumakudal Narsipur',29),(2769,'Tonse East',29),(2770,'Tumkur',29),(2771,'Turuvekere',29),(2772,'Udupi',29),(2773,'Udyavara',29),(2774,'Ullal',29),(2775,'Uppinangady (Uppinangadi)',29),(2776,'Vaddu',29),(2777,'Varamballi',29),(2778,'Venkatapura',29),(2779,'Vijayapura',29),(2780,'Virajpet',29),(2781,'Vittal',29),(2782,'Wadi',29),(2783,'Yadgir',29),(2784,'Yelandur',29),(2785,'Yelbarga (Yelburga)',29),(2786,'Yellapur',29),(2787,'Yellur',29),(2788,'Yenagudde',29),(2789,'Abdu Rahiman Nagar',32),(2790,'Adat',32),(2791,'Adichanalloor',32),(2792,'Adinad',32),(2793,'Adoor',32),(2794,'Aimanam',32),(2795,'Ajanur',32),(2796,'Akathiyoor',32),(2797,'Ala',32),(2798,'Alamcode',32),(2799,'Alamcode',32),(2800,'Alangad',32),(2801,'Alappuzha',32),(2802,'Alathur',32),(2803,'Alur',32),(2804,'Aluva',32),(2805,'Amballur',32),(2806,'Amballur',32),(2807,'Ancharakandy (Anjarakkandy)',32),(2808,'Angamaly',32),(2809,'Anjur',32),(2810,'Anthicad (Anthikad)',32),(2811,'Ariyallur',32),(2812,'Arookutty',32),(2813,'Aroor',32),(2814,'Athirampuzha',32),(2815,'Athiyannur',32),(2816,'Atholi',32),(2817,'Attingal',32),(2818,'Avanur',32),(2819,'Avinissery',32),(2820,'Ayancheri',32),(2821,'Ayanivelikulangara',32),(2822,'Azhikode North',32),(2823,'Azhikode South',32),(2824,'Azhiyur',32),(2825,'Azhoor',32),(2826,'Balusseri (Balussery)',32),(2827,'Bangra Manjeshwar',32),(2828,'Bare',32),(2829,'Beypore',32),(2830,'Bharanikkavu',32),(2831,'Brahmakulam',32),(2832,'Chala',32),(2833,'Chalakudy',32),(2834,'Changanassery',32),(2835,'Chavakkad',32),(2836,'Chavara',32),(2837,'Chekkiad',32),(2838,'Chelakkara',32),(2839,'Chelamattom',32),(2840,'Chelambra (Idimuzhikkal)',32),(2841,'Chelannur',32),(2842,'Cheleri',32),(2843,'Chelora',32),(2844,'Chemancheri',32),(2845,'Chemnad',32),(2846,'Chendamangalam',32),(2847,'Chendrappini',32),(2848,'Chengala',32),(2849,'Chengalam South',32),(2850,'Chengamanad',32),(2851,'Chengannur',32),(2852,'Chennithala',32),(2853,'Cheppad',32),(2854,'Cheranallur',32),(2855,'Cheriyamundam (Ceriyamundam)',32),(2856,'Cherpu',32),(2857,'Cherthala',32),(2858,'Cherukavu',32),(2859,'Cherukunnu',32),(2860,'Cheruthazham',32),(2861,'Cheruthuruthi',32),(2862,'Cheruvannur',32),(2863,'Chethipuzha',32),(2864,'Chevvoor',32),(2865,'Chingoli',32),(2866,'Chirakkal',32),(2867,'Chiramanangad (Chermanangad)',32),(2868,'Chiranellur',32),(2869,'Chittanda',32),(2870,'Chittilappilly',32),(2871,'Chittur-Thathamangalam',32),(2872,'Chockli',32),(2873,'Choolissery',32),(2874,'Choondal',32),(2875,'Choornikkara',32),(2876,'Chorode',32),(2877,'Chowwara',32),(2878,'Desamangalam',32),(2879,'Dharmadom',32),(2880,'Edacheri',32),(2881,'Edakkalathur',32),(2882,'Edakkazhiyur',32),(2883,'Edakkode',32),(2884,'Edappal (Edapal)',32),(2885,'Edathala',32),(2886,'Edathirinji',32),(2887,'Edathiruthy',32),(2888,'Edavilangu',32),(2889,'Elamkunnapuzha',32),(2890,'Elampalloor',32),(2891,'Elavally',32),(2892,'Elayavoor',32),(2893,'Eloor',32),(2894,'Enkakkad',32),(2895,'Eramala',32),(2896,'Eramalloor',32),(2897,'Eranellur',32),(2898,'Eranholi',32),(2899,'Erattupetta',32),(2900,'Eravattur',32),(2901,'Eravu',32),(2902,'Eruvatti (Eruvatty)',32),(2903,'Ettumanoor',32),(2904,'Eyyal',32),(2905,'Ezhome',32),(2906,'Ezhupunna',32),(2907,'Feroke',32),(2908,'Guruvayoor (Guruvayur)',32),(2909,'Haripad',32),(2910,'Hemambikanagar',32),(2911,'Hosabettu',32),(2912,'Irikkur',32),(2913,'Irimbiliyam',32),(2914,'Iringal',32),(2915,'Iringaprom',32),(2916,'Irinjalakuda',32),(2917,'Iriveri',32),(2918,'Iroopara',32),(2919,'Kadachira',32),(2920,'Kadamakkudy',32),(2921,'Kadannappalli',32),(2922,'Kadavallur',32),(2923,'Kadikkad',32),(2924,'Kadirur',32),(2925,'Kadungalloor',32),(2926,'Kainoor',32),(2927,'Kaipamangalam',32),(2928,'Kaiparamba',32),(2929,'Kakkanad',32),(2930,'Kakkodi',32),(2931,'Kalady',32),(2932,'Kalady',32),(2933,'Kalamassery',32),(2934,'Kallelibhagom',32),(2935,'Kallettumkara',32),(2936,'Kalliasseri',32),(2937,'Kalliyoor',32),(2938,'Kallur Thekkummuri',32),(2939,'Kallur Vadakkummuri',32),(2940,'Kalpetta',32),(2941,'Kanayannur',32),(2942,'Kandalloor',32),(2943,'Kandamkunnu',32),(2944,'Kandanassery',32),(2945,'Kanhangad',32),(2946,'Kanhirode',32),(2947,'Kaniyarkode',32),(2948,'Kanjikkuzhi',32),(2949,'Kanjiramkulam',32),(2950,'Kannadiparamba',32),(2951,'Kannamangalam',32),(2952,'Kannamangalam',32),(2953,'Kannapuram',32),(2954,'Kannur',32),(2955,'Kannur Cantonment',32),(2956,'Karakulam',32),(2957,'Karamuck',32),(2958,'Karikkad',32),(2959,'Karivellur',32),(2960,'Kariyannur',32),(2961,'Karthikappally',32),(2962,'Karumalloor',32),(2963,'Karuvanthuruthy',32),(2964,'Kasaragod',32),(2965,'Kattakampal',32),(2966,'Kattanam',32),(2967,'Kattipparuthi (Kattipparutti)',32),(2968,'Kattur (Kattoor)',32),(2969,'Kayamkulam',32),(2970,'Keekan',32),(2971,'Keerikkad',32),(2972,'Keezhallur',32),(2973,'Keezhariyur',32),(2974,'Keezhattingal',32),(2975,'Killannur',32),(2976,'Kizhakkumbhagom',32),(2977,'Kizhakkummuri',32),(2978,'Kizhuparamba',32),(2979,'Kizhuppillikkara',32),(2980,'Kizhuvalam-Koonthalloor',32),(2981,'Kochi [Cochin]',32),(2982,'Kodamthuruth',32),(2983,'Kodannur',32),(2984,'Kodungallur',32),(2985,'Kodur',32),(2986,'Koduvayur',32),(2987,'Koipady',32),(2988,'Kokkothamangalam',32),(2989,'Kolacherry',32),(2990,'Kolavelloor',32),(2991,'Kolazhy',32),(2992,'Kollam',32),(2993,'Komalapuram',32),(2994,'Kondotty',32),(2995,'Koodali',32),(2996,'Koothali',32),(2997,'Koothuparamba (Kuthuparamba)',32),(2998,'Koottilangadi',32),(2999,'Koovappady',32),(3000,'Koratty',32),(3001,'Kothamangalam',32),(3002,'Kottakkal',32),(3003,'Kottamkara',32),(3004,'Kottappally',32),(3005,'Kottappuram',32),(3006,'Kottarakkara',32),(3007,'Kottayam',32),(3008,'Kottayam-Malabar',32),(3009,'Kottuvally',32),(3010,'Kozhenchery (Kozhencherry)',32),(3011,'Kozhikode [Calicut]',32),(3012,'Kozhukkallur',32),(3013,'Kozhukkully',32),(3014,'Krishnapuram',32),(3015,'Kudappanakkunnu',32),(3016,'Kudlu',32),(3017,'Kulasekharapuram',32),(3018,'Kulathummal',32),(3019,'Kumaranellur',32),(3020,'Kumarapuram',32),(3021,'Kumbalam',32),(3022,'Kumbalangy',32),(3023,'Kunhimangalam',32),(3024,'Kunjathur',32),(3025,'Kunnamangalam',32),(3026,'Kunnamkulam',32),(3027,'Kunnathunad',32),(3028,'Kunnummal',32),(3029,'Kurattissery',32),(3030,'Kureekkad',32),(3031,'Kurichikkara',32),(3032,'Kurumathur',32),(3033,'Kurumpilavu',32),(3034,'Kuruvattur',32),(3035,'Kuthiathode',32),(3036,'Kuttiattoor',32),(3037,'Kuttikkattoor',32),(3038,'Kuttippuram',32),(3039,'Kuttoor',32),(3040,'Madathumpady',32),(3041,'Madayi',32),(3042,'Madayikonam',32),(3043,'Madhur',32),(3044,'Malappuram',32),(3045,'Malayinkeezhu',32),(3046,'Manakkody',32),(3047,'Manakunnam',32),(3048,'Manalur (Manaloor)',32),(3049,'Manantheri',32),(3050,'Manavalassery',32),(3051,'Mangalpady',32),(3052,'Mangattidam',32),(3053,'Maniyat',32),(3054,'Maniyoor',32),(3055,'Maniyur',32),(3056,'Manjeri',32),(3057,'Manjeshwar',32),(3058,'Mannanchery (Mannancherry)',32),(3059,'Mannar',32),(3060,'Mannarkad-I',32),(3061,'Maradu',32),(3062,'Marampilly',32),(3063,'Marancheri (Maranchery)',32),(3064,'Marathakkara',32),(3065,'Marutharode',32),(3066,'Mattannur (Mattanur)',32),(3067,'Mattoor',32),(3068,'Mavelikkara',32),(3069,'Mavilayi',32),(3070,'Mavoor',32),(3071,'Mayyanad',32),(3072,'Mayyil',32),(3073,'Meenad',32),(3074,'Menhaniam',32),(3075,'Meppayyur (Meppayur)',32),(3076,'Methala',32),(3077,'Minalur',32),(3078,'Mogral',32),(3079,'Mokeri',32),(3080,'Moonniyur (Thalappara)',32),(3081,'Moothakunnam',32),(3082,'Muhamma',32),(3083,'Mulamthuruthy (Mulanthuruthy)',32),(3084,'Mulavukad',32),(3085,'Mullassery',32),(3086,'Mundathikode',32),(3087,'Munderi',32),(3088,'Muringur Vadakkummuri',32),(3089,'Muthukulam',32),(3090,'Muthuthala',32),(3091,'Muvattupuzha',32),(3092,'Muzhappilangad',32),(3093,'Nadapuram',32),(3094,'Nadathara',32),(3095,'Naduvannur',32),(3096,'Naduvattom',32),(3097,'Nanmanda',32),(3098,'Nannambra',32),(3099,'Narath',32),(3100,'Nattakam',32),(3101,'Nedumangad',32),(3102,'Nedumbassery',32),(3103,'Nedumpana',32),(3104,'Nedumpura',32),(3105,'Neduva',32),(3106,'Nelluwaya',32),(3107,'Nenmenikkara',32),(3108,'New Mahe',32),(3109,'Neyyattinkara',32),(3110,'Nilambur',32),(3111,'Njarackal',32),(3112,'North Thrikkaripur',32),(3113,'Oachira',32),(3114,'Olavanna',32),(3115,'Ongallur-I',32),(3116,'Ongallur-II',32),(3117,'Oorakam',32),(3118,'Orumanayur',32),(3119,'Othukkungal',32),(3120,'Ottappalam (Ottapalam)',32),(3121,'Padiyam',32),(3122,'Padiyur',32),(3123,'Paduvilayi',32),(3124,'Paippad',32),(3125,'Palai',32),(3126,'Palakkad',32),(3127,'Palayad',32),(3128,'Palissery',32),(3129,'Pallichal',32),(3130,'Pallikal',32),(3131,'Pallikkara',32),(3132,'Pallikkunnu',32),(3133,'Pallippuram',32),(3134,'Pallippuram',32),(3135,'Pallippuram',32),(3136,'Paluvai',32),(3137,'Panachikkad',32),(3138,'Panangad',32),(3139,'Panangad',32),(3140,'Panayam',32),(3141,'Panmana',32),(3142,'Panniyannur',32),(3143,'Panoor',32),(3144,'Pantheeramkavu',32),(3145,'Pappinisseri',32),(3146,'Pappinivattom',32),(3147,'Parakkad',32),(3148,'Paralam',32),(3149,'Parappukkara',32),(3150,'Parappur',32),(3151,'Parassala',32),(3152,'Parasuvaikkal',32),(3153,'Paravoor (Paravur)',32),(3154,'Paravur',32),(3155,'Pariyaram (Pilathara)',32),(3156,'Pathanamthitta',32),(3157,'Pathirappally',32),(3158,'Pathiriyad',32),(3159,'Pathiyoor',32),(3160,'Pattambi',32),(3161,'Pattiom',32),(3162,'Pavaratty',32),(3163,'Payyannur (Payyanur)',32),(3164,'Pazhanji',32),(3165,'Perakam',32),(3166,'Peralassery (Peralasseri)',32),(3167,'Peramangalam',32),(3168,'Perinad',32),(3169,'Peringandoor',32),(3170,'Peringathur',32),(3171,'Perinjanam',32),(3172,'Perinthalmanna (Perintalmanna)',32),(3173,'Perole',32),(3174,'Perumanna',32),(3175,'Perumanna',32),(3176,'Perumbaikad',32),(3177,'Perumbavoor',32),(3178,'Perumbavoor',32),(3179,'Peruvallur',32),(3180,'Peruvayal',32),(3181,'Pilicode',32),(3182,'Pinarayi',32),(3183,'Pirayiri',32),(3184,'Ponmundam',32),(3185,'Ponnani',32),(3186,'Pookode',32),(3187,'Poolacode',32),(3188,'Poomangalam',32),(3189,'Poothakkulam',32),(3190,'Porathissery',32),(3191,'Porkulam',32),(3192,'Pottore',32),(3193,'Poyya',32),(3194,'Pudussery Central',32),(3195,'Pudussery West',32),(3196,'Pullur',32),(3197,'Punalur',32),(3198,'Punnayur',32),(3199,'Punnayurkulam',32),(3200,'Puranattukara',32),(3201,'Puthencruz',32),(3202,'Puthenvelikkara',32),(3203,'Puthukkad',32),(3204,'Puthunagaram',32),(3205,'Puthuppally',32),(3206,'Puthuppally',32),(3207,'Puthuppariyaram',32),(3208,'Puthur',32),(3209,'Puthur',32),(3210,'Puthuvype',32),(3211,'Puzhakkal',32),(3212,'Puzhathi',32),(3213,'Quilandy (Koyilandy)',32),(3214,'Ramanattukara',32),(3215,'Shiribagilu',32),(3216,'Shiriya',32),(3217,'Shoranur',32),(3218,'South Thrikkaripur',32),(3219,'Sreekaryam',32),(3220,'Talakkad',32),(3221,'Talikkulam (Thalikulam)',32),(3222,'Taliparamba',32),(3223,'Tanalur',32),(3224,'Thaikattussery',32),(3225,'Thaikkad',32),(3226,'Thalakkulathur',32),(3227,'Thalassery',32),(3228,'Thangalur',32),(3229,'Thanniyam',32),(3230,'Thazhakara',32),(3231,'Thazhecode',32),(3232,'Thazhuthala',32),(3233,'Thekkumbhagom',32),(3234,'Thekkumkara',32),(3235,'Thenhippalam (Chelari)',32),(3236,'Thennala (Tennala)',32),(3237,'Thikkody (Thikkodi)',32),(3238,'Thirumittacode-II',32),(3239,'Thirunavaya (Tirunavaya)',32),(3240,'Thiruvalla (Tiruvalla)',32),(3241,'Thiruvankulam',32),(3242,'Thodiyoor',32),(3243,'Thodupuzha',32),(3244,'Tholur',32),(3245,'Thottada',32),(3246,'Thrikkadavoor',32),(3247,'Thrikkaruva',32),(3248,'Thrikkodithanam',32),(3249,'Thrikkovilvattom',32),(3250,'Thrippunithura',32),(3251,'Thrissur',32),(3252,'Thrithala',32),(3253,'Thuneri',32),(3254,'Thurayur',32),(3255,'Tirur',32),(3256,'Tirurangadi',32),(3257,'Trikkur',32),(3258,'Triprangode',32),(3259,'Udma',32),(3260,'Uliyazhathura',32),(3261,'Ulliyeri',32),(3262,'Uppala',32),(3263,'Urakam',32),(3264,'Vadakara (Vatakara)',32),(3265,'Vadakkekad',32),(3266,'Vadakkekara',32),(3267,'Vadakkumbhagom',32),(3268,'Vadakkumkara',32),(3269,'Vadakkummuri',32),(3270,'Vadakkumthala',32),(3271,'Vadama',32),(3272,'Vadanappally',32),(3273,'Vaikom',32),(3274,'Vakkom',32),(3275,'Valapattanam',32),(3276,'Valayam',32),(3277,'Vallachira',32),(3278,'Vaniyamkulam- II',32),(3279,'Varam',32),(3280,'Varappuzha',32),(3281,'Varkala',32),(3282,'Vattappara',32),(3283,'Vattiyoorkavu',32),(3284,'Vayalar',32),(3285,'Vazhakkala',32),(3286,'Vazhakulam',32),(3287,'Vazhayur',32),(3288,'Veiloor',32),(3289,'Vellanikkara',32),(3290,'Vellookkara',32),(3291,'Velloorkunnam',32),(3292,'Velur',32),(3293,'Veluthur',32),(3294,'Venganoor',32),(3295,'Vengara',32),(3296,'Venginissery',32),(3297,'Vengola',32),(3298,'Venkitangu',32),(3299,'Venmanad',32),(3300,'Vijayapuram',32),(3301,'Vilappil',32),(3302,'Vilavoorkkal',32),(3303,'Villiappally',32),(3304,'Vylathur',32),(3305,'Wadakkanchery (Wadakkancherry)',32),(3306,'Agatti',31),(3307,'Amini',31),(3308,'Andrott',31),(3309,'Bangaram',31),(3310,'Bitra',31),(3311,'Cheriyam',31),(3312,'Chetlat',31),(3313,'Kadmat',31),(3314,'Kalpeni',31),(3315,'Kalpitti',31),(3316,'Kavaratti',31),(3317,'Kiltan',31),(3318,'Kodithala',31),(3319,'Minicoy',31),(3320,'Parali (I)',31),(3321,'Parali (II)',31),(3322,'Parali (III)',31),(3323,'Pitti (Birds\' Island)',31),(3324,'Pitti (I)',31),(3325,'Pitti (II)',31),(3326,'Suheli Cheriyakara',31),(3327,'Suheli Valiyakara',31),(3328,'Tilakkam (I)',31),(3329,'Tilakkam (II)',31),(3330,'Tilakkam (III)',31),(3331,'Tinnakara',31),(3332,'Viringili',31),(3333,'Agar',23),(3334,'Ahirkhedi',23),(3335,'Ajaigarh',23),(3336,'Akoda',23),(3337,'Akodia',23),(3338,'Alampur',23),(3339,'Alirajpur',23),(3340,'Alot',23),(3341,'Amanganj',23),(3342,'Amanganj',23),(3343,'Amarkantak',23),(3344,'Amarpatan',23),(3345,'Amarwara',23),(3346,'Ambada',23),(3347,'Ambah',23),(3348,'Amkhera',23),(3349,'Amla',23),(3350,'Amlai',23),(3351,'Anjad',23),(3352,'Antari',23),(3353,'Anuppur',23),(3354,'Aron',23),(3355,'Ashoknagar',23),(3356,'Ashta',23),(3357,'Athner',23),(3358,'Babai',23),(3359,'Badagaon',23),(3360,'Badagaon (Badagoan)',23),(3361,'Bada Malhera',23),(3362,'Badarwas',23),(3363,'Badawada',23),(3364,'Badi',23),(3365,'Badkuhi',23),(3366,'Badnagar',23),(3367,'Badnawar',23),(3368,'Badod',23),(3369,'Badoda',23),(3370,'Badoni',23),(3371,'Badra',23),(3372,'Bagh',23),(3373,'Bagli',23),(3374,'Baihar',23),(3375,'Baikunthpur',23),(3376,'Balaghat',23),(3377,'Baldeogarh',23),(3378,'Bamhani',23),(3379,'Bamor',23),(3380,'Bamora',23),(3381,'Banda',23),(3382,'Bangarda Bada',23),(3383,'Bangarda Chhota',23),(3384,'Bangawan',23),(3385,'Bank',23),(3386,'Bansatar Kheda',23),(3387,'Baraily',23),(3388,'Barela',23),(3389,'Barghat',23),(3390,'Bargi',23),(3391,'Barhi',23),(3392,'Barigarh',23),(3393,'Barman Kalan',23),(3394,'Barwaha',23),(3395,'Barwaha Kasba',23),(3396,'Barwani',23),(3397,'Basoda (Ganj Basoda)',23),(3398,'Begamganj',23),(3399,'Beohari',23),(3400,'Berasia',23),(3401,'Betma',23),(3402,'Betul',23),(3403,'Betul-Bazar',23),(3404,'Bhainsa',23),(3405,'Bhainsdehi',23),(3406,'Bhander',23),(3407,'Bhanpura',23),(3408,'Bharveli',23),(3409,'Bhaurasa',23),(3410,'Bhavra',23),(3411,'Bhedaghat',23),(3412,'Bhicholi Hapsi',23),(3413,'Bhikangaon',23),(3414,'Bhilakhedi',23),(3415,'Bhind',23),(3416,'Bhitarwar',23),(3417,'Bhopal',23),(3418,'Biaora',23),(3419,'Bichhiya',23),(3420,'Bijawar',23),(3421,'Bijuri',23),(3422,'Bilaua',23),(3423,'Bilpura',23),(3424,'Bina - Etawa',23),(3425,'Bina Railway Colony',23),(3426,'Birsinghpur',23),(3427,'Boda',23),(3428,'Borgaon',23),(3429,'Budni',23),(3430,'Burhanpur',23),(3431,'Burhar',23),(3432,'Buxwaha',23),(3433,'Buzurg',23),(3434,'Chachaura-Binaganj',23),(3435,'Chakghat',23),(3436,'Chandameta - Butaria',23),(3437,'Chanderi',23),(3438,'Chandia',23),(3439,'Chandla',23),(3440,'Chaurai Khas',23),(3441,'Chhanera',23),(3442,'Chhapiheda',23),(3443,'Chhatarpur',23),(3444,'Chhindwara',23),(3445,'Chichli',23),(3446,'Chicholi',23),(3447,'Chitrakoot',23),(3448,'Churhat',23),(3449,'Daboh',23),(3450,'Dabra',23),(3451,'Dabra',23),(3452,'Dahi',23),(3453,'Damoh',23),(3454,'Damua',23),(3455,'Datia',23),(3456,'Dehrisaray',23),(3457,'Deodara',23),(3458,'Deohra',23),(3459,'Deori',23),(3460,'Deori',23),(3461,'Depalpur',23),(3462,'Devendranagar',23),(3463,'Dewas',23),(3464,'Dhamnod',23),(3465,'Dhamnod',23),(3466,'Dhana',23),(3467,'Dhanpuri (Nargada Hari Dafai)',23),(3468,'Dhar',23),(3469,'Dharampuri',23),(3470,'Dhodaramohar (Bhoura)',23),(3471,'Dighawani',23),(3472,'Diken',23),(3473,'Dindori',23),(3474,'Dola',23),(3475,'Dongar Parasia',23),(3476,'Dumar Kachhar',23),(3477,'Dungariya Chhapara',23),(3478,'Gadarwara',23),(3479,'Gairatganj',23),(3480,'Gamiria Sagar',23),(3481,'Gandhi Sagar Hydel Col',23),(3482,'Garhakota',23),(3483,'Garhi-Malhara',23),(3484,'Garoth',23),(3485,'Garra',23),(3486,'Ghansaur (Ghansor)',23),(3487,'Ghoda Dongri Ryt',23),(3488,'Ghuwara',23),(3489,'Gogaon',23),(3490,'Gogapur (Mehidpur Road)',23),(3491,'Gohad',23),(3492,'Goraiya',23),(3493,'Gormi',23),(3494,'Gotegaon (Chhota Chhindwara)',23),(3495,'Govindgarh',23),(3496,'Gujarkheda',23),(3497,'Guna',23),(3498,'Gurh',23),(3499,'Gwalior',23),(3500,'Hanumana',23),(3501,'Harda',23),(3502,'Harduli',23),(3503,'Harpalpur',23),(3504,'Harrai',23),(3505,'Hatod',23),(3506,'Hatpiplya (Hatpipalya)',23),(3507,'Hatta',23),(3508,'Hatwas',23),(3509,'Hindoria',23),(3510,'Hirapur',23),(3511,'Hirdepur',23),(3512,'Hoshangabad',23),(3513,'Hukmakhedi',23),(3514,'Ichhawar',23),(3515,'Iklehra',23),(3516,'Indergarh',23),(3517,'Indore',23),(3518,'Isagarh',23),(3519,'Itarsi',23),(3520,'Jabalpur',23),(3521,'Jabalpur Cantonment',23),(3522,'Jabera',23),(3523,'Jaisinghnagar',23),(3524,'Jaithari',23),(3525,'Jaitpur',23),(3526,'Jaitwara',23),(3527,'Jamai',23),(3528,'Jaora',23),(3529,'Jatara',23),(3530,'Jaura Khurd',23),(3531,'Jawad',23),(3532,'Jawar',23),(3533,'Jeron Khalsa',23),(3534,'Jhabua',23),(3535,'Jhundpura',23),(3536,'Jiran',23),(3537,'Jirapur',23),(3538,'Jobat',23),(3539,'Joura',23),(3540,'Kailaras',23),(3541,'Kakarhati',23),(3542,'Kanad',23),(3543,'Kannod',23),(3544,'Kantaphod',23),(3545,'Kapuria',23),(3546,'Kareli',23),(3547,'Karera',23),(3548,'Kari',23),(3549,'Karmeta',23),(3550,'Karnawad',23),(3551,'Karrapur',23),(3552,'Kasrawad',23),(3553,'Katangi',23),(3554,'Katangi',23),(3555,'Kelhauri (Chachai)',23),(3556,'Keolari',23),(3557,'Khacharod (Khachrod)',23),(3558,'Khairi',23),(3559,'Khajuraho',23),(3560,'Khand (Bansagar)',23),(3561,'Khandwa',23),(3562,'Khaniyadhana',23),(3563,'Khargapur',23),(3564,'Khargone',23),(3565,'Khategaon',23),(3566,'Khetia',23),(3567,'Khilchipur',23),(3568,'Khirkiya',23),(3569,'Khor',23),(3570,'Khujner',23),(3571,'Khurai',23),(3572,'Kirnapur',23),(3573,'Kolar',23),(3574,'Kolaras',23),(3575,'Kosmi',23),(3576,'Kotar',23),(3577,'Kothi',23),(3578,'Kothri',23),(3579,'Kotma',23),(3580,'Kukdeshwar',23),(3581,'Kukshi',23),(3582,'Kumbhraj',23),(3583,'Kundam',23),(3584,'Kurwai',23),(3585,'Kymore',23),(3586,'Lahar',23),(3587,'Lakhnadon',23),(3588,'Lanji',23),(3589,'Lasudiya Mori',23),(3590,'Lateri',23),(3591,'Laundi (Lavkushnagar)',23),(3592,'Lidhora Khas',23),(3593,'Limbodi',23),(3594,'Lodhikheda',23),(3595,'Loharda',23),(3596,'Lonia Karbal',23),(3597,'Machalpur',23),(3598,'Madai',23),(3599,'Madhawgdha',23),(3600,'Maharajpur',23),(3601,'Maharajpur',23),(3602,'Maheshwar',23),(3603,'Mahidpur',23),(3604,'Mahura',23),(3605,'Maihar',23),(3606,'Majhauli',23),(3607,'Majhgawan',23),(3608,'Majholi',23),(3609,'Makdon',23),(3610,'Makronia Buzurg',23),(3611,'Maksi',23),(3612,'Malajkhand',23),(3613,'Malanpur',23),(3614,'Malhargarh',23),(3615,'Maliya Guda',23),(3616,'Manasa',23),(3617,'Manawar',23),(3618,'Mandav',23),(3619,'Mandideep',23),(3620,'Mandla',23),(3621,'Mandleshwar',23),(3622,'Mandsaur',23),(3623,'Manegaon',23),(3624,'Mangawan',23),(3625,'Manglaya Sadak',23),(3626,'Manpur',23),(3627,'Mau',23),(3628,'Mauganj',23),(3629,'Meghnagar',23),(3630,'Meharagaon',23),(3631,'Mehgaon',23),(3632,'Mhow Cantonment',23),(3633,'Mhowgaon',23),(3634,'Mihona',23),(3635,'Mohgaon',23),(3636,'Morar Cantonment',23),(3637,'Morena',23),(3638,'Multai',23),(3639,'Mundi',23),(3640,'Mungaoli',23),(3641,'Murwara (Katni)',23),(3642,'Nagda',23),(3643,'Nagod',23),(3644,'Nagri',23),(3645,'Naigarhi',23),(3646,'Nainpur',23),(3647,'Nalkheda',23),(3648,'Namli',23),(3649,'Nanpur',23),(3650,'Narayangarh',23),(3651,'Narsimhapur (Narsinghpur)',23),(3652,'Narsinghgarh',23),(3653,'Narsinghgarh',23),(3654,'Narwar',23),(3655,'Nasrullaganj',23),(3656,'Naudhia',23),(3657,'Neemuch',23),(3658,'Nepanagar',23),(3659,'Neuton Chikhli Kalan',23),(3660,'Niwari',23),(3661,'Niwas',23),(3662,'Nowbasata',23),(3663,'Nowgong',23),(3664,'Nowrozabad (Khodargama)',23),(3665,'Obedullaganj',23),(3666,'Omkareshwar',23),(3667,'Orchha',23),(3668,'Ordnance Factory Itarsi',23),(3669,'Ordnance Factory Khamaria',23),(3670,'Pachmarhi Cantonment',23),(3671,'Pachore',23),(3672,'Pal Chaurai (Pal Chourai)',23),(3673,'Palda',23),(3674,'Palera',23),(3675,'Pali',23),(3676,'Palsud',23),(3677,'Panagar',23),(3678,'Panara',23),(3679,'Pandhana',23),(3680,'Pandhurna',23),(3681,'Pankhedi',23),(3682,'Panna',23),(3683,'Pansemal',23),(3684,'Pasan',23),(3685,'Patan',23),(3686,'Patharia',23),(3687,'Pawai',23),(3688,'Petlawad',23),(3689,'Phuphkalan',23),(3690,'Pichhore',23),(3691,'Pichhore',23),(3692,'Pindrai',23),(3693,'Pipalrawan',23),(3694,'Pipariya',23),(3695,'Pipariya',23),(3696,'Piplanarayanwar',23),(3697,'Piploda',23),(3698,'Piplya Kumar',23),(3699,'Piplya Mandi',23),(3700,'Pipri',23),(3701,'Pithampur',23),(3702,'Polaykalan',23),(3703,'Porsa',23),(3704,'Prithvipur',23),(3705,'Raghogarh-Vijaypur',23),(3706,'Rahatgarh',23),(3707,'Raisen',23),(3708,'Rajakhedi',23),(3709,'Rajgarh',23),(3710,'Rajgarh',23),(3711,'Rajnagar',23),(3712,'Rajpur',23),(3713,'Ramgarh',23),(3714,'Rampura',23),(3715,'Rampur Baghelan',23),(3716,'Rampur Naikin',23),(3717,'Ranapur',23),(3718,'Ranipur (Tavanagar)',23),(3719,'Ratangarh',23),(3720,'Ratlam',23),(3721,'Rau',23),(3722,'Rehli',23),(3723,'Rehti',23),(3724,'Rewa',23),(3725,'Rosera',23),(3726,'Runji-Gautampura',23),(3727,'Sabalgarh',23),(3728,'Sabo',23),(3729,'Sagar',23),(3730,'Sagar Cantonment',23),(3731,'Sailana',23),(3732,'Sanawad',23),(3733,'Sanchi',23),(3734,'Sangvi',23),(3735,'Santer',23),(3736,'Sarangpur',23),(3737,'Sardarpur',23),(3738,'Sarni',23),(3739,'Satai',23),(3740,'Satlapur',23),(3741,'Satna',23),(3742,'Satwas',23),(3743,'Sausar',23),(3744,'Sawer',23),(3745,'Sehore',23),(3746,'Semaria',23),(3747,'Sendhwa',23),(3748,'Seondha',23),(3749,'Seoni',23),(3750,'Seoni-Malwa',23),(3751,'Sethiya (Sethia)',23),(3752,'Shahdol',23),(3753,'Shahgarh',23),(3754,'Shahpur',23),(3755,'Shahpur',23),(3756,'Shahpura',23),(3757,'Shahpura',23),(3758,'Shajapur',23),(3759,'Shamgarh',23),(3760,'Shamshabad',23),(3761,'Sheopur',23),(3762,'Shivpuri',23),(3763,'Shujalpur',23),(3764,'Sidhi',23),(3765,'Sihora',23),(3766,'Silwani',23),(3767,'Singoli',23),(3768,'Singrauli',23),(3769,'Sinhasa',23),(3770,'Sirgora',23),(3771,'Sirmour (Sirmaur)',23),(3772,'Sironj',23),(3773,'Sitamau',23),(3774,'Sohagpur',23),(3775,'Sonkatch',23),(3776,'Soyatkalan',23),(3777,'Suhagi',23),(3778,'Sultanpur',23),(3779,'Susner',23),(3780,'Suthaliya',23),(3781,'Suwasara',23),(3782,'Swroop Nagar',23),(3783,'Tal',23),(3784,'Talen',23),(3785,'Tarana',23),(3786,'Tarichar Kalan',23),(3787,'Tekanpur',23),(3788,'Tendukheda',23),(3789,'Tendukheda',23),(3790,'Teonthar',23),(3791,'Thandla',23),(3792,'Tikamgarh',23),(3793,'Timarni',23),(3794,'Tirodi',23),(3795,'Tonk Khurd',23),(3796,'Udaipura',23),(3797,'Ujjain',23),(3798,'Ukwa',23),(3799,'Umaria',23),(3800,'Unchahara (Unchehara)',23),(3801,'Unhel',23),(3802,'Vehicle Factory Area Jabalpur',23),(3803,'Vidisha',23),(3804,'Vijaypur',23),(3805,'Vijayraghavgarh',23),(3806,'Waraseoni',23),(3807,'Andro',14),(3808,'Bishnupur',14),(3809,'Chingangbam Leikai',14),(3810,'Heingang',14),(3811,'Heirok',14),(3812,'Hill Town',14),(3813,'Imphal',14),(3814,'Jiribam',14),(3815,'Kakching',14),(3816,'Kakching Khunou',14),(3817,'Kangpokpi',14),(3818,'Khongman',14),(3819,'Khurai Sajor Leikai',14),(3820,'Kiyamgei',14),(3821,'Kshetrigao',14),(3822,'Kumbi',14),(3823,'Kwakta',14),(3824,'Laipham Siphai',14),(3825,'Lairikyengbam Leikai',14),(3826,'Lamjaotongba',14),(3827,'Lamlai',14),(3828,'Lamsang (Lamshang)',14),(3829,'Langjing',14),(3830,'Lilong (Thoubal)',14),(3831,'Lilong (Imphal West)',14),(3832,'Luwangsangbam',14),(3833,'Mayang Imphal',14),(3834,'Moirang',14),(3835,'Moreh',14),(3836,'Nambol',14),(3837,'Naoriya Pakhanglakpa',14),(3838,'Ningthoukhong',14),(3839,'Oinam',14),(3840,'Porompat',14),(3841,'Rengkai',14),(3842,'Sagolband',14),(3843,'Samurou',14),(3844,'Sekmai Bazar',14),(3845,'Sikhong Sekmai',14),(3846,'Sugnu',14),(3847,'Takyel Mapal',14),(3848,'Tamenglong',14),(3849,'Thongju',14),(3850,'Thongkhong Laxmi Bazar',14),(3851,'Thoubal',14),(3852,'Torban (Kshetri Leikai)',14),(3853,'Ukhrul',14),(3854,'Wangjing',14),(3855,'Wangoi',14),(3856,'Yairipok',14),(3857,'Zenhang Lamka',14),(3858,'Baghmara',17),(3859,'Cherrapunjee (Cherrapunji)',17),(3860,'Jowai',17),(3861,'Lawsohtun',17),(3862,'Madanriting (Madanrting)',17),(3863,'Mairang',17),(3864,'Mawlai',17),(3865,'Mawpat',17),(3866,'Nongkseh',17),(3867,'Nongmynsong',17),(3868,'Nongpoh',17),(3869,'Nongstoin',17),(3870,'Nongthymmai',17),(3871,'Resubelpara',17),(3872,'Shillong',17),(3873,'Shillong Cantonment',17),(3874,'Tura',17),(3875,'Umlyngka',17),(3876,'Umpling',17),(3877,'Umroi',17),(3878,'Williamnagar',17),(3879,'Aizawl',15),(3880,'Bairabi',15),(3881,'Biate',15),(3882,'Champhai',15),(3883,'Darlawn',15),(3884,'Hnahthial',15),(3885,'Khawhai',15),(3886,'Khawzawl',15),(3887,'Kolasib',15),(3888,'Lawngtlai',15),(3889,'Lengpui',15),(3890,'Lunglei',15),(3891,'Mamit',15),(3892,'N. Kawnpui',15),(3893,'North Vanlaiphai',15),(3894,'Saiha',15),(3895,'Sairang',15),(3896,'Saitual',15),(3897,'Serchhip',15),(3898,'Thenzawl',15),(3899,'Tlabung',15),(3900,'Vairengte',15),(3901,'Zawlnuam',15),(3902,'Changtongya',13),(3903,'Chumukedima',13),(3904,'Dimapur',13),(3905,'Diphupar \'A\'',13),(3906,'Jalukie',13),(3907,'Kiphire',13),(3908,'Kohima',13),(3909,'Kohima Village',13),(3910,'Kuda',13),(3911,'Longleng',13),(3912,'Medziphema',13),(3913,'Mokokchung',13),(3914,'Mon Town',13),(3915,'Naginimora',13),(3916,'Peren',13),(3917,'Pfutsero',13),(3918,'Phek',13),(3919,'Puranabazar \'A\'',13),(3920,'Rangapahar',13),(3921,'Satakha Hq.',13),(3922,'Tseminyu',13),(3923,'Tuensang',13),(3924,'Tuli',13),(3925,'Wokha',13),(3926,'Zunheboto',13),(3927,'Agastinuagan',21),(3928,'Anandpur',21),(3929,'Anjira',21),(3930,'Anugul (Angul)',21),(3931,'Arjyapalli',21),(3932,'Asika',21),(3933,'Athagad',21),(3934,'Athmallik',21),(3935,'Badagada',21),(3936,'Badakodanda',21),(3937,'Badamba (Nizigarh)',21),(3938,'Badmal',21),(3939,'Balagoda (Bolani)',21),(3940,'Balangir',21),(3941,'Baleshwar (Balasore)',21),(3942,'Baliguda',21),(3943,'Balimela',21),(3944,'Balipatapur',21),(3945,'Balugaon',21),(3946,'Banaigarh',21),(3947,'Banapur',21),(3948,'Bandhbahal',21),(3949,'Bangomunda',21),(3950,'Banki',21),(3951,'Barapali',21),(3952,'Barbil',21),(3953,'Bardol',21),(3954,'Bargarh',21),(3955,'Baripada',21),(3956,'Basudebpur',21),(3957,'Baudhgarh (Boudh)',21),(3958,'Belagachhia',21),(3959,'Bellaguntha (Belaguntha)',21),(3960,'Belpahar',21),(3961,'Bhabinipur',21),(3962,'Bhadrak',21),(3963,'Bhakarsahi',21),(3964,'Bhanjanagar',21),(3965,'Bhapur',21),(3966,'Bhatli',21),(3967,'Bhawanipatna',21),(3968,'Bhuban',21),(3969,'Bhubaneswar',21),(3970,'Bijepur',21),(3971,'Binika',21),(3972,'Biramitrapur',21),(3973,'Birapratappur',21),(3974,'Bishamakatak (Bissam Cuttack)',21),(3975,'Borigam',21),(3976,'Boriguma (Borigumma)',21),(3977,'Brahmabarada',21),(3978,'Brahmapur (Berhampur)',21),(3979,'Brajarajnagar',21),(3980,'Budhapanka',21),(3981,'Buguda',21),(3982,'Bundia',21),(3983,'Burla',21),(3984,'Byasanagar',21),(3985,'Champua',21),(3986,'Chandapur',21),(3987,'Chandili',21),(3988,'Charibatia',21),(3989,'Chhatrapur',21),(3990,'Chikiti',21),(3991,'Chitrakonda',21),(3992,'Choudwar',21),(3993,'Cuttack',21),(3994,'Dadhapatna',21),(3995,'Daitari',21),(3996,'Damanjodi',21),(3997,'Danara',21),(3998,'Daringbadi',21),(3999,'Debagarh',21),(4000,'Dera Colliery Township',21),(4001,'Dhamanagar',21),(4002,'Dhenkanal',21),(4003,'Digapahandi',21),(4004,'Dungamal',21),(4005,'Erei',21),(4006,'Ganjam',21),(4007,'Ghantapada',21),(4008,'Godiputamatiapara',21),(4009,'Golabandha',21),(4010,'Gopalpur',21),(4011,'Gotamara',21),(4012,'Gudari',21),(4013,'G. Udayagiri',21),(4014,'Gunupur',21),(4015,'Hatibandha',21),(4016,'Hinjilicut',21),(4017,'Hirakud',21),(4018,'Indipur',21),(4019,'Itamati',21),(4020,'Jagatsinghapur (Jagatsinghpur)',21),(4021,'Jajanga',21),(4022,'Jajapur (Jajpur)',21),(4023,'Jalda',21),(4024,'Jaleshwar (Jaleswar)',21),(4025,'Jashipur',21),(4026,'Jatani',21),(4027,'Jeypur (Jeypore)',21),(4028,'Jharsuguda',21),(4029,'Jhumpura',21),(4030,'Joda',21),(4031,'Jorada (Bada)',21),(4032,'Junagarh',21),(4033,'Kabatabandha',21),(4034,'Kaipadar',21),(4035,'Kalarangiata',21),(4036,'Kaliapani',21),(4037,'Kalyanasingpur',21),(4038,'Kamakshyanagar',21),(4039,'Kandasar',21),(4040,'Kanheipur',21),(4041,'Kantabanji (Kantabanjhi)',21),(4042,'Kantilo',21),(4043,'Karanjia',21),(4044,'Kashinagar',21),(4045,'Kendrapara',21),(4046,'Kendujhar',21),(4047,'Kesinga',21),(4048,'Khaliapali',21),(4049,'Khalikote (Khallikote)',21),(4050,'Khandapada',21),(4051,'Khariar',21),(4052,'Khariar Road',21),(4053,'Khatiguda',21),(4054,'Khordha',21),(4055,'Kochinda (Kuchinda)',21),(4056,'Kodala',21),(4057,'Koida',21),(4058,'Konark',21),(4059,'Koraput',21),(4060,'Kotpad',21),(4061,'Krushnanandapur',21),(4062,'Kuanrmunda',21),(4063,'Kukudakhandi',21),(4064,'Kulad',21),(4065,'Kullada',21),(4066,'Kunjabangarh',21),(4067,'Kurumuli',21),(4068,'Lalsingi',21),(4069,'Lathikata',21),(4070,'Lochapada',21),(4071,'Loisinga',21),(4072,'Madanpur Rampur',21),(4073,'Majhihara',21),(4074,'Makundapur',21),(4075,'Malkangiri',21),(4076,'Mohana',21),(4077,'Mukhiguda',21),(4078,'Mundamarai',21),(4079,'Nabarangapur (Nabarangpur)',21),(4080,'Nalco',21),(4081,'Nayagarh',21),(4082,'Nilagiri',21),(4083,'Nimapada',21),(4084,'Nuahata',21),(4085,'Nuapatna',21),(4086,'O.C.L. Industrial Township',21),(4087,'Odagaon',21),(4088,'Padmapur',21),(4089,'Palalahada',21),(4090,'Palurgada',21),(4091,'Panposh',21),(4092,'Papadahandi',21),(4093,'Paradip',21),(4094,'Paradipgarh',21),(4095,'Paralakhemundi',21),(4096,'Pathar',21),(4097,'Patnagarh',21),(4098,'Patrapur',21),(4099,'Pattamundai',21),(4100,'Phulabani (Phulbani)',21),(4101,'Pipili',21),(4102,'Pitala',21),(4103,'Polasara',21),(4104,'Pratapsasan',21),(4105,'Puri',21),(4106,'Purusottampur',21),(4107,'Raighar',21),(4108,'Rairangpur',21),(4109,'Rajagangapur (Rajgangpur)',21),(4110,'Rajasunakhala',21),(4111,'Rambha',21),(4112,'Ramgarh',21),(4113,'Ranapurgada',21),(4114,'Raurkela (Rourkela)',21),(4115,'Raurkela Industrial Township',21),(4116,'Rayagada',21),(4117,'Rayagada',21),(4118,'Redhakhol (Rairakhol)',21),(4119,'Remuna',21),(4120,'Rengali',21),(4121,'Rengali Dam Project Township',21),(4122,'R. Udayagiri',21),(4123,'Sambalpur',21),(4124,'Saranga',21),(4125,'Sayadpur',21),(4126,'Sheragada',21),(4127,'Sohela',21),(4128,'Sonapur (Subarnapur, Sonepur)',21),(4129,'Soro',21),(4130,'Subalaya',21),(4131,'Sunabeda',21),(4132,'Sundargarh (Sundergarh)',21),(4133,'Surada',21),(4134,'Surala',21),(4135,'Suvani',21),(4136,'Talcher',21),(4137,'Tangi',21),(4138,'Tarbha',21),(4139,'Tensa',21),(4140,'Tikarpada',21),(4141,'Tipo',21),(4142,'Titlagarh',21),(4143,'Tushura',21),(4144,'Udala',21),(4145,'Umarkote (Umerkote)',21),(4146,'Venkatraipur',21),(4147,'Ariankuppam (Ariyankuppam)',34),(4148,'Karaikal',34),(4149,'Kurumbapet',34),(4150,'Mahé',34),(4151,'Manavely',34),(4152,'Ozhukarai',34),(4153,'Puducherry (Pondicherry)',34),(4154,'Thirumalairayanpattinam',34),(4155,'Villianur',34),(4156,'Yanam',34),(4157,'Abohar',3),(4158,'Adampur',3),(4159,'Ahmedgarh',3),(4160,'Ajnala',3),(4161,'Akalgarh',3),(4162,'Alawalpur',3),(4163,'Alhoran',3),(4164,'Amargarh',3),(4165,'Amloh',3),(4166,'Amritsar',3),(4167,'Amritsar Cantonment',3),(4168,'Anandpur Sahib',3),(4169,'Apra',3),(4170,'Aur',3),(4171,'Baba Bakala',3),(4172,'Baddowal',3),(4173,'Badhni Kalan',3),(4174,'Bagha Purana',3),(4175,'Balachaur',3),(4176,'Balongi',3),(4177,'Banga',3),(4178,'Banur',3),(4179,'Bareta',3),(4180,'Bariwala',3),(4181,'Barnala',3),(4182,'Baryar',3),(4183,'Bassi Pathana',3),(4184,'Batala',3),(4185,'Bathinda',3),(4186,'Begowal',3),(4187,'Behrampur',3),(4188,'Bhadaur',3),(4189,'Bhadson',3),(4190,'Bhagta Bhai Ka',3),(4191,'Bhamian Kalan',3),(4192,'Bhankharpur',3),(4193,'Bhattian',3),(4194,'Bhawanigarh',3),(4195,'Bhikhi',3),(4196,'Bhikhiwind',3),(4197,'Bhisiana',3),(4198,'Bhogpur',3),(4199,'Bhucho Mandi',3),(4200,'Bhulath',3),(4201,'Budha Theh',3),(4202,'Budhlada',3),(4203,'Bungal',3),(4204,'Chachoki',3),(4205,'Chamkaur Sahib',3),(4206,'Cheema',3),(4207,'Chogawan',3),(4208,'Chohal',3),(4209,'Chomon',3),(4210,'Daper',3),(4211,'Dasua (Dasuya)',3),(4212,'Daulatpur',3),(4213,'Dera Baba Nanak',3),(4214,'Dera Bassi',3),(4215,'Dhaki',3),(4216,'Dhanaula',3),(4217,'Dharamkot',3),(4218,'Dhariwal',3),(4219,'Dhilwan',3),(4220,'Dhin',3),(4221,'Dhuri',3),(4222,'Dina Nagar',3),(4223,'Dirba',3),(4224,'Doraha',3),(4225,'Faridkot',3),(4226,'Fatehgarh Churian',3),(4227,'Fateh Nangal',3),(4228,'Fazilka',3),(4229,'Firozpur',3),(4230,'Firozpur Cantonment',3),(4231,'Gardhiwala',3),(4232,'Garhshankar (Garhshanker)',3),(4233,'Ghagga',3),(4234,'Ghanauli',3),(4235,'Ghanaur',3),(4236,'Ghoh',3),(4237,'Gidderbaha (Giddarbaha)',3),(4238,'Gill',3),(4239,'Gobindgarh (Mandi Gobindgarh)',3),(4240,'Goniana',3),(4241,'Goraya',3),(4242,'Gurdaspur',3),(4243,'Guru Har Sahai',3),(4244,'Halwara',3),(4245,'Handiaya',3),(4246,'Hariana',3),(4247,'Hazipur (Hajipur)',3),(4248,'Hoshiarpur',3),(4249,'Hussainpur',3),(4250,'Jagraon',3),(4251,'Jaitu',3),(4252,'Jalalabad',3),(4253,'Jalandhar [Jullundur]',3),(4254,'Jalandhar Cantonment',3),(4255,'Jandiala',3),(4256,'Jandiala',3),(4257,'Jodhan',3),(4258,'Jugial',3),(4259,'Kapurthala',3),(4260,'Kartarpur',3),(4261,'Kathanian',3),(4262,'Khamanon',3),(4263,'Khambra on Nakodar Road',3),(4264,'Khanauri',3),(4265,'Khanna',3),(4266,'Kharar',3),(4267,'Khem Karan',3),(4268,'Khilchian',3),(4269,'Khothran',3),(4270,'Korianwali',3),(4271,'Kot',3),(4272,'Kot Fatta',3),(4273,'Kot Ise Khan',3),(4274,'Kot Kapura',3),(4275,'Kotla Nihang',3),(4276,'Kurali',3),(4277,'Lalru',3),(4278,'Lehragaga',3),(4279,'Lohian Khass',3),(4280,'Longowal',3),(4281,'Ludhiana',3),(4282,'Machhiwara',3),(4283,'Mahilpur',3),(4284,'Majitha',3),(4285,'Makhu',3),(4286,'Malerkotla',3),(4287,'Malikpur',3),(4288,'Mallanwala Khass',3),(4289,'Maloud (Malaudh)',3),(4290,'Malout',3),(4291,'Mamun',3),(4292,'Mansa',3),(4293,'Manwal',3),(4294,'Maur',3),(4295,'Mehna',3),(4296,'Mirpur',3),(4297,'Moga',3),(4298,'Moonak',3),(4299,'Morinda',3),(4300,'Mubarakpur',3),(4301,'Mudal',3),(4302,'Mudki',3),(4303,'Mukerian',3),(4304,'Muktsar (Sri Muktsar Sahib)',3),(4305,'Mullanpur Dakha',3),(4306,'Mullanpur Garib Dass',3),(4307,'Nabha',3),(4308,'Nakodar',3),(4309,'Nangal',3),(4310,'Nangli',3),(4311,'Narot Mehra',3),(4312,'Nawanshahr',3),(4313,'Naya Gaon',3),(4314,'Nehon',3),(4315,'Nilpur',3),(4316,'Nurmahal',3),(4317,'Partap Singhwala',3),(4318,'Pathankot',3),(4319,'Patiala',3),(4320,'Patran',3),(4321,'Patti',3),(4322,'Payal',3),(4323,'Phagwara',3),(4324,'Phagwara Sharki',3),(4325,'Phillaur',3),(4326,'Qadian',3),(4327,'Rahon',3),(4328,'Raikot',3),(4329,'Rail',3),(4330,'Raipur Rasulpur',3),(4331,'Raja Sansi',3),(4332,'Rajpura',3),(4333,'Rakri',3),(4334,'Raman',3),(4335,'Ramdas',3),(4336,'Rampura Phul',3),(4337,'Rayya',3),(4338,'Rupnagar',3),(4339,'Rurki Kasba',3),(4340,'Sahnewal',3),(4341,'Saloh',3),(4342,'Samana',3),(4343,'Samrala',3),(4344,'Sanaur',3),(4345,'Sangat',3),(4346,'Sangrur',3),(4347,'Sansarpur',3),(4348,'Sarai Khas',3),(4349,'Sardulgarh',3),(4350,'Sarna',3),(4351,'Satyewala',3),(4352,'Shahkot',3),(4353,'Sham ChaurasI',3),(4354,'Shikar',3),(4355,'Sirhind Fatehgarh Sahib',3),(4356,'Sohana',3),(4357,'Sri Hargobindpur',3),(4358,'Sufipind',3),(4359,'Sujanpur',3),(4360,'Sultanpur',3),(4361,'Sunam',3),(4362,'Talwandi Bhai',3),(4363,'Talwandi Sabo',3),(4364,'Talwara',3),(4365,'Tapa',3),(4366,'Tarn Taran',3),(4367,'Tharial',3),(4368,'Tharike',3),(4369,'Tibri',3),(4370,'Urmar Tanda',3),(4371,'Zira',3),(4372,'Zirakpur',3),(4373,'1 GB-A',8),(4374,'24 AS-C',8),(4375,'3 e Village',8),(4376,'3 STR',8),(4377,'8 PSD-B',8),(4378,'9 LLG (LALGARH)',8),(4379,'Abu Road',8),(4380,'Ahore',8),(4381,'Ajeetgarh',8),(4382,'Ajmer',8),(4383,'Akedadoongar',8),(4384,'Aklera',8),(4385,'Aligarh',8),(4386,'Alwar',8),(4387,'Amet',8),(4388,'Antah',8),(4389,'Anupgarh',8),(4390,'Asind',8),(4391,'Atru',8),(4392,'Babai',8),(4393,'Badlya',8),(4394,'Baggar',8),(4395,'Bagrana',8),(4396,'Bagru',8),(4397,'Bakani',8),(4398,'Bali',8),(4399,'Balotra',8),(4400,'Banasthali',8),(4401,'Bandikui',8),(4402,'Banswara',8),(4403,'Baral',8),(4404,'Baran',8),(4405,'Bargaon Rural',8),(4406,'Bari',8),(4407,'Bari Sadri',8),(4408,'Barmer',8),(4409,'Baskhoh',8),(4410,'Basni Belima',8),(4411,'Bassi',8),(4412,'Bay',8),(4413,'Bayana',8),(4414,'Bayana Rural',8),(4415,'Beawar',8),(4416,'Bedla',8),(4417,'Beejoliya Kalan (Bijolia)',8),(4418,'Begun',8),(4419,'Behror',8),(4420,'Beriyawali',8),(4421,'Bhadra',8),(4422,'Bhalariya',8),(4423,'Bharatpur',8),(4424,'Bhavri',8),(4425,'Bhawani Mandi',8),(4426,'Bhilwara',8),(4427,'Bhim',8),(4428,'Bhinder',8),(4429,'Bhinmal',8),(4430,'Bhiwadi',8),(4431,'Bhoogar',8),(4432,'Bhusawar',8),(4433,'Bhuwana',8),(4434,'Bichhri',8),(4435,'Bidasar',8),(4436,'Bikaner',8),(4437,'Bilara',8),(4438,'Bissau',8),(4439,'Boraj-Kazipura',8),(4440,'Borawar',8),(4441,'Budhpura',8),(4442,'Bundi',8),(4443,'Chaksu',8),(4444,'Chawand',8),(4445,'Chechat',8),(4446,'Chenar Village',8),(4447,'Chhabra',8),(4448,'Chhapar',8),(4449,'Chhipabarod',8),(4450,'Chhoti Sadri',8),(4451,'Chirawa',8),(4452,'Chittaurgarh (Chittorgarh)',8),(4453,'Chomu',8),(4454,'Churu',8),(4455,'Danta',8),(4456,'Dausa',8),(4457,'Deeg',8),(4458,'Delwara',8),(4459,'Deogarh',8),(4460,'Deoli',8),(4461,'Deshnoke',8),(4462,'Desoola',8),(4463,'Dhariawad',8),(4464,'Dhaulpur (Dholpur)',8),(4465,'Dhorimanna (Dhorimana)',8),(4466,'Didwana',8),(4467,'Diwakari',8),(4468,'Dungargarh',8),(4469,'Dungarpur',8),(4470,'Emri',8),(4471,'Falna',8),(4472,'Fatehnagar',8),(4473,'Fatehpur',8),(4474,'Gajsinghpur',8),(4475,'Galiakot',8),(4476,'Ganganagar (Sri Ganganagar)',8),(4477,'Gangapur',8),(4478,'Gangapur City',8),(4479,'Garhi',8),(4480,'Gogunda',8),(4481,'Goredi Chancha',8),(4482,'Gothan',8),(4483,'Gothra',8),(4484,'Govindgarh',8),(4485,'Govindgarh',8),(4486,'Goyli',8),(4487,'Guhala',8),(4488,'Gulabpura',8),(4489,'Hameer Garh',8),(4490,'Hanumangarh',8),(4491,'Hindaun',8),(4492,'Indragarh',8),(4493,'Islampur',8),(4494,'Jahazpur',8),(4495,'Jaipur',8),(4496,'Jaisalmer',8),(4497,'Jaitaran',8),(4498,'Jalor',8),(4499,'Jamwa Ramgarh',8),(4500,'Jhagarwas',8),(4501,'Jhalawar',8),(4502,'Jhalrapatan',8),(4503,'Jhunjhunu',8),(4504,'Jobner',8),(4505,'Jodhpur',8),(4506,'Kaithoon',8),(4507,'Kaman',8),(4508,'Kanor',8),(4509,'Kanota',8),(4510,'Kanwat',8),(4511,'Kapasan',8),(4512,'Kaprain',8),(4513,'Karanpur',8),(4514,'Karauli',8),(4515,'Kasba Bonli',8),(4516,'Kawai',8),(4517,'Kekri',8),(4518,'Kelwa',8),(4519,'Keshoraipatan',8),(4520,'Kesrisinghpur',8),(4521,'Khairabad',8),(4522,'Khairthal',8),(4523,'Khandela',8),(4524,'Khanpur',8),(4525,'Kherli',8),(4526,'Kherliganj',8),(4527,'Kherwara Chhaoni',8),(4528,'Khetri',8),(4529,'Kishangarh',8),(4530,'Kishangarh',8),(4531,'Kishangarh Renwal',8),(4532,'Kolayat',8),(4533,'Kolvi (Mandi Rajendrapur)',8),(4534,'Kota',8),(4535,'Kotputli',8),(4536,'Kuchaman City',8),(4537,'Kuchera',8),(4538,'Kumbhkot',8),(4539,'Kumher',8),(4540,'Kuri Bhagtasani',8),(4541,'Kushalgarh',8),(4542,'Lachhmangarh (Laxmangarh)',8),(4543,'Ladnu',8),(4544,'Lakheri',8),(4545,'Lalsot',8),(4546,'Losal',8),(4547,'Mahu Kalan',8),(4548,'Mahwa',8),(4549,'Makrana',8),(4550,'Makrana Village',8),(4551,'Malpura',8),(4552,'Malsisar',8),(4553,'Mandalgarh',8),(4554,'Mandawa',8),(4555,'Mandawar',8),(4556,'Mangrol',8),(4557,'Manoharpur (Monoharpur)',8),(4558,'Manoharthana',8),(4559,'Marwar Junction',8),(4560,'Mavli',8),(4561,'Merta City',8),(4562,'Merta Road',8),(4563,'Modak',8),(4564,'Mount Abu',8),(4565,'Mukandgarh (Mukundgarh)',8),(4566,'Mundwa',8),(4567,'Nadbai',8),(4568,'Nagar',8),(4569,'Nagaur',8),(4570,'Nainwa',8),(4571,'Nandri',8),(4572,'Nasirabad',8),(4573,'Nathdwara',8),(4574,'Nawa',8),(4575,'Nawalgarh',8),(4576,'Neem-Ka-Thana',8),(4577,'Neemrana',8),(4578,'Newa Talai',8),(4579,'Nimbahera',8),(4580,'Niwai (Newai)',8),(4581,'Nohar',8),(4582,'Nokha',8),(4583,'Nooan',8),(4584,'Padampur',8),(4585,'Pali',8),(4586,'Parbatsar',8),(4587,'Partapur',8),(4588,'Phalodi',8),(4589,'Phulera',8),(4590,'Pilani',8),(4591,'Pilibanga',8),(4592,'Pindwara',8),(4593,'Pipar City',8),(4594,'Pirawa',8),(4595,'Pokaran (Pokhran)',8),(4596,'Pratapgarh',8),(4597,'Pushkar',8),(4598,'Raisinghnagar',8),(4599,'Rajakhera',8),(4600,'Rajaldesar',8),(4601,'Rajgarh',8),(4602,'Rajgarh',8),(4603,'Rajsamand',8),(4604,'Ramganj Mandi',8),(4605,'Ramgarh',8),(4606,'Ramgarh',8),(4607,'Ramgarh',8),(4608,'Rani',8),(4609,'Ratangarh',8),(4610,'Ratannagar',8),(4611,'Rawatbhata',8),(4612,'Rawatsar',8),(4613,'Reengus',8),(4614,'Reodar',8),(4615,'Rishabhdeo',8),(4616,'Sadri',8),(4617,'Sadulshahar',8),(4618,'Sagwara',8),(4619,'Salumbar',8),(4620,'Sambhar',8),(4621,'Sanchore',8),(4622,'Sangaria',8),(4623,'Sangariya',8),(4624,'Sangod',8),(4625,'Santpur Rural',8),(4626,'Sapotra',8),(4627,'Sardargarh',8),(4628,'Sardarshahar',8),(4629,'Sarmathura',8),(4630,'Sarwar',8),(4631,'Satalkheri',8),(4632,'Sawa',8),(4633,'Sawai Madhopur',8),(4634,'Seemalwara (Simalwara)',8),(4635,'Semari',8),(4636,'Shahjahanpur',8),(4637,'Shahpura',8),(4638,'Shahpura',8),(4639,'Sheoganj',8),(4640,'Sikar',8),(4641,'Singhana',8),(4642,'Sirohi',8),(4643,'Sojat',8),(4644,'Sojat Road',8),(4645,'Sri Madhopur',8),(4646,'Sujangarh',8),(4647,'Suket',8),(4648,'Sumerganj Mandi',8),(4649,'Sumerpur',8),(4650,'Surajgarh',8),(4651,'Suratgarh',8),(4652,'Takhatgarh',8),(4653,'Talera',8),(4654,'Tapookra',8),(4655,'Taranagar',8),(4656,'Tijara',8),(4657,'Todabhim',8),(4658,'Todaraisingh',8),(4659,'Tonk',8),(4660,'Udaipur',8),(4661,'Udaipurwati',8),(4662,'Udpura',8),(4663,'Uniara',8),(4664,'Utarlai',8),(4665,'Vidyavihar',8),(4666,'Vijainagar',8),(4667,'Vijainagar',8),(4668,'Viratnagar',8),(4669,'Weir',8),(4670,'Gangtok (incl. Upper Tadong)',11),(4671,'Gyalshing',11),(4672,'Jorethang',11),(4673,'Mangan',11),(4674,'Namchi',11),(4675,'Nayabazar',11),(4676,'Rangpo',11),(4677,'Rhenak (Rhenock)',11),(4678,'Singtam',11),(4679,'Abiramam',33),(4680,'Achampudur',33),(4681,'Acharapakkam',33),(4682,'Achipatti',33),(4683,'Adaikkakuzhi',33),(4684,'Adikaratti',33),(4685,'Adiyanuthu',33),(4686,'Aduthurai (Maruthuvakudi)',33),(4687,'Agaram',33),(4688,'Agastheeswaram',33),(4689,'Alagappapuram (Azhagappapuram)',33),(4690,'Alamathi',33),(4691,'Alamelumangapuram',33),(4692,'Alampalayam',33),(4693,'Alandur',33),(4694,'Alanganallur',33),(4695,'Alangayam',33),(4696,'Alangudi',33),(4697,'Alangulam',33),(4698,'Alangulam',33),(4699,'Alanthurai',33),(4700,'Alapakkam',33),(4701,'Allapuram',33),(4702,'Alur (Aloor)',33),(4703,'Alwarkurichi',33),(4704,'Alwarthirunagiri',33),(4705,'Amathur',33),(4706,'Ambasamudram',33),(4707,'Ambattur',33),(4708,'Ambur',33),(4709,'Ammainaickanur',33),(4710,'Ammanur',33),(4711,'Ammapattinam',33),(4712,'Ammapettai',33),(4713,'Ammapettai',33),(4714,'Ammavarikuppam',33),(4715,'Ammoor',33),(4716,'Anaimalai',33),(4717,'Anaiyur',33),(4718,'Anaiyur',33),(4719,'Anakaputhur',33),(4720,'Ananthapuram',33),(4721,'Andankoil East',33),(4722,'Andipalayam',33),(4723,'Andipatti Jakkampatti',33),(4724,'Anjugrammam (Anjugramam)',33),(4725,'Annalagraharam',33),(4726,'Annamalai Nagar',33),(4727,'Annavasal',33),(4728,'Annur',33),(4729,'Anthiyur',33),(4730,'Anuppankulam',33),(4731,'Appakudal',33),(4732,'Arachalur',33),(4733,'Arakandanallur',33),(4734,'Arakonam (Arakkonam)',33),(4735,'Aralvaimozhi',33),(4736,'Arani',33),(4737,'Arani (Arni)',33),(4738,'Aranthangi',33),(4739,'Arasiramani',33),(4740,'Arasur',33),(4741,'Aravakurichi',33),(4742,'Aravankad (Aruvankadu)',33),(4743,'Arcot',33),(4744,'Arimalam',33),(4745,'Ariyalur',33),(4746,'Ariyappampalayam',33),(4747,'Ariyur',33),(4748,'Arumanai',33),(4749,'Arumbanur',33),(4750,'Arumbavur',33),(4751,'Arumuganeri',33),(4752,'Aruppukkottai',33),(4753,'Asaripallam',33),(4754,'Ashokapuram',33),(4755,'Athani',33),(4756,'Athanur',33),(4757,'Athimarapatti',33),(4758,'Athipatti',33),(4759,'Athipattu',33),(4760,'Athivilai',33),(4761,'Athur',33),(4762,'Athur',33),(4763,'Attayampatti',33),(4764,'Attur',33),(4765,'Avadattur',33),(4766,'Avadi',33),(4767,'Avalapalli',33),(4768,'Avalpoondurai',33),(4769,'Avanashi (Avinashi)',33),(4770,'Avaniapuram',33),(4771,'A. Vellalapatti (Vellalapatti)',33),(4772,'Ayacode',33),(4773,'Ayakudi',33),(4774,'Ayappakkam',33),(4775,'Aygudi',33),(4776,'Ayothiapattinam',33),(4777,'Ayyalur',33),(4778,'Ayyampalayam',33),(4779,'Ayyampettai',33),(4780,'Ayyampettai',33),(4781,'Ayyappanthangal',33),(4782,'Balakrishnampatti',33),(4783,'Balakrishnapuram',33),(4784,'Balasamudram',33),(4785,'Bargur',33),(4786,'Batlagundu',33),(4787,'Belur',33),(4788,'Bhavani',33),(4789,'Bhavanisagar',33),(4790,'Bhuvanagiri',33),(4791,'Bikketti',33),(4792,'B.Mallapuram',33),(4793,'B. Meenakshipuram',33),(4794,'Bodinayakanur (Bodinayakkanur)',33),(4795,'Boothapandi',33),(4796,'Boothipuram',33),(4797,'Brahmana Periya Agraharam',33),(4798,'Chakkarapalli',33),(4799,'Chathirareddipatti',33),(4800,'Chatrapatti',33),(4801,'Chenbagaramanputhur',33),(4802,'Chengalpattu',33),(4803,'Chengam',33),(4804,'Chengappalli',33),(4805,'Chennagiri',33),(4806,'Chennai [Madras]',33),(4807,'Chennasamudram',33),(4808,'Chennimalai',33),(4809,'Cheranmadevi',33),(4810,'Chetpet (Chettupattu)',33),(4811,'Chettiarpatti',33),(4812,'Chettinaickenpatti',33),(4813,'Chettipalayam',33),(4814,'Chettipalayam',33),(4815,'Chettithangal',33),(4816,'Chidambaram',33),(4817,'Chidambaram Nm',33),(4818,'Chinna Anuppanadi',33),(4819,'Chinnakalayamputhur',33),(4820,'Chinnakkampalayam',33),(4821,'Chinnalapatti',33),(4822,'Chinnamanur',33),(4823,'Chinnamudalaipatti',33),(4824,'Chinnasalem',33),(4825,'Chinnasekkadu',33),(4826,'Chinnathadagam',33),(4827,'Chinnavedampatti',33),(4828,'Chinniam palayam',33),(4829,'Chithode',33),(4830,'Chitlapakkam',33),(4831,'Cholapuram',33),(4832,'Choozhal',33),(4833,'Coimbatore',33),(4834,'Colachel (Kolachal)',33),(4835,'Coonoor',33),(4836,'Courtalam (Courtallam)',33),(4837,'Cuddalore',33),(4838,'Dalavaipatti',33),(4839,'Damalerimuthur',33),(4840,'Dasanaickenpatti',33),(4841,'Denkanikottai',33),(4842,'Desur',33),(4843,'Devadanapatti',33),(4844,'Devakottai',33),(4845,'Devarshola',33),(4846,'Devasthanam',33),(4847,'Devikapuram',33),(4848,'Devipattinam',33),(4849,'Dhalavoipuram',33),(4850,'Dhali',33),(4851,'Dhaliyur',33),(4852,'Dharamapuram',33),(4853,'Dharapadavedu',33),(4854,'Dharapuram',33),(4855,'Dharasuram (Darasuram)',33),(4856,'Dharmapuri',33),(4857,'Dindigul',33),(4858,'Doramangalam',33),(4859,'Dusi',33),(4860,'Edaganasalai',33),(4861,'Edaicode (Edaikodu)',33),(4862,'Edakalinadu',33),(4863,'Edappadi',33),(4864,'Edayanchavadi',33),(4865,'Elathur',33),(4866,'Elayirampannai',33),(4867,'Ellakkudy',33),(4868,'Ellandaikuttai',33),(4869,'Elumalai',33),(4870,'Eral',33),(4871,'Eranapuram',33),(4872,'Eraniel',33),(4873,'Eriodu (Eriyodu)',33),(4874,'Erode',33),(4875,'Erumaipatti',33),(4876,'Erumapalayam',33),(4877,'Eruvadi',33),(4878,'Ethapur',33),(4879,'Ettayapuram',33),(4880,'Ettimadai',33),(4881,'Ezhudesam',33),(4882,'Ganapathipuram',33),(4883,'Gandhinagar (Katpadi Extn)',33),(4884,'Gandipuram',33),(4885,'Gangaikondan',33),(4886,'Gangavalli',33),(4887,'Ganguvarpatti',33),(4888,'Gerugambakkam',33),(4889,'Gingee',33),(4890,'Gobichettipalayam',33),(4891,'Gopalasamudram',33),(4892,'Goundampalayam',33),(4893,'Gudalur',33),(4894,'Gudalur',33),(4895,'Gudalur',33),(4896,'Gudiyatham',33),(4897,'Gummidipoondi',33),(4898,'Gunduuppalavadi',33),(4899,'Hale-Dharmapuri',33),(4900,'Hanumanthampatti',33),(4901,'Harur',33),(4902,'Harveypatti',33),(4903,'Highways',33),(4904,'Hosur',33),(4905,'Hubbathala',33),(4906,'Huligal',33),(4907,'Idikarai',33),(4908,'Iduvai',33),(4909,'Ilampillai (Elampillai)',33),(4910,'Ilanji',33),(4911,'Ilayangudi (Ilaiyangudi)',33),(4912,'Iluppaiyurani',33),(4913,'Iluppur',33),(4914,'Inam Karur',33),(4915,'Inam Maniyachi',33),(4916,'Injambakkam',33),(4917,'Iravadanallur',33),(4918,'Irugur',33),(4919,'Jaffrabad',33),(4920,'Jagathala',33),(4921,'Jalakandapuram',33),(4922,'Jalladiampet',33),(4923,'Jambai',33),(4924,'Jayankondam',33),(4925,'Jolarpet',33),(4926,'Kadambathur',33),(4927,'Kadambur',33),(4928,'Kadaparai',33),(4929,'Kadathur',33),(4930,'Kadayal',33),(4931,'Kadayam',33),(4932,'Kadayampatti',33),(4933,'Kadayanallur',33),(4934,'Kadhirvedu',33),(4935,'Kailasagiri',33),(4936,'Kakkalur',33),(4937,'Kalakad (Kalakkad)',33),(4938,'Kalambur',33),(4939,'Kalapatti',33),(4940,'Kalappanaickenpatti',33),(4941,'Kalavai',33),(4942,'Kalinjur',33),(4943,'Kaliyakkavilai',33),(4944,'Kalladaikurichi',33),(4945,'Kallakkurichi (Kallakurichi)',33),(4946,'Kallakudi (Kallakudy)',33),(4947,'Kallangudy',33),(4948,'Kallukuttam',33),(4949,'Kalparapatti',33),(4950,'Kalugumalai',33),(4951,'Kamayagoundanpatti',33),(4952,'Kambainallur',33),(4953,'Kambam (Cumbum)',33),(4954,'Kamuthi',33),(4955,'Kanadukathan',33),(4956,'Kanam',33),(4957,'Kancheepuram (Kanchipuram)',33),(4958,'Kandanur',33),(4959,'Kangeyam',33),(4960,'Kangeyanallur',33),(4961,'Kaniyambadi',33),(4962,'Kaniyur',33),(4963,'Kaniyur',33),(4964,'Kanjikoil',33),(4965,'Kannamangalam',33),(4966,'Kannampalayam',33),(4967,'Kannanendal (Kannadendal)',33),(4968,'Kannankurichi',33),(4969,'Kannanoor',33),(4970,'Kannapalayam',33),(4971,'Kannivadi',33),(4972,'Kannivadi',33),(4973,'Kanniyakumari (Kanyakumari)',33),(4974,'Kappiyarai',33),(4975,'Karadipatti',33),(4976,'Karaikkudi (Karaikudi)',33),(4977,'Karaipudur',33),(4978,'Karamadai',33),(4979,'Karambakkam',33),(4980,'Karambakkudi',33),(4981,'Kariamangalam',33),(4982,'Kariapatti',33),(4983,'Karugampattur',33),(4984,'Karukkalvadi',33),(4985,'Karumandi Chellipalayam',33),(4986,'Karumathampatti',33),(4987,'Karungal',33),(4988,'Karunguzhi',33),(4989,'Karuppur',33),(4990,'Karur',33),(4991,'Kasinayagampatti',33),(4992,'Kasipalayam (E)',33),(4993,'Katpadi',33),(4994,'Kattathurai',33),(4995,'Kattimancode',33),(4996,'Kattivakkam (Kathivakkam)',33),(4997,'Kattumannarkoil',33),(4998,'Kattupakkam',33),(4999,'Kattuputhur',33),(5000,'Kaveripakkam',33),(5001,'Kaveripattinam',33),(5002,'Kayalpattinam',33),(5003,'Kayatharu',33),(5004,'Keelakarai (Kilakarai)',33),(5005,'Keelamanjakudi',33),(5006,'Keeramangalam',33),(5007,'Keeranur',33),(5008,'Keeranur',33),(5009,'Keeripatti',33),(5010,'Keezhkulam (Kilkulam)',33),(5011,'Kelamangalam',33),(5012,'Kembainaickenpalayam',33),(5013,'Kethi (Ketti)',33),(5014,'Kila Ambur',33),(5015,'Kilampadi',33),(5016,'Kilapavoor (Keezhapavur)',33),(5017,'Kilkunda',33),(5018,'Killai',33),(5019,'Killiyoor (Killiyur)',33),(5020,'Kilmanavur',33),(5021,'Kilpennathur (Kizh-Pennathur)',33),(5022,'Kilpudupakkam',33),(5023,'Kilvaithinankuppam',33),(5024,'Kilvelur',33),(5025,'Kinathukadavu',33),(5026,'K.Madapur',33),(5027,'Kodaikanal',33),(5028,'Kodavasal (Kudavasal)',33),(5029,'Kodivalasa',33),(5030,'Kodumudi',33),(5031,'Koilambakkam',33),(5032,'Koilpalayam',33),(5033,'Kolappalur',33),(5034,'Kolathupalayam',33),(5035,'Kolathur',33),(5036,'Kollancode (Kollankodu)',33),(5037,'Kollankoil',33),(5038,'Komaralingam',33),(5039,'Kombai',33),(5040,'Konavattam',33),(5041,'Kondalampatti',33),(5042,'Kondappanaickenpatti',33),(5043,'Kondasamudram',33),(5044,'Kondichettipatti',33),(5045,'Kondur',33),(5046,'Konerikuppam',33),(5047,'Konganapuram',33),(5048,'Kooraikundu',33),(5049,'Koothappar',33),(5050,'Koradacheri',33),(5051,'Kosavampatti',33),(5052,'Kotagiri',33),(5053,'Kothanallur (Kothinallur)',33),(5054,'Kottagoundampatty',33),(5055,'Kottaiyur',33),(5056,'Kottakuppam',33),(5057,'Kottaram',33),(5058,'Kottivakkam',33),(5059,'Kottur',33),(5060,'Kovalam (Covelong)',33),(5061,'Kovilpatti',33),(5062,'Kovur',33),(5063,'Krishnagiri',33),(5064,'Krishnarayapuram',33),(5065,'Krishnasamudram',33),(5066,'Kuchanur',33),(5067,'Kuhalur',33),(5068,'Kulappuram',33),(5069,'Kulasekaram (Kulasekarapuram)',33),(5070,'Kulathur (Kulathoor)',33),(5071,'Kulithalai',33),(5072,'Kullursandai',33),(5073,'Kumaragiri',33),(5074,'Kumarapalayam (Komarapalayam)',33),(5075,'Kumarapuram',33),(5076,'Kumbakonam',33),(5077,'Kundrathur',33),(5078,'Kuniyamuthur',33),(5079,'Kunnathur',33),(5080,'Kurichi',33),(5081,'Kurinjipadi',33),(5082,'Kurudampalayam',33),(5083,'Kurukkupatti',33),(5084,'Kurumbalur',33),(5085,'Kurumbapatti',33),(5086,'Kuruppanaickenpalayam',33),(5087,'Kuthalam',33),(5088,'Kuthanallur',33),(5089,'Kuthankuzhi',33),(5090,'Kuzhithurai',33),(5091,'Labbaikudikadu',33),(5092,'Lakkampatti',33),(5093,'Lakkiampatti',33),(5094,'Lakshminarayanapuram',33),(5095,'Lalgudi',33),(5096,'Lalpet',33),(5097,'Madaharpakkam',33),(5098,'Madambakkam',33),(5099,'Madathukulam',33),(5100,'Madavaram (Madhavaram)',33),(5101,'Madippakkam (Madipakkam)',33),(5102,'Madukkarai',33),(5103,'Madukkur',33),(5104,'Madurai',33),(5105,'Maduranthakam',33),(5106,'Maduravoyal',33),(5107,'Majaragollappatti',33),(5108,'Makkinampatti',33),(5109,'Malayadi',33),(5110,'Mallamooppampatti',33),(5111,'Mallankinaru',33),(5112,'Mallasamudram',33),(5113,'Mallur',33),(5114,'Malumichampatti',33),(5115,'Mamallapuram (Mahabalipuram)',33),(5116,'Mamsapuram',33),(5117,'Manachanallur',33),(5118,'Manakudi',33),(5119,'Manali',33),(5120,'Manalmedu',33),(5121,'Manalurpet',33),(5122,'Manamadurai',33),(5123,'Manapakkam',33),(5124,'Manapparai',33),(5125,'Manavalakurichi',33),(5126,'Mancad',33),(5127,'Mandaikadu',33),(5128,'Mandapam',33),(5129,'Mangadu',33),(5130,'Mangalam',33),(5131,'Mangalampet',33),(5132,'Manickapuram',33),(5133,'Manimutharu',33),(5134,'Manjakollai',33),(5135,'Manjalumoodu',33),(5136,'Mannarai',33),(5137,'Mannargudi',33),(5138,'Manthithoppu',33),(5139,'Mappilaiurani',33),(5140,'Maraimalainagar',33),(5141,'Marakkanam',33),(5142,'Maramangalathupatti',33),(5143,'Marandahalli',33),(5144,'Markayankottai',33),(5145,'Marudur',33),(5146,'Marungur (Marungoor)',33),(5147,'Maruthancode',33),(5148,'Masinaickenpatty',33),(5149,'Mathicode',33),(5150,'Mathigiri',33),(5151,'Mathur',33),(5152,'Mayiladuthurai',33),(5153,'Mecheri',33),(5154,'Medavakkam',33),(5155,'Meenambakkam',33),(5156,'Melacheval',33),(5157,'Melachokkanathapuram',33),(5158,'Melagaram',33),(5159,'Melamadai',33),(5160,'Melaparthibanur',33),(5161,'Melathiruppanthuruthi',33),(5162,'Melattur',33),(5163,'Melpattampakkam',33),(5164,'Melur',33),(5165,'Melvisharam',33),(5166,'Methukummal',33),(5167,'Mettamalai',33),(5168,'Mettunasuvanpalayam',33),(5169,'Mettupalayam',33),(5170,'Mettupalayam',33),(5171,'Mettur',33),(5172,'Mevalurkuppam',33),(5173,'Midalam',33),(5174,'Milavittan',33),(5175,'Minampalli-Pachamadevi',33),(5176,'Minjur',33),(5177,'Modakurichi',33),(5178,'Mohanur',33),(5179,'Molachur',33),(5180,'Mookondapalli',33),(5181,'Moolakaraipatti',33),(5182,'Moovarasampettai',33),(5183,'Mopperipalayam',33),(5184,'Morattupalayam',33),(5185,'Mudukulathur',33),(5186,'Mugalivakkam',33),(5187,'Mukasipidariyur',33),(5188,'Mukkudal',33),(5189,'Mulagumudu',33),(5190,'Mulanur',33),(5191,'Mullipattu',33),(5192,'Muruganpalayam',33),(5193,'Musiri',33),(5194,'Muthanampalayam',33),(5195,'Muthugoundam Pudur',33),(5196,'Muthukadu',33),(5197,'Muthupet',33),(5198,'Muthur',33),(5199,'Muttayyapuram',33),(5200,'Muzhucode',33),(5201,'Mylaudy (Myladi)',33),(5202,'Nadaikavu',33),(5203,'Nadukuthagai',33),(5204,'Naduvaneri',33),(5205,'Naduvattam',33),(5206,'Nagamalaipudukottai',33),(5207,'Nagamangalam',33),(5208,'Nagapattinam',33),(5209,'Nagavakulam',33),(5210,'Nagercoil',33),(5211,'Nagojanahalli',33),(5212,'Nallampatti',33),(5213,'Nallipalayam',33),(5214,'Nalloor (Nallur)',33),(5215,'Nallur',33),(5216,'Nallur $',33),(5217,'Namagiripettai',33),(5218,'Namakkal',33),(5219,'Nambiyur',33),(5220,'Nandambakkam',33),(5221,'Nandivaram - Guduvancheri',33),(5222,'Nangavalli',33),(5223,'Nangavaram',33),(5224,'Nanguneri',33),(5225,'Nanjikottai',33),(5226,'Nannilam',33),(5227,'Naranammalpuram',33),(5228,'Naranapuram',33),(5229,'Narasimhanaicken-palayam',33),(5230,'Narasingam',33),(5231,'Narasingapuram',33),(5232,'Narasingapuram',33),(5233,'Naravarikuppam',33),(5234,'Nasiyanur',33),(5235,'Natchiarkoil',33),(5236,'Natham',33),(5237,'Nathampannai',33),(5238,'Natrampalli',33),(5239,'Nattalam',33),(5240,'Nattapettai',33),(5241,'Nattarasankottai',33),(5242,'Navalpattu',33),(5243,'Navlock Garden',33),(5244,'Nazarathpettai',33),(5245,'Nazerath',33),(5246,'Nedungundram',33),(5247,'Needamangalam',33),(5248,'Neelagiri',33),(5249,'Neelambur',33),(5250,'Neelankarai',33),(5251,'Neikkarapatti',33),(5252,'Nellikuppam',33),(5253,'Nelliyalam',33),(5254,'Nemili',33),(5255,'Nemilicheri',33),(5256,'Neripperichal',33),(5257,'Nerkunram (Nerkundram)',33),(5258,'Nerkuppai',33),(5259,'Nerunjipettai',33),(5260,'Neykkarappatti',33),(5261,'Neyveli',33),(5262,'Neyyoor',33),(5263,'Nilaiyur I Bit',33),(5264,'Nilakkottai',33),(5265,'Nolambur',33),(5266,'Nullivilai',33),(5267,'Odaipatti',33),(5268,'Odaiyakulam',33),(5269,'Oddanchatram',33),(5270,'Odugathur',33),(5271,'Oggiyamduraipakkam',33),(5272,'Olagadam',33),(5273,'Omalur',33),(5274,'Orathanadu (Mukthambalpuram)',33),(5275,'Orikkai',33),(5276,'Othakadai',33),(5277,'Othakalmandapam',33),(5278,'Ottapparai',33),(5279,'O\' Valley',33),(5280,'Overi',33),(5281,'Pachchal',33),(5282,'Pacode',33),(5283,'Padaiveedu',33),(5284,'Padandal',33),(5285,'Padappai',33),(5286,'Padianallur',33),(5287,'Padikkasu vaithanpatti',33),(5288,'Padirikuppam',33),(5289,'Padmanabhapuram',33),(5290,'Painkulam',33),(5291,'Paiyur',33),(5292,'Palaganangudy',33),(5293,'Palakkodu',33),(5294,'Palamedu',33),(5295,'Palangarai',33),(5296,'Palani',33),(5297,'Palani Chettipatti',33),(5298,'Palappallam',33),(5299,'Palavakkam',33),(5300,'Palavansathu',33),(5301,'Palayam',33),(5302,'Palayampatti',33),(5303,'Palladam',33),(5304,'Pallanthurai',33),(5305,'Pallapalayam',33),(5306,'Pallapalayam',33),(5307,'Pallapatti',33),(5308,'Pallapatti',33),(5309,'Pallathur',33),(5310,'Pallavaram',33),(5311,'Pallikaranai',33),(5312,'Pallikonda',33),(5313,'Pallipalayam',33),(5314,'Pallipalayam Agraharam',33),(5315,'Pallipattu',33),(5316,'Pallippadai',33),(5317,'Paloor',33),(5318,'Palugal',33),(5319,'Pammal',33),(5320,'Panagudi',33),(5321,'Panaimarathupatti',33),(5322,'Panapakkam',33),(5323,'Pandamangalam',33),(5324,'Pandavarmangalam',33),(5325,'Pannaikadu',33),(5326,'Pannaipuram',33),(5327,'Panpoli',33),(5328,'Panruti',33),(5329,'Papanasam',33),(5330,'Pappankurichi',33),(5331,'Papparapatti',33),(5332,'Papparapatti',33),(5333,'Pappireddipatti',33),(5334,'Paramakudi',33),(5335,'Paramathi',33),(5336,'Parangipettai',33),(5337,'Paraniputhur',33),(5338,'Paravai',33),(5339,'Pasur',33),(5340,'Pathamadai (Pattamadai)',33),(5341,'Pattanam',33),(5342,'Pattinam',33),(5343,'Pattinamkattan',33),(5344,'Pattiveeranpatti',33),(5345,'Pattukkottai',33),(5346,'Pavali',33),(5347,'Peddikuppam',33),(5348,'Peerkankaranai',33),(5349,'Pennadam',33),(5350,'Pennagaram',33),(5351,'Pennathur',33),(5352,'Peraiyur',33),(5353,'Peralam',33),(5354,'Perambakkam',33),(5355,'Perambalur',33),(5356,'Peranamallur',33),(5357,'Peravurani',33),(5358,'Periagaram',33),(5359,'Periakottai',33),(5360,'Periapattinam (Periyapattinam)',33),(5361,'Periyakodiveri',33),(5362,'Periyakulam',33),(5363,'Periyakurichi',33),(5364,'Periyamanali',33),(5365,'Periyanaicken-palayam',33),(5366,'Periya Negamam',33),(5367,'Periyapatti',33),(5368,'Periyasemur',33),(5369,'Pernampattu',33),(5370,'Perumagalur',33),(5371,'Perumagoundampatti',33),(5372,'Perumanallur',33),(5373,'Perumandi',33),(5374,'Perundurai',33),(5375,'Perungalathur',33),(5376,'Perungudi',33),(5377,'Perungulam',33),(5378,'Perur',33),(5379,'Perur Chettipalayam',33),(5380,'Peruvilai',33),(5381,'Pethampalayam',33),(5382,'Pethanaickenpalayam',33),(5383,'Pichandarkovil',33),(5384,'Pillanallur',33),(5385,'P. J. Cholapuram',33),(5386,'P. Mettupalayam',33),(5387,'P. N. Patti',33),(5388,'Polichalur',33),(5389,'Pollachi',33),(5390,'Polur',33),(5391,'Ponmanai',33),(5392,'Ponnamaravathi',33),(5393,'Ponnampatti',33),(5394,'Ponneri',33),(5395,'Poolambadi',33),(5396,'Poolampatti',33),(5397,'Poolankinar',33),(5398,'Pooluvapatti',33),(5399,'Poonamallee',33),(5400,'Poravacheri',33),(5401,'Porur',33),(5402,'Pothanur',33),(5403,'Pothatturpettai',33),(5404,'Pudiyamputhur',33),(5405,'Pudukkottai',33),(5406,'Pudukkottai',33),(5407,'Pudupalayam',33),(5408,'Pudupalayam Agraharam',33),(5409,'Pudupatti',33),(5410,'Pudupattinam',33),(5411,'Pudupattinam',33),(5412,'Pudur (S)',33),(5413,'Puduvayal',33),(5414,'Puliankudi (Puliyankudi)',33),(5415,'Puliyoorsalai',33),(5416,'Puliyur',33),(5417,'Pullampadi (Pullambadi)',33),(5418,'Punjaipugalur',33),(5419,'Punjaipuliampatti',33),(5420,'Punjai Thottakurichi',33),(5421,'Puthagaram',33),(5422,'Puthalam',33),(5423,'Putheri',33),(5424,'Puthukkadai',33),(5425,'Puthur Agraharam',33),(5426,'Puvalur (Poovalur)',33),(5427,'Puzhal',33),(5428,'Puzhithivakkam (Ullagaram)',33),(5429,'Rajapalayam',33),(5430,'Rajapalayam',33),(5431,'Ramalingapuram',33),(5432,'Ramanathapuram',33),(5433,'Ramapuram',33),(5434,'Rameswaram',33),(5435,'Ranipettai (Ranipet)',33),(5436,'Rasipuram',33),(5437,'Rayagiri',33),(5438,'Reethapuram',33),(5439,'Rosalpatti',33),(5440,'R. Pudupatti',33),(5441,'R. S. Mangalam',33),(5442,'Rudravathi',33),(5443,'Sakkarakottai',33),(5444,'Sakkimangalam',33),(5445,'Salamedu',33),(5446,'Salangapalayam',33),(5447,'Salem',33),(5448,'Samalapuram',33),(5449,'Samanatham',33),(5450,'Samathur',33),(5451,'Samayanallur',33),(5452,'Sambavar Vadagarai',33),(5453,'Samusigapuram',33),(5454,'Sankaramanallur',33),(5455,'Sankarankoil (Sankarankovil)',33),(5456,'Sankaraperi',33),(5457,'Sankarapuram',33),(5458,'Sankarapuram',33),(5459,'Sankari (Sankagiri)',33),(5460,'Sankarnagar',33),(5461,'Sanniyasigundu',33),(5462,'Saravanampatti',33),(5463,'Sarcarsamakulam',33),(5464,'Sathankulam',33),(5465,'Sathiyavijayanagaram',33),(5466,'Sathkar',33),(5467,'Sathuvachari (Sathuvacheri)',33),(5468,'Sathyamangalam',33),(5469,'Sattur',33),(5470,'Sayalgudi',33),(5471,'Sayapuram',33),(5472,'Seerapalli',33),(5473,'Seithur',33),(5474,'Selathampatti',33),(5475,'Sembakkam',33),(5476,'Sembedu',33),(5477,'Sembianallur',33),(5478,'Semmipalayam',33),(5479,'Senapiratti',33),(5480,'Sengamalanachiarpatti',33),(5481,'Senneerkuppam',33),(5482,'Senthamangalam',33),(5483,'Sentharapatti',33),(5484,'Senur',33),(5485,'Sethiathoppu',33),(5486,'Sevilimedu',33),(5487,'Sevugampatti',33),(5488,'Sevur',33),(5489,'Sevur',33),(5490,'Shenbakkam',33),(5491,'Shenkottai (Sengottai)',33),(5492,'Sholavandan',33),(5493,'Sholinganallur',33),(5494,'Sholingur (Sholinghur)',33),(5495,'Sholur',33),(5496,'Sikkarayapuram',33),(5497,'Silaiman',33),(5498,'Silapadi',33),(5499,'Singampuneri (Singampunari)',33),(5500,'Singaperumalkoil',33),(5501,'Sircar Periapalayam',33),(5502,'Sirkali (Sirkazhi)',33),(5503,'Sirugamani',33),(5504,'Sirukalathur',33),(5505,'Sirukaveripakkam',33),(5506,'Sirumugai',33),(5507,'Sithayankottai',33),(5508,'Sithurajapuram',33),(5509,'Sivaganga',33),(5510,'Sivagiri',33),(5511,'Sivagiri',33),(5512,'Sivagiripatti',33),(5513,'Sivagnanapuram',33),(5514,'Sivakasi',33),(5515,'Sivanthipuram',33),(5516,'Somayampalayam',33),(5517,'Soolakkarai',33),(5518,'Soorapattu',33),(5519,'South Kannanur',33),(5520,'South Kodikulam',33),(5521,'South Nallur',33),(5522,'Srikalikapuram',33),(5523,'Srimushnam',33),(5524,'Sriperumbudur',33),(5525,'Sriramapuram',33),(5526,'Srivaikuntam',33),(5527,'Srivilliputhur',33),(5528,'Suchindrum (Suchindram)',33),(5529,'Suleeswaranpatti',33),(5530,'Sulur',33),(5531,'Sumaitheerthapuram',33),(5532,'Sundarapandiam',33),(5533,'Sundarapandianpattinam',33),(5534,'Sundarapandiapuram',33),(5535,'SuPallipattu',33),(5536,'Surampatti',33),(5537,'Surandai',33),(5538,'Suriyampalayam',33),(5539,'Swamimalai',33),(5540,'Tajpura',33),(5541,'Tambaram',33),(5542,'Tenkasi',33),(5543,'Terkukallikulam',33),(5544,'Thadikarankonam',33),(5545,'Thadikombu',33),(5546,'Thakkolam',33),(5547,'Thalainayar',33),(5548,'Thalakudi',33),(5549,'Thamaraikulam',33),(5550,'Thammampatti',33),(5551,'Thanakkankulam',33),(5552,'Thanjavur',33),(5553,'Thanthoni',33),(5554,'Thappakuttai',33),(5555,'Tharamangalam',33),(5556,'Tharangambadi',33),(5557,'Thathaiyangarpet',33),(5558,'Thathankuttai',33),(5559,'Thazhakudy',33),(5560,'Thedavur',33),(5561,'Theerthagiriyampattu',33),(5562,'Thenambakkam',33),(5563,'Thengampudur',33),(5564,'Theni Allinagaram',33),(5565,'Thenkarai',33),(5566,'Thenkarai',33),(5567,'Thenthamaraikulam',33),(5568,'Thenthiruperai',33),(5569,'Therur (Theroor)',33),(5570,'Thevaram',33),(5571,'Thevur',33),(5572,'Thiagadurgam',33),(5573,'Thikkanamcode',33),(5574,'Thindal',33),(5575,'Thingalnagar',33),(5576,'Thirparappu (Thiruparappu)',33),(5577,'Thirukarungudi',33),(5578,'Thirukkattupalli',33),(5579,'Thirumalayampalayam',33),(5580,'Thirumalpur',33),(5581,'Thirumangalam (Tirumangalam)',33),(5582,'Thirumazhisai',33),(5583,'Thirumuruganpoondi',33),(5584,'Thirunagar',33),(5585,'Thirunageswaram',33),(5586,'Thiruneermalai',33),(5587,'Thirunindravur (Thiruninravur)',33),(5588,'Thiruparankundram',33),(5589,'Thiruporur',33),(5590,'Thiruppalai',33),(5591,'Thiruppanandal',33),(5592,'Thirupuvanam (Thirubuvanam)',33),(5593,'Thirupuvanam',33),(5594,'Thiruthangal',33),(5595,'Thiruthuraipoondi',33),(5596,'Thiruvaiyaru',33),(5597,'Thiruvalam',33),(5598,'Thiruvallur (Tiruvallur)',33),(5599,'Thiruvarur',33),(5600,'Thiruvattar',33),(5601,'Thiruvenkadam',33),(5602,'Thiruvennainallur',33),(5603,'Thiruverumbur',33),(5604,'Thiruvidaimarudur',33),(5605,'Thisayanvilai',33),(5606,'Thondamuthur',33),(5607,'Thondi',33),(5608,'Thoothukkudi (Thoothukudi)',33),(5609,'Thorapadi',33),(5610,'Thorapadi',33),(5611,'Thottipalayam',33),(5612,'Thottiyam',33),(5613,'Thozhur',33),(5614,'Thudiyalur',33),(5615,'Thuraiyur',33),(5616,'Thuthipattu',33),(5617,'Thuvakudi',33),(5618,'Timiri',33),(5619,'Tindivanam',33),(5620,'Tiruchendur (Thiruchendur)',33),(5621,'Tiruchengode',33),(5622,'Tiruchirappalli',33),(5623,'Tirukalukundram',33),(5624,'Tirukkoyilur (Tirukoilur)',33),(5625,'Tirumalaigiri',33),(5626,'Tirunelveli',33),(5627,'Tirupathur (Tiruppattur)',33),(5628,'Tirupathur',33),(5629,'Tirupattur',33),(5630,'Tiruppur',33),(5631,'Tirusulam',33),(5632,'Tiruttani (Thiruttani)',33),(5633,'Tiruvannamalai',33),(5634,'Tiruverkadu',33),(5635,'Tiruvethipuram (Cheyyar)',33),(5636,'Tiruvottiyur',33),(5637,'Tittacheri',33),(5638,'Tittakudi',33),(5639,'Tittangulam',33),(5640,'T.Kallupatti',33),(5641,'TNPL Pugalur',33),(5642,'Udangudi',33),(5643,'Udayarpalayam',33),(5644,'Udhagamandalam (Ooty)',33),(5645,'Udumalaipettai',33),(5646,'Ullur',33),(5647,'Ulundurpettai',33),(5648,'Unjalur',33),(5649,'Unnamalaikadai',33),(5650,'Uppidamangalam',33),(5651,'Uppiliapuram',33),(5652,'Urapakkam',33),(5653,'Usilampatti',33),(5654,'Usuppur',33),(5655,'Uthamapalayam',33),(5656,'Uthangarai',33),(5657,'Uthayendram',33),(5658,'Uthiramerur',33),(5659,'Uthukkottai (Uthukottai)',33),(5660,'Uthukuli',33),(5661,'Vadakarai Keezhpadugai',33),(5662,'Vadakkanandal',33),(5663,'Vadakkuvalliyur',33),(5664,'Vadalur',33),(5665,'Vadamadurai',33),(5666,'Vadavalli',33),(5667,'Vaddakkankulam',33),(5668,'Vadi',33),(5669,'Vadipatti',33),(5670,'Vadugapatti',33),(5671,'Vadugapatti',33),(5672,'Vaitheeswarankoil',33),(5673,'Valangaiman',33),(5674,'Valasaravakkam',33),(5675,'Valathur',33),(5676,'Valavandankottai',33),(5677,'Valavanur',33),(5678,'Valayambattu',33),(5679,'Vallam',33),(5680,'Vallam',33),(5681,'Valparai',33),(5682,'Valvaithankoshtam',33),(5683,'Vanagaram',33),(5684,'Vanapadi',33),(5685,'Vanavasi',33),(5686,'Vandalur',33),(5687,'Vandavasi',33),(5688,'Vandiyur',33),(5689,'Vanganur',33),(5690,'Vaniputhur',33),(5691,'Vaniyambadi',33),(5692,'Vanniyoor',33),(5693,'Varadarajanpettai',33),(5694,'Vasudevanallur',33),(5695,'Vathirairuppu',33),(5696,'Vavarai',33),(5697,'Vazhapadi',33),(5698,'Vedapatti',33),(5699,'Vedaranyam',33),(5700,'Vedasandur',33),(5701,'Veeraganur',33),(5702,'Veerakeralam',33),(5703,'Veerakkalpudur',33),(5704,'Veerapandi',33),(5705,'Veerapandi',33),(5706,'Veerapandi',33),(5707,'Veerapandianpattinam Town',33),(5708,'Veeravanallur',33),(5709,'Velampalayam',33),(5710,'Velankanni',33),(5711,'Velayudampalayam',33),(5712,'Vellakinar',33),(5713,'Vellakkalpatty',33),(5714,'Vellakoil',33),(5715,'Vellalur (Vellalore)',33),(5716,'Vellamcode',33),(5717,'Vellaravalli',33),(5718,'Vellimalai',33),(5719,'Vellore',33),(5720,'Vellottamparappu',33),(5721,'Velur',33),(5722,'Vembadithalam',33),(5723,'Vengampudur',33),(5724,'Vengathur',33),(5725,'Vengavasal',33),(5726,'Vengikkal',33),(5727,'Venkarai',33),(5728,'Venkatachalapuram',33),(5729,'Venkatapuram',33),(5730,'Vennanthur',33),(5731,'Veppathur',33),(5732,'Verkilambi',33),(5733,'Vettaikaranpudur',33),(5734,'Vettavalam',33),(5735,'Vijayapuri',33),(5736,'Vikramasingapuram',33),(5737,'Vikravandi',33),(5738,'Vilacheri',33),(5739,'Vilangudi',33),(5740,'Vilankurichi',33),(5741,'Vilapakkam',33),(5742,'Vilar',33),(5743,'Vilathikulam',33),(5744,'Vilathurai',33),(5745,'Vilavancode',33),(5746,'Vilavur',33),(5747,'Villukuri',33),(5748,'Viluppuram',33),(5749,'Viraganur',33),(5750,'Viralimalai',33),(5751,'Virinchipuram',33),(5752,'Virudampattu',33),(5753,'Virudhachalam',33),(5754,'Virudhunagar',33),(5755,'Virupakshipuram',33),(5756,'Viswanatham',33),(5757,'V.Pudupatti',33),(5758,'V. Pudur',33),(5759,'Walajabad',33),(5760,'Walajapet',33),(5761,'Wellington',33),(5762,'Yercaud',33),(5763,'Zamin Uthukuli',33),(5764,'Zuzuvadi',33),(5765,'Achampet',36),(5766,'Adilabad',36),(5767,'Allipur',36),(5768,'Ameenapur',36),(5769,'Annaram',36),(5770,'Armur (Armoor)',36),(5771,'Asifabad',36),(5772,'Atmakur',36),(5773,'Bachpalle',36),(5774,'Badangpet',36),(5775,'Badepalle',36),(5776,'Ballepalle',36),(5777,'Bandlaguda (Jagir)',36),(5778,'Banswada',36),(5779,'Bellampalle',36),(5780,'Bhadrachalam',36),(5781,'Bhainsa',36),(5782,'Bhanur',36),(5783,'Bhimaram',36),(5784,'Bhongir',36),(5785,'Bhupalpalle',36),(5786,'Bibinagar',36),(5787,'Bodhan',36),(5788,'Boduppal',36),(5789,'Bollaram (Bolarum)',36),(5790,'Bonthapalle',36),(5791,'Boyapalle',36),(5792,'Chandur',36),(5793,'Chegunta',36),(5794,'Chennur',36),(5795,'Chinnachintakunta',36),(5796,'Chitkul',36),(5797,'Chityala',36),(5798,'Choutuppal',36),(5799,'Chunchupalle',36),(5800,'Dasnapur',36),(5801,'Devapur',36),(5802,'Devarakonda',36),(5803,'Dharmaram (P.B)',36),(5804,'Dornakal',36),(5805,'Dundigal',36),(5806,'Eddumailaram',36),(5807,'Enumamula',36),(5808,'Farooqnagar',36),(5809,'Gadwal',36),(5810,'Gajwel',36),(5811,'Garimellapadu',36),(5812,'Ghanpur',36),(5813,'Ghanpur Station',36),(5814,'Ghatkesar',36),(5815,'Gorrekunta',36),(5816,'Hyderabad',36),(5817,'Ibrahimpatnam (Bagath)',36),(5818,'Ichoda',36),(5819,'Isnapur',36),(5820,'Jadcherla',36),(5821,'Jagtial',36),(5822,'Jainoor',36),(5823,'Jallaram',36),(5824,'Jangaon',36),(5825,'Jawaharnagar',36),(5826,'Jillalguda (Jillelguda)',36),(5827,'Jogipet',36),(5828,'Kadipikonda',36),(5829,'Kagaznagar (Kaghaznagar)',36),(5830,'Kalwakurthy',36),(5831,'Kamalapuram',36),(5832,'Kamareddy',36),(5833,'Karimnagar',36),(5834,'Kasipet',36),(5835,'Khammam',36),(5836,'Khanapuram Haveli',36),(5837,'Kismatpur',36),(5838,'Kodad',36),(5839,'Kompalle',36),(5840,'Kondamallapalle',36),(5841,'Koratla',36),(5842,'Kothagudem',36),(5843,'Kothakota',36),(5844,'Kothapet',36),(5845,'Kothur',36),(5846,'Kyathampalle',36),(5847,'Laxmidevipalle',36),(5848,'Luxettipet',36),(5849,'Madhira',36),(5850,'Mahabubabad',36),(5851,'Mahbubnagar (Mahabubnagar)',36),(5852,'Mamnoor',36),(5853,'Mancherial',36),(5854,'Mandamarri',36),(5855,'Manugur',36),(5856,'Medak',36),(5857,'Medchal',36),(5858,'Medipalle',36),(5859,'Meerpet',36),(5860,'Metpalle',36),(5861,'Miryalaguda',36),(5862,'Muthangi',36),(5863,'Nagaram',36),(5864,'Nagarkurnool',36),(5865,'Nakrekal',36),(5866,'Nalgonda',36),(5867,'Narayankhed',36),(5868,'Narayanpet',36),(5869,'Narsampet',36),(5870,'Narsapur',36),(5871,'Narsingi',36),(5872,'Naspur',36),(5873,'Navandgi',36),(5874,'Nirmal',36),(5875,'Nizamabad',36),(5876,'Omerkhan Daira',36),(5877,'Osmania University',36),(5878,'Palakurthy',36),(5879,'Palwancha',36),(5880,'Peddapalle',36),(5881,'Peerzadguda',36),(5882,'Pothreddipalle',36),(5883,'Raghunathpur',36),(5884,'Ramagundam',36),(5885,'Ramannapeta',36),(5886,'Ratnapur',36),(5887,'Rekurthi',36),(5888,'Sadasivpet',36),(5889,'Sangareddy (Sangareddi)',36),(5890,'Sarapaka',36),(5891,'Sathupalle',36),(5892,'Secunderabad',36),(5893,'Shamshabad',36),(5894,'Shankarampet A',36),(5895,'Shivunipalle',36),(5896,'Siddipet',36),(5897,'Siddipet',36),(5898,'Singapur',36),(5899,'Sircilla',36),(5900,'Soanpet',36),(5901,'Suryapet',36),(5902,'Tandur',36),(5903,'Tangapur',36),(5904,'Teegalpahad',36),(5905,'Thallapalle',36),(5906,'Thimmapur',36),(5907,'Thorrur',36),(5908,'Turkayamjal',36),(5909,'Utnur',36),(5910,'Vatwarlapalle',36),(5911,'Vemulawada R',36),(5912,'Vicarabad (Vikarabad)',36),(5913,'Vijayapuri North',36),(5914,'Wanaparthy',36),(5915,'Warangal',36),(5916,'Yadagirigutta',36),(5917,'Yellandu',36),(5918,'Yellareddy',36),(5919,'Yenugonda',36),(5920,'Zahirabad (Zaheerabad)',36),(5921,'Amarpur',16),(5922,'Ambassa',16),(5923,'Anandanagar',16),(5924,'Bankimnagar',16),(5925,'Belonia',16),(5926,'Bishalgarh',16),(5927,'Briddhanagar',16),(5928,'Chandigarh',16),(5929,'Charipara',16),(5930,'Dewanpasa',16),(5931,'Dharmanagar',16),(5932,'Dhwajnagar',16),(5933,'Dukli',16),(5934,'Fatikroy',16),(5935,'Fulkumari',16),(5936,'Gakulnagar',16),(5937,'Gakulpur',16),(5938,'Gandhigram',16),(5939,'Kailasahar (Kailashahar)',16),(5940,'Kalachhari',16),(5941,'Kamalpur',16),(5942,'Kanchanpur',16),(5943,'Khowai',16),(5944,'Kumarghat',16),(5945,'Lebachhara',16),(5946,'Madhuban',16),(5947,'Madhupur',16),(5948,'Manu',16),(5949,'Matarbari',16),(5950,'Narsingarh',16),(5951,'Panisagar',16),(5952,'Radhakishorenagar',16),(5953,'Ranirbazar',16),(5954,'Sabroom',16),(5955,'Santir Bazar',16),(5956,'Singarbil',16),(5957,'Sonamura',16),(5958,'Taranagar',16),(5959,'Teliamura',16),(5960,'Udaipur',16),(5961,'Uttar Champamura',16),(5962,'Almora',9),(5963,'Almora Cantonment',9),(5964,'Badrinathpuri',9),(5965,'Bageshwar',9),(5966,'Bahadarabad',9),(5967,'Bajpur (Bazpur)',9),(5968,'Banbasa',9),(5969,'Bandiya (Bandia)',9),(5970,'Bangherimahabatpur (Must)',9),(5971,'Barkot',9),(5972,'Bhagwanpur',9),(5973,'Bhimtal',9),(5974,'Bhowali',9),(5975,'Central Hope Town',9),(5976,'Chakrata',9),(5977,'Chamba',9),(5978,'Chamoli Gopeshwar',9),(5979,'Champawat',9),(5980,'Clement Town',9),(5981,'Dehradun',9),(5982,'Dehradun Cantonment',9),(5983,'Devaprayag',9),(5984,'Dhaluwala',9),(5985,'Dhandera',9),(5986,'Dharchula',9),(5987,'Didihat',9),(5988,'Dineshpur',9),(5989,'Dogadda',9),(5990,'Doiwala',9),(5991,'Dwarahat',9),(5992,'Gadarpur',9),(5993,'Gangotri',9),(5994,'Gochar (Gauchar)',9),(5995,'Gumaniwala',9),(5996,'Haldwani-cum-Kathgodam',9),(5997,'Haldwani Talli',9),(5998,'Hardwar (Haridwar)',9),(5999,'Haripur Kalan',9),(6000,'Herbertpur',9),(6001,'Jagjeetpur',9),(6002,'Jaspur',9),(6003,'Jhabrera',9),(6004,'Jiwangarh',9),(6005,'Jonk',9),(6006,'Joshimath (Jyotirmath)',9),(6007,'Kaladhungi',9),(6008,'Kanchal Gosain',9),(6009,'Karnaprayag',9),(6010,'Kashipur',9),(6011,'Kashirampur',9),(6012,'Kedarnath',9),(6013,'Kela Khera',9),(6014,'Khanjarpur',9),(6015,'Kharak mafi',9),(6016,'Khatima',9),(6017,'Khatyari',9),(6018,'Kichha',9),(6019,'Kirtinagar',9),(6020,'Kotdwara (Kotdwar)',9),(6021,'Laksar',9),(6022,'Lalkuan',9),(6023,'Landaur (Landour)',9),(6024,'Landhaura',9),(6025,'Lansdowne',9),(6026,'Lohaghat',9),(6027,'Maholiya',9),(6028,'Mahua Dabra Haripura',9),(6029,'Mahua Kheraganj',9),(6030,'Manglaur',9),(6031,'Maohanpur Mohammadpur',9),(6032,'Mehu Wala Mafi',9),(6033,'Muni Ki Reti',9),(6034,'Mussoorie',9),(6035,'Nagala Imarti',9),(6036,'Nagla',9),(6037,'Nainital',9),(6038,'Nainital Cantonment',9),(6039,'Nandprayag (Nandaprayag)',9),(6040,'Narendranagar',9),(6041,'Natthan Pur',9),(6042,'Natthuwa Wala',9),(6043,'Padali Gujar',9),(6044,'Padampur Sukhran',9),(6045,'Pauri',9),(6046,'Piran Kaliyar',9),(6047,'Pithoragarh',9),(6048,'Pratitnagar',9),(6049,'Raipur',9),(6050,'Ramnagar',9),(6051,'Ranikhet',9),(6052,'Rawali Mahdood',9),(6053,'Rishikesh',9),(6054,'Rishikesh',9),(6055,'Roorkee',9),(6056,'Roorkee Cantonment',9),(6057,'Rudraprayag',9),(6058,'Rudrapur',9),(6059,'Saidpura',9),(6060,'Salempur Rajputan',9),(6061,'Shafipur',9),(6062,'Shahpur',9),(6063,'Shaktigarh',9),(6064,'Sitarganj',9),(6065,'Srinagar',9),(6066,'Sultanpur',9),(6067,'Sunhaira',9),(6068,'Tanakpur',9),(6069,'Tehri',9),(6070,'Umru Khurd',9),(6071,'Uttarkashi',9),(6072,'Vikasnagar',9),(6073,'Virbhadra',9),(6074,'Abupur',9),(6075,'Achalganj',9),(6076,'Achhalda',9),(6077,'Achhnera',9),(6078,'Adari',9),(6079,'Afzalgarh',9),(6080,'Agarwal Mandi',9),(6081,'Agra',9),(6082,'Agra Cantonment',9),(6083,'Ahrauli Shekh',9),(6084,'Ahraura',9),(6085,'Ailam',9),(6086,'Air Force Area',9),(6087,'Ajhuwa',9),(6088,'Ajitpur',9),(6089,'Akbarpur',9),(6090,'Akbarpur',9),(6091,'Alhaipur',9),(6092,'Aliganj',9),(6093,'Aligarh',9),(6094,'Allahabad',9),(6095,'Allahabad Cantonment',9),(6096,'Allahganj',9),(6097,'Allapur',9),(6098,'Almaspur',9),(6099,'Amanpur',9),(6100,'Amara Khaira Chak',9),(6101,'Ambehta',9),(6102,'Amehra Adipur',9),(6103,'Amethi',9),(6104,'Amethi',9),(6105,'Amethi Jadid',9),(6106,'Amila',9),(6107,'Amilo',9),(6108,'Aminagar Sarai',9),(6109,'Aminagar urf Bhurbaral',9),(6110,'Amraudha',9),(6111,'Amroha',9),(6112,'Anandnagar',9),(6113,'Anpara',9),(6114,'Antu',9),(6115,'Anupshahr',9),(6116,'Anurudhpur Purab Patti',9),(6117,'Aonla',9),(6118,'Arail Uparhar',9),(6119,'Armapur Estate',9),(6120,'Artauni',9),(6121,'Asapur',9),(6122,'Ashrafpur Jalal',9),(6123,'Ashrafpur Kichhauchha',9),(6124,'Atarra',9),(6125,'Atasu',9),(6126,'Atrari',9),(6127,'Atrauli',9),(6128,'Atrauliya (Atraulia)',9),(6129,'Auraiya',9),(6130,'Aurangabad',9),(6131,'Aurangabad Bangar',9),(6132,'Aurangabad Gadana',9),(6133,'Auras',9),(6134,'Awagarh',9),(6135,'Ayodhya',9),(6136,'Azamgarh',9),(6137,'Azizpur',9),(6138,'Azmatgarh',9),(6139,'Babarpur Ajitmal',9),(6140,'Baberu',9),(6141,'Babina',9),(6142,'Babrala',9),(6143,'Babugarh',9),(6144,'Bachhraon',9),(6145,'Bachhrawan',9),(6146,'Bad',9),(6147,'Bagh Nagar Urf Bakhira',9),(6148,'Baghpat',9),(6149,'Bah',9),(6150,'Bahadurganj',9),(6151,'Bahadurpur',9),(6152,'Bahalimpura',9),(6153,'Baheri',9),(6154,'Bahjoi',9),(6155,'Bahraich',9),(6156,'Bahsuma',9),(6157,'Bahuwa',9),(6158,'Bajna',9),(6159,'Bakalpur Mathura',9),(6160,'Bakewar',9),(6161,'Bakshi Ka Talab',9),(6162,'Baldeo',9),(6163,'Ballia',9),(6164,'Balrampur',9),(6165,'Banat',9),(6166,'Banda',9),(6167,'Bangarmau',9),(6168,'Banguwan Kalan',9),(6169,'Banjarepur',9),(6170,'Banki',9),(6171,'Bansdih',9),(6172,'Bansgaon',9),(6173,'Bansi',9),(6174,'Banthla',9),(6175,'Baragaon',9),(6176,'Baragaon',9),(6177,'Barahatir Jagdishpur',9),(6178,'Baraut',9),(6179,'Bareilly',9),(6180,'Bareilly Cantonment',9),(6181,'Barel',9),(6182,'Bargo',9),(6183,'Barha',9),(6184,'Barhalganj',9),(6185,'Barhani Bazar',9),(6186,'Barkhera',9),(6187,'Baroun',9),(6188,'Barsana',9),(6189,'Barua Sagar',9),(6190,'Barwar',9),(6191,'Barwara Mazra',9),(6192,'Basantpur Saitli',9),(6193,'Basta',9),(6194,'Basti',9),(6195,'Baswar',9),(6196,'Beelna',9),(6197,'Begumabad Budhana',9),(6198,'Behat',9),(6199,'Bela Pratapgarh',9),(6200,'Belthara Road',9),(6201,'Beniganj',9),(6202,'Benipur',9),(6203,'Beswan',9),(6204,'Bewar',9),(6205,'Bhabnan Bazar',9),(6206,'Bhadarsa',9),(6207,'Bhadohi',9),(6208,'Bhagawanpur',9),(6209,'Bhagipur',9),(6210,'Bhagwant Nagar',9),(6211,'Bharatganj',9),(6212,'Bhargain',9),(6213,'Bharthana',9),(6214,'Bharuhana',9),(6215,'Bharwari',9),(6216,'Bhatni Bazar',9),(6217,'Bhatpar Rani',9),(6218,'Bhawan Bahadur Nagar',9),(6219,'Bhinga',9),(6220,'Bhogaon',9),(6221,'Bhojpur Dharampur',9),(6222,'Bhokarhedi',9),(6223,'Bhulepur',9),(6224,'Bidhuna',9),(6225,'Bighapur',9),(6226,'Bihka Urf Pura Mufti',9),(6227,'Bijnor',9),(6228,'Bijpur',9),(6229,'Bikapur',9),(6230,'Bilari',9),(6231,'Bilariaganj',9),(6232,'Bilaspur',9),(6233,'Bilaspur',9),(6234,'Bilgram',9),(6235,'Bilhaur',9),(6236,'Bilram',9),(6237,'Bilsanda',9),(6238,'Bilsi',9),(6239,'Bindki',9),(6240,'Birbhanpur',9),(6241,'Birjapur',9),(6242,'Bisalpur',9),(6243,'Bisanda Buzurg',9),(6244,'Bisauli',9),(6245,'Bisharatganj',9),(6246,'Bishunipur',9),(6247,'Bisokhar',9),(6248,'Biswan',9),(6249,'Bithoor',9),(6250,'Budaun',9),(6251,'Budhana',9),(6252,'Bugrasi',9),(6253,'Bulandshahr',9),(6254,'Buxer',9),(6255,'Chail',9),(6256,'Chak Babura Alimabad',9),(6257,'Chakeri',9),(6258,'Chakia',9),(6259,'Chak Imam Ali',9),(6260,'Chakmano Urf Dargah',9),(6261,'Chak Sikari',9),(6262,'Chandauli',9),(6263,'Chandausi',9),(6264,'Chandpur',9),(6265,'Chandpur',9),(6266,'Charkhari',9),(6267,'Charthawal (Charthaval)',9),(6268,'Chaumuhan',9),(6269,'Chaurhat',9),(6270,'Chhapraula',9),(6271,'Chhaprauli',9),(6272,'Chharra Rafatpur',9),(6273,'Chhata',9),(6274,'Chhatari',9),(6275,'Chhibramau',9),(6276,'Chhitauni',9),(6277,'Chhitpur',9),(6278,'Chhutmalpur',9),(6279,'Chilkana Sultanpur',9),(6280,'Chipyana Buzurg',9),(6281,'Chirgaon',9),(6282,'Chitbara Gaon',9),(6283,'Chitrakoot Dham (Karwi)',9),(6284,'Chopan',9),(6285,'Choubepur Kalan',9),(6286,'Chunar',9),(6287,'Churk Ghurma',9),(6288,'Colonelganj',9),(6289,'Dadri',9),(6290,'Dahilamau',9),(6291,'Dalmau',9),(6292,'Dankaur',9),(6293,'Dariyabad',9),(6294,'Dasna',9),(6295,'Dataganj',9),(6296,'Daurala',9),(6297,'Dayalbagh',9),(6298,'Dehtora',9),(6299,'Deoband',9),(6300,'Deoranian',9),(6301,'Deoretha',9),(6302,'Deoria',9),(6303,'Deori Singhpura',9),(6304,'Deosaini',9),(6305,'Derapur',9),(6306,'Devinagar',9),(6307,'Dewa',9),(6308,'Dhakauli',9),(6309,'Dhampur',9),(6310,'Dhampur Husainpur',9),(6311,'Dhanauha',9),(6312,'Dhanauli',9),(6313,'Dhanaura',9),(6314,'Dhanipur',9),(6315,'Dhaura Tanda',9),(6316,'Dhaurehra',9),(6317,'Dhaurra Mafi',9),(6318,'Dibai',9),(6319,'Dibiyapur',9),(6320,'Dildarnagar Fatehpur Bazar',9),(6321,'Dindaspur',9),(6322,'Doghat',9),(6323,'Dohrighat',9),(6324,'Domariyaganj (Domariaganj)',9),(6325,'Dostpur',9),(6326,'Dudhi',9),(6327,'Dulhipur',9),(6328,'Ekdil',9),(6329,'Erich',9),(6330,'Etah',9),(6331,'Etawah',9),(6332,'Etmadpur',9),(6333,'Faizabad',9),(6334,'Faizabad Cantonment',9),(6335,'Faizganj',9),(6336,'Farah',9),(6337,'Faridnagar',9),(6338,'Faridpur',9),(6339,'Faridpur',9),(6340,'Fariha',9),(6341,'Farrukhabad-cum-Fatehgarh',9),(6342,'Fatehabad',9),(6343,'Fatehganj Pashchimi',9),(6344,'Fatehganj Purvi',9),(6345,'Fatehgarh',9),(6346,'Fatehpur',9),(6347,'Fatehpur',9),(6348,'Fatehpur Chaurasi',9),(6349,'Fatehpur Sikri',9),(6350,'Fazi Nagar',9),(6351,'Firozabad',9),(6352,'Gabhana',9),(6353,'Gaddoo Pur',9),(6354,'Gadhi',9),(6355,'Gagalhedi Must.',9),(6356,'Gajraula',9),(6357,'Gangaghat',9),(6358,'Gangapur',9),(6359,'Gangiri',9),(6360,'Gangoh',9),(6361,'Ganj Dundawara',9),(6362,'Ganj Muradabad',9),(6363,'Ganwaria Tulsipur (Dehat)',9),(6364,'Garauri',9),(6365,'Garautha',9),(6366,'Garhi Pukhta',9),(6367,'Garhi Tamana',9),(6368,'Gaura',9),(6369,'Gaura Barhaj',9),(6370,'Gaura Kala',9),(6371,'Gauri Bazar',9),(6372,'Gausganj',9),(6373,'Gawan',9),(6374,'Ghatampur',9),(6375,'Ghaziabad',9),(6376,'Ghazipur',9),(6377,'Ghiraur',9),(6378,'Ghorawal',9),(6379,'Ghosi',9),(6380,'Ghosia Bazar',9),(6381,'Ghughuli (Ghughali)',9),(6382,'Gird Baragaon',9),(6383,'Gird Gonda',9),(6384,'Gohand',9),(6385,'Gokul',9),(6386,'Gola Bazar',9),(6387,'Gola Gokaran Nath',9),(6388,'Gonda',9),(6389,'Gopamau',9),(6390,'Gopiganj',9),(6391,'Gorakhpur',9),(6392,'Gosainganj',9),(6393,'Gosainganj (Goshainganj)',9),(6394,'Got',9),(6395,'Govardhan',9),(6396,'Greater Noida',9),(6397,'Gulaothi',9),(6398,'Gulariya',9),(6399,'Gunnaur',9),(6400,'Gursahaiganj',9),(6401,'Gursarai',9),(6402,'Gyanpur',9),(6403,'Hafiz Ganj',9),(6404,'Hafizpur',9),(6405,'Haidergarh',9),(6406,'Haldaur',9),(6407,'Hallaur',9),(6408,'Hamirpur',9),(6409,'Handia',9),(6410,'Hapur',9),(6411,'Haqiqatpur Urf Khudawas',9),(6412,'Hardoi',9),(6413,'Harduaganj',9),(6414,'Hargaon',9),(6415,'Hariharpur',9),(6416,'Hariyawan',9),(6417,'Harpalpur',9),(6418,'Harraiya',9),(6419,'Harsewakpur No.2',9),(6420,'Hasangarh',9),(6421,'Hasanpur',9),(6422,'Hasayan',9),(6423,'Hastinapur',9),(6424,'Hata',9),(6425,'Hathgram',9),(6426,'Hathras',9),(6427,'Hathras Dehat',9),(6428,'Hyderabad',9),(6429,'Ibrahimpur',9),(6430,'Iffco Census Village',9),(6431,'Iglas',9),(6432,'Ikauna',9),(6433,'Iltifatganj Bazar',9),(6434,'Isapur Banger',9),(6435,'Islamnagar',9),(6436,'Itaunja',9),(6437,'Itwa',9),(6438,'Jafarabad',9),(6439,'Jagner',9),(6440,'Jahanabad',9),(6441,'Jahangirabad',9),(6442,'Jahangirpur',9),(6443,'Jais',9),(6444,'Jaithara',9),(6445,'Jakhaon',9),(6446,'Jalalabad',9),(6447,'Jalalabad',9),(6448,'Jalalabad',9),(6449,'Jalali',9),(6450,'Jalal Patti',9),(6451,'Jalalpur',9),(6452,'Jalalpur Dehat',9),(6453,'Jalaun',9),(6454,'Jalesar',9),(6455,'Jamshila',9),(6456,'Jamuhan',9),(6457,'Jangipur',9),(6458,'Jangl Hakeem No 2',9),(6459,'Janki Nagar',9),(6460,'Jansath',9),(6461,'Jarwal',9),(6462,'Jasra',9),(6463,'Jasrana',9),(6464,'Jaswantnagar',9),(6465,'Jatari (Jattari)',9),(6466,'Jaunpur',9),(6467,'Jewar',9),(6468,'Jhalu',9),(6469,'Jhansi',9),(6470,'Jhansi Cantonment',9),(6471,'Jhansi Railway Settlement',9),(6472,'Jhinjhak',9),(6473,'Jhinjhana',9),(6474,'Jhusi',9),(6475,'Jhusi Kohna',9),(6476,'Jiyanpur',9),(6477,'Joya',9),(6478,'Jugauli',9),(6479,'Jyoti Khuriya (Jyoti Khuria)',9),(6480,'Kabrai',9),(6481,'Kachhauna Patseni',9),(6482,'Kachhla',9),(6483,'Kachhwa',9),(6484,'Kachnar',9),(6485,'Kadaura',9),(6486,'Kadipur',9),(6487,'Kailashpur',9),(6488,'Kaimganj',9),(6489,'Kairana',9),(6490,'Kakari',9),(6491,'Kakarmatta',9),(6492,'Kakgaina',9),(6493,'Kakod',9),(6494,'Kakori',9),(6495,'Kakrala',9),(6496,'Kalinagar',9),(6497,'Kalli Pashchim',9),(6498,'Kallipur',9),(6499,'Kalpi',9),(6500,'Kalwari',9),(6501,'Kamalganj',9),(6502,'Kampil',9),(6503,'Kandharpur',9),(6504,'Kandhla',9),(6505,'Kandwa',9),(6506,'Kannauj',9),(6507,'Kanpur',9),(6508,'Kanpur Cantonment',9),(6509,'Kanth',9),(6510,'Kanth (Kant)',9),(6511,'Kaptanganj',9),(6512,'Karanpur',9),(6513,'Karari',9),(6514,'Kareli',9),(6515,'Karhal',9),(6516,'Karnawal',9),(6517,'Karwi Mafi',9),(6518,'Kasba Khanpur',9),(6519,'Kasba Sultanpur',9),(6520,'Kasganj',9),(6521,'Kasiya',9),(6522,'Kataka',9),(6523,'Katghar Lalganj',9),(6524,'Kathaura',9),(6525,'Kathera',9),(6526,'Katra',9),(6527,'Katra',9),(6528,'Katra Medniganj',9),(6529,'Katri Piper Khera',9),(6530,'Kaulakha',9),(6531,'Kauriaganj',9),(6532,'Kemri',9),(6533,'Kerakat',9),(6534,'Kesaripur',9),(6535,'Kewalpur',9),(6536,'Khadda',9),(6537,'Khaga',9),(6538,'Khailar',9),(6539,'Khair',9),(6540,'Khairabad',9),(6541,'Khairabad',9),(6542,'Khalilabad',9),(6543,'Khamaria',9),(6544,'Khandauli',9),(6545,'Khanpur',9),(6546,'Khanupur',9),(6547,'Kharela',9),(6548,'Khargupur',9),(6549,'Khariya',9),(6550,'Kharkhoda',9),(6551,'Khatauli',9),(6552,'Khatauli Rural',9),(6553,'Khekada',9),(6554,'Kheragarh',9),(6555,'Kheri',9),(6556,'Kherli Hafizpur',9),(6557,'Khetasarai',9),(6558,'Khojn Pur',9),(6559,'Khora',9),(6560,'Khudaganj',9),(6561,'Khurja',9),(6562,'Khurja Rural',9),(6563,'Khutar',9),(6564,'Kiraoali (Kiraoli)',9),(6565,'Kiratpur',9),(6566,'Kishni',9),(6567,'Kishunpur',9),(6568,'Kithaur',9),(6569,'Koeripur',9),(6570,'Konch',9),(6571,'Kopaganj',9),(6572,'Kora Jahanabad',9),(6573,'Koraon',9),(6574,'Korwa',9),(6575,'Kosi Kalan',9),(6576,'Kota',9),(6577,'Kotra',9),(6578,'Kotwa',9),(6579,'Kotwa (Kotwa II)',9),(6580,'Kotwali',9),(6581,'Kukra',9),(6582,'Kul Pahar',9),(6583,'Kunda',9),(6584,'Kundarki',9),(6585,'Kunwargaon',9),(6586,'Kuraoali (Kuraoli)',9),(6587,'Kurara',9),(6588,'Kursath',9),(6589,'Kursath',9),(6590,'Kurthi Jafarpur',9),(6591,'Kushinagar',9),(6592,'Kusmara',9),(6593,'Kwarasi',9),(6594,'Lachhiman Patti',9),(6595,'Laharpur',9),(6596,'Lahartara',9),(6597,'Lahsari',9),(6598,'Lakhimpur',9),(6599,'Lakhna',9),(6600,'Lalganj',9),(6601,'Lal Gopalganj Nindaura',9),(6602,'Lalhapur',9),(6603,'Lalitpur',9),(6604,'Lar',9),(6605,'Lawar',9),(6606,'Ledwa Mahua',9),(6607,'Lerhupur',9),(6608,'Lohta',9),(6609,'Loni',9),(6610,'Lucknow',9),(6611,'Lucknow Cantonment',9),(6612,'Machhlishahr (Machhali Shahar)',9),(6613,'Madhoganj',9),(6614,'Madhogarh',9),(6615,'Madiya',9),(6616,'Maghar',9),(6617,'Mahaban',9),(6618,'Maharajganj (Mahrajganj)',9),(6619,'Maharajganj (Mahrajganj)',9),(6620,'Maheshpur',9),(6621,'Mahewa Patti Pashchim Uparhar',9),(6622,'Mahimapur',9),(6623,'Mahmudabad',9),(6624,'Mahmudpur Taluka Madpur Sult',9),(6625,'Mahoba',9),(6626,'Maholi',9),(6627,'Mahona',9),(6628,'Mahrajganj',9),(6629,'Mahroni',9),(6630,'Mahroni Rural',9),(6631,'Mahul Khas (Mahul)',9),(6632,'Maigal Ganj',9),(6633,'Mailani',9),(6634,'Maina Maujpur',9),(6635,'Mainpuri',9),(6636,'Majhara Pipar Ahatmali',9),(6637,'Majhauliraj',9),(6638,'Makhanpur',9),(6639,'Malhipur',9),(6640,'Malihabad',9),(6641,'Mallawan',9),(6642,'Mandawar',9),(6643,'Manikpur',9),(6644,'Manikpur Sarhat',9),(6645,'Maniyar',9),(6646,'Manjhanpur',9),(6647,'Manjoor Garhi',9),(6648,'Mankapur',9),(6649,'Marehra',9),(6650,'Mariahu',9),(6651,'Maruadih',9),(6652,'Maruadih Railway Settlement',9),(6653,'Maswasi',9),(6654,'Mataundh',9),(6655,'Mathura',9),(6656,'Mathura Cantonment',9),(6657,'Mau Aima',9),(6658,'Maudaha',9),(6659,'Maunath Bhanjan (Mau)',9),(6660,'Mauranipur',9),(6661,'Maurawan',9),(6662,'Mawana',9),(6663,'Meerut',9),(6664,'Meerut Cantonment',9),(6665,'Mehdawal',9),(6666,'Mehnagar',9),(6667,'Mendu',9),(6668,'Middha',9),(6669,'Milak',9),(6670,'Miranpur',9),(6671,'Mirganj',9),(6672,'Mirzapur-cum-Vindhyachal',9),(6673,'Modinagar',9),(6674,'Mohammadabad',9),(6675,'Mohammadabad',9),(6676,'Mohammadi',9),(6677,'Mohan',9),(6678,'Mohanpur',9),(6679,'Mohenpur',9),(6680,'Mohiuddinpur',9),(6681,'Moradabad',9),(6682,'Moth',9),(6683,'Mubarakpur',9),(6684,'Mughalsarai',9),(6685,'Mughalsarai Railway Settlement',9),(6686,'Muhammadabad',9),(6687,'Mukrampur Khema',9),(6688,'Mundera Bazar',9),(6689,'Mundiya',9),(6690,'Muradgram Pur Pursi',9),(6691,'Muradnagar',9),(6692,'Mursan',9),(6693,'Musafirkhana',9),(6694,'Muzaffarnagar',9),(6695,'Nadigaon',9),(6696,'Nagina',9),(6697,'Nagram',9),(6698,'Nai Bazar',9),(6699,'Nainana-Brahman',9),(6700,'Nainana Jat',9),(6701,'Naiparapur',9),(6702,'Najibabad',9),(6703,'Nakur',9),(6704,'Nanauta',9),(6705,'Nandgaon',9),(6706,'Nanpara',9),(6707,'Naraini',9),(6708,'Narauli',9),(6709,'Naraura (Narora)',9),(6710,'Naugawan Sadat',9),(6711,'Nautanwa',9),(6712,'Nawabganj',9),(6713,'Nawabganj',9),(6714,'Nawabganj',9),(6715,'Nawabganj',9),(6716,'Nehtaur',9),(6717,'Nichlaul',9),(6718,'Nidhauli Kalan',9),(6719,'Nihal Garh Chak Jangla',9),(6720,'Nivi',9),(6721,'Niwari',9),(6722,'Nizamabad',9),(6723,'Noida',9),(6724,'Noorpur',9),(6725,'Northern Railway Colony',9),(6726,'Nyoria Husainpur',9),(6727,'Nyotini',9),(6728,'Obaree',9),(6729,'Obra',9),(6730,'Oel Dhakwa',9),(6731,'Orai',9),(6732,'Oran',9),(6733,'Ordinance Factory Muradnagar',9),(6734,'Pachperwa',9),(6735,'Padarathpur',9),(6736,'Padrauna',9),(6737,'Pahar Ganj',9),(6738,'Pahasu',9),(6739,'Paintepur',9),(6740,'Pakbara',9),(6741,'Pakriya Naugwan Mustqil',9),(6742,'Palhni',9),(6743,'Pali',9),(6744,'Pali',9),(6745,'Pali Khera',9),(6746,'Paliya Kalan (Palia Kalan)',9),(6747,'Palpur',9),(6748,'Para',9),(6749,'Parasi',9),(6750,'Parichha',9),(6751,'Parikshitgarh',9),(6752,'Parmanandpur',9),(6753,'Parsadepur',9),(6754,'Parsona',9),(6755,'Patadi',9),(6756,'Patala',9),(6757,'Patholi',9),(6758,'Patiyali',9),(6759,'Patti',9),(6760,'Pavi Sadakpur',9),(6761,'Phalauda',9),(6762,'Phaphund',9),(6763,'Phulpur',9),(6764,'Phulpur',9),(6765,'Phulwaria',9),(6766,'Pihani',9),(6767,'Pilibhit',9),(6768,'Pilkhana',9),(6769,'Pilkhuwa',9),(6770,'Pinahat',9),(6771,'Pipalsana Chaudhari',9),(6772,'Pipara Dand',9),(6773,'Pipiganj',9),(6774,'Pipraich',9),(6775,'Piprayli Bujurg',9),(6776,'Pipri',9),(6777,'Powayan (Pawayan)',9),(6778,'Pratapgarh City',9),(6779,'Premchak Urf Baheri',9),(6780,'Pukhrayan',9),(6781,'Puranpur',9),(6782,'Pura Pandey',9),(6783,'Purdilnagar',9),(6784,'Pure Tiwari',9),(6785,'Purquazi',9),(6786,'Purwa',9),(6787,'Qasimpur Power House Colony',9),(6788,'Rabupura',9),(6789,'Radhakund',9),(6790,'Rae Bareli',9),(6791,'Railway Settlement Roza',9),(6792,'Raja ka Rampur',9),(6793,'Rajapur',9),(6794,'Rajpur Bangar',9),(6795,'Ramdaspur Urf Nagal',9),(6796,'Ramgarh Panjoopur',9),(6797,'Ramkola',9),(6798,'Ramnagar',9),(6799,'Ramnagar',9),(6800,'Rampur',9),(6801,'Rampur',9),(6802,'Rampura',9),(6803,'Rampur Karkhana',9),(6804,'Rampur Maniharan',9),(6805,'Ranchi Bangar',9),(6806,'Ranipur',9),(6807,'Raniyan',9),(6808,'Rashidpur Garhi',9),(6809,'Rasra',9),(6810,'Rasulabad',9),(6811,'Rasulabad',9),(6812,'Ratanpura',9),(6813,'Rath',9),(6814,'Raya',9),(6815,'Renukoot',9),(6816,'Reoti',9),(6817,'Richha',9),(6818,'Risiya Bazar (Risia Bazar)',9),(6819,'Rithora',9),(6820,'Rohta',9),(6821,'Rori',9),(6822,'Rudauli',9),(6823,'Rudayan',9),(6824,'Rudrapur',9),(6825,'Runkata',9),(6826,'Rura',9),(6827,'Rustamnagar Sahaspur',9),(6828,'Sadabad',9),(6829,'Sadat',9),(6830,'Sadatmasaura',9),(6831,'Sadruddin Nagar',9),(6832,'Safipur',9),(6833,'Sahanpur',9),(6834,'Saharanpur',9),(6835,'Sahaspur',9),(6836,'Sahaswan',9),(6837,'Sahatwar',9),(6838,'Sahawar',9),(6839,'Sahjanwan',9),(6840,'Sahpau',9),(6841,'Saidhari',9),(6842,'Saidpur',9),(6843,'Saidpur',9),(6844,'Saidpur Khajuria',9),(6845,'Saijni Nankar',9),(6846,'Sainthal',9),(6847,'Saiyad Raza (Saiyad Raja)',9),(6848,'Sakaldiha',9),(6849,'Sakhanu',9),(6850,'Sakit',9),(6851,'Salarpur',9),(6852,'Salarpur Khadar',9),(6853,'Salempur',9),(6854,'Salon',9),(6855,'Sambhal',9),(6856,'Samdhan',9),(6857,'Samthar',9),(6858,'Sandi',9),(6859,'Sandila',9),(6860,'Sarai Abdulmalik',9),(6861,'Sarai Aquil',9),(6862,'Sarai Lahur Urf Lahurpur',9),(6863,'Sarai Mir',9),(6864,'Sarai Mohana',9),(6865,'Sardhana',9),(6866,'Sarila',9),(6867,'Sarsaul',9),(6868,'Sarsawa',9),(6869,'Sarsawan',9),(6870,'Sarwat',9),(6871,'Sasni',9),(6872,'Satiyava',9),(6873,'Satpokhari',9),(6874,'Satrikh',9),(6875,'Saunkh',9),(6876,'Saurikh',9),(6877,'Seohara',9),(6878,'Sewalkhas',9),(6879,'Sewarhi',9),(6880,'Shahabad',9),(6881,'Shahabad',9),(6882,'Shaha Urf Pipalgaon',9),(6883,'Shahbudinpur',9),(6884,'Shahganj',9),(6885,'Shahi',9),(6886,'Shahjahanpur',9),(6887,'Shahjahanpur Cantonment',9),(6888,'Shahpur',9),(6889,'Shamli',9),(6890,'Shamsabad',9),(6891,'Shamsabad',9),(6892,'Shankargarh',9),(6893,'Shekhpura',9),(6894,'Shergarh',9),(6895,'Sherkot',9),(6896,'Shikarpur',9),(6897,'Shikohabad',9),(6898,'Shishgarh',9),(6899,'Shivdaspur',9),(6900,'Shivli',9),(6901,'Shivrajpur',9),(6902,'Shohratgarh',9),(6903,'Siana',9),(6904,'Siddhaur',9),(6905,'Sidhauli',9),(6906,'Sidhpura',9),(6907,'Sikanderpur',9),(6908,'Sikanderpur',9),(6909,'Sikandra',9),(6910,'Sikandrabad',9),(6911,'Sikandrarao',9),(6912,'Sikri Kalan',9),(6913,'Sindhawali',9),(6914,'Singahi Bhiraura',9),(6915,'Sirathu',9),(6916,'Sirauli',9),(6917,'Sir Gobardhan',9),(6918,'Sirsa',9),(6919,'Sirsaganj',9),(6920,'Sirsi',9),(6921,'Sisauli',9),(6922,'Siswa Bazar',9),(6923,'Sitapur',9),(6924,'Sonbhadra (Robertsganj)',9),(6925,'Soraon',9),(6926,'Soron',9),(6927,'Suar',9),(6928,'Subeha',9),(6929,'Sujavalpur',9),(6930,'Sultanpur',9),(6931,'Sumerpur',9),(6932,'Suriyawan',9),(6933,'Susuwahi',9),(6934,'Suthana Barsola',9),(6935,'Suzabad',9),(6936,'Swamibagh',9),(6937,'Talbehat',9),(6938,'Talgram',9),(6939,'Tambaur-cum-Ahamdabad',9),(6940,'Tanda',9),(6941,'Tanda',9),(6942,'Tatarpur Lallu',9),(6943,'Thakurdwara',9),(6944,'Thana Bhawan',9),(6945,'Thiriya Nizamat Khan',9),(6946,'Tikait Nagar',9),(6947,'Tikri',9),(6948,'Tilhar',9),(6949,'Tilthi',9),(6950,'Tindwari',9),(6951,'Tirwaganj',9),(6952,'Titron',9),(6953,'Tondi Fatehpur',9),(6954,'Tulsipur',9),(6955,'Tundla',9),(6956,'Tundla Kham',9),(6957,'Tundla Railway Colony',9),(6958,'Ugu',9),(6959,'Ujhani',9),(6960,'Ujhari',9),(6961,'Umarha',9),(6962,'Umri',9),(6963,'Umri Kalan',9),(6964,'Un',9),(6965,'Unchahar',9),(6966,'Unnao',9),(6967,'Usawan',9),(6968,'Usehat',9),(6969,'Uska Bazar',9),(6970,'Utraula',9),(6971,'Varanasi [Benares]',9),(6972,'Varanasi Cantonment',9),(6973,'Vijaigarh',9),(6974,'Villimar Kundi',9),(6975,'Vrindavan',9),(6976,'Walidpur',9),(6977,'Warhapur',9),(6978,'Wazirganj',9),(6979,'Zaidpur',9),(6980,'Zamania',9),(6981,'Abhirampur',19),(6982,'Adra',19),(6983,'Ahmadpur',19),(6984,'Aiho',19),(6985,'Aistala',19),(6986,'Ajodhya Nagar',19),(6987,'Ajodhyanagar',19),(6988,'Alikhoja',19),(6989,'Alipukur',19),(6990,'Alipur',19),(6991,'Alipur',19),(6992,'Alipur (Alipore)',19),(6993,'Alipurduar',19),(6994,'Alipurduar Railway Junction',19),(6995,'Amalhara',19),(6996,'Amarshi Kasba',19),(6997,'Ambhua',19),(6998,'Amkula',19),(6999,'Amlagora',19),(7000,'Amlajora',19),(7001,'Amodghata',19),(7002,'Amta',19),(7003,'Amtala',19),(7004,'Anantabati',19),(7005,'Anantapur',19),(7006,'Anarbaria',19),(7007,'Andal (Gram)',19),(7008,'Andul',19),(7009,'Ankurhati',19),(7010,'Anulia',19),(7011,'Anup Nagar',19),(7012,'Arambag',19),(7013,'Argari',19),(7014,'Arjunpur',19),(7015,'Arra',19),(7016,'Arra',19),(7017,'Asansol',19),(7018,'Ashadtalya',19),(7019,'Asuti',19),(7020,'Aurangabad',19),(7021,'Babanpur',19),(7022,'Bablari Dewanganj',19),(7023,'Badamtam Tea Garden',19),(7024,'Badhagachhi',19),(7025,'Badkulla',19),(7026,'Baduria',19),(7027,'Bagbari',19),(7028,'Bagnan',19),(7029,'Bagula',19),(7030,'Baharu',19),(7031,'Bahir Sarbamangala',19),(7032,'Bahula',19),(7033,'Baidyabati',19),(7034,'Baidyanathpur',19),(7035,'Bairatisal',19),(7036,'Baisguri',19),(7037,'Baksa',19),(7038,'Baksinagar',19),(7039,'Baktarnagar',19),(7040,'Balarambati',19),(7041,'Balarampota',19),(7042,'Balarampur',19),(7043,'Balarampur',19),(7044,'Baliadanga',19),(7045,'Balibhara',19),(7046,'Balichak',19),(7047,'Balihati',19),(7048,'Ballavpur',19),(7049,'Bally',19),(7050,'Bally',19),(7051,'Baluhati',19),(7052,'Balurghat',19),(7053,'Bamangachhi',19),(7054,'Bamangram',19),(7055,'Bamanpukur',19),(7056,'Bamna',19),(7057,'Bamunara',19),(7058,'Bamunari',19),(7059,'Banagram',19),(7060,'Banarhat Tea Garden',19),(7061,'Bandhail',19),(7062,'Bandipur',19),(7063,'Bandoan',19),(7064,'Baneshwarpur',19),(7065,'Baneswar',19),(7066,'Bangalpur',19),(7067,'Bangsidharpur M P',19),(7068,'Ban Harishpur',19),(7069,'Baniara',19),(7070,'Baniban',19),(7071,'Baniban Jagadishpur',19),(7072,'Banjetia',19),(7073,'Bankra',19),(7074,'Bankra',19),(7075,'Bankul',19),(7076,'Bankura',19),(7077,'Bansberia',19),(7078,'Banshra',19),(7079,'Banshra',19),(7080,'Banupur',19),(7081,'Bara',19),(7082,'Bara Bamonia',19),(7083,'Barabazar',19),(7084,'Bara Jumla',19),(7085,'Bara Mohansingh',19),(7086,'Baranagar',19),(7087,'Barasat',19),(7088,'Bara Suzapur',19),(7089,'Barda',19),(7090,'Barddhaman (Bardhaman)',19),(7091,'Bargachhia',19),(7092,'Bargachhia',19),(7093,'Barijhati',19),(7094,'Barijpur',19),(7095,'Barjora',19),(7096,'Barkalikapur',19),(7097,'Barrackpore',19),(7098,'Barrackpur Cantonment',19),(7099,'Barua',19),(7100,'Barua Gopalpur',19),(7101,'Baruihuda',19),(7102,'Baruipara',19),(7103,'Baruipur',19),(7104,'Baruipur (P)',19),(7105,'Barunda',19),(7106,'Basai',19),(7107,'Basantapur',19),(7108,'Basanti',19),(7109,'Basantia',19),(7110,'Basina',19),(7111,'Basirhat',19),(7112,'Baska',19),(7113,'Basudebpur',19),(7114,'Basudebpur',19),(7115,'Batika',19),(7116,'Batul',19),(7117,'Bayarsing',19),(7118,'Begampur',19),(7119,'Begari',19),(7120,'Begun Kodar',19),(7121,'Beharia',19),(7122,'Beldanga',19),(7123,'Beldubi',19),(7124,'Belebathan',19),(7125,'Belgharia',19),(7126,'Beliatore',19),(7127,'Belumilki',19),(7128,'Benia Gram',19),(7129,'Benjanhari Acharial',19),(7130,'Benudia',19),(7131,'Berandari Bagaria',19),(7132,'Berhampore (Baharampur)',19),(7133,'Betpuli',19),(7134,'Bhabki',19),(7135,'Bhadreswar',19),(7136,'Bhagabatipur',19),(7137,'Bhandardaha',19),(7138,'Bhandar Gachha',19),(7139,'Bhangar Raghunathpur',19),(7140,'Bhangri Pratham Khanda',19),(7141,'Bhanowara',19),(7142,'Bhasa',19),(7143,'Bhasaipaikar',19),(7144,'Bhatenda',19),(7145,'Bhatpara',19),(7146,'Bhimram',19),(7147,'Bholar Dabri',19),(7148,'Bidhannagar',19),(7149,'Bidyadharpur',19),(7150,'Bikihakola',19),(7151,'Bilandapur',19),(7152,'Bilkanda',19),(7153,'Bilpahari',19),(7154,'Binnaguri',19),(7155,'Bipra Noapara',19),(7156,'Bira',19),(7157,'Birlapur',19),(7158,'Birnagar',19),(7159,'Birodhi',19),(7160,'Birpara',19),(7161,'Bishnupur',19),(7162,'Bishnupur',19),(7163,'Bishnupur',19),(7164,'Bishnupur',19),(7165,'Bolpur',19),(7166,'Bongaon (Bangaon)',19),(7167,'Bora Gagangohalia',19),(7168,'Borai',19),(7169,'Bowali',19),(7170,'Brindabanpur',19),(7171,'Budbud',19),(7172,'Budge Budge',19),(7173,'Buita',19),(7174,'Cart Road',19),(7175,'Chachanda',19),(7176,'Chak Alampur',19),(7177,'Chakapara',19),(7178,'Chak Bankola',19),(7179,'Chak Barbaria',19),(7180,'Chak Baria',19),(7181,'Chak Bhrigu',19),(7182,'Chakchaka',19),(7183,'Chakdaha',19),(7184,'Chak Enayetnagar',19),(7185,'Chakiabhita',19),(7186,'Chak Kanthalia',19),(7187,'Chak Kashipur',19),(7188,'Chakmeghoan',19),(7189,'Chalsa Mahabari',19),(7190,'Chaltia',19),(7191,'Champahati',19),(7192,'Champdani',19),(7193,'Chamrail',19),(7194,'Chanchal',19),(7195,'Chandannagar',19),(7196,'Chandapur Champagachhi',19),(7197,'Chanddandaha',19),(7198,'Chandipur',19),(7199,'Chandpala Anantapathpur',19),(7200,'Chandpara',19),(7201,'Chandpur',19),(7202,'Chandpur M',19),(7203,'Chandrakona',19),(7204,'Chandrapur',19),(7205,'Chandrapur',19),(7206,'Chandrapur',19),(7207,'Chanduria',19),(7208,'Chapari',19),(7209,'Chapra',19),(7210,'Chapui',19),(7211,'Char Brahmanagar',19),(7212,'Charka',19),(7213,'Char Maijdia',19),(7214,'Chaspara',19),(7215,'Chata Kalikapur',19),(7216,'Chatta Baria',19),(7217,'Chaulia',19),(7218,'Chechakhata',19),(7219,'Chekya',19),(7220,'Chelad',19),(7221,'Chhatianmor',19),(7222,'Chhekati',19),(7223,'Chhora',19),(7224,'Chhota Laukuthi',19),(7225,'Chhota Suzapur',19),(7226,'Chikanpara',19),(7227,'Chikrand',19),(7228,'Chinchuria',19),(7229,'Chittaranjan',19),(7230,'Chong Ghurali',19),(7231,'Chongtong Tea Garden',19),(7232,'Chopra',19),(7233,'Contai',19),(7234,'Cooper\'s Camp',19),(7235,'Dabgram',19),(7236,'Dafahat',19),(7237,'Dafarpur',19),(7238,'Dafarpur',19),(7239,'Dainhat',19),(7240,'Dakhin Rampur',19),(7241,'Dakra',19),(7242,'Dakshin Bagdogra',19),(7243,'Dakshin Baguan',19),(7244,'Dakshin Chatra',19),(7245,'Dakshin Jhapardaha',19),(7246,'Dakshin Khagrabari',19),(7247,'Dakshin Khanda',19),(7248,'Dakshin Odlabari',19),(7249,'Dakshin Rajyadharpur',19),(7250,'Dakshin Raypur',19),(7251,'Dakshin Santoshpur',19),(7252,'Dalkhola',19),(7253,'Dalurband',19),(7254,'Dandirhat',19),(7255,'Danga',19),(7256,'Dankuni',19),(7257,'Darappur',19),(7258,'Darjiling (Darjeeling)',19),(7259,'Daulatpur',19),(7260,'Deara',19),(7261,'Debipur',19),(7262,'Debipur',19),(7263,'Deora',19),(7264,'Deora',19),(7265,'Deulgram',19),(7266,'Deuli',19),(7267,'Deulia',19),(7268,'Deulpur',19),(7269,'Dhakuria',19),(7270,'Dhaliabari',19),(7271,'Dhamua',19),(7272,'Dhania',19),(7273,'Dhanyakuria',19),(7274,'Dharmapur',19),(7275,'Dhatrigram',19),(7276,'Dhola',19),(7277,'Dhuilya',19),(7278,'Dhulagari',19),(7279,'Dhulasimla',19),(7280,'Dhulian',19),(7281,'Dhunki',19),(7282,'Dhupguri',19),(7283,'Dhusaripara',19),(7284,'Diamond Harbour',19),(7285,'Digha',19),(7286,'Digha',19),(7287,'Dighirpar',19),(7288,'Dignala',19),(7289,'Dihi Kalas',19),(7290,'Dihimandalghat',19),(7291,'Dinga Khola',19),(7292,'Dinhata',19),(7293,'Dogachhia',19),(7294,'Domjur',19),(7295,'Domohani',19),(7296,'Donalia',19),(7297,'Dubra',19),(7298,'Dubrajpur',19),(7299,'Dudhkalmi',19),(7300,'Dum Dum',19),(7301,'Dumriguri',19),(7302,'Dungra Khasmahal',19),(7303,'Durganagar',19),(7304,'Durgapur',19),(7305,'Durllabhganj',19),(7306,'Dwari Geria',19),(7307,'Egara',19),(7308,'Egra',19),(7309,'Ekabbarpur',19),(7310,'Eksara',19),(7311,'English Bazar',19),(7312,'Erashal',19),(7313,'Falakata',19),(7314,'Farakka Barrage Township',19),(7315,'Fatehpur',19),(7316,'Fatellapur',19),(7317,'Fatepur',19),(7318,'Gabberia',19),(7319,'Gadigachha',19),(7320,'Gairkata',19),(7321,'Gangadharpur',19),(7322,'Gangadharpur',19),(7323,'Gangapur',19),(7324,'Gangarampur',19),(7325,'Gangnapur',19),(7326,'Gangni',19),(7327,'Gangpur',19),(7328,'Ganye Gangadharpur',19),(7329,'Garalgachha',19),(7330,'Garbeta',19),(7331,'Garh Kamalpur',19),(7332,'Garia',19),(7333,'Garshyamnagar',19),(7334,'Garulia',19),(7335,'Gaur Daha',19),(7336,'Gayespur',19),(7337,'Geni',19),(7338,'Ghatal',19),(7339,'Ghola Noapara',19),(7340,'Ghoraberia',19),(7341,'Ghoralia',19),(7342,'Ghorsala',19),(7343,'Ghosal Chak',19),(7344,'Ghuni',19),(7345,'Ghutgarya',19),(7346,'Ging Tea Garden',19),(7347,'Giria',19),(7348,'Goaljan',19),(7349,'Goasafat',19),(7350,'Gobardanga',19),(7351,'Gobindapur',19),(7352,'Goda',19),(7353,'Gondalpara',19),(7354,'Gopalpur',19),(7355,'Gopalpur',19),(7356,'Gopalpur',19),(7357,'Gopinathpur',19),(7358,'Gopjan',19),(7359,'Gora Bazar',19),(7360,'Guma',19),(7361,'Guriahati',19),(7362,'Guskara',19),(7363,'Habra',19),(7364,'Hafania',19),(7365,'Halalpur Krishnapur',19),(7366,'Haldia',19),(7367,'Haldibari',19),(7368,'Halisahar',19),(7369,'Halyan',19),(7370,'Hansghara',19),(7371,'Hanskunda',19),(7372,'Hanspukuria',19),(7373,'Haora (Howrah)',19),(7374,'Harharia Chak',19),(7375,'Haridasmati',19),(7376,'Hariharpur',19),(7377,'Harinadibhastsala',19),(7378,'Harindanga',19),(7379,'Haringhata Farm',19),(7380,'Haripur',19),(7381,'Harirampur',19),(7382,'Harishpur',19),(7383,'Hasimnagar',19),(7384,'Hatgachha',19),(7385,'Hatsimla',19),(7386,'Hijuli',19),(7387,'Hijuli',19),(7388,'Hincha Gerya',19),(7389,'Hingalganj',19),(7390,'Hirapur',19),(7391,'Hutmura',19),(7392,'Ichhapur (Ichapore)',19),(7393,'Ichhapur Defence Estate',19),(7394,'Ichhlampur',19),(7395,'Ilambazar',19),(7396,'Islampur',19),(7397,'Islampur',19),(7398,'Itahar',19),(7399,'Itinda',19),(7400,'Jadupur',19),(7401,'Jafarpur',19),(7402,'Jafrabad',19),(7403,'Jagadanandapur',19),(7404,'Jagadishpur',19),(7405,'Jagannathpur',19),(7406,'Jagatballavpur',19),(7407,'Jagatnagar',19),(7408,'Jagijhora Barabak',19),(7409,'Jagtaj',19),(7410,'Jala Kendua',19),(7411,'Jalalpur',19),(7412,'Jallabad',19),(7413,'Jalpaiguri',19),(7414,'Jaluidanga',19),(7415,'Jamuria',19),(7416,'Janai',19),(7417,'Jangal',19),(7418,'Jangalpara',19),(7419,'Jangipur',19),(7420,'Jateshwar',19),(7421,'Jatragachhi',19),(7422,'Jaygaon (Jaigaon)',19),(7423,'Jaykrishnapur',19),(7424,'Jaykrishnapur',19),(7425,'Jaynagar',19),(7426,'Jaynagar Mazilpur',19),(7427,'Jaypur',19),(7428,'Jaypur Bil',19),(7429,'Jemari (J.K. Nagar Township)',19),(7430,'Jetia',19),(7431,'Jhalda',19),(7432,'Jhalda',19),(7433,'Jhangra',19),(7434,'Jhanti Pahari',19),(7435,'Jhargram',19),(7436,'Jhorhat',19),(7437,'Jiaganj-Azimganj',19),(7438,'Jirat',19),(7439,'Jitu',19),(7440,'Joka',19),(7441,'Jot Kamal',19),(7442,'Joypul',19),(7443,'Jujarsaha',19),(7444,'Kachu Pukur',19),(7445,'Kaijuri',19),(7446,'Kajora',19),(7447,'Kakdihi',19),(7448,'Kakramari',19),(7449,'Kalaikunda',19),(7450,'Kalara',19),(7451,'Kalaria',19),(7452,'Kaliaganj',19),(7453,'Kalikapota',19),(7454,'Kalikapur',19),(7455,'Kalikapur Barasat',19),(7456,'Kalimpong',19),(7457,'Kalipur',19),(7458,'Kalkut',19),(7459,'Kalna',19),(7460,'Kalua',19),(7461,'Kalyani',19),(7462,'Kalyanpur',19),(7463,'Kamalapur',19),(7464,'Kamarhati',19),(7465,'Kamat Phulbari',19),(7466,'Kamgachhi',19),(7467,'Kamranga',19),(7468,'Kanaipur',19),(7469,'Kanaipur',19),(7470,'Kanchrapara',19),(7471,'Kandi',19),(7472,'Kanganbaria',19),(7473,'Kanki',19),(7474,'Kanksa',19),(7475,'Kankuria',19),(7476,'Kanpur',19),(7477,'Kantaberia',19),(7478,'Kantaranguri',19),(7479,'Kantlia',19),(7480,'Kanyanagar',19),(7481,'Kapashanria',19),(7482,'Karari Chandpur',19),(7483,'Karia',19),(7484,'Karidhya',19),(7485,'Karimpur',19),(7486,'Kasba',19),(7487,'Kashimnagar',19),(7488,'Kasim Bazar (Cossimbazar)',19),(7489,'Katwa',19),(7490,'Kaugachhi',19),(7491,'Kenda',19),(7492,'Kendra Khottamdi',19),(7493,'Kendua',19),(7494,'Kendua',19),(7495,'Keota',19),(7496,'Kesabpur',19),(7497,'Khadalgobra',19),(7498,'Khadinan',19),(7499,'Khagrabari',19),(7500,'Khajutti',19),(7501,'Khalia',19),(7502,'Khalisani',19),(7503,'Khalor',19),(7504,'Khandra',19),(7505,'Khanpur',19),(7506,'Khantora',19),(7507,'Kharagpur',19),(7508,'Kharagpur Railway Settlement',19),(7509,'Kharar',19),(7510,'Khardah',19),(7511,'Kharia',19),(7512,'Kharibari',19),(7513,'Kharimala Khagrabari',19),(7514,'Kharisha',19),(7515,'Kharsarai',19),(7516,'Khasjalalsi',19),(7517,'Khatra',19),(7518,'Khidirpur (Kidderpore)',19),(7519,'Khodarampur',19),(7520,'Khodar Bazar',19),(7521,'Khorddabamonia',19),(7522,'Koch Bihar (Cooch Behar)',19),(7523,'Kodalia',19),(7524,'Kohetpur',19),(7525,'Kokapur',19),(7526,'Kola',19),(7527,'Kolaghat',19),(7528,'Kolkata [Calcutta]',19),(7529,'Komarhat',19),(7530,'Konardihi',19),(7531,'Konnagar',19),(7532,'Kotbar',19),(7533,'Kotulpur',19),(7534,'Koyra',19),(7535,'Kriparampur',19),(7536,'Krishna Chandrapur',19),(7537,'Krishnanagar',19),(7538,'Krishnapur',19),(7539,'Krishnapur',19),(7540,'Krishna Sali',19),(7541,'Kshidirpur',19),(7542,'Kshirpai (Khirpai)',19),(7543,'Kulberia',19),(7544,'Kuldanga',19),(7545,'Kulia',19),(7546,'Kulihanda',19),(7547,'Kulitapara',19),(7548,'Kulti',19),(7549,'Kumirmora',19),(7550,'Kunustara',19),(7551,'Kurseong',19),(7552,'Kusadanga',19),(7553,'Labhpur',19),(7554,'Lagda',19),(7555,'Lalman',19),(7556,'Lalpur',19),(7557,'Lalpur',19),(7558,'Lapara',19),(7559,'Laskarpara',19),(7560,'Lataguri',19),(7561,'Ledisol',19),(7562,'Madanpur',19),(7563,'Madhusudanpur',19),(7564,'Madhyamgram',19),(7565,'Madna',19),(7566,'Magrahat',19),(7567,'Mahadeb Nagar',19),(7568,'Mahal',19),(7569,'Mahendrapur',19),(7570,'Maheshtala',19),(7571,'Mahiari',19),(7572,'Mahira',19),(7573,'Mahishrekha',19),(7574,'Mainaguri',19),(7575,'Majdia',19),(7576,'Majiara',19),(7577,'Makardaha',19),(7578,'Makhal Tala',19),(7579,'Mal',19),(7580,'Mallik Bagan',19),(7581,'Mallikpur',19),(7582,'Mamrejpur',19),(7583,'Manbazar',19),(7584,'Mandarbani',19),(7585,'Mangalbari',19),(7586,'Mangarjung Tea Garden (Nagri)',19),(7587,'Manikpur',19),(7588,'Manirampur',19),(7589,'Mansinhapur',19),(7590,'Manushpur',19),(7591,'Maricha',19),(7592,'Masat',19),(7593,'Masat',19),(7594,'Masila',19),(7595,'Maslandapur',19),(7596,'Mathabhanga',19),(7597,'Mathapari',19),(7598,'Mathurapur',19),(7599,'Mathurapur',19),(7600,'Matialihat',19),(7601,'Matiari',19),(7602,'Matla',19),(7603,'Mechiabasti',19),(7604,'Medinipur (Midnapore)',19),(7605,'Mekliganj (Mekhliganj)',19),(7606,'Memari',19),(7607,'Mihitikri',19),(7608,'Milki',19),(7609,'Minakhan',19),(7610,'Mira',19),(7611,'Mirdhanga',19),(7612,'Mirik',19),(7613,'Mirjapur',19),(7614,'Mirzapur',19),(7615,'Mirzapur',19),(7616,'Mithipur',19),(7617,'Mohanpur',19),(7618,'Mohanpur',19),(7619,'Mugkalyan',19),(7620,'Muragachha',19),(7621,'Murarai',19),(7622,'Murgathaul',19),(7623,'Murshidabad',19),(7624,'Murulia',19),(7625,'Nababpur',19),(7626,'Nabadwip',19),(7627,'Nabaghanapur',19),(7628,'Nabagram',19),(7629,'Nabagram Colony',19),(7630,'Naba Kola',19),(7631,'Nabghara',19),(7632,'Nabgram',19),(7633,'Nachhratpur Katabari',19),(7634,'Nadabhanga',19),(7635,'Nagar Changrabandha',19),(7636,'Nagdaha',19),(7637,'Nahazari',19),(7638,'Naihati',19),(7639,'Nainan',19),(7640,'Naiti',19),(7641,'Naldanga',19),(7642,'Nalhati',19),(7643,'Nalpur',19),(7644,'Namajgram',19),(7645,'Nandigram',19),(7646,'Nari',19),(7647,'Naridana',19),(7648,'Nasaratpur',19),(7649,'Nasibpur',19),(7650,'Nasra',19),(7651,'Natibpur',19),(7652,'Naul',19),(7653,'Naupala',19),(7654,'Nawapara (Nuapada)',19),(7655,'Nayabahadurpur',19),(7656,'Nazirpur',19),(7657,'Nebadhai Duttapukur',19),(7658,'New Barrackpore',19),(7659,'Nibra',19),(7660,'Nimpith',19),(7661,'Nimsa',19),(7662,'Nischintapur',19),(7663,'Noapara',19),(7664,'Nokpul',19),(7665,'North Dumdum',19),(7666,'Nrisinghapur',19),(7667,'Oadipur',19),(7668,'Odlabari',19),(7669,'Old Malda',19),(7670,'Ondal',19),(7671,'Osmanpur',19),(7672,'Osmanpur',19),(7673,'Pairagachha',19),(7674,'Palashban',19),(7675,'Palashi',19),(7676,'Palladaha',19),(7677,'Paltapara',19),(7678,'Panchghara',19),(7679,'Panchghara',19),(7680,'Panchla',19),(7681,'Panchpara',19),(7682,'Pandua',19),(7683,'Pangachhiya',19),(7684,'Paniara',19),(7685,'Panihati',19),(7686,'Panpara',19),(7687,'Panskura',19),(7688,'Panuhat',19),(7689,'Panuria',19),(7690,'Parangarpar',19),(7691,'Paranpara',19),(7692,'Parashkol',19),(7693,'Parasia',19),(7694,'Parbbatipur',19),(7695,'Par Beliya',19),(7696,'Parota',19),(7697,'Par Patiram',19),(7698,'Paschim Bainan',19),(7699,'Paschimbhatjangla',19),(7700,'Paschim Gazipur',19),(7701,'Paschim Jitpur',19),(7702,'Paschim Panchla',19),(7703,'Paschim Punropara',19),(7704,'Pashchim Khalna',19),(7705,'Patdaha',19),(7706,'Patharberia',19),(7707,'Patihal',19),(7708,'Patuli',19),(7709,'Patulia',19),(7710,'Petua',19),(7711,'Phulia',19),(7712,'Piarinagar',19),(7713,'Poali',19),(7714,'Podara',19),(7715,'Prayagpur',19),(7716,'Priyanagar',19),(7717,'Pujali',19),(7718,'Punglia',19),(7719,'Purba Bishnupur M',19),(7720,'Purba Ranaghat',19),(7721,'Purbba Narayanpur',19),(7722,'Purbba Tajpur (Purba Tajpur)',19),(7723,'Puruliya (Purulia)',19),(7724,'Purusottampur',19),(7725,'Radhanagar',19),(7726,'Radhapur',19),(7727,'Raghabpur',19),(7728,'Raghabpur',19),(7729,'Raghudebbati',19),(7730,'Raghudebpur',19),(7731,'Raghunathchak',19),(7732,'Raghunathpur',19),(7733,'Raghunathpur',19),(7734,'Raghunathpur (PS-Dankuni)',19),(7735,'Raghunathpur (PS-Magra)',19),(7736,'Raigachhi',19),(7737,'Raiganj',19),(7738,'Raipur',19),(7739,'Raipur Bazar',19),(7740,'Rajapur',19),(7741,'Rajarhat Gopalpur',19),(7742,'Rajbalhat',19),(7743,'Rajnagar',19),(7744,'Rajpur Sonarpur',19),(7745,'Ramakantapur',19),(7746,'Ramanathpur',19),(7747,'Ramchandrapur',19),(7748,'Rameswarpur',19),(7749,'Ramjibanpur',19),(7750,'Ramkrishnapur',19),(7751,'Ramnagar',19),(7752,'Ramnagar',19),(7753,'Rampurhat',19),(7754,'Ranaghat',19),(7755,'Ranaghat',19),(7756,'Rangabhita',19),(7757,'Raniganj',19),(7758,'Ratibati',19),(7759,'Raynagar',19),(7760,'Rekjuani',19),(7761,'Rishra',19),(7762,'Rishra',19),(7763,'Rongmook Ceder Tea Garden',19),(7764,'Rudrapur',19),(7765,'Ruiya',19),(7766,'Sadigachhi',19),(7767,'Sadpur',19),(7768,'Saguna',19),(7769,'Sahajadpur',19),(7770,'Sahapur',19),(7771,'Sahapur',19),(7772,'Sahebganj',19),(7773,'Sahebpur',19),(7774,'Sainthia',19),(7775,'Salap',19),(7776,'Salar',19),(7777,'Salipur',19),(7778,'Saltor',19),(7779,'Samali',19),(7780,'Samuktola',19),(7781,'Sangrampur',19),(7782,'Sankarpur',19),(7783,'Sankrail',19),(7784,'Sankrailjala',19),(7785,'Santipur (Shantipur)',19),(7786,'Santoshpur',19),(7787,'Sarenga',19),(7788,'Sarpi',19),(7789,'Sashpur',19),(7790,'Satigachha',19),(7791,'Sehara',19),(7792,'Serampore',19),(7793,'Serpur',19),(7794,'Shankara',19),(7795,'Shankhanagar',19),(7796,'Shantipur',19),(7797,'Shashati',19),(7798,'Shibalaya',19),(7799,'Shilda',19),(7800,'Shimulpur',19),(7801,'Shuvararah',19),(7802,'Shyamdhan',19),(7803,'Shyampur',19),(7804,'Shyampur',19),(7805,'Sibdanga Badarpur',19),(7806,'Sibnagar',19),(7807,'Siduli',19),(7808,'Silampur',19),(7809,'Siliguri',19),(7810,'Simhat',19),(7811,'Simla',19),(7812,'Simlapal',19),(7813,'Simurali',19),(7814,'Singtam Tea Garden',19),(7815,'Singur',19),(7816,'Sirakol',19),(7817,'Sirsha',19),(7818,'Sisha-Jumrha',19),(7819,'Sobhaganj',19),(7820,'Solgohalia',19),(7821,'Sonada Khasmahal',19),(7822,'Sonamukhi',19),(7823,'Sonatala',19),(7824,'Sonatikiri',19),(7825,'Sonda',19),(7826,'South Dumdum',19),(7827,'Srikantabati',19),(7828,'Srimantapur',19),(7829,'Sripur',19),(7830,'Srirampur',19),(7831,'Subarnapur',19),(7832,'Sukdal',19),(7833,'Sukhiapokhri',19),(7834,'Sulanggari',19),(7835,'Suri',19),(7836,'Surul',19),(7837,'Swangrampur',19),(7838,'Taherpur',19),(7839,'Takagach',19),(7840,'Taki',19),(7841,'Talbandha',19),(7842,'Taldi',19),(7843,'Tamluk',19),(7844,'Tarakeswar',19),(7845,'Tari',19),(7846,'Teghari',19),(7847,'Teghari',19),(7848,'Tehatta',19),(7849,'Teleni Para',19),(7850,'Telipara Tea Garden D',19),(7851,'Tentulkuli',19),(7852,'Tiorkhali',19),(7853,'Tisa',19),(7854,'Titagarh',19),(7855,'Topsi',19),(7856,'Tufanganj',19),(7857,'Tulshighata',19),(7858,'Udang',19),(7859,'Ukhra',19),(7860,'Ula',19),(7861,'Uluberia',19),(7862,'Usthi',19),(7863,'Uttampur',19),(7864,'Uttar Bagdogra',19),(7865,'Uttar Bagundi',19),(7866,'Uttar Bishnupur',19),(7867,'Uttar Durgapur',19),(7868,'Uttar Goara',19),(7869,'Uttar Jhapardaha',19),(7870,'Uttar Kalas',19),(7871,'Uttar Kamakhyaguri',19),(7872,'Uttar Kusum',19),(7873,'Uttar Latabari',19),(7874,'Uttar Madarihat',19),(7875,'Uttar Mahammadpur',19),(7876,'Uttarpara Kotrung',19),(7877,'Uttarparanij',19),(7878,'Uttar Pirpur',19),(7879,'Uttar Raypur',19),(7880,'Uttar Satali',19);
/*!40000 ALTER TABLE `master_forms_city` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_course`
--

DROP TABLE IF EXISTS `master_forms_course`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_course` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `course` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_course`
--

LOCK TABLES `master_forms_course` WRITE;
/*!40000 ALTER TABLE `master_forms_course` DISABLE KEYS */;
INSERT INTO `master_forms_course` VALUES (1,'MBA'),(2,'BBA'),(3,'BCCA');
/*!40000 ALTER TABLE `master_forms_course` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_day`
--

DROP TABLE IF EXISTS `master_forms_day`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_day` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `day` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_day`
--

LOCK TABLES `master_forms_day` WRITE;
/*!40000 ALTER TABLE `master_forms_day` DISABLE KEYS */;
INSERT INTO `master_forms_day` VALUES (1,'Monday'),(2,'Tuesday'),(3,'Wednesday'),(4,'Thursday'),(5,'Friday'),(6,'Saturday');
/*!40000 ALTER TABLE `master_forms_day` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_degree`
--

DROP TABLE IF EXISTS `master_forms_degree`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_degree` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `degree` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=6 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_degree`
--

LOCK TABLES `master_forms_degree` WRITE;
/*!40000 ALTER TABLE `master_forms_degree` DISABLE KEYS */;
INSERT INTO `master_forms_degree` VALUES (1,'B.E.'),(2,'B.Sc'),(3,'B.A.'),(4,'BBA'),(5,'B.Com');
/*!40000 ALTER TABLE `master_forms_degree` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_degreestreamorfield`
--

DROP TABLE IF EXISTS `master_forms_degreestreamorfield`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_degreestreamorfield` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stream_or_field_name` varchar(50) DEFAULT NULL,
  `fk_degree_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `master_forms_degrees_fk_degree_id_4cd0f600_fk_master_fo` (`fk_degree_id`),
  CONSTRAINT `master_forms_degrees_fk_degree_id_4cd0f600_fk_master_fo` FOREIGN KEY (`fk_degree_id`) REFERENCES `master_forms_degree` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_degreestreamorfield`
--

LOCK TABLES `master_forms_degreestreamorfield` WRITE;
/*!40000 ALTER TABLE `master_forms_degreestreamorfield` DISABLE KEYS */;
INSERT INTO `master_forms_degreestreamorfield` VALUES (1,'Computer Technology',1),(2,'Informaction Science & Engineering',2),(3,'Mechanical Engineering',1);
/*!40000 ALTER TABLE `master_forms_degreestreamorfield` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_district`
--

DROP TABLE IF EXISTS `master_forms_district`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_district` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `district` varchar(30) DEFAULT NULL,
  `fk_state_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `master_forms_distric_fk_state_id_19fe7428_fk_master_fo` (`fk_state_id`),
  CONSTRAINT `master_forms_distric_fk_state_id_19fe7428_fk_master_fo` FOREIGN KEY (`fk_state_id`) REFERENCES `master_forms_state` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=732 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_district`
--

LOCK TABLES `master_forms_district` WRITE;
/*!40000 ALTER TABLE `master_forms_district` DISABLE KEYS */;
INSERT INTO `master_forms_district` VALUES (1,'Anantapur',28),(2,'Chittoor',28),(3,'East Godavari',28),(4,'Guntur',28),(5,'Kadapa',28),(6,'Krishna',28),(7,'Kurnool',28),(8,'Prakasam',28),(9,'Sri Potti Sriramulu Nellore',28),(10,'Srikakulam',28),(11,'Visakhapatnam',28),(12,'Vizianagaram',28),(13,'West Godavari',28),(14,'Anjaw',12),(15,'Changlang',12),(16,'East Kameng',12),(17,'East Siang',12),(18,'Kamle',12),(19,'Kra Daadi',12),(20,'Kurung Kumey',12),(21,'Lepa-Rada',12),(22,'Lohit',12),(23,'Longding',12),(24,'Lower Dibang Valley',12),(25,'Lower Siang',12),(26,'Lower Subansiri',12),(27,'Namsai',12),(28,'Pakke-Kessang',12),(29,'Papum Pare',12),(30,'Shi Yomi',12),(31,'Siang',12),(32,'Tawang',12),(33,'Tirap',12),(34,'Upper Dibang Valley',12),(35,'Upper Siang',12),(36,'Upper Subansiri',12),(37,'West Kameng',12),(38,'West Siang',12),(39,'Baksa',18),(40,'Barpeta',18),(41,'Bishwanath',18),(42,'Bongaigaon',18),(43,'Cachar',18),(44,'Charaideo',18),(45,'Chirang',18),(46,'Darrang',18),(47,'Dhemaji',18),(48,'Dhubri',18),(49,'Dibrugarh',18),(50,'Dima Hasao',18),(51,'Goalpara',18),(52,'Golaghat',18),(53,'Hailakandi',18),(54,'Hojai',18),(55,'Jorhat',18),(56,'Kamrup',18),(57,'Kamrup Metropolitan',18),(58,'Karbi Anglong',18),(59,'Karimganj',18),(60,'Kokrajhar',18),(61,'Lakhimpur',18),(62,'Majuli',18),(63,'Morigaon',18),(64,'Nagaon',18),(65,'Nalbari',18),(66,'Sivasagar',18),(67,'South Salmara',18),(68,'Sonitpur',18),(69,'Tinsukia',18),(70,'Udalguri',18),(71,'West Karbi Anglong',18),(72,'Araria',10),(73,'Arwal',10),(74,'Aurangabad',10),(75,'Banka',10),(76,'Begusarai',10),(77,'Bhagalpur',10),(78,'Bhojpur',10),(79,'Buxar',10),(80,'Darbhanga',10),(81,'East Champaran',10),(82,'Gaya',10),(83,'Gopalganj',10),(84,'Jamui',10),(85,'Jehanabad',10),(86,'Kaimur',10),(87,'Katihar',10),(88,'Khagaria',10),(89,'Kishanganj',10),(90,'Lakhisarai',10),(91,'Madhepura',10),(92,'Madhubani',10),(93,'Munger',10),(94,'Muzaffarpur',10),(95,'Nalanda',10),(96,'Nawada',10),(97,'Patna',10),(98,'Purnia',10),(99,'Rohtas',10),(100,'Saharsa',10),(101,'Samastipur',10),(102,'Saran',10),(103,'Sheikhpura',10),(104,'Sheohar',10),(105,'Sitamarhi',10),(106,'Siwan',10),(107,'Supaul',10),(108,'Vaishali',10),(109,'West Champaran',10),(110,'Balod',22),(111,'Baloda Bazar',22),(112,'Balrampur',22),(113,'Bastar',22),(114,'Bemetara',22),(115,'Bijapur',22),(116,'Bilaspur',22),(117,'Dantewada',22),(118,'Dhamtari',22),(119,'Durg',22),(120,'Gariaband',22),(121,'Janjgir-Champa',22),(122,'Jashpur',22),(123,'Kabirdham',22),(124,'Kanker',22),(125,'Kondagaon',22),(126,'Korba',22),(127,'Korea',22),(128,'Mahasamund',22),(129,'Mungeli',22),(130,'Narayanpur',22),(131,'Raigarh',22),(132,'Raipur',22),(133,'Rajnandgaon',22),(134,'Sukma',22),(135,'Surajpur',22),(136,'Surguja',22),(137,'North Goa',30),(138,'South Goa',30),(139,'Ahmedabad',24),(140,'Amreli',24),(141,'Anand',24),(142,'Aravalli',24),(143,'Banaskantha',24),(144,'Bharuch',24),(145,'Bhavnagar',24),(146,'Botad',24),(147,'Chhota Udepur',24),(148,'Dahod',24),(149,'Dang',24),(150,'Devbhoomi Dwarka',24),(151,'Gandhinagar',24),(152,'Gir Somnath',24),(153,'Jamnagar',24),(154,'Junagadh',24),(155,'Kheda',24),(156,'Kutch',24),(157,'Mahisagar',24),(158,'Mehsana',24),(159,'Morbi',24),(160,'Narmada',24),(161,'Navsari',24),(162,'Panchmahal',24),(163,'Patan',24),(164,'Porbandar',24),(165,'Rajkot',24),(166,'Sabarkantha',24),(167,'Surat',24),(168,'Surendranagar',24),(169,'Tapi',24),(170,'Vadodara',24),(171,'Valsad',24),(172,'Ambala',6),(173,'Bhiwani',6),(174,'Charkhi Dadri',6),(175,'Faridabad',6),(176,'Fatehabad',6),(177,'Gurugram',6),(178,'Hissar',6),(179,'Jhajjar',6),(180,'Jind',6),(181,'Kaithal',6),(182,'Karnal',6),(183,'Kurukshetra',6),(184,'Mahendragarh',6),(185,'Nuh',6),(186,'Palwal',6),(187,'Panchkula',6),(188,'Panipat',6),(189,'Rewari',6),(190,'Rohtak',6),(191,'Sirsa',6),(192,'Sonipat',6),(193,'Yamuna Nagar',6),(194,'Bilaspur',2),(195,'Chamba',2),(196,'Hamirpur',2),(197,'Kangra',2),(198,'Kinnaur',2),(199,'Kullu',2),(200,'Lahaul and Spiti',2),(201,'Mandi',2),(202,'Shimla',2),(203,'Sirmaur',2),(204,'Solan',2),(205,'Una',2),(206,'Bokaro',20),(207,'Chatra',20),(208,'Deoghar',20),(209,'Dhanbad',20),(210,'Dumka',20),(211,'East Singhbhum',20),(212,'Garhwa',20),(213,'Giridih',20),(214,'Godda',20),(215,'Gumla',20),(216,'Hazaribag',20),(217,'Jamtara',20),(218,'Khunti',20),(219,'Koderma',20),(220,'Latehar',20),(221,'Lohardaga',20),(222,'Pakur',20),(223,'Palamu',20),(224,'Ramgarh',20),(225,'Ranchi',20),(226,'Sahibganj',20),(227,'Seraikela Kharsawan',20),(228,'Simdega',20),(229,'West Singhbhum',20),(230,'Bagalkot',29),(231,'Ballari',29),(232,'Belagavi',29),(233,'Bengaluru Rural',29),(234,'Bengaluru Urban',29),(235,'Bidar',29),(236,'Chamarajnagar',29),(237,'Chikkaballapur',29),(238,'Chikkamagaluru',29),(239,'Chitradurga',29),(240,'Dakshina Kannada',29),(241,'Davanagere',29),(242,'Dharwad',29),(243,'Gadag',29),(244,'Hassan',29),(245,'Haveri',29),(246,'Kalaburagi',29),(247,'Kodagu',29),(248,'Kolar',29),(249,'Koppal',29),(250,'Mandya',29),(251,'Mysuru',29),(252,'Raichur',29),(253,'Ramanagara',29),(254,'Shivamogga',29),(255,'Tumakuru',29),(256,'Udupi',29),(257,'Uttara Kannada',29),(258,'Vijayapura',29),(259,'Yadgir',29),(260,'Alappuzha',32),(261,'Ernakulam',32),(262,'Idukki',32),(263,'Kannur',32),(264,'Kasaragod',32),(265,'Kollam',32),(266,'Kottayam',32),(267,'Kozhikode',32),(268,'Malappuram',32),(269,'Palakkad',32),(270,'Pathanamthitta',32),(271,'Thrissur',32),(272,'Thiruvananthapuram',32),(273,'Wayanad',32),(274,'Agar Malwa',23),(275,'Alirajpur',23),(276,'Anuppur',23),(277,'Ashok Nagar',23),(278,'Balaghat',23),(279,'Barwani',23),(280,'Betul',23),(281,'Bhind',23),(282,'Bhopal',23),(283,'Burhanpur',23),(284,'Chhatarpur',23),(285,'Chhindwara',23),(286,'Damoh',23),(287,'Datia',23),(288,'Dewas',23),(289,'Dhar',23),(290,'Dindori',23),(291,'Guna',23),(292,'Gwalior',23),(293,'Harda',23),(294,'Hoshangabad',23),(295,'Indore',23),(296,'Jabalpur',23),(297,'Jhabua',23),(298,'Katni',23),(299,'Khandwa (East Nimar)',23),(300,'Khargone (West Nimar)',23),(301,'Mandla',23),(302,'Mandsaur',23),(303,'Morena',23),(304,'Narsinghpur',23),(305,'Neemuch',23),(306,'Niwari',23),(307,'Panna',23),(308,'Raisen',23),(309,'Rajgarh',23),(310,'Ratlam',23),(311,'Rewa',23),(312,'Sagar',23),(313,'Satna',23),(314,'Sehore',23),(315,'Seoni',23),(316,'Shahdol',23),(317,'Shajapur',23),(318,'Sheopur',23),(319,'Shivpuri',23),(320,'Sidhi',23),(321,'Singrauli',23),(322,'Tikamgarh',23),(323,'Ujjain',23),(324,'Umaria',23),(325,'Vidisha',23),(326,'Ahmednagar',27),(327,'Akola',27),(328,'Amravati',27),(329,'Aurangabad',27),(330,'Beed',27),(331,'Bhandara',27),(332,'Buldhana',27),(333,'Chandrapur',27),(334,'Dhule',27),(335,'Gadchiroli',27),(336,'Gondia',27),(337,'Hingoli',27),(338,'Jalgaon',27),(339,'Jalna',27),(340,'Kolhapur',27),(341,'Latur',27),(342,'Mumbai City',27),(343,'Mumbai suburban',27),(344,'Nanded',27),(345,'Nandurbar',27),(346,'Nagpur',27),(347,'Nashik',27),(348,'Osmanabad',27),(349,'Palghar',27),(350,'Parbhani',27),(351,'Pune',27),(352,'Raigad',27),(353,'Ratnagiri',27),(354,'Sangli',27),(355,'Satara',27),(356,'Sindhudurg',27),(357,'Solapur',27),(358,'Thane',27),(359,'Wardha',27),(360,'Washim',27),(361,'Yavatmal',27),(362,'Bishnupur',14),(363,'Chandel',14),(364,'Churachandpur',14),(365,'Imphal East',14),(366,'Imphal West',14),(367,'Jiribam',14),(368,'Kakching',14),(369,'Kamjong',14),(370,'Kangpokpi',14),(371,'Noney',14),(372,'Pherzawl',14),(373,'Senapati',14),(374,'Tamenglong',14),(375,'Tengnoupal',14),(376,'Thoubal',14),(377,'Ukhrul',14),(378,'East Garo Hills',17),(379,'East Khasi Hills',17),(380,'East Jaintia Hills',17),(381,'North Garo Hills',17),(382,'Ri Bhoi',17),(383,'South Garo Hills',17),(384,'South West Garo Hills',17),(385,'South West Khasi Hills',17),(386,'West Jaintia Hills',17),(387,'West Garo Hills',17),(388,'West Khasi Hills',17),(389,'Aizawl',15),(390,'Champhai',15),(391,'Kolasib',15),(392,'Lawngtlai',15),(393,'Lunglei',15),(394,'Mamit',15),(395,'Saiha',15),(396,'Serchhip',15),(397,'Dimapur',13),(398,'Kiphire',13),(399,'Kohima',13),(400,'Longleng',13),(401,'Mokokchung',13),(402,'Mon',13),(403,'Noklak',13),(404,'Peren',13),(405,'Phek',13),(406,'Tuensang',13),(407,'Wokha',13),(408,'Zunheboto',13),(409,'Angul',21),(410,'Boudh (Bauda)',21),(411,'Bhadrak',21),(412,'Balangir',21),(413,'Bargarh (Baragarh)',21),(414,'Balasore',21),(415,'Cuttack',21),(416,'Debagarh (Deogarh)',21),(417,'Dhenkanal',21),(418,'Ganjam',21),(419,'Gajapati',21),(420,'Jharsuguda',21),(421,'Jajpur',21),(422,'Jagatsinghpur',21),(423,'Khordha',21),(424,'Kendujhar (Keonjhar)',21),(425,'Kalahandi',21),(426,'Kandhamal',21),(427,'Koraput',21),(428,'Kendrapara',21),(429,'Malkangiri',21),(430,'Mayurbhanj',21),(431,'Nabarangpur',21),(432,'Nuapada',21),(433,'Nayagarh',21),(434,'Puri',21),(435,'Rayagada',21),(436,'Sambalpur',21),(437,'Subarnapur (Sonepur)',21),(438,'Sundargarh',21),(439,'Amritsar',3),(440,'Barnala',3),(441,'Bathinda',3),(442,'Firozpur',3),(443,'Faridkot',3),(444,'Fatehgarh Sahib',3),(445,'Fazilka[13]',3),(446,'Gurdaspur',3),(447,'Hoshiarpur',3),(448,'Jalandhar',3),(449,'Kapurthala',3),(450,'Ludhiana',3),(451,'Mansa',3),(452,'Moga',3),(453,'Sri Muktsar Sahib',3),(454,'Pathankot',3),(455,'Patiala',3),(456,'Rupnagar',3),(457,'Sahibzada Ajit Singh Nagar',3),(458,'Sangrur',3),(459,'Shahid Bhagat Singh Nagar',3),(460,'Tarn Taran',3),(461,'Ajmer',8),(462,'Alwar',8),(463,'Bikaner',8),(464,'Barmer',8),(465,'Banswara',8),(466,'Bharatpur',8),(467,'Baran',8),(468,'Bundi',8),(469,'Bhilwara',8),(470,'Churu',8),(471,'Chittorgarh',8),(472,'Dausa',8),(473,'Dholpur',8),(474,'Dungarpur',8),(475,'Ganganagar',8),(476,'Hanumangarh',8),(477,'Jhunjhunu',8),(478,'Jalore',8),(479,'Jodhpur',8),(480,'Jaipur',8),(481,'Jaisalmer',8),(482,'Jhalawar',8),(483,'Karauli',8),(484,'Kota',8),(485,'Nagaur',8),(486,'Pali',8),(487,'Pratapgarh',8),(488,'Rajsamand',8),(489,'Sikar',8),(490,'Sawai Madhopur',8),(491,'Sirohi',8),(492,'Tonk',8),(493,'Udaipur',8),(494,'East Sikkim',11),(495,'North Sikkim',11),(496,'South Sikkim',11),(497,'West Sikkim',11),(498,'Ariyalur',33),(499,'Chengalpattu',33),(500,'Chennai',33),(501,'Coimbatore',33),(502,'Cuddalore',33),(503,'Dharmapuri',33),(504,'Dindigul',33),(505,'Erode',33),(506,'Kallakurichi',33),(507,'Kanchipuram',33),(508,'Kanyakumari',33),(509,'Karur',33),(510,'Krishnagiri',33),(511,'Madurai',33),(512,'Nagapattinam',33),(513,'Nilgiris',33),(514,'Namakkal',33),(515,'Perambalur',33),(516,'Pudukkottai',33),(517,'Ramanathapuram',33),(518,'Ranipet',33),(519,'Salem',33),(520,'Sivaganga',33),(521,'Tenkasi',33),(522,'Tirupur',33),(523,'Tiruchirappalli',33),(524,'Theni',33),(525,'Tirunelveli',33),(526,'Thanjavur',33),(527,'Thoothukudi',33),(528,'Tirupattur',33),(529,'Tiruvallur',33),(530,'Tiruvarur',33),(531,'Tiruvannamalai',33),(532,'Vellore',33),(533,'Viluppuram',33),(534,'Virudhunagar',33),(535,'Adilabad',36),(536,'Komaram Bheem',36),(537,'Bhadradri Kothagudem',36),(538,'Hyderabad',36),(539,'Jagtial',36),(540,'Jangaon',36),(541,'Jayashankar Bhupalpally',36),(542,'Jogulamba Gadwal',36),(543,'Kamareddy',36),(544,'Karimnagar',36),(545,'Khammam',36),(546,'Mahabubabad',36),(547,'Mahbubnagar',36),(548,'Mancherial',36),(549,'Medak',36),(550,'Medchal-Malkajgiri',36),(551,'Mulugu',36),(552,'Nalgonda',36),(553,'Narayanpet',36),(554,'Nagarkurnool',36),(555,'Nirmal',36),(556,'Nizamabad',36),(557,'Peddapalli',36),(558,'Rajanna Sircilla',36),(559,'Ranga Reddy',36),(560,'Sangareddy',36),(561,'Siddipet',36),(562,'Suryapet',36),(563,'Vikarabad',36),(564,'Wanaparthy',36),(565,'Warangal Urban',36),(566,'Warangal Rural',36),(567,'Yadadri Bhuvanagiri',36),(568,'Dhalai',16),(569,'Gomati',16),(570,'Khowai[14]',16),(571,'North Tripura',16),(572,'Sepahijala[15]',16),(573,'South Tripura',16),(574,'Unokoti[16]',16),(575,'West Tripura',16),(576,'Agra',9),(577,'Aligarh',9),(578,'Allahabad',9),(579,'Ambedkar Nagar',9),(580,'Amethi[17]',9),(581,'Amroha',9),(582,'Auraiya',9),(583,'Azamgarh',9),(584,'Bagpat',9),(585,'Bahraich',9),(586,'Ballia',9),(587,'Balrampur',9),(588,'Banda',9),(589,'Barabanki',9),(590,'Bareilly',9),(591,'Basti',9),(592,'Bhadohi',9),(593,'Bijnor',9),(594,'Budaun',9),(595,'Bulandshahr',9),(596,'Chandauli',9),(597,'Chitrakoot',9),(598,'Deoria',9),(599,'Etah',9),(600,'Etawah',9),(601,'Faizabad',9),(602,'Farrukhabad',9),(603,'Fatehpur',9),(604,'Firozabad',9),(605,'Gautam Buddh Nagar',9),(606,'Ghaziabad',9),(607,'Ghazipur',9),(608,'Gonda',9),(609,'Gorakhpur',9),(610,'Hamirpur',9),(611,'Hapur',9),(612,'Hardoi',9),(613,'Hathras',9),(614,'Jalaun',9),(615,'Jaunpur',9),(616,'Jhansi',9),(617,'Kannauj',9),(618,'Kanpur Dehat',9),(619,'Kanpur Nagar',9),(620,'Kasganj',9),(621,'Kaushambi',9),(622,'Kushinagar',9),(623,'Lakhimpur Kheri',9),(624,'Lalitpur',9),(625,'Lucknow',9),(626,'Maharajganj',9),(627,'Mahoba',9),(628,'Mainpuri',9),(629,'Mathura',9),(630,'Mau',9),(631,'Meerut',9),(632,'Mirzapur',9),(633,'Moradabad',9),(634,'Muzaffarnagar',9),(635,'Pilibhit',9),(636,'Pratapgarh',9),(637,'Raebareli',9),(638,'Rampur',9),(639,'Saharanpur',9),(640,'Sambhal',9),(641,'Sant Kabir Nagar',9),(642,'Shahjahanpur',9),(643,'Shamli[18]',9),(644,'Shravasti',9),(645,'Siddharthnagar',9),(646,'Sitapur',9),(647,'Sonbhadra',9),(648,'Sultanpur',9),(649,'Unnao',9),(650,'Varanasi',9),(651,'Almora',5),(652,'Bageshwar',5),(653,'Chamoli',5),(654,'Champawat',5),(655,'Dehradun',5),(656,'Haridwar',5),(657,'Nainital',5),(658,'Pauri Garhwal',5),(659,'Pithoragarh',5),(660,'Rudraprayag',5),(661,'Tehri Garhwal',5),(662,'Udham Singh Nagar',5),(663,'Uttarkashi',5),(664,'Alipurduar',19),(665,'Bankura',19),(666,'Paschim Bardhaman',19),(667,'Purba Bardhaman',19),(668,'Birbhum',19),(669,'Cooch Behar',19),(670,'Dakshin Dinajpur',19),(671,'Darjeeling',19),(672,'Hooghly',19),(673,'Howrah',19),(674,'Jalpaiguri',19),(675,'Jhargram',19),(676,'Kalimpong',19),(677,'Kolkata',19),(678,'Maldah',19),(679,'Murshidabad',19),(680,'Nadia',19),(681,'North 24 Parganas',19),(682,'Paschim Medinipur',19),(683,'Purba Medinipur',19),(684,'Purulia',19),(685,'South 24 Parganas',19),(686,'Uttar Dinajpur',19),(687,'Nicobar',35),(688,'North and Middle Andaman',35),(689,'South Andaman',35),(690,'Chandigarh',4),(691,'Dadra and Nagar Haveli',26),(692,'Daman',25),(693,'Diu',25),(694,'Anantnag',1),(695,'Bandipora',1),(696,'Baramulla',1),(697,'Badgam',1),(698,'Doda',1),(699,'Ganderbal',1),(700,'Jammu',1),(701,'Kathua',1),(702,'Kishtwar',1),(703,'Kulgam',1),(704,'Kupwara',1),(705,'Poonch',1),(706,'Pulwama',1),(707,'Rajouri',1),(708,'Ramban',1),(709,'Reasi',1),(710,'Samba',1),(711,'Shopian',1),(712,'Srinagar',1),(713,'Udhampur',1),(714,'Kargil',37),(715,'Leh',37),(716,'Lakshadweep',31),(717,'Central Delhi',7),(718,'East Delhi',7),(719,'New Delhi',7),(720,'North Delhi',7),(721,'North East Delhi',7),(722,'North West Delhi',7),(723,'Shahdara',7),(724,'South Delhi',7),(725,'South East Delhi',7),(726,'South West Delhi',7),(727,'West Delhi',7),(728,'Karaikal',34),(729,'Mahé',34),(730,'Pondicherry',34),(731,'Yanam',34);
/*!40000 ALTER TABLE `master_forms_district` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_gender`
--

DROP TABLE IF EXISTS `master_forms_gender`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_gender` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `gender` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_gender`
--

LOCK TABLES `master_forms_gender` WRITE;
/*!40000 ALTER TABLE `master_forms_gender` DISABLE KEYS */;
INSERT INTO `master_forms_gender` VALUES (1,'Male'),(2,'Female'),(3,'Transgender');
/*!40000 ALTER TABLE `master_forms_gender` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_lecture`
--

DROP TABLE IF EXISTS `master_forms_lecture`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_lecture` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `lecture` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_lecture`
--

LOCK TABLES `master_forms_lecture` WRITE;
/*!40000 ALTER TABLE `master_forms_lecture` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_forms_lecture` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_module`
--

DROP TABLE IF EXISTS `master_forms_module`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_module` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `module_name` varchar(100) DEFAULT NULL,
  `module_url` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_module`
--

LOCK TABLES `master_forms_module` WRITE;
/*!40000 ALTER TABLE `master_forms_module` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_forms_module` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_mothertongue`
--

DROP TABLE IF EXISTS `master_forms_mothertongue`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_mothertongue` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `mother_tongue` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_mothertongue`
--

LOCK TABLES `master_forms_mothertongue` WRITE;
/*!40000 ALTER TABLE `master_forms_mothertongue` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_forms_mothertongue` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_nationality`
--

DROP TABLE IF EXISTS `master_forms_nationality`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_nationality` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `nationality` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_nationality`
--

LOCK TABLES `master_forms_nationality` WRITE;
/*!40000 ALTER TABLE `master_forms_nationality` DISABLE KEYS */;
INSERT INTO `master_forms_nationality` VALUES (1,'Indian'),(2,'Other');
/*!40000 ALTER TABLE `master_forms_nationality` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_physicallychallenged`
--

DROP TABLE IF EXISTS `master_forms_physicallychallenged`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_physicallychallenged` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `physically_challenged` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_physicallychallenged`
--

LOCK TABLES `master_forms_physicallychallenged` WRITE;
/*!40000 ALTER TABLE `master_forms_physicallychallenged` DISABLE KEYS */;
INSERT INTO `master_forms_physicallychallenged` VALUES (1,'A'),(2,'B'),(3,'C');
/*!40000 ALTER TABLE `master_forms_physicallychallenged` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_postalcode`
--

DROP TABLE IF EXISTS `master_forms_postalcode`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_postalcode` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `postal_code` varchar(30) DEFAULT NULL,
  `fk_city_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `master_forms_postalc_fk_city_id_2824d8e0_fk_master_fo` (`fk_city_id`),
  CONSTRAINT `master_forms_postalc_fk_city_id_2824d8e0_fk_master_fo` FOREIGN KEY (`fk_city_id`) REFERENCES `master_forms_city` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_postalcode`
--

LOCK TABLES `master_forms_postalcode` WRITE;
/*!40000 ALTER TABLE `master_forms_postalcode` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_forms_postalcode` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_religion`
--

DROP TABLE IF EXISTS `master_forms_religion`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_religion` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `religion` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_religion`
--

LOCK TABLES `master_forms_religion` WRITE;
/*!40000 ALTER TABLE `master_forms_religion` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_forms_religion` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_reserved`
--

DROP TABLE IF EXISTS `master_forms_reserved`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_reserved` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `reserved` varchar(50) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_reserved`
--

LOCK TABLES `master_forms_reserved` WRITE;
/*!40000 ALTER TABLE `master_forms_reserved` DISABLE KEYS */;
INSERT INTO `master_forms_reserved` VALUES (1,'SC'),(2,'ST'),(3,'DT(A)'),(4,'NT(B)'),(5,'NT(C)'),(6,'NT(D)');
/*!40000 ALTER TABLE `master_forms_reserved` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_screen`
--

DROP TABLE IF EXISTS `master_forms_screen`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_screen` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `screen_name` varchar(100) DEFAULT NULL,
  `screen_url` varchar(100) DEFAULT NULL,
  `fk_module_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `master_forms_screen_fk_module_id_a0dd4ce8_fk_master_fo` (`fk_module_id`),
  CONSTRAINT `master_forms_screen_fk_module_id_a0dd4ce8_fk_master_fo` FOREIGN KEY (`fk_module_id`) REFERENCES `master_forms_module` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_screen`
--

LOCK TABLES `master_forms_screen` WRITE;
/*!40000 ALTER TABLE `master_forms_screen` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_forms_screen` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_section`
--

DROP TABLE IF EXISTS `master_forms_section`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_section` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sections` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_section`
--

LOCK TABLES `master_forms_section` WRITE;
/*!40000 ALTER TABLE `master_forms_section` DISABLE KEYS */;
INSERT INTO `master_forms_section` VALUES (1,'A'),(2,'B'),(3,'C');
/*!40000 ALTER TABLE `master_forms_section` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_semester`
--

DROP TABLE IF EXISTS `master_forms_semester`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_semester` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `semester` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_semester`
--

LOCK TABLES `master_forms_semester` WRITE;
/*!40000 ALTER TABLE `master_forms_semester` DISABLE KEYS */;
INSERT INTO `master_forms_semester` VALUES (1,'I'),(2,'II'),(3,'III'),(4,'IV'),(5,'V'),(6,'VI');
/*!40000 ALTER TABLE `master_forms_semester` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_state`
--

DROP TABLE IF EXISTS `master_forms_state`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_state` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `state` varchar(30) DEFAULT NULL,
  `fk_nationality_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `master_forms_state_fk_nationality_id_3c0b8a99_fk_master_fo` (`fk_nationality_id`),
  CONSTRAINT `master_forms_state_fk_nationality_id_3c0b8a99_fk_master_fo` FOREIGN KEY (`fk_nationality_id`) REFERENCES `master_forms_nationality` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=38 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_state`
--

LOCK TABLES `master_forms_state` WRITE;
/*!40000 ALTER TABLE `master_forms_state` DISABLE KEYS */;
INSERT INTO `master_forms_state` VALUES (1,'Jammu & Kashmir',NULL),(2,'Himachal Pradesh',NULL),(3,'Punjab',NULL),(4,'Chandigarh',NULL),(5,'Uttarakhand',NULL),(6,'Haryana',NULL),(7,'Delhi',NULL),(8,'Rajasthan',NULL),(9,'Uttar Pradesh',NULL),(10,'Bihar',NULL),(11,'Sikkim',NULL),(12,'Arunachal Pradesh',NULL),(13,'Nagaland',NULL),(14,'Manipur',NULL),(15,'Mizoram',NULL),(16,'Tripura',NULL),(17,'Meghalaya',NULL),(18,'Assam',NULL),(19,'West Bengal',NULL),(20,'Jharkhand',NULL),(21,'Odisha',NULL),(22,'Chhattisgarh',NULL),(23,'Madhya Pradesh',NULL),(24,'Gujarat',NULL),(25,'Daman & Diu',NULL),(26,'Dadra & Nagar Haveli',NULL),(27,'Maharashtra',NULL),(28,'Andhra Pradesh',NULL),(29,'Karnataka',NULL),(30,'Goa',NULL),(31,'Lakshadweep',NULL),(32,'Kerala',NULL),(33,'Tamil Nadu',NULL),(34,'Puducherry',NULL),(35,'Andaman & Nicobar Islands',NULL),(36,'Telengana',NULL),(37,'Ladakh',NULL);
/*!40000 ALTER TABLE `master_forms_state` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_streamorfield`
--

DROP TABLE IF EXISTS `master_forms_streamorfield`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_streamorfield` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `stream_or_field_name` varchar(100) DEFAULT NULL,
  `fk_twelveth_or_diploma_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `master_forms_streamo_fk_twelveth_or_diplo_4d9f8c83_fk_master_fo` (`fk_twelveth_or_diploma_id`),
  CONSTRAINT `master_forms_streamo_fk_twelveth_or_diplo_4d9f8c83_fk_master_fo` FOREIGN KEY (`fk_twelveth_or_diploma_id`) REFERENCES `master_forms_twelvethordiploma` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=7 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_streamorfield`
--

LOCK TABLES `master_forms_streamorfield` WRITE;
/*!40000 ALTER TABLE `master_forms_streamorfield` DISABLE KEYS */;
INSERT INTO `master_forms_streamorfield` VALUES (1,'Computer Technology',1),(2,'Informaction Science & Engineering',1),(3,'Mechanical Engineering',1),(4,'Electrical & Electronics Engineering',1),(5,'Arts',2),(6,'Science',2);
/*!40000 ALTER TABLE `master_forms_streamorfield` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_subcast`
--

DROP TABLE IF EXISTS `master_forms_subcast`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_subcast` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `sub_cast` varchar(50) DEFAULT NULL,
  `fk_cast_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `master_forms_subcast_fk_cast_id_a970cff4_fk_master_forms_cast_id` (`fk_cast_id`),
  CONSTRAINT `master_forms_subcast_fk_cast_id_a970cff4_fk_master_forms_cast_id` FOREIGN KEY (`fk_cast_id`) REFERENCES `master_forms_cast` (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=9 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_subcast`
--

LOCK TABLES `master_forms_subcast` WRITE;
/*!40000 ALTER TABLE `master_forms_subcast` DISABLE KEYS */;
INSERT INTO `master_forms_subcast` VALUES (1,'A',1),(2,'B',1),(3,'A',2),(4,'B',2),(5,'A',3),(6,'B',3),(7,'A',4),(8,'B',4);
/*!40000 ALTER TABLE `master_forms_subcast` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_subject`
--

DROP TABLE IF EXISTS `master_forms_subject`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_subject` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `subjects` varchar(100) DEFAULT NULL,
  `compulsory_attendance` varchar(5) DEFAULT NULL,
  `fk_course_id` int(11) DEFAULT NULL,
  `fk_semesters_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `master_forms_subject_fk_course_id_62860505_fk_master_fo` (`fk_course_id`),
  KEY `master_forms_subject_fk_semesters_id_ef5a2700_fk_master_fo` (`fk_semesters_id`),
  CONSTRAINT `master_forms_subject_fk_course_id_62860505_fk_master_fo` FOREIGN KEY (`fk_course_id`) REFERENCES `master_forms_course` (`id`),
  CONSTRAINT `master_forms_subject_fk_semesters_id_ef5a2700_fk_master_fo` FOREIGN KEY (`fk_semesters_id`) REFERENCES `master_forms_semester` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_subject`
--

LOCK TABLES `master_forms_subject` WRITE;
/*!40000 ALTER TABLE `master_forms_subject` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_forms_subject` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_tehsil`
--

DROP TABLE IF EXISTS `master_forms_tehsil`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_tehsil` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tehsil` varchar(30) DEFAULT NULL,
  `fk_state_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `master_forms_tehsil_fk_state_id_afe78b2d_fk_master_fo` (`fk_state_id`),
  CONSTRAINT `master_forms_tehsil_fk_state_id_afe78b2d_fk_master_fo` FOREIGN KEY (`fk_state_id`) REFERENCES `master_forms_state` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_tehsil`
--

LOCK TABLES `master_forms_tehsil` WRITE;
/*!40000 ALTER TABLE `master_forms_tehsil` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_forms_tehsil` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_time`
--

DROP TABLE IF EXISTS `master_forms_time`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_time` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `time` time(6) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_time`
--

LOCK TABLES `master_forms_time` WRITE;
/*!40000 ALTER TABLE `master_forms_time` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_forms_time` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_twelvethordiploma`
--

DROP TABLE IF EXISTS `master_forms_twelvethordiploma`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_twelvethordiploma` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `twelveth_or_diploma` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_twelvethordiploma`
--

LOCK TABLES `master_forms_twelvethordiploma` WRITE;
/*!40000 ALTER TABLE `master_forms_twelvethordiploma` DISABLE KEYS */;
INSERT INTO `master_forms_twelvethordiploma` VALUES (1,'Diploma'),(2,'Twelveth');
/*!40000 ALTER TABLE `master_forms_twelvethordiploma` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_useroperation`
--

DROP TABLE IF EXISTS `master_forms_useroperation`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_useroperation` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `status` varchar(50) DEFAULT NULL,
  `special_data` varchar(50) DEFAULT NULL,
  `view_data` varchar(50) DEFAULT NULL,
  `edit_data` varchar(50) DEFAULT NULL,
  `save_data` varchar(50) DEFAULT NULL,
  `delete_data` varchar(50) DEFAULT NULL,
  `fk_module_id` int(11) DEFAULT NULL,
  `fk_screen_id` int(11) DEFAULT NULL,
  `fk_user_role_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `master_forms_userope_fk_module_id_6112d7f3_fk_master_fo` (`fk_module_id`),
  KEY `master_forms_userope_fk_screen_id_1321cdfb_fk_master_fo` (`fk_screen_id`),
  KEY `master_forms_userope_fk_user_role_id_9bfa238a_fk_master_fo` (`fk_user_role_id`),
  CONSTRAINT `master_forms_userope_fk_module_id_6112d7f3_fk_master_fo` FOREIGN KEY (`fk_module_id`) REFERENCES `master_forms_module` (`id`),
  CONSTRAINT `master_forms_userope_fk_screen_id_1321cdfb_fk_master_fo` FOREIGN KEY (`fk_screen_id`) REFERENCES `master_forms_screen` (`id`),
  CONSTRAINT `master_forms_userope_fk_user_role_id_9bfa238a_fk_master_fo` FOREIGN KEY (`fk_user_role_id`) REFERENCES `master_forms_userrole` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_useroperation`
--

LOCK TABLES `master_forms_useroperation` WRITE;
/*!40000 ALTER TABLE `master_forms_useroperation` DISABLE KEYS */;
/*!40000 ALTER TABLE `master_forms_useroperation` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_userrole`
--

DROP TABLE IF EXISTS `master_forms_userrole`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_userrole` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_role` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_userrole`
--

LOCK TABLES `master_forms_userrole` WRITE;
/*!40000 ALTER TABLE `master_forms_userrole` DISABLE KEYS */;
INSERT INTO `master_forms_userrole` VALUES (1,'Faculty');
/*!40000 ALTER TABLE `master_forms_userrole` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_usertype`
--

DROP TABLE IF EXISTS `master_forms_usertype`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_usertype` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_type` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_usertype`
--

LOCK TABLES `master_forms_usertype` WRITE;
/*!40000 ALTER TABLE `master_forms_usertype` DISABLE KEYS */;
INSERT INTO `master_forms_usertype` VALUES (1,'Student'),(2,'Faculty');
/*!40000 ALTER TABLE `master_forms_usertype` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Table structure for table `master_forms_yearofadmission`
--

DROP TABLE IF EXISTS `master_forms_yearofadmission`;
/*!40101 SET @saved_cs_client     = @@character_set_client */;
/*!50503 SET character_set_client = utf8mb4 */;
CREATE TABLE `master_forms_yearofadmission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `year_of_admission` varchar(30) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB AUTO_INCREMENT=4 DEFAULT CHARSET=latin1;
/*!40101 SET character_set_client = @saved_cs_client */;

--
-- Dumping data for table `master_forms_yearofadmission`
--

LOCK TABLES `master_forms_yearofadmission` WRITE;
/*!40000 ALTER TABLE `master_forms_yearofadmission` DISABLE KEYS */;
INSERT INTO `master_forms_yearofadmission` VALUES (1,'2017'),(2,'2018'),(3,'2019');
/*!40000 ALTER TABLE `master_forms_yearofadmission` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2020-01-06 12:16:07
