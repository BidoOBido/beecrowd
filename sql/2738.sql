select c."name", cast((((s.math*2)+(s."specific"*3)+(s.project_plan*5))/10) as numeric(4,2)) as "avg" 
  from candidate c
 inner join score s on s.candidate_id = c.id
 order by 2 desc