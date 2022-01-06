select pd.name, pv."name"
  from products pd
 inner join providers pv on pv.id = pd.id_providers
 where pv."name" = 'Ajax SA'