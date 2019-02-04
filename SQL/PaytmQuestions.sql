#Command for printing Employees earning more than their bosses
select a.emp_id,a.name,a.salary from employee a where salary >(select b.salary from employee b where b.emp_id=a.boss_id);

#Command to print all the employees working in a different department from their bosses
select a.emp_id,a.boss_id,a.name,a.dept_id from employee a where a.dept_id not in (select b.dept_id from employee b where b.emp_id=a.boss_id);

#Print the department names of all employees
select a.emp_id,a.dept_id,b.department_name,a.name from employee a inner join department b 
where a.dept_id=b.dept_id;


select * from employee;
select * from department;
commit;