select pd."name",
  pv."name",
  ct."name"
from products pd
  inner join providers pv on pv.id = pd.id_providers
  inner join categories ct on ct.id = pd.id_categories
where pv."name" = 'Sansul SA'
  and ct."name" = 'Imported'