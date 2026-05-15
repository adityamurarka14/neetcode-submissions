-- Write your query below
-- select name
-- from customers
-- where id not in (select customer_id from orders)

select c.name
from customers c
where not exists (
    select 1 from orders o
    where o.customer_id = c.id
)