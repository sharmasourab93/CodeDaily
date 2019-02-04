use pac;
select DATABASES;
select database();
show tables;


CREATE TABLE student(
first_name VARCHAR(30) NOT NULL,last_name VARCHAR(30) NOT NULL,email VARCHAR(60) NULL,
street VARCHAR(50) NOT NULL,CITY VARCHAR(40) NOT NULL,state CHAR(2) NOT NULL DEFAULT "PA",
zip MEDIUMINT UNSIGNED NOT NULL,phone VARCHAR(20) NOT NULL,birth_date DATE NOT NULL,
sex ENUM('M','F') NOT NULL,date_entered TIMESTAMP,lunch_cost FLOAT NULL,
student_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY);
insert into student value 
('Sale','Looper','slooper@aol.com','123 Not main Street','Nagima','TN',98991,'888-223-8901',"1959-2-21",'F',NOW(),2.50,NULL),
('Juno','Cooper','jcooper@aol.com','123 Juno St.','Hiroshima','JP',55555,'123-223-8901',"1966-4-22",'F',NOW(),3.55,NULL),
('Jubli','Cooper','jbcooper@aol.com','123 Junli St.','Kohima','MN',98989,'091-223-8901',"1959-5-12",'M',NOW(),3.50,NULL),
('Derek','Banas','db@aol.com','123 DB St.','Yakima','WA',98901,'792-223-8922',"1959-2-22",'M',NOW(),3.50,NULL),
('Jubliant','Dollar','JubliantDollar@aol.com','123 JD St.','NEWARK','NJ',98901,'294-223-8901',"1959-7-22",'M',NOW(),6.50,NULL),
('Ela','Cooper','ecooper@aol.com','123 Ela St.','Elamor','AZ',98544,'542-223-8901',"1959-8-22",'M',NOW(),3.50,NULL);
desc student;


CREATE TABLE class(
name VARCHAR(30) NOT NULL,class_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY);

CREATE TABLE test3(
date DATE NOT NULL,type ENUM('T','Q') NOT NULL,class_id INT UNSIGNED NOT NULL,
test_id INT UNSIGNED NOT NULL AUTO_INCREMENT PRIMARY KEY);

ALTER TABLE test3 
ADD maxscore INT NOT NULL AFTER type;
INSERT into test3 values 
('2014-8-25','Q',15,1,NULL),
('2014-8-27','Q',15,1,NULL),
('2014-8-29','T',30,1,NULL),
('2014-8-29','T',30,2,NULL),
('2014-8-27','Q',15,4,NULL),
('2014-8-29','T',30,4,NULL);
describe test3;
select * from test3;

create table score(
student_id INT UNSIGNED NOT NULL,event_id INT UNSIGNED NOT NULL,score INT NOT NULL,PRIMARY KEY(event_id,student_id));

ALTER TABLE score change event_id test_id,int unsigned NOT NULL;
DESCRIBE score;
insert into score values
(5,3,26),(5,4,27),(5,5,13),(5,6,27),(6,1,13),(6,2,13),(6,4,26),(6,5,13),(6,6,26),
(7,1,13),(7,2,13),(7,3,25),(7,4,27),(7,5,13),(8,1,14),(8,3,26),(8,4,23),(8,5,12),
(8,6,24),(1,1,15),(1,2,14),(1,3,28),(1,4,29),(1,5,15),(1,6,27),(2,1,15),(2,2,14),
(2,3,26),(2,4,28),(2,5,14),(2,6,26),(3,1,14),(3,2,14),(3,5,13);


create table absence( student_id INT UNSIGNED NOT NULL,date DATE not null,PRIMARY KEY(student_id,date));
describe absence;
insert into absence values
(6,'2014-08-29'),(7,'2014-08-29'),(8,'2014-08-27');


select  FIRST_NAME,LAST_NAME 
FROM student;

show tables;
RENAME TABLE 
absence to absences,
class to classes,
score to scores,
student to students,
test3 to tests;


select first_name,last_name,state from students where state="WA";
select first_name,last_name,state from students where YEAR(birth_date)>1959;
select first_name,last_name,birth_date from students where MONTH(birth_date)=2 or STATE="WA";
select last_name,state,birth_date from students where DAY(birth_date)>=12 && (state="WA"|| state="NJ");
select last_name from students where last_name is NOT NULL;
select first_name,last_name from students ORDER BY last_name DESC;
select first_name,last_name,state from students ORDER BY state DESC,last_name ASC;
select first_name,last_name,state from students LIMIT 5;#LIMIT 5,10
select CONCAT(first_name," ",last_name) AS 'NAME',CONCAT(city," ",state) AS 'HOMETOWN' from students;
select first_name,last_name from students where first_name LIKE 'D%' or last_name LIKE'%n';
select last_name,first_name from students where first_name LIKE '___y';
select DISTINCT state from students order by state;
select count(DISTINCT state) from students;
select count(*) from students where sex='M';
select sex,count(*) from students group by sex;
select MONTH(birth_date) as 'Month',count(*) from students,GROUP BY 'Month', ORDER BY 'Month';

use pac;

select state,count(state) as 'Amount' from students group by state having Amount>1;
select test_id as 'Test', MIN(score) as min,MAX(score) as max, max(score)-min(score) as 'range',sum(score) as total,avg(score) as average from scores group by test_id;


select * from absences;
select student_id, test_id from scores where student_id=6;
insert into scores values(6,3,24);
DELETE from absences where student_id=6;

ALTER table absences add column test_taken char(1) not null default 'F'after student_id;
ALTER TABLE absences modify column test_taken ENUM('T','F') not null default 'F';
ALTER TABLE absences DROP COLUMN test_taken;


update scores set score=25 where student_id=4 and test_id=3;
select first_name,last_name, birth_date from students where birth_date between '1960-1-1' AND '1970-1-1';
select first_name,last_name from students where first_name in ('Bobby','Derek','Dale');


select student_id,date,score,maxscore from tests,scores where date='2014-08-25' and tests.test_id =scores.test_id;
select scores.student_id,tests.date,scores.score,tests.maxscore from tests,scores where date='2014-08-25' and tests.test_id=scores.test_id;
select CONCAT(students.first_name," ",students.last_name) as Name,tests.date,scores.score,tests.maxscore from tests,scores,students where date='2014-08-25' and tests.test_id=scores.test_id and scores.student_id=students.student_id;

select students.student_id, concat(students.first_name," ",students.last_name) AS Name, count(absences.date) as absences from students,absences where students.student_id=absences.student_id group by students.student_id;

select students.student_id,concat(students.first_name," ",students.last_name) As Name,count(absences.date) AS absences from students LEFT JOIN absences on students.student_id=absences.student_id group by students.student_id;
select students.first_name,students.last_name,scores.test_id,scores.score from students INNER JOIN scores on students.student_id=scores.student_id where scores.score<=15 order by scores.test_id;