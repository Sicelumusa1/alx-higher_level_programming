-- Lists all genres from hbtn_0d_tvshows and displays the number of shows linked to each.
SELECT tv_genrres.name AS genre, COUNT(tv_show_genres.genre_id) AS number_of _shows
FROM tv_genres
LEFT JOIN tv_show_genres ON tv_genres.id = tv_show_genres.genre_id
GROUP BY tv_genres.id, tv_genres.name
HAVING number_of _shows > 0
order by number_of _shows DESC;
