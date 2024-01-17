-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
SELECT gn.name AS 'genre', COUNT(sh_gn.genre_id) AS 'number_of_shows'
FROM tv_genres gn RIGHT JOIN tv_show_genres sh_gn ON (gn.id = sh_gn.genre_id) GROUP BY genre ORDER BY number_of_shows DESC;

