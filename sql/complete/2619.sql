select pd."name",
  pv."name",
  pd.price
from products pd
  inner join providers pv on pv.id = pd.id_providers
  inner join categories ct on ct.id = pd.id_categories
where ct."name" = 'Super Luxury'
  and pd.price > 1000