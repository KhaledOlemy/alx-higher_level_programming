-- lists all genres of the show Dexter.
-- The tv_shows table contains only one record where title = Dexter (but the id can be different)
-- Each record should display: tv_genres.name
-- Results must be sorted in ascending order by the genre name
SELECT tv_gn.name FROM tv_genres tv_gn INNER JOIN tv_show_genres tv_sh_gn ON (tv_sh_gn.genre_id=tv_gn.id) WHERE (tv_shows.title='Dexter') ORDER BY tv_gn.name;
