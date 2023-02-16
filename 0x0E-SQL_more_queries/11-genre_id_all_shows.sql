-- select evry show with their genre
SELECT S.`title`, g.`genre_id` FROM `tv_shows` AS s LEFT OUTER JOIN `tv_show_genres` AS g ON S.`id` = g.`shows_id` ORDER BY s.`title`, g.`genre_id`;
