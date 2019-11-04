--CREATE SCHEMA stackoverflow_filtered;
SET search_path TO stackoverflow_filtered;

SELECT city, COUNT(*)
FROM stackoverflow_filtered.results
GROUP BY city
HAVING COUNT(*) > 1;

SELECT DISTINCT	date(created_at), COUNT(*)
FROM stackoverflow_filtered.results
GROUP BY created_at;

select  distinct display_name, reputation, results.views, up_votes, view_count
FROM stackoverflow_filtered.results 
group by display_name, reputation, results.views, up_votes, view_count
order by reputation desc;

--Sibi has the highest reputation which means ;
--1. question is voted up: +5
--2. answer is voted up: +10
--3. answer is marked “accepted”: +15 (+2 to acceptor)
--4. suggested edit is accepted: +2 (up to +1000 total per user)
--5. bounty awarded to your answer: + full bounty amount
--Reputation is a rough measurement of how much the community trusts you; 
--it is earned by convincing your peers that you know what you’re talking about.