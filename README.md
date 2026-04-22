# Simple Django Admin to Front Page Image/Text Project

## Features
- Django project name: `myproject`
- Django app name: `myapp`
- Add image + text from admin panel
- Display added content on front page
- SQLite database for easy local run

## Setup Steps
```bash
python -m venv venv
venv\Scripts\activate   # Windows
# source venv/bin/activate   # Linux/Mac
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

## URLs
- Front page: `http://127.0.0.1:8000/`
- Admin panel: `http://127.0.0.1:8000/admin/`

## How to use
1. Login to admin panel
2. Open **Home Contents**
3. Click **Add Home Content**
4. Enter title, description, upload image, save
5. Open front page and check output
