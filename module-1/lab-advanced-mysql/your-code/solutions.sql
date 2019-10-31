use publications;

#Challenge 1.
# Paso 1
select ta.title_id as ti, au_id as ai, 
t.price*s.qty*t.royalty/100*ta.royaltyper/100 as sr
 from  titleauthor as ta
inner join titles as t
on ta.title_id = t.title_id
inner join sales as s
on s.title_id=ta.title_id;	

#Paso 2
create temporary table publications.tt
select ta.title_id as ti, au_id as ai, 
t.price*s.qty*t.royalty/100*ta.royaltyper/100 as sr
 from  titleauthor as ta
inner join titles as t
on ta.title_id = t.title_id
inner join sales as s
on  s.title_id=ta.title_id;	

select ti, ai, sum(sr) as a from
tt group by ai, ti;

#Paso 3
select ti, ai, sum(sr) as a from
tt group by ai, ti
order by a desc limit 3;

#Challenge 2
select ti, ai, sum(sr) as a from
(select ta.title_id as ti, au_id as ai, 
t.price*s.qty*t.royalty/100*ta.royaltyper/100 as sr
 from  titleauthor as ta
inner join titles as t
on ta.title_id = t.title_id
inner join sales as s
on  s.title_id=ta.title_id) as g
group by ai, ti
order by a desc limit 3;	


#Challenge 3
CREATE TABLE publications.most_profiting_authors
select ti, sum(sr) as p
from tt 
group by ai, ti
order by p desc;