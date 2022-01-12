select name,
    sum(matches) as matches,
    sum(victories) as victories,
    sum(defeats) as defeats,
    sum(draws) as draws,
    sum((victories * 3) + (draws)) as score
from (
        select t.name,
            count(1) as matches,
            sum(
                case
                    when m.team_1_goals > m.team_2_goals then 1
                    else 0
                end
            ) as victories,
            sum(
                case
                    when m.team_1_goals < m.team_2_goals then 1
                    else 0
                end
            ) as defeats,
            sum(
                case
                    when m.team_1_goals = m.team_2_goals then 1
                    else 0
                end
            ) as draws
        from teams t
            inner join matches m on m.team_1 = t.id
        group by name
        union all
        select t.name,
            count(1) as matches,
            sum(
                case
                    when m.team_2_goals > m.team_1_goals then 1
                    else 0
                end
            ) as victories,
            sum(
                case
                    when m.team_2_goals < m.team_1_goals then 1
                    else 0
                end
            ) as defeats,
            sum(
                case
                    when m.team_2_goals = m.team_1_goals then 1
                    else 0
                end
            ) as draws
        from teams t
            inner join matches m on m.team_2 = t.id
        group by name
    ) as t
group by name
order by score desc,
    name asc