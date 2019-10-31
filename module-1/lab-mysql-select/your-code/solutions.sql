use publications;

#Challenge 1
select titleauthor.au_id, 
authors.au_lname as last_name, 
authors.au_fname as first_name, 
titles.title, 
publishers.pub_name as publisher
from titles
left join publishers
on titles.pub_id = publishers.pub_id
left join titleauthor
on titles.title_id = titleauthor.title_id
left join authors
on authors.au_id = titleauthor.au_id;

#Challenge 2
select authors.au_id as authorsID, 
authors.au_lname as last_name, 
authors.au_fname as first_name,
pubs.pub_name as Publisher,
count(title.title) as title_count
from publications.authors as authors
left join publications.titleauthor as ta
on authors.au_id=ta.au_id
left join publications.titles as title
on ta.title_id=title.title_id
left join publications.publishers as pubs
on title.pub_id = pubs.pub_id
group by authors.au_id,pubs.pub_name
;

#Challenge 3
select authors.au_id as authorsID, authors.au_lname as last_name, 
authors.au_fname as first_name,
sum(sales.qty) as total
from publications.authors as authors
left join publications.titleauthor as ta
on authors.au_id=ta.au_id
left join publications.titles as title
on ta.title_id=title.title_id
left join publications.sales as sales
on title.title_id=sales.title_id
group by authors.au_id
order by s desc
limit 3
;

#Challenge 4
select authors.au_id as author_ID, 
authors.au_lname as last_name, 
authors.au_fname as first_name,
sum(sales.qty) as total
from publications.authors as authors
left join publications.titleauthor as ta
on authors.au_id=ta.au_id
left join publications.titles as title
on ta.title_id=title.title_id
left join publications.sales as sales
on title.title_id=sales.title_id
group by authors.au_id
order by total desc
;