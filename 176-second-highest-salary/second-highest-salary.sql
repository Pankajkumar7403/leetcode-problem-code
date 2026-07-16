# Write your MySQL query statement belows

select max(salary) as SecondHighestSalary 
from Employee
where salary<(
    select max(salary) from Employee
    
)