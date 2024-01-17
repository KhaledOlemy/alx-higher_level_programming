-- list all genres not linked to the show Dexter
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT tv_gn.name from tv_genres tv_gn
LEFT JOIN tv_show_genres tv_sh_gn ON (tv_sh_gn.genre_id = tv_gn.id)
LEFT JOIN tv_shows tv_sh ON (tv_sh_gn.show_id = tv_sh.id)
WHERE tv_sh.title <> 'Dexter'
ORDER BY tv_gn.name ASC;
