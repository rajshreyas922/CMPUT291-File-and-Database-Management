.print Question 2 - penukond
select salesreps.emp_id, count(orders.rep)
from salesreps left outer join orders
on orders.rep = salesreps.emp_id
group by salesreps.emp_id;



