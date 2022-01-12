select d.name,
    round(sum((150 * a.hours) * (1 + (ws.bonus / 100))), 1) as salary
from doctors d
    inner join attendances a on a.id_doctor = d.id
    inner join work_shifts ws on ws.id = a.id_work_shift
group by d.name
order by salary desc