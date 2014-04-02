DROP TABLE IF EXISTS "rdb_user_profile";
CREATE TABLE rdb_user_profile(
	user_id bigserial primary key,
	user_password varchar(32),
	user_email varchar(256),
	user_mobile varchar(32),
	user_name varchar(128),
	user_nick varchar(128),
	login_type smallint,
	register_time timestamp,
	register_ip varchar(32),
	last_login_time timestamp,
	last_login_ip varchar(32),
	user_image varchar(32),
	real_name varchar(32),
	sex smallint,
	birth_year smallint,
	birth_month smallint,
	birth_day smallint,
	province varchar(128),
	city varchar(128),
	district varchar(512),
	signature varchar(512),
	third_key varchar(512),
	third_type smallint
);

DROP TABLE IF EXISTS "rdb_post";
CREATE TABLE rdb_post(
	id bigserial primary key,
	user_id bigint,
	book_id bigint,
	place_id bigint,
	post_content text,
	post_image varchar(32),
	post_source smallint,
	post_type smallint,
	create_time timestamp,
  	update_time timestamp,
  	post_status smallint,
  	post_audit smallint
  	);

DROP TABLE IF EXISTS "rdb_book";
CREATE TABLE rdb_book(
	id bigserial primary key,
	isbn10 varchar(32),
	isbn13 varchar(32),
	title varchar(128),
	origin_title varchar(128),
	alt_title varchar(128),
	sub_title varchar(128),
	book_image varchar(32),
	book_introduction text,
	book_recommended_text text,
	book_status smallint
 	);

DROP TABLE IF EXISTS "rdb_author";
CREATE TABLE rdb_author(
	id bigserial primary key,
	name varchar(128),
	origin_name varchar(128),
	introduction text,
	author_status smallint
	);

DROP TABLE IF EXISTS "rdb_publisher";
CREATE TABLE rdb_publisher(
	id bigserial primary key,
	name varchar(128),
	origin_name varchar(128),
	publisher_status smallint
	);

DROP TABLE IF EXISTS "rdb_book_author";
CREATE TABLE rdb_book_author(
	id bigserial primary key,
	book_id bigint,
	author_id bigint,
	status smallint
	);

DROP TABLE IF EXISTS "rdb_book_publisher";
CREATE TABLE rdb_book_publisher(
	id bigserial primary key,
	book_id bigint,
	publisher_id bigint,
	status smallint
	);

DROP TABLE IF EXISTS "rdb_user_third";
CREATE TABLE rdb_user_third(
	id bigserial primary key,
	third_key varchar(128)
	);
