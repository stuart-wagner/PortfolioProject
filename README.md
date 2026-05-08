# AI Portfolio Website

A professional Django 6.0 portfolio website showcasing six AI and full-stack technical projects. Built with Bootstrap 5 for responsive design and configured for production deployment on Render.

## Features

- **Dynamic Project Management**: Database-driven project showcase with detailed pages
- **Responsive Design**: Bootstrap 5 CDN for professional, mobile-friendly UI
- **Multiple Views**: Home, About, Projects (grid), Project Detail, Skills, Resume, Contact
- **Admin Dashboard**: Django admin for easy project management
- **Production Ready**: Configured for Render deployment with PostgreSQL
- **Static File Handling**: WhiteNoise for efficient static file serving

## Tech Stack

- **Backend**: Django 6.0
- **Database**: SQLite (dev) / PostgreSQL (production)
- **Frontend**: Bootstrap 5 (CDN)
- **Static Files**: WhiteNoise
- **Web Server**: Gunicorn
- **Deployment**: Render.com

## Project Structure

```
portfolio_project/
├── portfolio/              # Main app
│   ├── models.py          # Project model with 10 fields
│   ├── views.py           # Views for all pages
│   ├── forms.py           # Contact form
│   ├── admin.py           # Admin configuration
│   ├── urls.py            # App URL routing
│   ├── templates/         # HTML templates
│   │   └── portfolio/
│   │       ├── base.html  # Base template with nav
│   │       ├── home.html  # Hero section + featured projects
│   │       ├── about.html # About page
│   │       ├── projects.html # Projects grid
│   │       ├── project_detail.html # Detailed project page
│   │       ├── skills.html # Technical skills
│   │       ├── resume.html # Resume viewer
│   │       └── contact.html # Contact form
│   ├── management/
│   │   └── commands/
│   │       └── seed_projects.py # Database seeding
├── portfolio_project/      # Project settings
│   ├── settings.py        # Django configuration (production-ready)
│   ├── urls.py            # Main URL routing
│   ├── wsgi.py            # WSGI application
├── requirements.txt       # Python dependencies
├── Procfile              # Render deployment configuration
└── manage.py
```

## Installation

### Local Development

1. **Clone and setup environment**
   ```bash
   cd PortfolioProject
   source venv/Scripts/activate  # Windows: venv\Scripts\activate
   pip install -r requirements.txt
   ```

2. **Run migrations**
   ```bash
   python manage.py migrate
   ```

3. **Seed initial data**
   ```bash
   python manage.py seed_projects
   ```

4. **Create admin user**
   ```bash
   python manage.py createsuperuser
   ```

5. **Run development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the site**
   - Main site: http://localhost:8000/
   - Admin: http://localhost:8000/admin/

## Database Models

### Project Model (11 fields)
- **title** (CharField): Project name
- **summary** (CharField): One-sentence summary
- **business_problem** (TextField): Problem statement
- **tools_used** (CharField): Comma-separated technologies
- **key_features** (TextField): Feature list
- **your_role** (TextField): Your responsibilities
- **biggest_challenge** (TextField): Technical challenge faced
- **what_learned** (TextField): Key learnings
- **screenshot** (ImageField): Project image (optional)
- **link** (URLField): GitHub/demo link (optional)
- **order** (PositiveIntegerField): Display order on projects page

Auto-generated:
- **slug** (SlugField): URL-safe identifier (auto-generated from title)

**Features**: 
- Projects are ordered by the `order` field in admin
- Reorderable directly in admin list view via editable column
- Slug auto-generates from title on save

### SkillType Model
- **name** (CharField): Category name (e.g., Languages, Frameworks)
- **icon** (CharField): FontAwesome icon class (16 options available)
- **color** (CharField): Bootstrap color class (8 options)
- **order** (PositiveIntegerField): Display order on skills page

**Features**: Reorderable in admin list view

### Skill Model
- **name** (CharField): Individual skill name
- **skill_type** (ForeignKey): Reference to SkillType
- **order** (PositiveIntegerField): Display order within skill type

**Constraints**: Unique combination of name + skill_type

### Portrait Model
- **image** (ImageField): Profile photo (uploads to `portraits/`)
- **uploaded_at** (DateTimeField): Auto-generated timestamp
- **is_active** (BooleanField): Only one portrait can be active

**Features**: Auto-ensures only one active portrait

### Resume Model
- **file** (FileField): Resume PDF/document (uploads to `resumes/`)
- **uploaded_at** (DateTimeField): Auto-generated timestamp
- **is_active** (BooleanField): Only one resume can be active

**Features**: Auto-ensures only one active resume

## Seeded Projects

1. **Conversational AI Chatbot** - LangChain + OpenAI
2. **n8n Agent Workflow Automation** - Workflow orchestration
3. **LangChain RAG Agent System** - Retrieval-Augmented Generation
4. **Google AI Studio Multimodal Project** - Multimodal AI
5. **Machine Learning Predictive Model** - scikit-learn
6. **Campus SkillSwap Django App** - Full-stack CRUD

## Deployment to Render

### Prerequisites

- Render.com account
- GitHub repository with this code
- PostgreSQL database (Render provides free tier)

### Setup Steps

1. **Connect Repository**
   - Push code to GitHub
   - Connect repository to Render

2. **Create PostgreSQL Database**
   - Create new PostgreSQL instance on Render
   - Note the internal database URL

3. **Create Web Service**
   - New → Web Service
   - Connect GitHub repository
   - Select Python environment
   - Build command: `pip install -r requirements.txt`
   - Start command: `web: python manage.py migrate && gunicorn portfolio_project.wsgi`

4. **Configure Environment Variables**
   
   In Render dashboard, set:
   ```
   SECRET_KEY=your-secure-random-key
   DEBUG=False
   ALLOWED_HOSTS=your-domain.onrender.com
   DATABASE_URL=postgresql://user:pass@host:5432/dbname
   EMAIL_BACKEND=django.core.mail.backends.smtp.EmailBackend
   EMAIL_HOST=smtp.gmail.com
   EMAIL_PORT=587
   EMAIL_USE_TLS=True
   EMAIL_HOST_USER=your-email@gmail.com
   EMAIL_HOST_PASSWORD=your-app-specific-password
   SECURE_SSL_REDIRECT=True
   SESSION_COOKIE_SECURE=True
   CSRF_COOKIE_SECURE=True
   ```

5. **Deploy**
   - Render automatically deploys on push
   - Check deployment logs for errors
   - Visit your domain once deployment completes

### Post-Deployment

1. **Create superuser on production**
   ```bash
   # Via Render shell or local with production DATABASE_URL
   python manage.py createsuperuser
   ```

2. **Seed projects** (if needed)
   ```bash
   python manage.py seed_projects
   ```

3. **Collect static files**
   ```bash
   python manage.py collectstatic --noinput
   ```

## Configuration Notes

### Email Setup (Contact Form)

The contact form requires email configuration:

- **Gmail**: Use app-specific password (not regular password)
- **Other providers**: Update EMAIL_HOST and EMAIL_PORT accordingly
- **Development**: Uses console backend by default (no emails sent)

### Static Files

- WhiteNoise handles static file serving in production
- `STATIC_ROOT` set to `staticfiles/`
- Run `collectstatic` on deployment for production databases

### Media Files

- Project screenshots upload to `media/projects/`
- Ensure write permissions on production
- For Render: use S3 or similar for persistent storage

## Customization

### Reorder Projects

Projects can be reordered via Django admin:

1. Go to `/admin/portfolio/project/`
2. See the "Order" column in the list view
3. Click on the order value for any project to edit it directly
4. Lower numbers appear first on the projects page
5. Click "Save" to apply changes

The same reordering feature works for:
- **SkillTypes**: `/admin/portfolio/skilltype/`
- **Skills**: `/admin/portfolio/skill/`

### Add New Projects

1. Via Django admin:
   - Go to `/admin/portfolio/project/`
   - Click "Add Project"
   - Fill all fields (order is optional, defaults to 0)
   - Save

2. Via management command:
   - Edit `portfolio/management/commands/seed_projects.py`
   - Run: `python manage.py seed_projects`

### Add Custom Skills

1. Create SkillType (category):
   - Go to `/admin/portfolio/skilltype/`
   - Click "Add Skill Type"
   - Choose name, icon (FontAwesome), color, and order

2. Add Skills to the type:
   - Go to `/admin/portfolio/skill/`
   - Click "Add Skill"
   - Assign to SkillType and set order

### Upload Portrait and Resume

- **Portrait**: Upload one image via `/admin/portfolio/portrait/`
  - Recommended: PNG with transparent background
  - Only active portrait displays on home page
- **Resume**: Upload one file via `/admin/portfolio/resume/`
  - Only active resume displays on resume page

### Modify Styling

- Edit CSS in `portfolio/templates/portfolio/base.html`
- Bootstrap classes available from CDN
- Add custom CSS in `<style>` block

### Change Contact Email

- Update recipient email in `portfolio/views.py` (contact function)
- Or add environment variable for flexibility

## Custom Template Tags

Custom template filters are available for template use:

### split Filter
Splits a string by a separator:
```django
{{ tools_used|split:"," }}
```

### strip_spaces Filter
Removes leading/trailing whitespace:
```django
{{ value|strip_spaces }}
```

## Troubleshooting

### Static files not loading in production
```bash
python manage.py collectstatic --noinput
# Restart Render service
```

### Database migrations fail
- Ensure DATABASE_URL is correct
- Check PostgreSQL service is running
- Verify user permissions

### Contact form not sending
- Check EMAIL_* environment variables
- Test with console backend first
- Verify Gmail app password (if using Gmail)

### Project slugs not working
- Slugs auto-generate from titles with spaces converted to hyphens
- Check `project_detail.html` uses correct slug URL

## Dependencies

See `requirements.txt` for complete list:
- Django 6.0.5
- Gunicorn (web server)
- WhiteNoise (static files)
- dj-database-url (database config)
- psycopg2-binary (PostgreSQL)
- Pillow (image processing)

## License

This project is open source and available for personal and professional use.

## Support

For issues or questions:
1. Check Django documentation: https://docs.djangoproject.com/
2. Review Render deployment guide: https://render.com/docs
3. Check your environment variables and logs
