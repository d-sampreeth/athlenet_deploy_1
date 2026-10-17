# Athlenet — React + Tailwind + Django

A full-stack sports networking platform for players, coaches and general users.

## Removed by design
- Reels
- Stories

Athlenet focuses on opportunities, meaningful community posts, sports news, profiles, messaging and notifications.

## Frontend
- React 18
- Vite 5
- Tailwind CSS 3
- React Router
- Axios
- Lucide icons

## Backend
- Django 5.2
- Django REST Framework
- SimpleJWT
- SQLite by default
- Media uploads for profile photos, certificates and post/news images

## Run backend
```powershell
cd backend
python -m venv venv
.\venv\Scripts\Activate.ps1
pip install -r requirements.txt
python manage.py migrate
python manage.py createsuperuser
python manage.py seed_demo
python manage.py runserver
```

Backend API: http://127.0.0.1:8000/api/
Admin: http://127.0.0.1:8000/admin/

## Run frontend
```powershell
cd frontend
npm install
npm run dev
```

Frontend: http://localhost:5173/

## Deploy on Vercel

The repository-root `vercel.json` deploys the Django backend and Vite frontend as
separate services. The frontend is served at `/`; `/api`, `/admin`, `/media`,
and `/static` are routed to the backend. The frontend uses same-origin `/api`
requests, while Vite proxies those paths to the local Django server during
development.

Set `DJANGO_SECRET_KEY` in Vercel before deployment, and set
`DJANGO_ALLOWED_HOSTS` to a comma-separated list if serving the app from custom
domains. `DJANGO_DEBUG` defaults to `true` locally and `false` on Vercel. The
current SQLite database and local media directory are not persistent Vercel
storage; configure a managed database and media store before relying on
production writes or uploads.

## Deploy on Render

Create a Blueprint in Render from this repository and select the root
`render.yaml`. It defines a Django web service, a Vite static site, and a
PostgreSQL database, with the frontend backend URL filled from the backend
service automatically. The backend start command applies database migrations
before starting Gunicorn.

The Blueprint currently uses Render's free service/database plans. Free
services can spin down while idle, and free databases have plan-specific
lifetime and storage limits. Uploaded media remains on the backend filesystem
and is not persistent across deploys/restarts; configure persistent/object
storage before relying on uploads in production.

## Demo accounts
Password for demo accounts: `Athlenet@123`
- demo_coach
- demo_player
- demo_user

## Main working modules
- JWT login/register with live password-strength guidance and server-side password rules
- Unique mobile numbers per account and editable email addresses from the profile editor
- Connections page for managing followed members
- Player, Coach and General User profiles
- Coach opportunity creation
- Opportunity search by keyword, sport and location
- Player opportunity applications
- Community posts with image uploads and likes
- Local Hub directory with member search, role/sport/location filters, follows and direct messages
- Sports news with location filtering and search
- Global search for people, opportunities and news
- Profiles, follow and direct messaging
- Profile pages show the member's community posts and player achievements
- Notifications and mark-as-read
- Django admin

## Important
The project includes the initial `core` migration. On a fresh checkout always run `python manage.py migrate` before registering users.
