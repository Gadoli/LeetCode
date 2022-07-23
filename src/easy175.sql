/* Write your MySQL query statement below
LeetCode - Easy 175. Combine Two Tables
*/
select firstName, lastName, city, state
from Person left join Address
on Person.PersonId = Address.PersonId;
