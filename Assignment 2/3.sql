.print Question 3 - penukond
select orders.product, products.description
from orders, products
where products.price > 2000 and orders.product = products.product_id
group by orders.product 
having count(orders.product) < 3;