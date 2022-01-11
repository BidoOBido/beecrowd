select m.id,
  m."name"
from movies m
  inner join genres g on g.id = m.id_genres
  and g.description = 'Action'