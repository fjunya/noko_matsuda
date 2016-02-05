-- MySQL dump 10.13  Distrib 5.5.35, for Linux (x86_64)
--
-- Host: localhost    Database: stormy_sapphire
-- ------------------------------------------------------
-- Server version	5.5.35-log

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
-- Dumping data for table `account`
--

LOCK TABLES `account` WRITE;
/*!40000 ALTER TABLE `account` DISABLE KEYS */;
INSERT INTO `account` VALUES (1,'','03-1111-3333','',NULL,NULL,1,NULL,1,'2015-12-19 23:00:00','2016-01-03 06:01:00',1),(2,'','03-2222-3333','',NULL,NULL,1,NULL,1,'2015-12-19 23:00:00','2015-12-28 02:06:17',2),(5,'テスト部署','123-456-789','テスト説明','2015-12-24 00:00:00','2016-04-04 00:00:00',0,NULL,1,'2015-12-20 03:51:41','2015-12-21 14:41:11',24),(6,'テスト部署','123-456-784','テスト説明',NULL,NULL,1,NULL,1,'2015-12-20 03:53:26','2015-12-27 22:44:51',25),(7,'テスト部署','123-456-789','テスト説明',NULL,NULL,1,NULL,1,'2015-12-20 04:08:53','2015-12-28 02:06:46',26),(14,'','','',NULL,NULL,1,NULL,1,'2015-12-21 05:18:02','2015-12-21 05:18:02',33);
/*!40000 ALTER TABLE `account` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `account_account_groups`
--

LOCK TABLES `account_account_groups` WRITE;
/*!40000 ALTER TABLE `account_account_groups` DISABLE KEYS */;
INSERT INTO `account_account_groups` VALUES (35,1,6),(30,2,5),(24,5,3),(25,6,5),(33,7,3),(32,7,5),(22,14,3);
/*!40000 ALTER TABLE `account_account_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `account_group`
--

LOCK TABLES `account_group` WRITE;
/*!40000 ALTER TABLE `account_group` DISABLE KEYS */;
INSERT INTO `account_group` VALUES (3,'テストグループ1','テスト説明'),(5,'テストグループ2','テスト説明'),(6,'テストグループ3','テスト説明');
/*!40000 ALTER TABLE `account_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group`
--

LOCK TABLES `auth_group` WRITE;
/*!40000 ALTER TABLE `auth_group` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_group_permissions`
--

LOCK TABLES `auth_group_permissions` WRITE;
/*!40000 ALTER TABLE `auth_group_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_group_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_permission`
--

LOCK TABLES `auth_permission` WRITE;
/*!40000 ALTER TABLE `auth_permission` DISABLE KEYS */;
INSERT INTO `auth_permission` VALUES (1,'Can add log entry',1,'add_logentry'),(2,'Can change log entry',1,'change_logentry'),(3,'Can delete log entry',1,'delete_logentry'),(4,'Can add permission',2,'add_permission'),(5,'Can change permission',2,'change_permission'),(6,'Can delete permission',2,'delete_permission'),(7,'Can add group',3,'add_group'),(8,'Can change group',3,'change_group'),(9,'Can delete group',3,'delete_group'),(10,'Can add user',4,'add_user'),(11,'Can change user',4,'change_user'),(12,'Can delete user',4,'delete_user'),(13,'Can add content type',5,'add_contenttype'),(14,'Can change content type',5,'change_contenttype'),(15,'Can delete content type',5,'delete_contenttype'),(16,'Can add session',6,'add_session'),(17,'Can change session',6,'change_session'),(18,'Can delete session',6,'delete_session'),(19,'Can add account group',7,'add_accountgroup'),(20,'Can change account group',7,'change_accountgroup'),(21,'Can delete account group',7,'delete_accountgroup'),(22,'Can add account',8,'add_account'),(23,'Can change account',8,'change_account'),(24,'Can delete account',8,'delete_account'),(25,'Can add information',9,'add_information'),(26,'Can change information',9,'change_information'),(27,'Can delete information',9,'delete_information'),(28,'Can add participant',10,'add_participant'),(29,'Can change participant',10,'change_participant'),(30,'Can delete participant',10,'delete_participant'),(31,'Can add participant group',11,'add_participantgroup'),(32,'Can change participant group',11,'change_participantgroup'),(33,'Can delete participant group',11,'delete_participantgroup'),(34,'Can add recurrence pattern',12,'add_recurrencepattern'),(35,'Can change recurrence pattern',12,'change_recurrencepattern'),(36,'Can delete recurrence pattern',12,'delete_recurrencepattern'),(37,'Can add tms user',13,'add_tmsuser'),(38,'Can change tms user',13,'change_tmsuser'),(39,'Can delete tms user',13,'delete_tmsuser'),(40,'Can add conference',14,'add_conference'),(41,'Can change conference',14,'change_conference'),(42,'Can delete conference',14,'delete_conference'),(43,'Can add resource',15,'add_resource'),(44,'Can change resource',15,'change_resource'),(45,'Can delete resource',15,'delete_resource');
/*!40000 ALTER TABLE `auth_permission` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user`
--

LOCK TABLES `auth_user` WRITE;
/*!40000 ALTER TABLE `auth_user` DISABLE KEYS */;
INSERT INTO `auth_user` VALUES (1,'pbkdf2_sha256$20000$XPSmfvLwxzBw$kA5ePsCzyotKtOwlGjU36KCFsSqWd9Y/Wu8t9pn7uJE=','2016-01-03 06:01:29',1,'papp','admin','papp','admin@papp.com',1,1,'2015-12-04 19:12:23'),(2,'pbkdf2_sha256$20000$D97Fqyle3pSM$AYYXVhKRIVaRAdfrpDrVjALQxkVZAO0ZuLl54TVMuu4=',NULL,0,'mazda0','shuu','mazda','nint@gmail.com',1,1,'2015-12-04 19:14:08'),(24,'pbkdf2_sha256$20000$1qzTcuwm3mQV$5F6DKjKHWUMyM7oH3vcaUPYGixRQQ4RbDMKRiW9BoRQ=','2016-01-03 05:54:20',0,'mazda1','shuu','mazda','nint@gmail.com',1,1,'2015-12-20 03:51:41'),(25,'pbkdf2_sha256$20000$MZxhpIoOQbmK$2kRwdu8uzGWVbJlOjB4wPNlh2nfqWBGHvXiHb49ljVQ=','2015-12-27 23:37:39',0,'mazda2','shuu','mazda','nint@gmail.com',0,1,'2015-12-20 03:53:26'),(26,'pbkdf2_sha256$20000$BKIdXA4x4bRL$4yPzwH87dZiicUAexBwiPTnbwXMkr75S8UQdzVUlXkY=','2015-12-20 06:09:23',0,'mazda3','shuu','mazda','nint@gmail.com',0,1,'2015-12-20 04:08:53'),(33,'pbkdf2_sha256$20000$xNhSlKxF1Jkq$AgZsEwhH/HrY1JmGBSZ4TetrxrBnJDaxxRXsBka7d5M=',NULL,0,'mazda4','shuu','mazda','nint@gmail.com',0,1,'2015-12-21 05:18:02');
/*!40000 ALTER TABLE `auth_user` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_groups`
--

LOCK TABLES `auth_user_groups` WRITE;
/*!40000 ALTER TABLE `auth_user_groups` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_groups` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `auth_user_user_permissions`
--

LOCK TABLES `auth_user_user_permissions` WRITE;
/*!40000 ALTER TABLE `auth_user_user_permissions` DISABLE KEYS */;
/*!40000 ALTER TABLE `auth_user_user_permissions` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `conference`
--

LOCK TABLES `conference` WRITE;
/*!40000 ALTER TABLE `conference` DISABLE KEYS */;
INSERT INTO `conference` VALUES (1,'111','分子生物資源特論（修士）','会議 ID 1','テスト　ユーザ','テスト部署','nint@gmail.com','111-222-3333','テスト説明','分子生物資源特論（修士）','2016-01-15 09:10:00','2016-01-15 09:50:00','1024','sharpness','h.263','0',NULL,'テストパスワード',1234,'テストパスワード',0,1,'','sameLayout',555,10,'','','','','','','','','','','','','','','','',0,5,2,NULL,NULL),(2,'222','【愛媛連大】中間発表会（植物生産学分野）','会議 ID 2','テスト　ユーザ','テスト部署','nint@gmail.com','111-222-3333','テスト説明','【愛媛連大】中間発表会（植物生産学分野）','2016-01-15 09:30:00','2016-01-15 10:10:00','1024','sharpness','h.263','1',NULL,'テストパスワード',1234,'テストパスワード',1,0,'','xxx',555,10,'','','','','','','','','','','','','','','','',0,25,24,NULL,NULL),(3,'333','【農工大・岩手大】馬臨床学','会議 ID 3','テスト　ユーザ','テスト部署','nint@gmail.com','111-222-3333','テスト説明','【農工大・岩手大】馬臨床学','2016-01-15 08:50:00','2016-01-15 09:30:00','1024','sharpness','h.263','1',NULL,'テストパスワード',1234,'テストパスワード',0,0,'','sameLayout',555,10,'','','','','','','','','','','','','','','','',0,28,24,NULL,NULL);
/*!40000 ALTER TABLE `conference` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `conference_participants`
--

LOCK TABLES `conference_participants` WRITE;
/*!40000 ALTER TABLE `conference_participants` DISABLE KEYS */;
INSERT INTO `conference_participants` VALUES (3,1,2),(1,1,3),(2,1,29),(4,2,7),(5,2,31),(6,2,61),(8,3,8),(7,3,14),(9,3,36);
/*!40000 ALTER TABLE `conference_participants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_admin_log`
--

LOCK TABLES `django_admin_log` WRITE;
/*!40000 ALTER TABLE `django_admin_log` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_admin_log` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_content_type`
--

LOCK TABLES `django_content_type` WRITE;
/*!40000 ALTER TABLE `django_content_type` DISABLE KEYS */;
INSERT INTO `django_content_type` VALUES (8,'account','account'),(7,'account','accountgroup'),(1,'admin','logentry'),(3,'auth','group'),(2,'auth','permission'),(4,'auth','user'),(5,'contenttypes','contenttype'),(9,'menu','information'),(10,'participant','participant'),(11,'participant','participantgroup'),(14,'reserve','conference'),(12,'reserve','recurrencepattern'),(15,'reserve','resource'),(13,'reserve','tmsuser'),(6,'sessions','session');
/*!40000 ALTER TABLE `django_content_type` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_migrations`
--

LOCK TABLES `django_migrations` WRITE;
/*!40000 ALTER TABLE `django_migrations` DISABLE KEYS */;
INSERT INTO `django_migrations` VALUES (1,'contenttypes','0001_initial','2016-01-03 00:20:13'),(2,'auth','0001_initial','2016-01-03 00:20:13'),(3,'account','0001_initial','2016-01-03 00:20:13'),(4,'admin','0001_initial','2016-01-03 00:20:14'),(5,'contenttypes','0002_remove_content_type_name','2016-01-03 00:20:14'),(6,'auth','0002_alter_permission_name_max_length','2016-01-03 00:20:14'),(7,'auth','0003_alter_user_email_max_length','2016-01-03 00:20:14'),(8,'auth','0004_alter_user_username_opts','2016-01-03 00:20:14'),(9,'auth','0005_alter_user_last_login_null','2016-01-03 00:20:14'),(10,'auth','0006_require_contenttypes_0002','2016-01-03 00:20:14'),(11,'menu','0001_initial','2016-01-03 00:20:14'),(12,'participant','0001_initial','2016-01-03 00:20:14'),(13,'reserve','0001_initial','2016-01-03 00:20:15'),(14,'sessions','0001_initial','2016-01-03 00:20:15');
/*!40000 ALTER TABLE `django_migrations` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `django_session`
--

LOCK TABLES `django_session` WRITE;
/*!40000 ALTER TABLE `django_session` DISABLE KEYS */;
/*!40000 ALTER TABLE `django_session` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `information`
--

LOCK TABLES `information` WRITE;
/*!40000 ALTER TABLE `information` DISABLE KEYS */;
INSERT INTO `information` VALUES (1,'http://165.93.50.42/が予約サーバ本体のURLです。<br>\ndummyを追加する場合には、最後に選択してください。',1,'2015-12-22 00:00:00',1),(2,'<a href=\"http://165.93.50.42/\">http://165.93.50.42/</a>が予約サーバ本体のURLです。<br>\r\ndummyを追加する場合には、最後に選択してください。',1,'2015-12-30 03:28:27',24);
/*!40000 ALTER TABLE `information` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `participant`
--

LOCK TABLES `participant` WRITE;
/*!40000 ALTER TABLE `participant` DISABLE KEYS */;
INSERT INTO `participant` VALUES (1,'01.帯広畜産大学','dial_out','h323',NULL,'auto','158.208.128.180','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(2,'02.弘前大学','dial_out','h323',NULL,'auto','133.60.141.226','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(3,'03.岩手大学　連合','dial_out','h323',NULL,'auto','160.29.40.1','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(4,'04.山形大学','dial_out','h323',NULL,'auto','133.24.225.34','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(5,'05.茨城大学','dial_out','h323',NULL,'auto','157.80.80.192','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(6,'06.宇都宮大学','dial_out','h323',NULL,'auto','160.12.178.21','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(7,'07.東京農工大学　府中本部','dial_out','h323',NULL,'auto','165.93.79.11','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(8,'08.東京農工大学　府中連合','dial_out','h323',NULL,'auto','165.93.79.19','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(9,'09.東京農工大学　小金井中央棟5階','dial_out','h323',NULL,'auto','165.93.79.27','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(10,'10.東京農工大学　小金井8号館K3D','dial_out','h323',NULL,'auto','165.93.79.35','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(11,'11.静岡大学','dial_out','h323',NULL,'auto','133.70.4.25','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(12,'12.岐阜大学','dial_out','h323',NULL,'auto','133.66.52.200','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(13,'13.鳥取大学','dial_out','h323',NULL,'auto','160.15.19.2','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(14,'14.島根大学','dial_out','h323',NULL,'auto','192.244.211.176','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(15,'15.山口大学','dial_out','h323',NULL,'auto','133.62.227.194','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(16,'16.香川大学','dial_out','h323',NULL,'auto','133.92.112.76','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(17,'17.愛媛大学　連合','dial_out','h323',NULL,'auto','133.71.241.111','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(18,'18.愛媛大学　大講義室','dial_out','h323',NULL,'auto','133.71.241.121','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(19,'19.高知大学','dial_out','h323',NULL,'auto','133.97.251.10','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(20,'20.佐賀大学','dial_out','h323',NULL,'auto','133.49.76.241','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(21,'21.鹿児島大学　連合','dial_out','h323',NULL,'auto','163.209.56.1','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(22,'22.鹿児島大学　水産学部','dial_out','h323',NULL,'auto','163.209.56.11','','','323_id','','uri_type','none','hdx8000','2.5',0,'2014-05-28 IP変更tobi old=57.5'),(23,'23.琉球大学','dial_out','h323',NULL,'auto','133.13.98.11','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(24,'24.農工大　小金井11号多目的','dial_out','h323',NULL,'auto','165.93.79.102','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(25,'25.農工大　小金井L1321','dial_out','h323',NULL,'auto','165.93.79.84','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(26,'26.農工大　小金井 L1331','dial_out','h323',NULL,'auto','165.93.79.93','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(27,'27.農工大　小金井 L0111','dial_out','h323',NULL,'auto','165.93.79.64','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(28,'28.農工大　小金井 L0026','dial_out','h323',NULL,'auto','165.93.79.75','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(29,'29.農工大　府中本館講堂','dial_out','h323',NULL,'auto','165.93.79.43','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(30,'30.農工大　府中25番教室','dial_out','h323',NULL,'auto','165.93.79.53','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(31,'31.農工大　小金井中央棟 中会議','dial_out','h323',NULL,'auto','165.93.79.118','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(32,'32.農工大　小金井BASE専攻長室','dial_out','h323',NULL,'auto','165.93.79.125','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(33,'33.農工大　府中本館第２会議室','dial_out','h323',NULL,'auto','165.93.79.111','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(34,'34.農工大　小金井8号館K5A-Polycom','dial_out','h323',NULL,'auto','165.93.79.132','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(35,'35.農工大　府中学務教育支援室１','dial_out','h323',NULL,'auto','165.93.79.139','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(36,'36.農工大　小金井中央棟2F会議室','dial_out','h323',NULL,'auto','165.93.79.145','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(37,'37.農工大　小金井8号館K5A-Sonyテスト','dial_out','h323',NULL,'auto','165.93.79.154','','','323_id','','uri_type','none','other_sd','',0,''),(38,'38.香川大学 BW106','dial_out','h323',NULL,'auto','133.92.113.151','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(39,'39.農工大　小金井8号館K3A','dial_out','h323',NULL,'auto','165.93.79.177','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(40,'40.農工大　府中遠隔講義室F2B','dial_out','h323',NULL,'auto','165.93.79.198','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(41,'41.岩手大学生命系_遠隔講義室','dial_out','h323',NULL,'auto','160.29.40.17','','','323_id','','uri_type','none','hdx8000','2.5',0,''),(42,'42.農工大　府中新4号館32番教室','dial_out','h323',NULL,'auto','165.93.79.219','','','323_id','','uri_type','none','hdx8000','2.5',0,'2013-0316追加tob'),(43,'43.岩手大学　農学部７番講義室','dial_out','h323',NULL,'auto','160.29.40.33','','','323_id','','uri_type','none','hdx8000','2.5',0,'2013-0316追加tob'),(44,'44.岩手大学　動物病院　実習室３','dial_out','h323',NULL,'auto','160.29.40.49','','','323_id','','uri_type','none','hdx8000','2.5',0,'2013-0927追加tobi'),(45,'45.岩手大学 産業動物診療棟遠隔講義室','dial_out','h323',NULL,'auto','160.29.40.65','','','323_id','','uri_type','none','hdx8000','2.5',0,'2014-03-19追加tobi'),(46,'46.農工大 府中　第1講義棟22番教室','dial_out','h323',NULL,'auto','165.93.79.227','','','323_id','','uri_type','none','hdx8000','2.5',0,'2014-03-19追加tobi'),(47,'47.農工大 府中　第1講義棟23番教室','dial_out','h323',NULL,'auto','165.93.79.235','','','323_id','','uri_type','none','hdx8000','2.5',0,'2014-03-19追加tobi'),(48,'KEIO-SFC-RMX2000','dial_in','h323',NULL,'auto','133.27.177.200','','','323_id','','uri_type','none','other_hd','',0,'慶應大SFC RMX-2000カスケード'),(49,'Polycom_TestSite','dial_out','h323',384,'auto','140.242.250.200','','','323_id','','uri_type','none','','',0,''),(50,'dummy100','dial_in','h323',NULL,'auto','172.24.0.100','','','323_id','','uri_type','none','','',0,''),(51,'dummy101','dial_in','h323',NULL,'auto','172.24.0.101','','','323_id','','uri_type','none','','',0,''),(52,'dummy102','dial_in','h323',NULL,'auto','172.24.0.102','','','323_id','','uri_type','none','','',0,''),(53,'dummy103','dial_in','h323',NULL,'auto','172.24.0.103','','','323_id','','uri_type','none','','',0,''),(54,'dummy104','dial_in','h323',NULL,'auto','172.24.0.104','','','323_id','','uri_type','none','','',0,''),(55,'dummy105','dial_in','h323',NULL,'auto','172.24.0.105','','','323_id','','uri_type','none','','',0,''),(56,'dummy106','dial_in','h323',NULL,'auto','172.24.0.106','','','323_id','','uri_type','none','','',0,''),(57,'dummy107','dial_in','h323',NULL,'auto','172.24.0.107','','','323_id','','uri_type','none','','',0,''),(58,'dummy108','dial_in','h323',NULL,'auto','172.24.0.108','','','323_id','','uri_type','none','','',0,''),(59,'dummy109','dial_in','h323',NULL,'auto','172.24.0.109','','','323_id','','uri_type','none','','',0,''),(60,'dummy110','dial_in','h323',NULL,'auto','172.24.0.110','','','323_id','','uri_type','none','','',0,''),(61,'dummy111','dial_in','h323',NULL,'auto','172.24.0.111','','','323_id','','uri_type','none','','',0,''),(62,'dummy112','dial_in','h323',NULL,'auto','172.24.0.112','','','323_id','','uri_type','none','','',0,''),(63,'dummy113','dial_in','h323',NULL,'auto','172.24.0.113','','','323_id','','uri_type','none','','',0,''),(64,'dummy114','dial_in','h323',NULL,'auto','172.24.0.114','','','323_id','','uri_type','none','','',0,''),(65,'dummy115','dial_in','h323',NULL,'auto','172.24.0.115','','','323_id','','uri_type','none','','',0,''),(66,'dummy116','dial_in','h323',NULL,'auto','172.24.0.116','','','323_id','','uri_type','none','','',0,''),(67,'dummy117','dial_in','h323',NULL,'auto','172.24.0.117','','','323_id','','uri_type','none','','',0,''),(68,'dummy118','dial_in','h323',NULL,'auto','172.24.0.118','','','323_id','','uri_type','none','','',0,''),(69,'dummy119','dial_in','h323',NULL,'auto','172.24.0.119','','','323_id','','uri_type','none','','',0,''),(70,'mazda test','dial_in','h323',1920,'h264','127.0.0.1','111222333','xxxx','email_id','yyy','uri_type','none','hdx7000','1.0',1,'説明'),(71,'農工大　府中　新2号館2階-Codec','dial_out','h323',NULL,'auto','165.93.79.159','','','323_id','','uri_type','none','','',0,'Codec Only (Sony)'),(72,'農工大　府中新2号館1F会議室','dial_out','h323',NULL,'auto','165.93.79.173','','','323_id','','uri_type','none','','',0,'Codec Only (Polycom) 状態不明'),(73,'農工大　府中新2号館4Fゼミ室','dial_out','h323',NULL,'auto','165.93.79.174','','','323_id','','uri_type','none','','',0,'Codec Only (Sony) 状態不明'),(74,'農工大　府中新2号館5F学科長室','dial_out','h323',NULL,'auto','165.93.79.175','','','323_id','','uri_type','none','','',0,'Codec Only (Polycom) 状態不明'),(75,'農工大　本部情報係-テスト','dial_out','h323',NULL,'auto','165.93.79.161','','','323_id','','uri_type','none','','',0,'Codec Only (Sony)'),(76,'農工大　８号館K5D-Polycom','dial_out','h323',NULL,'auto','165.93.79.151','','','323_id','','uri_type','none','','',0,'Codec Only (Polycom)'),(77,'農工大　８号館テストSONY','dial_out','h323',NULL,'auto','165.93.79.176','','','323_id','','uri_type','none','','',0,'Codec Only (Sony)-hagi');
/*!40000 ALTER TABLE `participant` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `participant_group`
--

LOCK TABLES `participant_group` WRITE;
/*!40000 ALTER TABLE `participant_group` DISABLE KEYS */;
INSERT INTO `participant_group` VALUES (2,'01.Ｉwate-ren','岩手大学連合農学研究科'),(3,'02.Noko-u-ren','東京農工大学連合農学研究科'),(4,'03.Gihu-ren','岐阜大学連合農学研究科'),(5,'04.Tottori-ren','鳥取大学連合農学研究科'),(6,'05.Ehime-ren','愛媛大学連合農学研究科'),(7,'06.kagosima-ren','鹿児島大学連合農学研究科'),(8,'08.全拠点（連合農学）','連合農学研究科全拠点'),(9,'09.TUAT','東京農工大学内'),(10,'10.Ehime','愛媛大学内'),(11,'11.Kagoshima','鹿児島大学内'),(12,'12.Reserved','テスト中'),(13,'99.dummy00','ダミー端末（外部接続のリソース確保）'),(14,'99.dummy01','ダミー端末（外部接続のリソース確保）');
/*!40000 ALTER TABLE `participant_group` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `participant_group_participants`
--

LOCK TABLES `participant_group_participants` WRITE;
/*!40000 ALTER TABLE `participant_group_participants` DISABLE KEYS */;
INSERT INTO `participant_group_participants` VALUES (1,2,1),(2,2,2),(3,2,3),(4,2,4),(5,3,5),(6,3,6),(7,3,8),(8,4,11),(9,4,12),(10,5,13),(11,5,14),(12,5,15),(13,6,16),(14,6,17),(15,6,19),(16,7,20),(17,7,21),(18,7,22),(19,7,23),(20,8,1),(21,8,2),(22,8,3),(23,8,4),(24,8,5),(25,8,6),(26,8,8),(27,8,11),(28,8,12),(29,8,13),(30,8,14),(31,8,15),(32,8,16),(33,8,17),(34,8,19),(35,8,20),(36,8,21),(37,8,22),(38,8,23),(39,9,7),(40,9,8),(41,9,9),(42,9,10),(43,9,24),(44,9,25),(45,9,26),(46,9,27),(47,9,28),(48,9,29),(49,9,30),(50,9,31),(51,9,32),(52,9,33),(53,9,34),(54,9,35),(55,9,36),(56,9,37),(57,9,39),(58,9,40),(59,9,42),(60,9,46),(61,9,47),(62,10,17),(63,10,18),(64,11,21),(65,11,22),(66,12,24),(67,12,25),(68,12,26),(69,12,27),(70,12,28),(71,12,29),(72,12,30),(73,12,31),(74,12,32),(75,12,33),(76,12,34),(77,12,35),(78,12,36),(79,12,37),(80,12,38),(81,13,50),(82,13,51),(83,13,52),(84,13,53),(85,13,54),(86,13,55),(87,13,56),(88,13,57),(89,13,58),(90,13,59),(91,14,60),(92,14,61),(93,14,62),(94,14,63),(95,14,64),(96,14,65),(97,14,66),(98,14,67),(99,14,68),(100,14,69);
/*!40000 ALTER TABLE `participant_group_participants` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `recurrence_pattern`
--

LOCK TABLES `recurrence_pattern` WRITE;
/*!40000 ALTER TABLE `recurrence_pattern` DISABLE KEYS */;
/*!40000 ALTER TABLE `recurrence_pattern` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `resource`
--

LOCK TABLES `resource` WRITE;
/*!40000 ALTER TABLE `resource` DISABLE KEYS */;
INSERT INTO `resource` VALUES (8,'2016-01-15',55,1),(9,'2016-01-15',56,1),(10,'2016-01-15',57,1),(6,'2016-01-15',58,1),(7,'2016-01-15',59,1),(11,'2016-01-15',57,2),(12,'2016-01-15',58,2),(13,'2016-01-15',59,2),(14,'2016-01-15',60,2),(15,'2016-01-15',61,2),(1,'2016-01-15',53,3),(2,'2016-01-15',54,3),(3,'2016-01-15',55,3),(4,'2016-01-15',56,3),(5,'2016-01-15',57,3);
/*!40000 ALTER TABLE `resource` ENABLE KEYS */;
UNLOCK TABLES;

--
-- Dumping data for table `tms_user`
--

LOCK TABLES `tms_user` WRITE;
/*!40000 ALTER TABLE `tms_user` DISABLE KEYS */;
/*!40000 ALTER TABLE `tms_user` ENABLE KEYS */;
UNLOCK TABLES;
/*!40103 SET TIME_ZONE=@OLD_TIME_ZONE */;

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;

-- Dump completed on 2016-01-02 21:11:53
