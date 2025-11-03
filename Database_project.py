set serveroutput on;
drop table Institution cascade constraints;
drop table Conferenceuser cascade constraints;
drop table Conference cascade constraints;
drop table ConferenceSession cascade constraints;
drop table ConferenceRole cascade constraints;
drop table Paper cascade constraints;
drop table PaperAuthor cascade constraints;
drop table Topic cascade constraints;
drop table PaperTopic cascade constraints;
drop table PaperBid cascade constraints;
drop table Registration cascade constraints;
drop table PaperReview cascade constraints;
drop table Message cascade constraints;

-- Table to store institutions

CREATE TABLE Institution (
institution_id int,
institution_name VARCHAR2(100),
country VARCHAR2(100),
primary key(institution_id));

-- Table to store users (aNiliated with one institution)

CREATE TABLE Conferenceuser(
user_id int,
institution_id int ,
user_name VARCHAR2(100),
address VARCHAR2(200),
zipcode VARCHAR2(10),
email VARCHAR2(100),
user_country VARCHAR2(100),
primary key(user_id),
foreign key(institution_id) references Institution(institution_id)
);

-- Table to store conferences

CREATE TABLE Conference (
conference_id int,
conference_title VARCHAR2(200),
conference_year int,
start_date DATE,
end_date DATE,
submission_due_time TIMESTAMP,
review_due_time TIMESTAMP,
camera_ready_due_time TIMESTAMP,
conference_city VARCHAR2(100),
conference_country VARCHAR2(100),
early_registration_date DATE,
early_registration_fee NUMBER,
regular_registration_fee NUMBER,
primary key(conference_id)
);

-- Table to store conference sessions

CREATE TABLE ConferenceSession (
session_id int,
conference_id int,
session_chair_user_id int,
session_title VARCHAR2(200),
start_time TIMESTAMP,
end_time TIMESTAMP,
primary key(session_id),
foreign key(conference_id) references Conference(conference_id)
);

-- Table to store user roles in conferences

CREATE TABLE ConferenceRole (
user_id INT ,
conference_id INT ,
con_role VARCHAR2(50), -- instead of role - con_role
PRIMARY KEY (user_id, conference_id, con_role),
FOREIGN KEY(user_id) REFERENCES ConferenceUser(user_id),
FOREIGN KEY(conference_id) REFERENCES Conference(conference_id)
);

-- Table to store papers

CREATE TABLE Paper(
paper_id int ,
conference_id int,
title VARCHAR2(300),
submit_time TIMESTAMP,
avg_review_score NUMBER(3, 2),
status VARCHAR2(50),
session_id int,
PRIMARY KEY(paper_id),
FOREIGN KEY(session_id) REFERENCES ConferenceSession(session_id),
FOREIGN KEY(conference_id) REFERENCES Conference(conference_id)
);

-- Table to store paper authors

CREATE TABLE PaperAuthor (
paper_id int,
author_user_id int,
author_order NUMBER,
PRIMARY KEY (paper_id, author_user_id),
FOREIGN KEY(paper_id) REFERENCES Paper(paper_id),
FOREIGN KEY(author_user_id) REFERENCES ConferenceUser(user_id)
);

-- Table to store topics

CREATE TABLE Topic (
topic_id INT,
topic_name VARCHAR2(100),
PRIMARY KEY(topic_id)
);

-- Table to associate papers with topics

CREATE TABLE PaperTopic (
paper_id INT,
topic_id INT,
PRIMARY KEY (paper_id, topic_id),
FOREIGN KEY(paper_id) REFERENCES Paper(paper_id),
FOREIGN KEY(topic_id) REFERENCES Topic(topic_id)
);

-- Table for reviewers bidding on papers

CREATE TABLE PaperBid (
bid_id INT,
reviewer_user_id INT,
paper_id INT,
PRIMARY KEY(bid_id),
FOREIGN KEY(reviewer_user_id) REFERENCES ConferenceUser(user_id),
FOREIGN KEY(paper_id) REFERENCES Paper(paper_id)
);

-- Table to store Paper Review

CREATE TABLE PaperReview (
review_id INT PRIMARY KEY,
reviewer_user_id INT REFERENCES ConferenceUser(user_id),
paper_id INT REFERENCES Paper(paper_id),
review_score NUMBER(2, 1),
comments VARCHAR(1000),
review_upload_time TIMESTAMP
);

-- Table to store Registration

CREATE TABLE Registration (
registration_id INT PRIMARY KEY,
conference_id INT REFERENCES Conference(conference_id),
user_id INT REFERENCES ConferenceUser(user_id),
registration_fee INT,
payment_date DATE,
payment_status VARCHAR(20)
);

-- Table to store Messages
CREATE TABLE Message (
message_id INT PRIMARY KEY,
user_id INT REFERENCES ConferenceUser(user_id),
message_time TIMESTAMP,
message_body VARCHAR2(1000)
);

insert into institution values(1, 'UMBC', 'USA');
insert into institution values(2, 'IITB', 'INDIA');
insert into institution values(3, 'ICL', 'UK');
insert into institution values(4, 'UCD', 'IRELAND');
insert into institution values(5, 'CBS', 'DENMARK');

insert into conferenceuser values(1, 1, 'Aakash', '218 Garden Ridge Road', '21228',
'is620group80@gmail.com', 'INDIA');
insert into conferenceuser values(2, 2, 'Mansi', '219 Garden Ridge Road', '21229',
'is620group81@gmail.com', 'TURKEY');
insert into conferenceuser values(3, 3, 'Akanksha', '220 Garden Ridge Road', '21230',
'is620group82@gmail.com', 'BULGARIA');
insert into conferenceuser values(4, 4, 'Vishv', '221 Garden Ridge Road', '21231',
'is620group83@gmail.com', 'INDIA');
insert into conferenceuser values(5, 4, 'Ranveer', '222 Garden Ridge Road', '21232',
'is620group84@gmail.com', 'INDIA');

INSERT INTO conference VALUES (
1, 'Quantum Physics Symposium', 2024,
TO_DATE('2024-05-01', 'YYYY-MM-DD'),
TO_DATE('2024-05-03', 'YYYY-MM-DD'),
TO_DATE('2024-02-15 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
TO_DATE('2024-03-15 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
TO_DATE('2024-04-01 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
'New York',
'USA',
TO_DATE('2024-01-15', 'YYYY-MM-DD'),
200,
300
);

INSERT INTO conference VALUES (
2, 'Astrophysics and Cosmology Conference', 2024,
TO_DATE('2024-06-10', 'YYYY-MM-DD'),
TO_DATE('2024-06-12', 'YYYY-MM-DD'),
TO_DATE('2024-03-30 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
TO_DATE('2024-04-30 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
TO_DATE('2024-05-10 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
'London',
'UK',
TO_DATE('2024-02-15', 'YYYY-MM-DD'),
150,
250
);

INSERT INTO conference VALUES (
3, 'Particle Physics Summit', 2024,
TO_DATE('2024-07-20', 'YYYY-MM-DD'),
TO_DATE('2024-07-22', 'YYYY-MM-DD'),
TO_DATE('2024-04-30 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
TO_DATE('2024-05-30 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
TO_DATE('2024-06-15 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
'Berlin',
'Germany',
TO_DATE('2024-03-15', 'YYYY-MM-DD'),
180,
280
);

INSERT INTO conference VALUES (
4, 'Nuclear Physics Forum', 2024,
TO_DATE('2024-08-15', 'YYYY-MM-DD'),
TO_DATE('2024-08-17', 'YYYY-MM-DD'),
TO_DATE('2024-05-15 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
TO_DATE('2024-06-15 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
TO_DATE('2024-07-01 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
'Sydney',
'Australia',
TO_DATE('2024-04-01', 'YYYY-MM-DD'),
220,
350
);

INSERT INTO conference VALUES (
5, 'Theoretical Physics Conference', 2024,
TO_DATE('2024-09-05', 'YYYY-MM-DD'),
TO_DATE('2024-09-07', 'YYYY-MM-DD'),
TO_DATE('2024-06-20 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
TO_DATE('2024-07-20 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
TO_DATE('2024-08-05 23:59:59', 'YYYY-MM-DD HH24:MI:SS'),
'Tokyo',
'Japan',
TO_DATE('2024-05-01', 'YYYY-MM-DD'),
200,
300
);

-- Additional randomized entries with multiple roles for users across conferences

INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (1, 2, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (1, 3, 'Reviewer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (1, 4,
'Participant');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (1, 5, 'Author');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (1, 5, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (2, 1, 'Reviewer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (2, 2, 'Author');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (2, 3,
'Participant');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (2, 4, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (2, 5, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (3, 1,
'Participant');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (3, 2, 'Author');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (3, 3, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (3, 4, 'Reviewer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (3, 5, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (4, 1, 'Author');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (4, 2, 'Reviewer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (4, 3, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (4, 4, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (4, 5,
'Participant');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (5, 1, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (5, 2,
'Participant');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (5, 3, 'Author');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (5, 4, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (5, 5, 'Reviewer');

-- Additional roles within the same conferences for some users

INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (1, 3, 'Author');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (2, 3, 'Reviewer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (3, 1, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (4, 5, 'Author');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (5, 2, 'Organizer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (1, 2, 'Reviewer');
INSERT INTO ConferenceRole (user_id, conference_id, con_role) VALUES (2, 2, 'Reviewer');

-- Inserting 5 records into ConferenceSession table

INSERT INTO ConferenceSession VALUES (
1, 1, 101, 'Quantum Computing Advances',
TO_TIMESTAMP('2024-05-01 09:00:00', 'YYYY-MM-DD HH24:MI:SS'),
TO_TIMESTAMP('2024-05-01 10:30:00', 'YYYY-MM-DD HH24:MI:SS')
);
INSERT INTO ConferenceSession VALUES (
2, 2, 102, 'Dark Matter and Cosmology',
TO_TIMESTAMP('2024-06-10 11:00:00', 'YYYY-MM-DD HH24:MI:SS'),
TO_TIMESTAMP('2024-06-10 12:30:00', 'YYYY-MM-DD HH24:MI:SS')
);
INSERT INTO ConferenceSession VALUES (
3, 3, 103, 'Higgs Boson Discoveries',
TO_TIMESTAMP('2024-07-20 14:00:00', 'YYYY-MM-DD HH24:MI:SS'),
TO_TIMESTAMP('2024-07-20 15:30:00', 'YYYY-MM-DD HH24:MI:SS')
);
INSERT INTO ConferenceSession VALUES (
4, 4, 104, 'Nuclear Reactor Safety',
TO_TIMESTAMP('2024-08-15 10:00:00', 'YYYY-MM-DD HH24:MI:SS'),
TO_TIMESTAMP('2024-08-15 11:30:00', 'YYYY-MM-DD HH24:MI:SS')
);
INSERT INTO ConferenceSession VALUES (
5, 5, 105, 'String Theory and Beyond',
TO_TIMESTAMP('2024-09-05 16:00:00', 'YYYY-MM-DD HH24:MI:SS'),
TO_TIMESTAMP('2024-09-05 17:30:00', 'YYYY-MM-DD HH24:MI:SS')
);
-- Inserting 5 records into Paper table
INSERT INTO Paper VALUES (
1, 1, 'Quantum Cryptography: A New Era of Security',
TO_TIMESTAMP('2024-02-10 10:30:00', 'YYYY-MM-DD HH24:MI:SS'),
4.5, 'Accepted', 1
);
INSERT INTO Paper VALUES (
2, 2, 'Dark Energy Exploration: Expanding the Universe',
TO_TIMESTAMP('2024-03-20 12:00:00', 'YYYY-MM-DD HH24:MI:SS'),
4.7, 'Rejected', 2
);
INSERT INTO Paper VALUES (
3, 3, 'The Higgs Mechanism and Beyond',
TO_TIMESTAMP('2024-04-15 15:00:00', 'YYYY-MM-DD HH24:MI:SS'),
4.3, 'Submitted', 3
);
INSERT INTO Paper VALUES (
4, 4, 'Safety Measures in Modern Nuclear Reactors',
TO_TIMESTAMP('2024-05-25 09:45:00', 'YYYY-MM-DD HH24:MI:SS'),
4.1, 'Under Review', 4
);
INSERT INTO Paper VALUES (
5, 5, 'String Theory: Implications for Quantum Gravity',
TO_TIMESTAMP('2024-06-10 14:15:00', 'YYYY-MM-DD HH24:MI:SS'),
4.6, 'Camera Ready Received', 5
);
INSERT INTO Paper VALUES (
10, 2, 'String Theory: Implications for Quantum Gravity',
TO_TIMESTAMP('2024-06-10 14:15:00', 'YYYY-MM-DD HH24:MI:SS'),
4.6, 'Camera Ready Received', 5
);

INSERT INTO PaperAuthor VALUES (1, 1, 1);
INSERT INTO PaperAuthor VALUES (1, 2, 2);
INSERT INTO PaperAuthor VALUES (2, 3, 1);
INSERT INTO PaperAuthor VALUES (3, 4, 1);
INSERT INTO PaperAuthor VALUES (4, 5, 1);
INSERT INTO PaperAuthor VALUES (10, 1, 5);
INSERT INTO Topic VALUES (100, 'Cyber Security');
INSERT INTO Topic VALUES (101, 'Data Science ');
INSERT INTO Topic VALUES (102, 'Machine Learning');
INSERT INTO Topic VALUES (104, 'Information System');
INSERT INTO Topic VALUES (105, 'Cloud Computing');

-- Inserting 5 records into PaperTopic table

INSERT INTO PaperTopic VALUES (1, 100); -- Paper 1: "Quantum Cryptography: A New Era
of Security" is related to "Cyber Security"
INSERT INTO PaperTopic VALUES (2, 101); -- Paper 2: "Dark Energy Exploration: Expanding
the Universe" is related to "Data Science"
INSERT INTO PaperTopic VALUES (3, 102); -- Paper 3: "The Higgs Mechanism and Beyond"
is related to "Machine Learning"
INSERT INTO PaperTopic VALUES (4, 104); -- Paper 4: "Safety Measures in Modern Nuclear
Reactors" is related to "Information System"
INSERT INTO PaperTopic VALUES (5, 105); -- Paper 5: "String Theory: Implications for
Quantum Gravity" is related to "Cloud Computing"
INSERT INTO PaperBid VALUES (10 , 1, 1);
INSERT INTO PaperBid VALUES (11, 2, 2);
INSERT INTO PaperBid VALUES (12, 3, 3);
INSERT INTO PaperBid VALUES (13, 4, 4);
INSERT INTO PaperBid VALUES (15, 4, 2);
INSERT INTO PaperBid VALUES (14, 5, 5);
INSERT INTO PaperBid VALUES (20, 4, 10);
INSERT INTO PaperReview VALUES (1, 1, 1, 4.5, 'Excellent insights into quantum security
techniques.', TO_TIMESTAMP('2024-02-15 11:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO PaperReview VALUES (6, 1, 1, 5, 'Excellent insights into quantum security
techniques.', TO_TIMESTAMP('2024-02-15 11:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO PaperReview VALUES (12, 1, 1, 5, NULL, TO_TIMESTAMP('2024-02-15
11:00:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO PaperReview VALUES (2, 2, 2, 4.7, 'A comprehensive study with significant
implications.', TO_TIMESTAMP('2024-03-22 09:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO PaperReview VALUES (11, 2, 2, NULL, NULL , TO_TIMESTAMP('2024-03-22
09:30:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO PaperReview VALUES (3, 3, 3, 4.3, 'Interesting perspective, though some
areas need more depth.', TO_TIMESTAMP('2024-04-18 14:00:00', 'YYYY-MM-DD
HH24:MI:SS'));
INSERT INTO PaperReview VALUES (4, 4, 4, 4.1, 'A solid review of safety protocols, but lacks
recent data.', TO_TIMESTAMP('2024-05-27 16:45:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO PaperReview VALUES (5, 4, 2, 4.1, 'A solid review of safety protocols, but lacks
recent data.', TO_TIMESTAMP('2024-05-27 16:45:00', 'YYYY-MM-DD HH24:MI:SS'));
INSERT INTO PaperReview VALUES (7, 5, 5, 4.6, 'Well-written and thought-provoking, with
great references.', TO_TIMESTAMP('2024-06-12 10:30:00', 'YYYY-MM-DD HH24:MI:SS'));

-- Inserting 5 records into the Registration table

INSERT INTO Registration VALUES (
1, 1, 1, 200, TO_DATE('2024-01-15', 'YYYY-MM-DD'), 'Paid' -- Registration for Quantum
Physics Symposium by user 1
);
INSERT INTO Registration VALUES (
2, 2, 2, 150, TO_DATE('2024-02-20', 'YYYY-MM-DD'), 'Paid' -- Registration for Astrophysics
and Cosmology Conference by user 2
);
INSERT INTO Registration VALUES (
3, 3, 3, 180, TO_DATE('2024-03-25', 'YYYY-MM-DD'), 'Pending' -- Registration for Particle
Physics Summit by user 3
);
INSERT INTO Registration VALUES (
4, 4, 4, 220, TO_DATE('2024-04-10', 'YYYY-MM-DD'), 'Paid' -- Registration for Nuclear
Physics Forum by user 4
);
INSERT INTO Registration VALUES (
5, 5, 5, 200, TO_DATE('2024-05-05', 'YYYY-MM-DD'), 'Paid' -- Registration for Theoretical
Physics Conference by user 5
);
-- Inserting 5 records into the Message table
INSERT INTO Message VALUES (
1, 1, TO_TIMESTAMP('2024-01-10 08:30:00', 'YYYY-MM-DD HH24:MI:SS'),
'Looking forward to the ICML conference in 2024!'
);
INSERT INTO Message VALUES (
2, 2, TO_TIMESTAMP('2024-02-15 10:45:00', 'YYYY-MM-DD HH24:MI:SS'),
'KDD 2024 is going to be an exciting opportunity for learning.'
);
INSERT INTO Message VALUES (
3, 3, TO_TIMESTAMP('2024-03-20 12:00:00', 'YYYY-MM-DD HH24:MI:SS'),
'Can’t wait for the ACL conference presentations!'
);
INSERT INTO Message VALUES (
4, 4, TO_TIMESTAMP('2024-04-05 14:20:00', 'YYYY-MM-DD HH24:MI:SS'),
'The ICIS 2024 lineup is impressive.'
);
INSERT INTO Message VALUES (
5, 5, TO_TIMESTAMP('2024-05-12 09:10:00', 'YYYY-MM-DD HH24:MI:SS'),
'I am ready for ICSE 2024 and looking forward to meeting industry experts.'
);
/*

-- Retrieving all values from each table

SELECT * FROM Institution;
SELECT * FROM ConferenceUser;
SELECT * FROM Conference;
SELECT * FROM ConferenceSession;
SELECT * FROM ConferenceRole;
SELECT * FROM Paper;
SELECT * FROM PaperAuthor;
SELECT * FROM Topic;
SELECT * FROM PaperTopic;
SELECT * FROM PaperBid;
SELECT * FROM Registration;
SELECT * FROM PaperReview;
SELECT * FROM Message;
*/

--Feature 9: *** (Challenging)

--Assign a paper to a reviewer.

--Input: a paper ID, maximal number of papers a reviewer can review. This procedure tries
to find a reviewer who has no conflict of interest, has not reached capacity
--, and has not reviewed the input paper. Priority is given to those who have bid for this
paper.
--The procedure does the following:
--1) first check whether the paper ID is valid. If not print a message invalid paper ID and
stop.
--2) use an explicit cursor to find users who have 'Reviewer' role at the conference this
paper was submitted to, and these users have no conflict of interest
--(meaning the users' institution does not match the institution of any author of the paper),
and has not reviewed this paper.
--You can use not exists subquery here.
--3) for each such user, check whether the user has reviewed the maximal number of
papers allowed (an input parameter) for the conference this paper is submitted to.
--If so, print 'User X has reached capacity' where X is user id.
--4) if the user has not reached capacity, check whether the (explicit cursor and if loop
filtered user_ids) has bid for the paper.
--If so, print 'Assign to user X' where X is user ID. Insert a row into review table with a new
review ID, user id as this user's ID, paper ID as input paper ID,
--and lead other columns null. Stop the procedure.
--5) if after checking all users in step 2, no reviewer has been assigned, print 'no one has
bid for this paper',

select * from paperreview;
drop sequence rid;
create sequence rid start with 20;
/*
create or replace procedure assign_paper_reviewer(paperID IN paper.paper_ID%type,
max_rev_limit IN int)
IS
check_paper_id int;

--step 2
cursor c1 is select cu.user_id from paper p, conference c, conferencerole cr,
conferenceuser cu where p.conference_id= c.conference_id and
c.conference_id = cr.conference_id and cr.user_id = cu.user_id and cr.con_role = 'Reviewer'
and p.paper_id = paperid and cu.institution_id not in
(select institution_id from paper p, paperauthor pa, conferenceuser cu where p.paper_id =
pa.paper_id and pa.author_user_id = cu.user_id and p.paper_id = paperid);
check_if_reviewer_assigned int;
check_capacity int;
check_user_bid int;
begin

--step 1
select count(*) into check_paper_id from paper where paper_id=paperid;
if check_paper_id = 0 then
dbms_output.put_line('invalid paper ID');
else
select count(*) into check_if_reviewer_assigned from paper p, conference c,
conferencerole cr, conferenceuser cu where p.conference_id= c.conference_id and
c.conference_id = cr.conference_id and cr.user_id = cu.user_id and cr.con_role =
'Reviewer' and p.paper_id = paperid and cu.institution_id not in
(select institution_id from paper p, paperauthor pa, conferenceuser cu where p.paper_id
= pa.paper_id and pa.author_user_id = cu.user_id and p.paper_id = paperid);
if check_if_reviewer_assigned = 0 then
dbms_output.put_line('no one has the role reviewer and has no conflict of interest');
else
for item in c1
loop

--step 3
select count(*) into check_capacity from paperreview where reviewer_user_id =
item.user_id and paper_id = paperID;
--for conference in the above join, paper id has been checked.
if check_capacity >= max_rev_limit then
--step 5
dbms_output.put_line('User ' || item.user_id || ' has reached capacity');
else

--step 4
select count(*) into check_user_bid from paperbid where reviewer_user_id =
item.user_id;
if check_user_bid = 0 then
dbms_output.put_line('no one has bid for this paper');
else
dbms_output.put_line('Assign to ' || item.user_id);
insert into paperreview values(rid.nextval, item.user_id, paperID, NULL,
NULL, NULL);
end if;
end if;
end loop;
end if;
end if;
end;
/
*/
create or replace procedure assign_paper_reviewer(paperID IN paper.paper_ID%type,
max_rev_limit IN int)
IS
check_paper_id int;

--step 2
cursor c1 is select cu.user_id from paper p, conference c, conferencerole cr,
conferenceuser cu where p.conference_id= c.conference_id and
c.conference_id = cr.conference_id and cr.user_id = cu.user_id and cr.con_role = 'Reviewer'
and p.paper_id = paperid and cu.institution_id not in
(select institution_id from paper p, paperauthor pa, conferenceuser cu where p.paper_id =
pa.paper_id and pa.author_user_id = cu.user_id and p.paper_id = paperid);
check_if_reviewer_assigned int;
check_capacity int;
check_capacity_again int;
check_user_bid int;
begin

--step 1
select count(*) into check_paper_id from paper where paper_id=paperid;
if check_paper_id = 0 then
dbms_output.put_line('invalid paper ID');
else
select count(*) into check_if_reviewer_assigned from paper p, conference c,
conferencerole cr, conferenceuser cu where p.conference_id= c.conference_id and
c.conference_id = cr.conference_id and cr.user_id = cu.user_id and cr.con_role =
'Reviewer' and p.paper_id = paperid and cu.institution_id not in
(select institution_id from paper p, paperauthor pa, conferenceuser cu where p.paper_id
= pa.paper_id and pa.author_user_id = cu.user_id and p.paper_id = paperid);
if check_if_reviewer_assigned = 0 then
dbms_output.put_line('no one has the role reviewer and has no conflict of interest');
else
for item in c1
loop

--step 3
select count(*) into check_capacity from paperreview where reviewer_user_id =
item.user_id and paper_id = paperID;
--for conference in the above join, paper id has been checked.
if check_capacity >= max_rev_limit then
--step 5
dbms_output.put_line('User ' || item.user_id || ' has reached capacity');
else

--step 4
select count(*) into check_user_bid from paperbid where reviewer_user_id =
item.user_id and paper_id = paperid;
if check_user_bid = 0 then
dbms_output.put_line('no one has bid for this paper');

-- step 6
dbms_output.put_line('Assign to ' || item.user_id || ' since no one has bid for
this paper');
DBMS_OUTPUT.NEW_LINE;
DBMS_OUTPUT.NEW_LINE;
insert into paperreview values(rid.nextval, item.user_id, paperID, NULL,
NULL, NULL);
else
NULL, NULL);
end if;
end if;
end loop;
end if;
end if;
end;
/
dbms_output.put_line('Assign to ' || item.user_id);
DBMS_OUTPUT.NEW_LINE;
insert into paperreview values(rid.nextval, item.user_id, paperID, NULL,
exec assign_paper_reviewer(10,12);
select * from paperreview;
select cu.user_id from paper p, conference c, conferencerole cr, conferenceuser cu where
p.conference_id= c.conference_id and
c.conference_id = cr.conference_id and cr.user_id = cu.user_id and cr.con_role = 'Reviewer'
and p.paper_id = paperid and cu.institution_id not in
(select institution_id from paper p, paperauthor pa, conferenceuser cu where p.paper_id =
pa.paper_id and pa.author_user_id = cu.user_id and p.paper_id = paperid);
select count(*) from paperreview pr, paper p where p.paper_id = pr.paper_id and
reviewer_user_id = 4 and p.paper_id = 2;
drop sequence mid;
create sequence mid start with 6;
select * from message;
--Feature 10: Send a review reminder. Input: a conference ID and an input time.
--The procedure does the following:
--1) it first checks whether the conference ID is valid. If not print a message 'Invalid
conference ID';
-- Implicit cursor
--2) it then finds all reviews for papers submitted in the conference and the review due time
has passed but the review has not yet been uploaded.
--The review due time is passed means the review due time is earlier than the input time.
--The review is not uploaded if the review score or review comment is null.
--Explicit Cursor retrieves review_id. Join between conference, conferencerole,
conferenceuser and Paperreview.
--3) for each past-due review found in step 2, insert a row to the message table with a newly
generated message ID,
-- user id as the user id of the review, and message time as the input time, and message
body as
--'Your review for paper X submitted to conference Y is past-due, please upload your review
asap', where X is the paper ID of the review,
--and Y is the title of the conference. Please also print a message 'Sent reminder to user X
for missing review for paper Y' where X is user id and y is paper ID.
Create or replace procedure Review_reminder(p_conference_id in
conference.conference_id%type, due_time in timestamp)
is
check_conference_id int;
cursor c1 is select conference_title, pr.review_id, pr.reviewer_user_id, pr.paper_id from
conference c, paper p, paperreview pr where c.conference_id= p.conference_id and
pr.paper_id = p.paper_id
and c.conference_id = p_conference_id and c.review_due_time < due_time and
(pr.comments IS null or pr.review_score is null);
Begin
Select count(*) into check_conference_id from conference where conference_id =
p_conference_id;
if check_conference_id = 0 then
dbms_output.put_line('Invalid conference ID');
else
for item in c1
loop
insert into message values (mid.nextval, item.reviewer_user_id, due_time, 'Your
review for paper ' || item.paper_id ||
' submitted to conference ' || item.conference_title || ' is past due, please upload
your review asap');
dbms_output.put_line('Sent reminder to user ' || item.reviewer_user_id || ' for
missing review for paper '
|| item.paper_id || ' review id is ' || item.review_id);
end loop;
end if;
end;
/
--test case 1 - invalid conference ID
exec review_reminder( 100, timestamp '2024-3-16 00:00:00');
--test case 2 - expecting intended output
exec review_reminder( 1, timestamp '2024-3-16 00:00:00');
select * from message;
--testing SQL join in explicit cursor
/*
select pr.review_id, pr.reviewer_user_id from conference c, paper p, paperreview pr where
c.conference_id= p.conference_id and
pr.paper_id = p.paper_id and c.conference_id = 1 and c.review_due_time < timestamp
'2024-3-16 00:00:00' and (pr.comments IS null or pr.review_score is null);
*/
create or replace procedure assign_paper_reviewer(paperID IN paper.paper_ID%type,
max_rev_limit IN int)
IS
check_paper_id int;
--step 2
cursor c1 is select cu.user_id from paper p, conference c, conferencerole cr,
conferenceuser cu where p.conference_id= c.conference_id and
c.conference_id = cr.conference_id and cr.user_id = cu.user_id and cr.con_role = 'Reviewer'
and p.paper_id = paperid and cu.institution_id not in
(select institution_id from paper p, paperauthor pa, conferenceuser cu where p.paper_id =
pa.paper_id and pa.author_user_id = cu.user_id and p.paper_id = paperid);
check_if_reviewer_assigned int;
check_capacity int;
check_user_bid int;
begin
--step 1
select count(*) into check_paper_id from paper where paper_id=paperid;
if check_paper_id = 0 then
dbms_output.put_line('invalid paper ID');
else
select count(*) into check_if_reviewer_assigned from paper p, conference c,
conferencerole cr, conferenceuser cu where p.conference_id= c.conference_id and
c.conference_id = cr.conference_id and cr.user_id = cu.user_id and cr.con_role =
'Reviewer' and p.paper_id = paperid and cu.institution_id not in
(select institution_id from paper p, paperauthor pa, conferenceuser cu where p.paper_id
= pa.paper_id and pa.author_user_id = cu.user_id and p.paper_id = paperid);
if check_if_reviewer_assigned = 0 then
dbms_output.put_line('no one has bid for this paper');
else
for item in c1
loop
--step 3
select count(*) into check_capacity from paperreview pr, paper p where p.paper_id
= pr.paper_id and
pr.reviewer_user_id = item.user_id and p.paper_id = paperID;
--for conference in the above join, paper id has been checked.
if check_capacity >= max_rev_limit then
--step 5
dbms_output.put_line('User ' || item.user_id || ' has reached capacity');
else
--step 4
select count(*) into check_user_bid from paperbid where reviewer_user_id =
item.user_id;
if check_user_bid = 0 then
dbms_output.put_line('User has not bid for this paper');
else
dbms_output.put_line('Assign to ' || item.user_id);
insert into paperreview values(rid.nextval, item.user_id, paperID, NULL,
NULL, NULL);
end if;
end if;
end loop;
end if;
end if;
end;
/
commit;