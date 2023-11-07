--
-- PostgreSQL database dump
--

-- Dumped from database version 15.4 (Homebrew)
-- Dumped by pg_dump version 15.4

-- Started on 2023-11-07 09:29:52 JST

SET statement_timeout = 0;
SET lock_timeout = 0;
SET idle_in_transaction_session_timeout = 0;
SET client_encoding = 'UTF8';
SET standard_conforming_strings = on;
SELECT pg_catalog.set_config('search_path', '', false);
SET check_function_bodies = false;
SET xmloption = content;
SET client_min_messages = warning;
SET row_security = off;

SET default_tablespace = '';

SET default_table_access_method = heap;

--
-- TOC entry 214 (class 1259 OID 16391)
-- Name: book_user; Type: TABLE; Schema: public; Owner: book_user
--

CREATE TABLE public.book_user (
    user_id character varying(255) NOT NULL,
    passwd character varying(255) NOT NULL,
    email character varying(255) NOT NULL,
    user_shi character varying(255),
    user_mei character varying(255),
    del boolean
);


ALTER TABLE public.book_user OWNER TO book_user;

--
-- TOC entry 216 (class 1259 OID 16399)
-- Name: books; Type: TABLE; Schema: public; Owner: book_user
--

CREATE TABLE public.books (
    id integer NOT NULL,
    name character varying(255),
    volume character varying(255),
    author character varying(255),
    publisher character varying(255),
    memo text,
    create_date timestamp with time zone NOT NULL,
    del boolean
);


ALTER TABLE public.books OWNER TO book_user;

--
-- TOC entry 215 (class 1259 OID 16398)
-- Name: books_id_seq; Type: SEQUENCE; Schema: public; Owner: book_user
--

CREATE SEQUENCE public.books_id_seq
    AS integer
    START WITH 1
    INCREMENT BY 1
    NO MINVALUE
    NO MAXVALUE
    CACHE 1;


ALTER TABLE public.books_id_seq OWNER TO book_user;

--
-- TOC entry 3620 (class 0 OID 0)
-- Dependencies: 215
-- Name: books_id_seq; Type: SEQUENCE OWNED BY; Schema: public; Owner: book_user
--

ALTER SEQUENCE public.books_id_seq OWNED BY public.books.id;


--
-- TOC entry 3465 (class 2604 OID 16402)
-- Name: books id; Type: DEFAULT; Schema: public; Owner: book_user
--

ALTER TABLE ONLY public.books ALTER COLUMN id SET DEFAULT nextval('public.books_id_seq'::regclass);


--
-- TOC entry 3612 (class 0 OID 16391)
-- Dependencies: 214
-- Data for Name: book_user; Type: TABLE DATA; Schema: public; Owner: book_user
--

COPY public.book_user (user_id, passwd, email, user_shi, user_mei, del) FROM stdin;
aaa	aaa	aaa	aaa	aaa	f
iii	iii	iii	iii	iii	f
\.


--
-- TOC entry 3614 (class 0 OID 16399)
-- Dependencies: 216
-- Data for Name: books; Type: TABLE DATA; Schema: public; Owner: book_user
--

COPY public.books (id, name, volume, author, publisher, memo, create_date, del) FROM stdin;
1	a	a	a	a		2023-10-26 10:49:29.971751+09	t
2	a	a	a	a		2023-10-26 10:49:29.998429+09	t
3	a	a	a	a		2023-10-26 10:49:39.551816+09	t
4	a	a	a	a		2023-10-26 11:32:18.810099+09	t
5	a	a	a	a		2023-10-26 11:34:15.377504+09	t
6	a	a	a	a		2023-10-26 11:34:23.570139+09	t
7	a	a	a	a		2023-10-26 11:49:10.791394+09	t
8	a	a	a	a		2023-10-30 11:03:58.935359+09	t
9	a	a	a	a	a	2023-10-31 11:00:11.585336+09	t
10	a	a	a	a		2023-10-31 11:00:20.135963+09	t
11	aa	a	a	a		2023-10-31 11:14:40.421375+09	t
12	a	a	a	a		2023-10-31 11:15:05.649309+09	t
13	あ	あ	あ	あ	あああa	2023-10-31 11:45:22.250536+09	t
14	呪術廻戦	1巻	芥見下々	集英社	おもしろい	2023-11-01 14:08:12.68171+09	f
\.


--
-- TOC entry 3621 (class 0 OID 0)
-- Dependencies: 215
-- Name: books_id_seq; Type: SEQUENCE SET; Schema: public; Owner: book_user
--

SELECT pg_catalog.setval('public.books_id_seq', 14, true);


--
-- TOC entry 3467 (class 2606 OID 16397)
-- Name: book_user book_user_pkey; Type: CONSTRAINT; Schema: public; Owner: book_user
--

ALTER TABLE ONLY public.book_user
    ADD CONSTRAINT book_user_pkey PRIMARY KEY (user_id);


--
-- TOC entry 3469 (class 2606 OID 16406)
-- Name: books books_pkey; Type: CONSTRAINT; Schema: public; Owner: book_user
--

ALTER TABLE ONLY public.books
    ADD CONSTRAINT books_pkey PRIMARY KEY (id);


-- Completed on 2023-11-07 09:29:53 JST

--
-- PostgreSQL database dump complete
--

