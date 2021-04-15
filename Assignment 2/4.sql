.print Question 4 - penukond
select products.description, products.price, Products.qty_on_hand, sum(orders.qty)
from orders, products
where orders.product = products.product_id
group by products.product_id having 0.75*Products.qty_on_hand < sum(orders.qty);