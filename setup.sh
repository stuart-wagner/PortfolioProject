#!/bin/bash
# Quick setup script for development

echo "Setting up AI Portfolio Website..."

# Activate virtual environment
source venv/Scripts/activate

# Install dependencies
echo "Installing dependencies..."
pip install -r requirements.txt

# Run migrations
echo "Running migrations..."
python manage.py migrate

# Seed database
echo "Seeding database with projects..."
python manage.py seed_projects

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

echo ""
echo "Setup complete!"
echo ""
echo "Next steps:"
echo "1. Create a superuser: python manage.py createsuperuser"
echo "2. Run the development server: python manage.py runserver"
echo "3. Visit http://localhost:8000"
echo "4. Access admin at http://localhost:8000/admin/"
