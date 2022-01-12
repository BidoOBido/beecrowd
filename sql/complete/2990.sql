select e.cpf,
    e.enome,
    d.dnome
from empregados e
    inner join departamentos d on d.dnumero = e.dnumero
where e.cpf_supervisor is null
order by e.cpf asc