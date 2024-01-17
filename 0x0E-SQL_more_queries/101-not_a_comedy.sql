-- lists all shows without the genre Comedy in the database hbtn_0d_tvshows.
-- The tv_genres table contains only one record where name = Comedy (but the id can be different)
-- Each record should display: tv_shows.title
-- Results must be sorted in ascending order by the show title
SELECT tv_sh.title FROM tv_shows tv_sh
WHERE title NOT IN
(
SELECT tv_sh.title FROM tv_shows tv_sh
LEFT JOIN tv_show_genres tv_sh_gn ON (tv_sh_gn.show_id = tv_sh.id)
LEFT JOIN tv_genres tv_gn ON (tv_gn.id = tv_sh_gn.genre_id)
Where tv_gn.name = "Comedy"
)
ORDER BY tv_sh.title ASC;
