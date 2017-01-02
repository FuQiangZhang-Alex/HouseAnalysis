
CREATE SCHEMA IF NOT EXISTS stage;

DROP TABLE IF EXISTS stage.house_index;
CREATE TABLE stage.house_index (
	name VARCHAR(2048),
	href VARCHAR(2048),
	city VARCHAR(255),
	house_type VARCHAR(2048),
	title_img VARCHAR(2048),
	price VARCHAR(2048),
	address VARCHAR(2048),
	tel VARCHAR(2048),
	source VARCHAR(2048),
	tags VARCHAR(2048),
	addtion VARCHAR(4096),
	upd_time timestamp default now()
);
ALTER TABLE stage.house_index ADD PRIMARY KEY (name, href);

delete from stage.house_index;

select count(*) from stage.house_index hi
where hi.source like '%fang.com';


