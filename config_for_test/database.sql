CREATE DATABASE `python` CHARACTER SET utf8 COLLATE utf8_general_ci;
use python;

create table articles(id integer primary key auto_increment,
title varchar(1000) not null,
url varchar(1000) not null,
comments int,
thumbs int
)ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1;

insert into articles(title, url,comments,thumbs)
values('abc','http://abc',1,1);
insert into articles(title, url,comments,thumbs)
values('学习','http://abc/学习',1,1);

insert into articles (title, url,comments,thumbs)
values('Python 模拟登录和抓取文章', 'http://blog.csdn.net/flsmgf/article/details/78462939', '1', '1');
