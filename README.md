📝 Scatter Thoughts Blog App
A full-featured personal blogging platform where users can express thoughts, share posts, and manage content. Built with Django, it features a polished UI, full authentication flow, and is ready for deployment.

🌐 Live Demo
🔗 scatteredthoughts.onrender.com

🚀 Features
User Authentication – Register, log in/out, and reset passwords securely

User Profiles – View and update personal profile information

Post Management – Create, edit, and delete blog posts with ease

Pagination – Cleanly paginated feed and user-specific posts

Media Uploads – Upload images and profile pictures

Admin Interface – Manage users and posts via Django Admin

Responsive Design – Mobile-friendly interface using Bootstrap 5

🛠️ Technologies Used
Backend: Django (Python)

Database: SQLite (PostgreSQL for production)

Frontend: HTML5, CSS3, Bootstrap 5, Django Templating

Forms: django-crispy-forms

Deployment:  Render

📁 Project Structure

Django_full_featured_web_app/
├── blog/               # Blog post logic and templates
├── users/              # User registration, login, profile updates
├── media/              # Uploaded media (profile pics, images)
├── static/             # CSS, JS, and other static files
├── Django_full_featured_web_app/   # Base Django project settings
├── db.sqlite3 (optional, replaced by PostgreSQL in production)
├── manage.py
├── requirements.txt

📁 GitHub Repo:
Efe-The-Menace/Full-Featured-Web-App


cd Django_full_featured_web_app
⚙️ Installation & Setup

# Clone the repo
git clone https://github.com/Efe-The-Menace/Full-Featured-Web-App.git
cd Django_full_featured_web_app

# Create and activate virtual environment
python -m venv venv
source venv/bin/activate     # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set up PostgreSQL credentials in environment variables or .env

# Run migrations
python manage.py migrate

# Start the development server
python manage.py runserver



📌 Future Enhancements
Blog post comments system

Like/Bookmark feature

User bios & extended profiles

Tag-based filtering and categories

Search functionality


🤝 Contributing
Pull requests are welcome!
Feel free to fork the repository, push improvements, and open a Pull Request.

👨‍💻 Author
David Obasuyi
Backend Developer | Django & Python
Built as a passion project and learning tool.
