select 'Approved: ' || "name" as "name",
  grade
from students
where grade >= 7
order by 2 desc