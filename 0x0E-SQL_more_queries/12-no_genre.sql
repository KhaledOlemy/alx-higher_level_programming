-- lists all shows contained in hbtn_0d_tvshows without a genre linked.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
SELECT sh.title, gn.genre_id FROM tv_shows sh LEFT JOIN tv_show_genres gn ON (sh.id = gn.show_id) WHERE gn.genre_id IS NULL ORDER BY sh.title ASC, gn.genre_id ASC;
