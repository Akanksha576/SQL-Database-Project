# Conference Management System 

Overview:

This project is a database driven Conference Management System built using Oracle SQL and PL SQL. It manages conferences, users, paper submissions, reviews, sessions, and registrations. It also includes automated workflows for reviewer assignment and reminder notifications.

Features:

- Manage conferences with dates, location, and registration details
- Handle users and institutions
- Support roles such as Author, Reviewer, Organizer
- Paper submission and author mapping
- Topic classification of papers
- Reviewer bidding system
- Paper review management with scores and comments
- Conference session scheduling
- Registration and payment tracking
- Messaging system for notifications

Database Design: 

Core Tables
-  Institution
- ConferenceUser
- Conference
- ConferenceSession
- ConferenceRole
- Paper
- PaperAuthor
- Topic
- PaperTopic
- PaperBid
- PaperReview
- Registration
- Message
  
All tables use primary and foreign keys to maintain data integrity.

Advanced Features:

- Reviewer Assignment
Automatically assigns reviewers based on:
 - No conflict of interest
 - Reviewer role
 - Maximum review capacity
 - Preference for users who bid

Procedure: 
assign_paper_reviewer(paperID, max_review_limit)

- Review Reminder
Sends reminders when:
 - Review deadline has passed
 - Review is incomplete

Procedure:
review_reminder(conference_id, time)

Technologies: 
- Oracle SQL
- PL SQL
- Stored Procedures
-Relational Database Design
   
How to Run: 
- Open Oracle SQL Developer
- Run the SQL script
- Execute procedures:
- exec assign_paper_reviewer(10, 12);
- exec review_reminder(1, timestamp '2024-03-16 00:00:00');

Project Structure: 

backend
 -SQL scripts
 -PL SQL procedures

frontend
 - Placeholder for UI
 - README.md

Future Improvements:

- Build frontend using React or Flask
- Add authentication
- Create dashboards
- Enable real time notifications

Contribution:

- Designed schema
- Built tables and relationships
- Developed procedures for automation
