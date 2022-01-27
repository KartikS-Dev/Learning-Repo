create database moviesdata;
use moviesdata;
create table movies(
movie_name varchar(99),
release_date varchar(99),
revenue_earned varchar(999)
);

select * from moviesdata.movies;

Select 
dISTINCT (SUBSTR(release_date,1,4)) AS YEAR,
(SELECT SUM(revenue_earned) FROM movies
Where revenue_earned=(
select revenue_earned from movies group by 
)
)
as totalRevenue
From moviesdata.movies;



