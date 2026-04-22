Conference Management System
Overview
This project is a database driven conference management system built using Oracle SQL and PL SQL. It manages conferences, users, paper submissions, reviews, sessions, and registrations. It also includes automated procedures for reviewer assignment and reminder notifications.
Features
• Manage conferences with dates, location, and registration details
• Handle users and institutions
• Support multiple roles like Author, Reviewer, Organizer
• Paper submission and author mapping
• Topic based classification of papers
• Reviewer bidding system
• Paper review management with scores and comments
• Conference session scheduling
• Registration and payment tracking
• Messaging system for notifications
Database Design
The system follows a relational schema with normalized tables.
Main entities
• Institution
• ConferenceUser
• Conference
• ConferenceSession
• ConferenceRole
• Paper
• PaperAuthor
• Topic
• PaperTopic
• PaperBid
• PaperReview
• Registration
• Message
Each table uses primary keys and foreign keys to maintain data integrity.
Advanced Features
Reviewer Assignment
Automatically assigns reviewers to papers based on:
• No conflict of interest
• Reviewer role in conference
• Maximum review capacity
• Preference for users who bid
If no bids exist, system still assigns a valid reviewer
Procedure
assign_paper_reviewer(paperID, max_review_limit)
Review Reminder System
Sends reminders to reviewers when:
• Review deadline has passed
• Review is incomplete
Automatically inserts notification into Message table
Procedure
review_reminder(conference_id, time)
Technologies Used
• Oracle SQL
• PL SQL
• Relational Database Design
• Stored Procedures
• Cursors and Transactions
How to Run
Open Oracle SQL Developer or any Oracle environment
Run the script file
All tables and sample data will be created
Execute procedures using
Example
exec assign_paper_reviewer(10, 12);
exec review_reminder(1, timestamp '2024-03-16 00:00:00');
Sample Data
The project includes sample data for
• Conferences across multiple countries
• Users with different roles
• Papers with reviews and topics
• Registrations and messages
This helps in testing queries and procedures easily
Project Structure
backend
Contains database schema, SQL scripts, and PL SQL procedures
frontend
Can be extended to build UI for submission and review system
Future Improvements
• Build frontend using React or Flask
• Add authentication and user login
• Dashboard for conference analytics
• Real time notifications
• API integration
