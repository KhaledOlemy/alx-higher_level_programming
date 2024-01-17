-- lists all shows contained in the database hbtn_0d_tvshows.
-- Each record should display: tv_shows.title - tv_show_genres.genre_id
-- Results must be sorted in ascending order by tv_shows.title and tv_show_genres.genre_id
-- If a show doesn’t have a genre, display NULL
SELECT sh.title, gn.genre_id FROM tv_shows sh FULL OUTER JOIN tv_show_genres gn ORDER BY sh.title ASC, gn.genre_id ASC;
