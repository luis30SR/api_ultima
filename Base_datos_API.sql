PGDMP  $    .            
    {            db_luis2    16.1    16.1     �           0    0    ENCODING    ENCODING        SET client_encoding = 'UTF8';
                      false            �           0    0 
   STDSTRINGS 
   STDSTRINGS     (   SET standard_conforming_strings = 'on';
                      false            �           0    0 
   SEARCHPATH 
   SEARCHPATH     8   SELECT pg_catalog.set_config('search_path', '', false);
                      false            �           1262    16397    db_luis2    DATABASE     ~   CREATE DATABASE db_luis2 WITH TEMPLATE = template0 ENCODING = 'UTF8' LOCALE_PROVIDER = libc LOCALE = 'Spanish_Colombia.1252';
    DROP DATABASE db_luis2;
                postgres    false            �            1259    16409    movie    TABLE     �   CREATE TABLE public.movie (
    id character(36) NOT NULL,
    titulo character varying(50),
    duracion smallint,
    lanzamiento date
);
    DROP TABLE public.movie;
       public         heap    postgres    false            �          0    16409    movie 
   TABLE DATA           B   COPY public.movie (id, titulo, duracion, lanzamiento) FROM stdin;
    public          postgres    false    215   P       P           2606    16413    movie movie_pkey 
   CONSTRAINT     N   ALTER TABLE ONLY public.movie
    ADD CONSTRAINT movie_pkey PRIMARY KEY (id);
 :   ALTER TABLE ONLY public.movie DROP CONSTRAINT movie_pkey;
       public            postgres    false    215            �   �   x�u��m1�7c.^��3<���P�^�B��,�syK�
�����<a�ĀPc�R�k���\LQ�'��$��f������`���9Y��ocg�1�ً���x>����a��q��e+��5�;a4on�h��ݠYf �۽�F����r�x7[�+��#����>�     