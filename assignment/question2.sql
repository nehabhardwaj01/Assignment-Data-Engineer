select
    d.DepartmentName,
    max(p.UnitPrice) as max_unit_price_per_department
from Product p
group by p.departmentID
right join Department d on p.departmentID = d.ID