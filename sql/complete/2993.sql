select amount
from value_table vt
group by amount
order by count(amount) desc
limit 1