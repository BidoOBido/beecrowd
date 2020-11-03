select distinct m.id, m."name"
  from movies m
 inner join genres g on g.id = m.id_genres
 inner join movies_actors ma on ma.id_movies = m.id
 inner join actors a on a.id = ma.id_actors
 where a."name" like '%Silva%'
   and g.description = 'Action'