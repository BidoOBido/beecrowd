select c."name",
    o.id
from customers c
    inner join orders o on o.id_customers = c.id
where o.orders_date between '2016-01-01' and '2016-06-30'