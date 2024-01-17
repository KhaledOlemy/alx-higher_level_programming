-- lists all shows from hbtn_0d_tvshows_rate by their rating.
-- Each record should display: tv_shows.title - rating sum
-- Results must be sorted in descending order by the rating
SELECT tv_sh.title, SUM(tv_rt.rate) AS 'rating' FROM tv_shows tv_sh
LEFT JOIN tv_show_ratings tv_rt ON (tv_sh.id = tv_rt.show_id)
GROUP BY title
ORDER BY rating DESC;
