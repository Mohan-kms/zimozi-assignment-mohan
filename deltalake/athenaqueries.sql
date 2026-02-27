create external table orders(order_id INT,customer_name string,amount int, order_date date) partitioned by (year string,month string,day string) ROW FORMAT delimited fields terminated by ',' stored AS TEXTFILE location 's3://zimozi-mohan-2026-demo/datalake/orders/';
msck repair table orders;
select * from orders;
select * from orders where day='26';