# 📝 Scatter Thoughts Blog App

A full-featured personal blogging platform where users can express thoughts, share posts, and manage content. Built with **Django**, it features a polished UI, full authentication flow, media uploads, and is ready for deployment.

🔗 **[Live Demo](https://scatter-thoughts.onrender.com)**

---

## 🚀 Features

- 🔐 **User Authentication** – Register, login/logout, and reset passwords securely  
- 👤 **User Profiles** – View and update personal profile information  
- 📝 **Post Management** – Create, edit, and delete blog posts with ease  
- 📄 **Pagination** – Clean paginated views for global and user-specific feeds  
- 🖼️ **Media Uploads** – Upload profile pictures and post images  
- 🛠️ **Admin Interface** – Manage users and posts via Django Admin  
- 📱 **Responsive Design** – Mobile-friendly interface using Bootstrap 5  

---

## 🛠️ Technologies Used

- **Backend**: Django (Python)
- **Database**: PostgreSQL
- **Frontend**: HTML5, CSS3, Bootstrap 5, Django Templating
- **Forms**: [`django-crispy-forms`](https://django-crispy-forms.readthedocs.io/)
- **Deployment**: 
  - Backend: [Render](https://render.com)  
  - Frontend: [Vercel](https://vercel.com)

---

## 📁 Project Structure

Django_full_featured_web_app/
├── blog/ # Blog post logic and templates
├── users/ # User registration and profile updates
├── media/ # Uploaded media (profile pics, images)
├── static/ # CSS, JS, and other static files
├── Django_full_featured_web_app/ # Project settings
├── manage.py
├── requirements.txt
└── db.sqlite3 (for dev only — PostgreSQL in production)



📦 **GitHub Repo**: [Efe-The-Menace/Full-Featured-Web-App](https://github.com/Efe-The-Menace/Full-Featured-Web-App)

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/Efe-The-Menace/Full-Featured-Web-App.git
cd Django_full_featured_web_app

# Create virtual environment
python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Set PostgreSQL credentials (via environment variables or .env)

# Apply migrations
python manage.py migrate

# Start development server
python manage.py runserver



📌 Future Enhancements
💬 Blog post commenting system

❤️ Like / Bookmark feature

🧾 Extended profiles & user bios

🏷️ Tags and category filtering

🔍 Full-text search functionality

📈 SEO & Open Graph integration

🤝 Contributing
Pull requests are welcome!
Feel free to fork the repository, push improvements, and submit a PR.

👨‍💻 Author
David “Efe” Obasuyi
Backend Developer | Django & Python
Built as a passion project and personal learning experience.
