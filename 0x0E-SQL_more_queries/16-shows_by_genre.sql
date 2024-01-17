-- lists all shows, and all genres linked to that show, from the database hbtn_0d_tvshows.
-- If a show doesn’t have a genre, display NULL in the genre column
-- Each record should display: tv_shows.title - tv_genres.name
-- Results must be sorted in ascending order by the show title and genre name
SELECT tv_sh.title, tv_gn.name FROM tv_shows tv_sh
LEFT JOIN tv_show_genres tv_sh_gn ON (tv_sh.id = tv_sh_gn.show_id)
LEFT JOIN tv_genres tv_gn ON (tv_sh_gn.genre_id = tv_gn.id)
GROUP BY tv_gn.name
ORDER BY tv_sh.title ASC, tv_gn.name ASC;
