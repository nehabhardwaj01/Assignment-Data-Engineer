select
    department,
    count(*) as total_count
from Employees
group by department
having sum(salary) > 15000
order by total_count desc;