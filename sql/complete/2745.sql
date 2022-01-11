select "name",
  round((salary * 0.1), 02) as tax
from people
where salary > 3000