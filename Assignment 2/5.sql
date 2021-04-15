.print Question 5 - penukond
select s.name
from  salesreps as s, offices
where s.rep_office = offices.office and (offices.city = 'Edmonton' or offices.city = 'Calgary')
and exists 	(select salesreps.manager
		from salesreps, offices
		where salesreps.emp_id = s.manager and salesreps.rep_office = offices.office and 
		not (offices.city = 'Edmonton' or offices.city = 'Calgary'));