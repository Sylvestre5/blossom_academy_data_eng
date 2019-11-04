CREATE SCHEMA stackoverflow_filtered;
SET search_path TO stackoverflow_filtered;
--CREATE TABLE results();

CREATE INDEX ind_btree_reputation ON stackoverflow_filtered.results USING BTREE(reputation);

CREATE INDEX ind_hash_display_name ON stackoverflow_filtered.results USING HASH(display_name);

CREATE VIEW stackoverflow_filtered."view_filtered_results" AS 
SELECT display_name, city, question_id
FROM stackoverflow_filtered.results
WHERE accepted_answer_id IS NOT NULL;

CREATE MATERIALIZED VIEW IF NOT EXISTS stackoverflow_filtered."mat_view_filtered_results" AS
SELECT display_name, city, question_id
FROM stackoverflow_filtered.results
WHERE accepted_answer_id IS not null;

--Views                                            Materialize views
--1. not stored physically                         Stored on a disk
--2. Updated upon usage                            Updated manually using triggers
--3. Is a display hence no memory space required   Utilize memory space as it is stored physically