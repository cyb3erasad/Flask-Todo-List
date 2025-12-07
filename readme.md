📌 Flask To-Do List Application — Documentation

A simple and modern To-Do List web application built using Flask, SQLAlchemy, Flask-Login, and Bootstrap.
Users can register, log in, add tasks, edit tasks, mark them as complete, and delete tasks.

🚀 Features
🔐 User Authentication

User Registration

User Login

Password hashing using Flask-Bcrypt

Session management with Flask-Login

Only logged-in users can access or modify their tasks

Each user has their own separate tasks


📝 Task Management

Add new tasks

Mark tasks as complete

Edit task title

Delete tasks

Completed tasks are visually highlighted

Tasks are connected to the user via user_id


🎨 Beautiful UI

Built with modern Bootstrap 5 and custom CSS:

Gradient backgrounds

Rounded cards

Smooth animations

Clean typography

Responsive on all screen sizes

/project
│
├── app.py
├── models.py          <-- (added)
├── requirements.txt
├── .env               <-- optional, for SECRET_KEY
├── /templates
│      ├── register.html
│      ├── login.html
│      ├── home.html
│      ├── edit.html
│
└── /static
       ├── style.css
       └── (other assets)


⚙️ Installation & Setup
1. Clone the project
git clone https://github.com/cyb3erasad/Flask-Todo-List.git
cd project


2. Create Virtual Environment
    python -m venv venv
    venv\Scripts\activate   

3. Install dependencies
    pip install -r requirements.txt

💡 Conclusion

This project is a great introduction to Flask, covering:

Routing

Templates

Authentication

Database relationships

UI design

CRUD operations

It can be used as a portfolio project or extended into a full productivity app.
