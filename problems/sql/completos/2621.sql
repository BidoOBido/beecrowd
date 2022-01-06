select pt.name
from products pt
inner join providers pv on pv.id = pt.id_providers
where pt.amount between 10 and 20
  and pv.name like 'P%'