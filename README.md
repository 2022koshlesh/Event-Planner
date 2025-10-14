# Event Planning Platform

A beginner-friendly Django web application for managing events, tracking guests, handling RSVPs, managing budgets, and coordinating with vendors.

## Features

- **Event Management** - Create, edit, and manage multiple events
- **Guest Management** - Track guest lists and manage RSVPs
- **Budget Tracking** - Monitor estimated vs actual costs for events
- **Vendor Management** - Manage vendor database and event assignments

## Tech Stack

- **Backend:** Django 5.0+
- **Database:** SQLite (development) with easy PostgreSQL migration path
- **Frontend:** Bootstrap 5, Django Templates
- **Email:** Gmail SMTP

## Installation

1. **Clone the repository**
   ```bash
   git clone <repository-url>
   cd event-planning-platform
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   
   # Windows
   venv\Scripts\activate
   
   # Linux/Mac
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   cp .env.example .env
   # Edit .env with your Gmail SMTP credentials
   ```

5. **Run migrations**
   ```bash
   python manage.py migrate
   ```

6. **Create superuser**
   ```bash
   python manage.py createsuperuser
   ```

7. **Run development server**
   ```bash
   python manage.py runserver
   ```

8. **Access the application**
   - Web: http://localhost:8000
   - Admin: http://localhost:8000/admin

## Git Hooks Setup

```bash
# Windows
.githooks\setup-hooks.bat

# Linux/Mac
bash .githooks/setup-hooks.sh

# Install linting tools
pip install flake8 black isort
```

## Project Structure

```
event_planning_platform/
├── accounts/        # User authentication
├── events/          # Event management
├── guests/          # Guest and RSVP management  
├── budget/          # Budget tracking
├── vendors/         # Vendor management
├── core/            # Shared utilities
├── templates/       # HTML templates
├── static/          # Static files
└── config/          # Project settings
```

## Usage

1. Register a new account or login
2. Create your first event
3. Add guests to your event
4. Track your event budget
5. Assign vendors to your event

## Development

### Code Quality

```bash
# Check code style
flake8 .

# Format code
black .

# Sort imports
isort .
```

### Commit Convention

```
feat: Add new feature
fix: Fix bug
docs: Update documentation
style: Format code
refactor: Refactor code
```

## CI/CD

GitHub Actions runs linting checks on every push/PR:
- Code linting (flake8)
- Code formatting check (black)
- Import sorting check (isort)

## Documentation

See [docs/project_plan.md](docs/project_plan.md) for the complete implementation plan.

##  Roadmap

**Phase 1:** Foundation ✅
- User authentication
- Event CRUD operations
- Basic dashboard

**Phase 2:** Guest Management (In Progress)
- Guest list management
- RSVP system

**Phase 3-6:** Remaining features
- Budget tracking enhancements
- Vendor management features
- UI improvements
