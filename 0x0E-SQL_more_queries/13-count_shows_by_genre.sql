-- lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
-- Each record should display: <TV Show genre> - <Number of shows linked to this genre>
-- First column must be called genre
-- Second column must be called number_of_shows
-- Don’t display a genre that doesn’t have any shows linked
-- Results must be sorted in descending order by the number of shows linked
SELECT gn.name, COUNT(*) FROM tv_shows sh NATURAL JOIN tv_show_genres gn ON (sh.id = gn.show_id) ORDER BY COUNT(*) DESC;
