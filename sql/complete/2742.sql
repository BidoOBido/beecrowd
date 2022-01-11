select lr."name",
  round((lr.omega * 1.618), 3) as "Fator N"
from life_registry lr
  inner join dimensions dm on dm.id = lr.dimensions_id
where dm."name" in ('C875', 'C774')
  and lr."name" like '%Richard%'
order by 2