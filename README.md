# Student_Management_System
💾 Database Setup
Create a database named rec in your MySQL server:

sql
Copy
Edit
CREATE DATABASE rec;
Create a table named student:

sql
Copy
Edit
CREATE TABLE student (
    rollNo INT PRIMARY KEY,
    name VARCHAR(50),
    fname VARCHAR(50),
    sub VARCHAR(50),
    grade VARCHAR(10)
);
Update your MySQL credentials in the dbFun() function inside main.py.

🚀 How to Run
Clone this repository:

bash
Copy
Edit
git clone https://github.com/your-username/student-record-system.git
cd student-record-system
Install dependencies (if any):

bash
Copy
Edit
pip install pymysql
Run the application:

bash
Copy
Edit
python main.py
🧠 Learning Outcomes
Object-Oriented Programming with GUI

Working with relational databases in Python

Tkinter Treeview and custom styling

Building real-world CRUD applications

🙌 Contributing
Pull requests are welcome! For major changes, please open an issue first to discuss what you would like to change.



🤝 Connect with Me
🔗 LinkedIn: [linkedin.com/in/basanta-mukherjee](https://www.linkedin.com/in/basanta-mukherjee-478523297/)



🌟 Star this repo if you find it helpful!
