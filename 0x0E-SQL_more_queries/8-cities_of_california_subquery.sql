-- select all california cities
SELECT `id`, `name` FROM `cities` WHERE `id` = (SELECT `id` FROM `states` WHERE `name` = 'California') ORDER BY `id` ASC;
