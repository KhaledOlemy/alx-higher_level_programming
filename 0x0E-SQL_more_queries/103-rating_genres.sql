-- lists all genres in the database hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_genres.name - rating sum
-- Results must be sorted in descending order by their rating
SELECT tv_gn.name, SUM(tv_rt.rate) AS rating FROM tv_genres tv_gn
LEFT JOIN tv_show_genres tv_sh_gn ON (tv_sh_gn.genre_id = tv_gn.id)
LEFT JOIN tv_shows tv_sh ON (tv_sh.id = tv_sh_gn.show_id)
LEFT JOIN tv_show_ratings tv_rt ON (tv_sh.id = tv_rt.show_id)
GROUP BY tv_gn.name
ORDER BY rating DESC;
