INSERT INTO `auth_user` (`id`, `password`, `last_login`, `is_superuser`, `username`, `first_name`, `last_name`, `email`, `is_staff`, `is_active`, `date_joined`) VALUES (1, 'pbkdf2_sha256$20000$XPSmfvLwxzBw$kA5ePsCzyotKtOwlGjU36KCFsSqWd9Y/Wu8t9pn7uJE=', NOW(), 1, 'papp', 'admin', 'papp', 'admin@papp.com', 1, 1, NOW());
INSERT INTO `account` (`id`, `dept`, `tel`, `info`, `date_from`, `date_to`, `no_validity`, `reserve_days`, `no_reserve_days`, `created_at`, `updated_at`, `user_id`) VALUES (1, '', '', '', NULL, NULL, 1, NULL, 1, NOW(), NOW(), 1);

