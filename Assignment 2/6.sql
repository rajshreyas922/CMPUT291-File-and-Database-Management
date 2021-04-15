.print Question 6 - penukond
select o.city
from offices o
where o.sales > (select sum(salesreps.sales)
		 from salesreps
		 where o.office = salesreps.rep_office);