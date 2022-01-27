##Query Start
##gives total rev per year , avg rev per year , movies released per year , total movies made less than 1cr per year 
##Temporary Tables
with less_Making_Movies AS(
	select YEAR(release_date)as year, count(movie_name) as total_movies_made_less
    From 
		movies
    Where cast(replace(replace(revenue_earned,",",""),"$","")as double)<10000000.00
    group by year
	order by year
)

##select * from less_Making_Movies;

select 
YEAR(release_date)as year ,
#replace to remove , and & and cast to make it into number format for arithematic operations
sum(cast(replace(replace(revenue_earned,",",""),"$","")as float)) as total_revenue_per_year,
AVG(cast(replace(replace(revenue_earned,",",""),"$","")as float)) as avg_revenue_per_year,
count(movie_name)as movies_released,
less_Making_Movies.total_movies_made_less
from movies
Right Join 
less_Making_Movies On
YEAR(movies.release_date) = less_Making_Movies.year
group by year
order by year;

##Query End
