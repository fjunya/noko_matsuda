DROP TABLE IF EXISTS `account`;
CREATE TABLE `account` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `dept` varchar(64) DEFAULT NULL,
  `tel` varchar(32) DEFAULT NULL,
  `info` varchar(64) DEFAULT NULL,
  `date_from` datetime DEFAULT NULL,
  `date_to` datetime DEFAULT NULL,
  `no_validity` tinyint(1) DEFAULT NULL,
  `reserve_days` smallint(5) unsigned DEFAULT NULL,
  `no_reserve_days` tinyint(1) DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `updated_at` datetime NOT NULL,
  `user_id` int(11),
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`),
  CONSTRAINT `account_user_id_6addb41f823fe7d_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `account_account_groups`;
CREATE TABLE `account_account_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `account_id` int(11) NOT NULL,
  `accountgroup_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `account_id` (`account_id`,`accountgroup_id`),
  KEY `account_acc_accountgroup_id_774a30e16570ad56_fk_account_group_id` (`accountgroup_id`),
  CONSTRAINT `account_acc_accountgroup_id_774a30e16570ad56_fk_account_group_id` FOREIGN KEY (`accountgroup_id`) REFERENCES `account_group` (`id`),
  CONSTRAINT `account_account_groups_account_id_47fe0c33ebe1a922_fk_account_id` FOREIGN KEY (`account_id`) REFERENCES `account` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `account_group`;
CREATE TABLE `account_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(24) NOT NULL,
  `info` varchar(64) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_group`;
CREATE TABLE `auth_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(80) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `name` (`name`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_group_permissions`;
CREATE TABLE `auth_group_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `group_id` (`group_id`,`permission_id`),
  KEY `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_group__permission_id_1f49ccbbdc69d2fc_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_group_permission_group_id_689710a9a73b7457_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_permission`;
CREATE TABLE `auth_permission` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `name` varchar(255) NOT NULL,
  `content_type_id` int(11) NOT NULL,
  `codename` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `content_type_id` (`content_type_id`,`codename`),
  CONSTRAINT `auth__content_type_id_508cf46651277a81_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_user`;
CREATE TABLE `auth_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `password` varchar(128) NOT NULL,
  `last_login` datetime DEFAULT NULL,
  `is_superuser` tinyint(1) NOT NULL,
  `username` varchar(30) NOT NULL,
  `first_name` varchar(30) NOT NULL,
  `last_name` varchar(30) NOT NULL,
  `email` varchar(254) NOT NULL,
  `is_staff` tinyint(1) NOT NULL,
  `is_active` tinyint(1) NOT NULL,
  `date_joined` datetime NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `username` (`username`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_user_groups`;
CREATE TABLE `auth_user_groups` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `group_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`group_id`),
  KEY `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` (`group_id`),
  CONSTRAINT `auth_user_groups_group_id_33ac548dcf5f8e37_fk_auth_group_id` FOREIGN KEY (`group_id`) REFERENCES `auth_group` (`id`),
  CONSTRAINT `auth_user_groups_user_id_4b5ed4ffdb8fd9b0_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `auth_user_user_permissions`;
CREATE TABLE `auth_user_user_permissions` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `user_id` int(11) NOT NULL,
  `permission_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `user_id` (`user_id`,`permission_id`),
  KEY `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` (`permission_id`),
  CONSTRAINT `auth_user_u_permission_id_384b62483d7071f0_fk_auth_permission_id` FOREIGN KEY (`permission_id`) REFERENCES `auth_permission` (`id`),
  CONSTRAINT `auth_user_user_permissi_user_id_7f0938558328534a_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `conference`;
CREATE TABLE `conference` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `tms_conferenceId` varchar(30) NOT NULL,
  `mcu_conferenceName` varchar(30) NOT NULL,
  `mcu_conferenceNo` varchar(30) NOT NULL,
  `userName` varchar(50) NOT NULL,
  `department` varchar(50) NOT NULL,
  `mail` varchar(254) NOT NULL,
  `tel` varchar(50) NOT NULL,
  `description` varchar(100) NOT NULL,
  `title` varchar(100) NOT NULL,
  `startTime` datetime NOT NULL,
  `endTime` datetime NOT NULL,
  `bandwidth` varchar(20) NOT NULL,
  `videoQuality` varchar(50) NOT NULL,
  `h239` varchar(10) NOT NULL,
  `encrypted` varchar(10) NOT NULL,
  `pin` int(11) DEFAULT NULL,
  `controlPassword` varchar(50) NOT NULL,
  `conferencePassword` int(11) NOT NULL,
  `chairPassword` varchar(50) NOT NULL,
  `recording` tinyint(1) NOT NULL,
  `isWebEx` tinyint(1) NOT NULL,
  `mailForWebEx` varchar(500) NOT NULL,
  `layout_mode` varchar(50) NOT NULL,
  `presenter` int(11) DEFAULT NULL,
  `layout_no` int(11) DEFAULT NULL,
  `pane1` varchar(50) NOT NULL,
  `pane2` varchar(50) NOT NULL,
  `pane3` varchar(50) NOT NULL,
  `pane4` varchar(50) NOT NULL,
  `pane5` varchar(50) NOT NULL,
  `pane6` varchar(50) NOT NULL,
  `pane7` varchar(50) NOT NULL,
  `pane8` varchar(50) NOT NULL,
  `pane9` varchar(50) NOT NULL,
  `pane10` varchar(50) NOT NULL,
  `pane11` varchar(50) NOT NULL,
  `pane12` varchar(50) NOT NULL,
  `pane13` varchar(50) NOT NULL,
  `pane14` varchar(50) NOT NULL,
  `pane15` varchar(50) NOT NULL,
  `pane16` varchar(50) NOT NULL,
  `isStarted` tinyint(1) NOT NULL,
  `use_resource` int(11) NOT NULL,
  `createUser_id` int(11) DEFAULT NULL,
  `recurrencePattern_id` int(11),
  `tmsUser_id` int(11),
  PRIMARY KEY (`id`),
  KEY `conference_createUser_id_61944e2e490eeb1b_fk_auth_user_id` (`createUser_id`),
  KEY `conference_7aec9283` (`recurrencePattern_id`),
  KEY `conference_93f36f89` (`tmsUser_id`),
  CONSTRAINT `conference_tmsUser_id_6d4811b81c7af7f8_fk_tms_user_id` FOREIGN KEY (`tmsUser_id`) REFERENCES `tms_user` (`id`),
  CONSTRAINT `conference_createUser_id_61944e2e490eeb1b_fk_auth_user_id` FOREIGN KEY (`createUser_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `c_recurrencePattern_id_6506efbf518f6403_fk_recurrence_pattern_id` FOREIGN KEY (`recurrencePattern_id`) REFERENCES `recurrence_pattern` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `conference_participants`;
CREATE TABLE `conference_participants` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `conference_id` int(11) NOT NULL,
  `participant_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `conference_id` (`conference_id`,`participant_id`),
  KEY `conference_par_participant_id_5fd0654c295913ce_fk_participant_id` (`participant_id`),
  CONSTRAINT `conference_par_participant_id_5fd0654c295913ce_fk_participant_id` FOREIGN KEY (`participant_id`) REFERENCES `participant` (`id`),
  CONSTRAINT `conference_parti_conference_id_4b60ac884ab6fbb2_fk_conference_id` FOREIGN KEY (`conference_id`) REFERENCES `conference` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `django_admin_log`;
CREATE TABLE `django_admin_log` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `action_time` datetime NOT NULL,
  `object_id` longtext,
  `object_repr` varchar(200) NOT NULL,
  `action_flag` smallint(5) unsigned NOT NULL,
  `change_message` longtext NOT NULL,
  `content_type_id` int(11) DEFAULT NULL,
  `user_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  KEY `djang_content_type_id_697914295151027a_fk_django_content_type_id` (`content_type_id`),
  KEY `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` (`user_id`),
  CONSTRAINT `django_admin_log_user_id_52fdd58701c5f563_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`),
  CONSTRAINT `djang_content_type_id_697914295151027a_fk_django_content_type_id` FOREIGN KEY (`content_type_id`) REFERENCES `django_content_type` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `django_content_type`;
CREATE TABLE `django_content_type` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app_label` varchar(100) NOT NULL,
  `model` varchar(100) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `django_content_type_app_label_45f3b1d93ec8c61c_uniq` (`app_label`,`model`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `django_migrations`;
CREATE TABLE `django_migrations` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `app` varchar(255) NOT NULL,
  `name` varchar(255) NOT NULL,
  `applied` datetime NOT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `django_session`;
CREATE TABLE `django_session` (
  `session_key` varchar(40) NOT NULL,
  `session_data` longtext NOT NULL,
  `expire_date` datetime NOT NULL,
  PRIMARY KEY (`session_key`),
  KEY `django_session_de54fa62` (`expire_date`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `information`;
CREATE TABLE `information` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `body` longtext,
  `type` int(10) unsigned DEFAULT NULL,
  `created_at` datetime NOT NULL,
  `user_id` int(11) DEFAULT NULL,
  PRIMARY KEY (`id`),
  KEY `information_user_id_381f89a0ae122d8e_fk_auth_user_id` (`user_id`),
  CONSTRAINT `information_user_id_381f89a0ae122d8e_fk_auth_user_id` FOREIGN KEY (`user_id`) REFERENCES `auth_user` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `participant`;
CREATE TABLE `participant` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `display_name` varchar(40) NOT NULL,
  `direction` varchar(12) NOT NULL,
  `type` varchar(8) NOT NULL,
  `bitrate` int(10) unsigned DEFAULT NULL,
  `video_protocol` varchar(8) NOT NULL,
  `ip_address` varchar(32) NOT NULL,
  `phone1` varchar(32) DEFAULT NULL,
  `alias_name` varchar(32) DEFAULT NULL,
  `alias_type` varchar(8) DEFAULT NULL,
  `sip_address` varchar(80) DEFAULT NULL,
  `sip_address_type` varchar(24) DEFAULT NULL,
  `cascade_role` varchar(12) NOT NULL,
  `model` varchar(12) NOT NULL,
  `software_version` varchar(12) NOT NULL,
  `audio_only_flg` tinyint(1) DEFAULT NULL,
  `info` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `participant_group`;
CREATE TABLE `participant_group` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `group_name` varchar(24) NOT NULL,
  `info` varchar(128) DEFAULT NULL,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `participant_group_participants`;
CREATE TABLE `participant_group_participants` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `participantgroup_id` int(11) NOT NULL,
  `participant_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `participantgroup_id` (`participantgroup_id`,`participant_id`),
  KEY `participant_gr_participant_id_28bfc0f7fd0d7e68_fk_participant_id` (`participant_id`),
  CONSTRAINT `participant_gr_participant_id_28bfc0f7fd0d7e68_fk_participant_id` FOREIGN KEY (`participant_id`) REFERENCES `participant` (`id`),
  CONSTRAINT `par_participantgroup_id_3e9bd505440afe10_fk_participant_group_id` FOREIGN KEY (`participantgroup_id`) REFERENCES `participant_group` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `recurrence_pattern`;
CREATE TABLE `recurrence_pattern` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `resource`;
CREATE TABLE `resource` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  `date` date NOT NULL,
  `slot` smallint(5) unsigned NOT NULL,
  `conference_id` int(11) NOT NULL,
  PRIMARY KEY (`id`),
  UNIQUE KEY `resource_conference_id_7b89de1d34d049a0_uniq` (`conference_id`,`date`,`slot`),
  CONSTRAINT `resource_conference_id_6b671f3a1608deb2_fk_conference_id` FOREIGN KEY (`conference_id`) REFERENCES `conference` (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;


DROP TABLE IF EXISTS `tms_user`;
CREATE TABLE `tms_user` (
  `id` int(11) NOT NULL AUTO_INCREMENT,
  PRIMARY KEY (`id`)
) ENGINE=InnoDB DEFAULT CHARSET=utf8;
