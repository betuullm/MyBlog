# My Blog ✍️📰

This project is a simple and modern blog application built with Django. Users can create blog posts, add multiple images to each post, and view posts in a clean, responsive interface.

## Features 🚀

- User registration & login
- Create, list, and view blog posts
- Add multiple images to each post
- About page
- Content management via admin panel
- Modern & responsive UI

## Installation ⚙️

1. **Clone the repository:**
   ```powershell
   git clone <project-link>
   cd my_blog
   ```
2. **Create and activate a virtual environment:**
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
3. **Install dependencies:**
   ```powershell
   pip install -r requirements.txt
   ```
4. **Apply database migrations:**
   ```powershell
   python manage.py migrate
   ```
5. **Create a superuser:**
   ```powershell
   python manage.py createsuperuser
   ```
6. **Start the development server:**
   ```powershell
   python manage.py runserver
   ```

## Usage 📝

- View all blog posts on the homepage
- After logging in, create new posts and add images
- Access the admin panel at `/admin/`
- Visit the about page at `/about/`

## Requirements 📦

- Python 3.7+
- Django 3.2+
- Pillow
- Cloudinary (optional, for cloud image storage)

## Project Structure 🗂️

- `blog/` : Main app directory
- `templates/` : HTML templates
- `static/` : Static files (CSS, JS, images)
- `media/` : User-uploaded images
- `my_blog/` : Project settings and URL routing