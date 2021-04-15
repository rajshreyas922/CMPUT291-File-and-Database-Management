.print Question 7 - penukond
select products.description
from orders, products
where orders.product = products.product_id
group by orders.product having count(orders.product) = (select max(c)
							from( 
							select count(orders.product) as c
							from orders
							group by orders.product));
