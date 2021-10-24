/*==============================================================*/
/* DBMS name:      MySQL 5.0                                    */
/* Created on:     2021/10/24 18:03:20                          */
/*==============================================================*/


drop table if exists Music;

drop table if exists user;

/*==============================================================*/
/* Table: Music                                                 */
/*==============================================================*/
create table music
(
   id                   int not null auto_increment,
   title                char(255),
   artist               char(255),
   duration             int(64),
   size                 int(64),
   source               binary(5242880),
   album                char(255),
   album_photo          binary(65536),
   owner_id             integer not null,
   primary key (id)
);

/*==============================================================*/
/* Table: user                                                  */
/*==============================================================*/
create table user
(
   id                   int not null,
   user_id              integer,
   email                char(255),
   phone_number         char(20),
   login_name           char(20),
   nick_name            char(50),
   password             char(255),
   head_photo           binary(11664),
   primary key (id)
);

alter table music add constraint FK_Reference_1 foreign key (owner_id)
      references user (id) on delete restrict on update restrict;

