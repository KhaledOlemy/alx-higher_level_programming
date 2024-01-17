-- lists all shows contained in hbtn_0d_tvshows that have at least one genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- one SELECT statement
SELECT sh.title, gn.genre_id FROM tv_shows sh LEFT JOIN tv_show_genres gn ON (sh.id = gn.show_id) ORDER BY sh.title ASC, gn.genre_id ASC;
