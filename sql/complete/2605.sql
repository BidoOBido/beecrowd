select p1."name",
    p2."name"
from products p1
    inner join providers p2 on p1.id_providers = p2.id
where p1.id_categories = 6