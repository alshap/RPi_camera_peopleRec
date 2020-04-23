
CREATE TABLE public.people_record
(
	id integer NOT NULL DEFAULT nextval('people_record_id_seq'::regclass),
	amount integer NOT NULL,
	datetime text COLLATE pg_catalog.'default' NOT NULL,
	CONSTRAINT people_record_pkey PRIMARY KEY (id)
)
WITH (
	OIDS = FALSE
)
