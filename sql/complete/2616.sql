select c.id,
  c."name"
from customers c
  left join locations l on l.id_customers = c.id
where l.id is null
order by 1