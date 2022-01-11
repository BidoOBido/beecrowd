(
   select 'Podium: ' || team
   from league
   order by "position"
   limit 3
)
union all
(
   select 'Demoted: ' || team
   from (
         select "position",
            team
         from league
         order by "position" desc
         limit 2
      ) as t
   order by "position"
)