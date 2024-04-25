/*
SQLyog Community v13.1.6 (64 bit)
MySQL - 5.7.9 : Database - humanresourcemanagement
*********************************************************************
*/

/*!40101 SET NAMES utf8 */;

/*!40101 SET SQL_MODE=''*/;

/*!40014 SET @OLD_UNIQUE_CHECKS=@@UNIQUE_CHECKS, UNIQUE_CHECKS=0 */;
/*!40014 SET @OLD_FOREIGN_KEY_CHECKS=@@FOREIGN_KEY_CHECKS, FOREIGN_KEY_CHECKS=0 */;
/*!40101 SET @OLD_SQL_MODE=@@SQL_MODE, SQL_MODE='NO_AUTO_VALUE_ON_ZERO' */;
/*!40111 SET @OLD_SQL_NOTES=@@SQL_NOTES, SQL_NOTES=0 */;
CREATE DATABASE /*!32312 IF NOT EXISTS*/`humanresourcemanagement` /*!40100 DEFAULT CHARACTER SET latin1 */;

USE `humanresourcemanagement`;

/*Table structure for table `attendance` */

DROP TABLE IF EXISTS `attendance`;

CREATE TABLE `attendance` (
  `attendance_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  `status` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`attendance_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `attendance` */

insert  into `attendance`(`attendance_id`,`staff_id`,`date`,`status`) values 
(1,4,'18-04-2024','present'),
(2,1,'19-03-2024','absent');

/*Table structure for table `chat` */

DROP TABLE IF EXISTS `chat`;

CREATE TABLE `chat` (
  `chat_id` int(11) NOT NULL AUTO_INCREMENT,
  `sender_id` int(11) DEFAULT NULL,
  `receiver_id` int(11) DEFAULT NULL,
  `message` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`chat_id`)
) ENGINE=MyISAM DEFAULT CHARSET=latin1;

/*Data for the table `chat` */

/*Table structure for table `complaints` */

DROP TABLE IF EXISTS `complaints`;

CREATE TABLE `complaints` (
  `complaints_id` int(11) NOT NULL AUTO_INCREMENT,
  `staff_id` int(11) DEFAULT NULL,
  `complaint_des` varchar(100) DEFAULT NULL,
  `reply` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`complaints_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `complaints` */

insert  into `complaints`(`complaints_id`,`staff_id`,`complaint_des`,`reply`,`date`) values 
(1,1,'test_desc','test_desc reply','13-04-000'),
(2,10,'test complaint','null','2024-02-22'),
(4,12,'test comaplaint 7777','null','2024-03-07'),
(7,12,'testing 7777','null','2024-03-07'),
(6,12,'new page testing','reply to new page','2024-03-07'),
(8,12,'test complaint','null','2024-03-07'),
(9,12,'test complaint','null','2024-03-07'),
(10,3,'jhjhjhjhj','reply for jjjj','2024-03-07'),
(11,12,'send from staff agin','agin reply','2024-03-14'),
(12,3,'send from hr','reply for hr','2024-03-14');

/*Table structure for table `designation` */

DROP TABLE IF EXISTS `designation`;

CREATE TABLE `designation` (
  `designation_id` int(11) NOT NULL AUTO_INCREMENT,
  `designation_name` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`designation_id`)
) ENGINE=MyISAM AUTO_INCREMENT=2 DEFAULT CHARSET=latin1;

/*Data for the table `designation` */

insert  into `designation`(`designation_id`,`designation_name`) values 
(1,'mca');

/*Table structure for table `hr_team` */

DROP TABLE IF EXISTS `hr_team`;

CREATE TABLE `hr_team` (
  `hr_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `name` varchar(100) DEFAULT NULL,
  `qualification` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`hr_id`)
) ENGINE=MyISAM AUTO_INCREMENT=13 DEFAULT CHARSET=latin1;

/*Data for the table `hr_team` */

insert  into `hr_team`(`hr_id`,`login_id`,`name`,`qualification`,`phone`,`email`) values 
(7,38,'vysakh','mtech','98197827827','vysakh@gmail.com'),
(10,41,'ajesh','10','17981782782','ajesh@gmail.com'),
(11,42,'hr','mba','12345678','hr@gmail.com');

/*Table structure for table `login` */

DROP TABLE IF EXISTS `login`;

CREATE TABLE `login` (
  `login_id` int(11) NOT NULL AUTO_INCREMENT,
  `username` varchar(100) DEFAULT NULL,
  `password` varchar(100) DEFAULT NULL,
  `usertype` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`login_id`)
) ENGINE=MyISAM AUTO_INCREMENT=45 DEFAULT CHARSET=latin1;

/*Data for the table `login` */

insert  into `login`(`login_id`,`username`,`password`,`usertype`) values 
(34,'alex','alex','staff'),
(42,'hr123','hr123','hr'),
(41,'ajesh123','ajesh123','hr'),
(40,'vysakh','vysakh','hr'),
(39,'vysakh','vysakh','hr'),
(38,'vysakh','vysakh','hr'),
(37,'ebin','ebin','hr'),
(36,'ajoy','ajoy','hr'),
(33,'agin123','agin1234','staff'),
(32,'ajesh123','ajesh123','hr'),
(31,'ebin123','ebin123','hr'),
(30,'vysakh123','vysakh123','hr'),
(35,'ajoy123','ajoy123','user'),
(25,'admin','admin ','admin'),
(26,'ebin123','ebin123','hr'),
(43,'hr123','hr123','hr'),
(44,'staff123','staff123','staff');

/*Table structure for table `notification` */

DROP TABLE IF EXISTS `notification`;

CREATE TABLE `notification` (
  `notification_id` int(11) NOT NULL AUTO_INCREMENT,
  `notification_des` varchar(100) DEFAULT NULL,
  `date` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`notification_id`)
) ENGINE=MyISAM AUTO_INCREMENT=3 DEFAULT CHARSET=latin1;

/*Data for the table `notification` */

insert  into `notification`(`notification_id`,`notification_des`,`date`) values 
(1,'test','2024-02-16'),
(2,'maintenace','2014-02-18');

/*Table structure for table `staff` */

DROP TABLE IF EXISTS `staff`;

CREATE TABLE `staff` (
  `staff_id` int(11) NOT NULL AUTO_INCREMENT,
  `login_id` int(11) DEFAULT NULL,
  `designation_id` int(11) DEFAULT NULL,
  `first_name` varchar(100) DEFAULT NULL,
  `last_name` varchar(100) DEFAULT NULL,
  `gender` varchar(100) DEFAULT NULL,
  `dob` varchar(100) DEFAULT NULL,
  `phone` varchar(100) DEFAULT NULL,
  `email` varchar(100) DEFAULT NULL,
  PRIMARY KEY (`staff_id`)
) ENGINE=MyISAM AUTO_INCREMENT=15 DEFAULT CHARSET=latin1;

/*Data for the table `staff` */

insert  into `staff`(`staff_id`,`login_id`,`designation_id`,`first_name`,`last_name`,`gender`,`dob`,`phone`,`email`) values 
(12,33,1,'agin','s','male','18-05-2001','8111966314','agin@gmail.com'),
(10,23,1,'ajesh','minadiyil','male','15-07-2001','19189289800','ajesh@gmail.com'),
(11,24,1,'vysakh','s','male','15-07-2000','1234567896','vysakh@gmail.com'),
(14,44,1,'staff','staff','male','13-04-2000','1726762762762','ajoy@gmailcom'),
(13,35,1,'ajoy','john','male','13-04-2000','28282882','ajoy@gmailcom');

/*!40101 SET SQL_MODE=@OLD_SQL_MODE */;
/*!40014 SET FOREIGN_KEY_CHECKS=@OLD_FOREIGN_KEY_CHECKS */;
/*!40014 SET UNIQUE_CHECKS=@OLD_UNIQUE_CHECKS */;
/*!40111 SET SQL_NOTES=@OLD_SQL_NOTES */;
