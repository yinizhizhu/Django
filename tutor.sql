-- phpMyAdmin SQL Dump
-- version 3.4.10.1
-- http://www.phpmyadmin.net
--
-- 主机: localhost
-- 生成日期: 2015 年 11 月 26 日 10:42
-- 服务器版本: 5.5.20
-- PHP 版本: 5.3.10
-- create database tutor default charset=utf8;

SET SQL_MODE="NO_AUTO_VALUE_ON_ZERO";
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8 */;

--
-- 数据库: `tutor`
--

-- --------------------------------------------------------

--
-- 表的结构 `addr_book_content_student`
--

CREATE TABLE IF NOT EXISTS `addr_book_content_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `school` varchar(15) NOT NULL,
  `grade` varchar(15) NOT NULL,
  `wenli` tinyint(1) NOT NULL,
  `subjects` varchar(18) NOT NULL,
  `freestate` tinyint(1) NOT NULL,
  `publishdate` datetime NOT NULL,
  `timerequest` varchar(42) NOT NULL,
  `sexrequest` int(11) NOT NULL,
  `judge` varchar(50) NOT NULL,
  `costperhour` int(11) NOT NULL,
  `star` int(11) NOT NULL,
  `evaluation` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- 表的结构 `addr_book_content_teacher`
--

CREATE TABLE IF NOT EXISTS `addr_book_content_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `wenli` tinyint(1) NOT NULL,
  `subjects` varchar(18) NOT NULL,
  `freestate` tinyint(1) NOT NULL,
  `publishdate` datetime NOT NULL,
  `timeforteaching` varchar(42) NOT NULL,
  `getperhour` int(11) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;
----------------------------------------------------

--
-- 表的结构 `addr_book_content_teacher_content_stu`
--

CREATE TABLE IF NOT EXISTS `addr_book_content_teacher_content_stu` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `content_teacher_id` int(11) NOT NULL,
  `content_student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_teacher_id` (`content_teacher_id`,`content_student_id`),
  KEY `addr_book_content_teacher_content_stu_ca34eb29` (`content_teacher_id`),
  KEY `addr_book_content_teacher_content_stu_522af42a` (`content_student_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=3 ;

--
-- 表的结构 `addr_book_student`
--

CREATE TABLE IF NOT EXISTS `addr_book_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `sex` tinyint(1) NOT NULL,
  `age` int(11) NOT NULL,
  `tel` varchar(15) NOT NULL,
  `email` varchar(75) NOT NULL,
  `address` varchar(50) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- 表的结构 `addr_book_student_content`
--

CREATE TABLE IF NOT EXISTS `addr_book_student_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `student_id` int(11) NOT NULL,
  `content_student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `student_id` (`student_id`,`content_student_id`),
  KEY `addr_book_student_content_94741166` (`student_id`),
  KEY `addr_book_student_content_522af42a` (`content_student_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;
-----------------------------------------------------

--
-- 表的结构 `addr_book_teacher`
--

CREATE TABLE IF NOT EXISTS `addr_book_teacher` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(10) NOT NULL,
  `sex` tinyint(1) NOT NULL,
  `age` int(11) NOT NULL,
  `college` varchar(20) NOT NULL,
  `major` varchar(20) NOT NULL,
  `tel` varchar(15) NOT NULL,
  `email` varchar(75) NOT NULL,
  `address` varchar(50) NOT NULL,
  `image` varchar(100) NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=4 ;

--
-- 表的结构 `addr_book_teacher_content`
--

CREATE TABLE IF NOT EXISTS `addr_book_teacher_content` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `teacher_id` int(11) NOT NULL,
  `content_teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `teacher_id` (`teacher_id`,`content_teacher_id`),
  KEY `addr_book_teacher_content_c12e9d48` (`teacher_id`),
  KEY `addr_book_teacher_content_ca34eb29` (`content_teacher_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=5 ;

-- --------------------------------------------------------

--
-- 表的结构 `addr_book_user`
--

CREATE TABLE IF NOT EXISTS `addr_book_user` (
  `username` varchar(10) NOT NULL,
  `email` varchar(75) NOT NULL,
  `password` varchar(20) NOT NULL,
  `teacher_id` int(11) NOT NULL,
  PRIMARY KEY (`username`),
  KEY `addr_book_user_c12e9d48` (`teacher_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

-- --------------------------------------------------------

--
-- 表的结构 `addr_book_user_student`
--

CREATE TABLE IF NOT EXISTS `addr_book_user_student` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` varchar(10) NOT NULL,
  `student_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`student_id`),
  KEY `addr_book_user_student_6340c63c` (`user_id`),
  KEY `addr_book_user_student_94741166` (`student_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=7 ;

--
-- 表的结构 `auth_group`
--

CREATE TABLE IF NOT EXISTS `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_group_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group_permissions_5f412f9a` (`group_id`),
  KEY `auth_group_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_permission`
--

CREATE TABLE IF NOT EXISTS `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(50) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  KEY `auth_permission_37ef4eb4` (`content_type_id`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=34 ;

--
-- 转存表中的数据 `auth_permission`
--

INSERT INTO `auth_permission` (`id`, `name`, `content_type_id`, `codename`) VALUES
(1, 'Can add log entry', 1, 'add_logentry'),
(2, 'Can change log entry', 1, 'change_logentry'),
(3, 'Can delete log entry', 1, 'delete_logentry'),
(4, 'Can add permission', 2, 'add_permission'),
(5, 'Can change permission', 2, 'change_permission'),
(6, 'Can delete permission', 2, 'delete_permission'),
(7, 'Can add group', 3, 'add_group'),
(8, 'Can change group', 3, 'change_group'),
(9, 'Can delete group', 3, 'delete_group'),
(10, 'Can add user', 4, 'add_user'),
(11, 'Can change user', 4, 'change_user'),
(12, 'Can delete user', 4, 'delete_user'),
(13, 'Can add content type', 5, 'add_contenttype'),
(14, 'Can change content type', 5, 'change_contenttype'),
(15, 'Can delete content type', 5, 'delete_contenttype'),
(16, 'Can add session', 6, 'add_session'),
(17, 'Can change session', 6, 'change_session'),
(18, 'Can delete session', 6, 'delete_session'),
(19, 'Can add content_student', 7, 'add_content_student'),
(20, 'Can change content_student', 7, 'change_content_student'),
(21, 'Can delete content_student', 7, 'delete_content_student'),
(22, 'Can add content_teacher', 8, 'add_content_teacher'),
(23, 'Can change content_teacher', 8, 'change_content_teacher'),
(24, 'Can delete content_teacher', 8, 'delete_content_teacher'),
(25, 'Can add student', 9, 'add_student'),
(26, 'Can change student', 9, 'change_student'),
(27, 'Can delete student', 9, 'delete_student'),
(28, 'Can add teacher', 10, 'add_teacher'),
(29, 'Can change teacher', 10, 'change_teacher'),
(30, 'Can delete teacher', 10, 'delete_teacher'),
(31, 'Can add user', 11, 'add_user'),
(32, 'Can change user', 11, 'change_user'),
(33, 'Can delete user', 11, 'delete_user');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user`
--

CREATE TABLE IF NOT EXISTS `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime NOT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(75) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=2 ;

--
-- 转存表中的数据 `auth_user`
--

INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES
(1, 'pbkdf2_sha256$12000$a0H5wQ1j0iAm$yhnv7cghlHWdZc1PzqDo+sOuzmC90yhrm6hqkXMJNro=', '2015-11-25 13:58:28', 1, 'lijiahe19941013@sina.cn', '', '', 'lijiahe19941013@sina.cn', 1, 1, '2015-11-25 13:58:28');

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_groups`
--

CREATE TABLE IF NOT EXISTS `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_6340c63c` (`user_id`),
  KEY `auth_user_groups_5f412f9a` (`group_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `auth_user_user_permissions`
--

CREATE TABLE IF NOT EXISTS `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_user_permissions_6340c63c` (`user_id`),
  KEY `auth_user_user_permissions_83d7f98b` (`permission_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `django_admin_log`
--

CREATE TABLE IF NOT EXISTS `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `user_id` int(11) NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  PRIMARY KEY (`id`),
  KEY `django_admin_log_6340c63c` (`user_id`),
  KEY `django_admin_log_37ef4eb4` (`content_type_id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 ;

-- --------------------------------------------------------

--
-- 表的结构 `django_content_type`
--

CREATE TABLE IF NOT EXISTS `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(100) NOT NULL,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `app_label` (`app_label`,`model`)
) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=12 ;

--
-- 转存表中的数据 `django_content_type`
--

INSERT INTO `django_content_type` (`id`, `name`, `app_label`, `model`) VALUES
(1, 'log entry', 'admin', 'logentry'),
(2, 'permission', 'auth', 'permission'),
(3, 'group', 'auth', 'group'),
(4, 'user', 'auth', 'user'),
(5, 'content type', 'contenttypes', 'contenttype'),
(6, 'session', 'sessions', 'session'),
(7, 'content_student', 'addr_book', 'content_student'),
(8, 'content_teacher', 'addr_book', 'content_teacher'),
(9, 'student', 'addr_book', 'student'),
(10, 'teacher', 'addr_book', 'teacher'),
(11, 'user', 'addr_book', 'user');

-- --------------------------------------------------------

--
-- 表的结构 `django_session`
--

CREATE TABLE IF NOT EXISTS `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_b7b81f0c` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;

--
-- 转存表中的数据 `django_session`
--

INSERT INTO `django_session` (`session_key`, `session_data`, `expire_date`) VALUES
('0hl8jo2320lssub9rujy2lnllujz305d', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-09 14:10:12'),
('106mn3wml8vyy04s4r9ofattd8zi7ecn', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-09 14:01:21'),
('3o3oc7uic58f7rrulgln3d3kcxzsnatk', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 07:21:13'),
('5q0hv1520j2rvcufsauq2d4ccioqa0sn', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 08:08:43'),
('8s3zpziosqhwbv7624cma387wtkn1h8h', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 08:19:14'),
('9ir0iuaf34wnepghex7d54e4w5whp14x', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 07:12:24'),
('dv7i0pv4np3zgrkmhek9hsgf1ipr7t31', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 08:19:20'),
('dy685fg0pg2r1rqpeoacufsj2hwvjcu9', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-09 15:00:57'),
('ggh288yo02qfssgzubiv6aw685txvdrx', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 07:18:53'),
('h833pzdzl425dp4z2z0mdi522fo7yqsk', 'YzcxZWNhMTAxYmE5OTNjYWU5NGMzYzIzZWNmNzIwZGZiNmVkOTJjNDp7ImRqYW5nb19sYW5ndWFnZSI6InpoLWNuIn0=', '2015-12-10 09:43:20'),
('hypy3cgl5drkv89xnnuribakgl3o37j4', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 08:19:34'),
('jixezphcu63evq1jde17edbbx2yxz6y8', 'NjBjNjhlNmQzMDJkZGY3ZDkwODZmM2VhNDFjNjVkZWEzOTNiZWRjNjp7InVzZXJfaWQiOiJ5aW5pemhpemh1IiwiZGphbmdvX2xhbmd1YWdlIjoiemgtY24ifQ==', '2015-12-10 07:47:17'),
('jrjbfvc1i8j7ehiuqf48t3ks902azfo6', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 07:12:55'),
('kj0j6fephajfnnd4qhxwmld0e0qk5qz5', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 08:18:58'),
('klf9737edzli59fkbiyavxzrqerv38y5', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 07:12:27'),
('lugj0slb31f54x0mgfc5ipb1040j177u', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 08:19:25'),
('niij0u3cc5s8b7ybscow6rdjlgz61ym3', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 07:12:21'),
('o9krvobghth7v7twlp82vfzqbq5k9n7z', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 07:11:51'),
('rmae54orjx6znq1et4ylhe7bk3vk1qoi', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 07:18:47'),
('sqshpqpmx6t3sbwz912kzir3458opg60', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 08:19:49'),
('stb1po8gifeqvypuja0dvyfbdzxe1ldm', 'NjBjNjhlNmQzMDJkZGY3ZDkwODZmM2VhNDFjNjVkZWEzOTNiZWRjNjp7InVzZXJfaWQiOiJ5aW5pemhpemh1IiwiZGphbmdvX2xhbmd1YWdlIjoiemgtY24ifQ==', '2015-12-09 15:00:42'),
('tjr9ye1bwi1maw7cbkbzdhhq8hshy2l7', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-09 14:10:15'),
('uuxnbliquz1pdda3u82nn5zdiuaxu3pa', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-09 14:10:51'),
('wmlgja55kp2tc7ewb8pjsfqslpus9zq0', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-09 14:01:12'),
('xwqfejwpqhljjzsl5hghfkzkhi2ptmd7', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 07:12:51'),
('zl0fuvfm8s1sejmuos6eyg59bal7rt5g', 'Y2E5NDVhYzlkZTVmOWViNzQzYjJlNTJmYjk2ZWE2MGVhNzFiMmYzOTp7ImRqYW5nb19sYW5ndWFnZSI6ImVuIn0=', '2015-12-10 07:12:58');

--
-- 限制导出的表
--

--
-- 限制表 `addr_book_content_teacher_content_stu`
--
ALTER TABLE `addr_book_content_teacher_content_stu`
  ADD CONSTRAINT `content_student_id_refs_id_9c2ee12b` FOREIGN KEY (`content_student_id`) REFERENCES `addr_book_content_student` (`id`),
  ADD CONSTRAINT `content_teacher_id_refs_id_1ecfae1b` FOREIGN KEY (`content_teacher_id`) REFERENCES `addr_book_content_teacher` (`id`);

--
-- 限制表 `addr_book_student_content`
--
ALTER TABLE `addr_book_student_content`
  ADD CONSTRAINT `content_student_id_refs_id_3077919c` FOREIGN KEY (`content_student_id`) REFERENCES `addr_book_content_student` (`id`),
  ADD CONSTRAINT `student_id_refs_id_8240608c` FOREIGN KEY (`student_id`) REFERENCES `addr_book_student` (`id`);

--
-- 限制表 `addr_book_teacher_content`
--
ALTER TABLE `addr_book_teacher_content`
  ADD CONSTRAINT `content_teacher_id_refs_id_37ac9bf5` FOREIGN KEY (`content_teacher_id`) REFERENCES `addr_book_content_teacher` (`id`),
  ADD CONSTRAINT `teacher_id_refs_id_e2c2b80b` FOREIGN KEY (`teacher_id`) REFERENCES `addr_book_teacher` (`id`);

--
-- 限制表 `addr_book_user`
--
ALTER TABLE `addr_book_user`
  ADD CONSTRAINT `teacher_id_refs_id_b3931f4d` FOREIGN KEY (`teacher_id`) REFERENCES `addr_book_teacher` (`id`);

--
-- 限制表 `addr_book_user_student`
--
ALTER TABLE `addr_book_user_student`
  ADD CONSTRAINT `student_id_refs_id_c448fc73` FOREIGN KEY (`student_id`) REFERENCES `addr_book_student` (`id`),
  ADD CONSTRAINT `user_id_refs_username_44bd1b2f` FOREIGN KEY (`user_id`) REFERENCES `addr_book_user` (`username`);

--
-- 限制表 `auth_group_permissions`
--
ALTER TABLE `auth_group_permissions`
  ADD CONSTRAINT `group_id_refs_id_f4b32aac` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `permission_id_refs_id_6ba0f519` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`);

--
-- 限制表 `auth_permission`
--
ALTER TABLE `auth_permission`
  ADD CONSTRAINT `content_type_id_refs_id_d043b34a` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`);

--
-- 限制表 `auth_user_groups`
--
ALTER TABLE `auth_user_groups`
  ADD CONSTRAINT `group_id_refs_id_274b862c` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  ADD CONSTRAINT `user_id_refs_id_40c41112` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `auth_user_user_permissions`
--
ALTER TABLE `auth_user_user_permissions`
  ADD CONSTRAINT `permission_id_refs_id_35d9ac25` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  ADD CONSTRAINT `user_id_refs_id_4dc23c39` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

--
-- 限制表 `django_admin_log`
--
ALTER TABLE `django_admin_log`
  ADD CONSTRAINT `content_type_id_refs_id_93d2d1f8` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`),
  ADD CONSTRAINT `user_id_refs_id_c0d12874` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`);

/*!40101 SET CHARACTER_SET_CLIENT=@OLD_CHARACTER_SET_CLIENT */;
/*!40101 SET CHARACTER_SET_RESULTS=@OLD_CHARACTER_SET_RESULTS */;
/*!40101 SET COLLATION_CONNECTION=@OLD_COLLATION_CONNECTION */;
