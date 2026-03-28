# SpringBoard_Many_to_Many_Blogly
### Full-Stack Blog Management System with Relational Tagging

**Blogly** is a robust content management application built with **Python** and **Flask**. It features a multi-layered relational database that allows for seamless management of users, blog posts, and dynamic tags. 

The core of this project is implementing a **Many-to-Many relationship** using a custom join table, combined with a modular **Jinja2 template inheritance** system for a clean, consistent UI.

---

## 🚀 Key Features
- **User Management:** Full CRUD suite for user profiles, including custom avatar handling and automated image URL fallbacks.
- **Relational Blogging:** Users are linked to their posts via One-to-Many relationships with SQLAlchemy `backref` support.
- **Advanced Tagging Engine:** Posts and Tags are linked via a `post_tags` association table, enabling users to categorize content dynamically.
- **Automated Timestamps:** Server-side timestamping for all posts using `db.func.now()` for accurate data tracking.
- **Developer-Friendly Tools:** Integrated with **Flask-DebugToolbar** for real-time request and SQL query analysis.
---

## 🛠️ Tech Stack
- **Backend:** Python 3, Flask
- **Database:** PostgreSQL, Flask-SQLAlchemy (ORM)
- **Frontend:** Jinja2 Templates (Inheritance-based), HTML5, CSS3 (Bootstrap 5)
- **Scripting:** jQuery, Axios (for future API expansion)
---

## 📂 Frontend Architecture: Template Inheritance
To ensure a scalable and maintainable UI, the project uses Jinja2 Template Inheritance. By defining a `base.html` skeleton, the application maintains a consistent layout while allowing specific views to inject unique content.

- **Base Layout:** Manages global head metadata, Bootstrap 5 integration, and shared script libraries (jQuery, Axios).
- **Block Overrides:** Specific templates use `{% extends %}` and `{% block %}` to override titles, headers, and body content dynamically based on the route.

---

## 📂 Database Architecture
The schema is designed for high data integrity and efficient querying:

- **Users (`users`):** Primary profiles with `id`, `first_name`, `last_name`, and `image_url`.
- **Posts (`posts`):** Stores content with a foreign key to `users`. Features a `user` relationship for easy dot-notation access.
- **Tags (`tags`):** Unique labels for categorizing content.
- **PostTags (`post_tags`):** The **Join Table** that bridges `posts.id` and `tags.id`, creating the many-to-many link.

---

## 🔧 Installation & Quick Start

1. **Clone the Repo:**
   ```bash
   git clone [https://github.com/Dochi4/SpringBoard_Many_to_Many_Blogly.git](https://github.com/Dochi4/SpringBoard_Many_to_Many_Blogly.git)
   cd SpringBoard_Many_to_Many_Blogly
## Setup Environment

# Create a virtual environment
python3 -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

#Initialize & Seed Database:
createdb blogly

# Run the seed file to create tables and populate test data
python3 seed.py

# Run App:
flask run
