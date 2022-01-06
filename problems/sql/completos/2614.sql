select c."name", r.rentals_date
  from customers c
 inner join rentals r on r.id_customers = c.id
 where r.rentals_date between '2016-09-01' and '2016-09-30'