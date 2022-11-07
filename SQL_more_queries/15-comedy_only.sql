SELECT ts.title FROM tv_shows ts
JOIN tv_show_genres tsg ON ts.id = tsg.show_id
WHERE tsg.genre_id = 5
ORDER BY ts.title ASC;