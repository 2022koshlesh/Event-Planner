# Event Planning Platform
# SnapShots

<img width="1919" height="940" alt="Screenshot 2025-11-19 141701" src="https://github.com/user-attachments/assets/47e41c5d-5b2f-49d6-812f-3c2e82ba713f" />

<img width="1919" height="933" alt="Screenshot 2025-11-19 141719" src="https://github.com/user-attachments/assets/806963fa-fc95-4e98-bdcf-06fd22663436" />

<img width="1919" height="940" alt="Screenshot 2025-11-19 141822" src="https://github.com/user-attachments/assets/f7326188-d38c-4251-9468-c12638da3da3" />

<img width="1919" height="931" alt="Screenshot 2025-11-19 141854" src="https://github.com/user-attachments/assets/2baa3889-565e-48d4-a8ee-dbb6858c9fce" />

<img width="1919" height="938" alt="Screenshot 2025-11-19 141910" src="https://github.com/user-attachments/assets/f5eb9411-3827-4784-8256-42b3ba951551" />

<img width="1916" height="935" alt="Screenshot 2025-11-19 141924" src="https://github.com/user-attachments/assets/4999183f-8db7-44f4-b439-355860520d20" />

<img width="1919" height="932" alt="Screenshot 2025-11-19 142019" src="https://github.com/user-attachments/assets/a5c11b5d-4d0e-45d7-85cc-8b9feacd132c" />

<img width="1919" height="935" alt="Screenshot 2025-11-19 142044" src="https://github.com/user-attachments/assets/e2bd7e8c-ad4e-4298-9254-d6cf38e16837" />






A Django web application for managing events with a comprehensive invitation system, guest tracking, RSVP management, budget monitoring, and vendor coordination.

## Features

### 🎉 Event Management
- Create, edit, and manage multiple events
- Track event details (date, venue, capacity, status)
- Event dashboard with statistics

### 📨 Invitation System
- **Send Invitations** - Invite registered users to your events
- **Real-time Notifications** - Red badge shows pending invitations count
- **Accept/Decline** - One-click invitation response system
- **Invitation Tracking** - Monitor pending, accepted, and declined invitations
- **Personal Messages** - Add optional notes when sending invitations
- **Secure Authorization** - Only event organizers can manage invitations

### 👥 Guest Management
- View confirmed guests (users who accepted invitations)
- Track RSVP status (pending, accepted, declined)
- Manage number of attendees per guest
- Guest statistics dashboard

### 💰 Budget Tracking
- Monitor estimated vs actual costs for events
- Track expenses by category

### 🏢 Vendor Management
- Manage vendor database and event assignments
- Track vendor contact information

## Tech Stack

- **Backend:** Django 5.0+
- **Database:** SQLite (development) with easy PostgreSQL migration path
- **Frontend:** Bootstrap 5, Bootstrap Icons, Django Templates
- **Forms:** Django Crispy Forms with Bootstrap 5
- **Authentication:** Django built-in auth system
- **Email:** Gmail SMTP (configured for notifications)

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

### Getting Started

1. **Register an Account**
   - Navigate to http://localhost:8000
   - Click "Register" and create your account
   - You'll be automatically logged in

2. **Create Your First Event**
   - Click "Events" → "Create Event"
   - Fill in event details (title, date, venue, capacity, etc.)
   - Submit to create the event

### Invitation Workflow (Event Organizer)

3. **Send Invitations**
   - Go to your event details page
   - Click "Manage Invitations"
   - Click "Send Invitation"
   - Select a registered user from the dropdown
   - Add an optional personal message
   - Submit to send the invitation

4. **Track Invitations**
   - View invitation statistics (pending, accepted, declined)
   - See all invitations in a detailed table
   - Cancel pending invitations if needed

5. **Manage Confirmed Guests**
   - Click "View Confirmed Guests"
   - See all users who accepted your invitation
   - Edit RSVP details (status, number of attendees, notes)
   - Remove guests if needed

### Invitation Workflow (Invitee)

1. **View Your Invitations**
   - When invited, you'll see a red notification badge on "My Invitations" in the navbar
   - Click "My Invitations" to view all pending invitations

2. **Respond to Invitations**
   - Review event details, organizer, and personal message
   - Click "Accept" to confirm attendance
   - Click "Decline" to reject the invitation
   - View your invitation history (past responses)

### Additional Features

- **Budget Tracking** - Add and monitor expenses for your events
- **Vendor Management** - Create vendor profiles and assign them to events
- **Dashboard** - View overview of all your events and activities

## Development

### Running Tests

```bash
# Run all tests
python manage.py test

# Run tests for a specific app
python manage.py test guests
python manage.py test events
python manage.py test budget
python manage.py test vendors

# Run with verbose output
python manage.py test -v 2

# Run specific test class or method
python manage.py test guests.tests.InvitationViewTestCase
python manage.py test guests.tests.InvitationViewTestCase.test_invitation_create_post_success
```

**Test Coverage:**
- ✅ Invitation System: 21 comprehensive tests
  - Model tests (Invitation, Guest, RSVP)
  - View tests (Create, List, Respond, Delete)
  - Authorization and security tests
  - Template tag tests

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
test: Add or update tests
```

## CI/CD

GitHub Actions runs linting checks on every push/PR:
- Code linting (flake8)
- Code formatting check (black)
- Import sorting check (isort)

## Documentation

See [docs/project_plan.md](docs/project_plan.md) for the complete implementation plan.

## Roadmap

**Phase 1:** Foundation ✅
- User authentication and authorization
- Event CRUD operations
- User dashboard with event overview

**Phase 2:** Invitation & Guest Management ✅
- User-based invitation system
- Real-time notification badges
- Accept/Decline invitation workflow
- Guest list management for confirmed attendees
- RSVP tracking system
- Comprehensive test coverage (21 tests)

**Phase 3:** Budget Management (In Progress)
- Budget category management
- Expense tracking
- Budget vs actual cost analysis
- Budget reports and visualizations

**Phase 4:** Vendor Management
- Enhanced vendor profiles
- Vendor assignment to events
- Vendor contact management
- Vendor performance tracking

**Phase 5:** Enhancements
- Email notifications for invitations
- Calendar integration
- Event templates
- Export guest lists
- Advanced reporting

**Phase 6:** Polish & Optimization
- UI/UX improvements
- Performance optimization
- Mobile responsiveness
- Additional security features

## Key Features Implemented

### Invitation System (Latest)
- ✅ Send invitations to registered users
- ✅ Invitation status tracking (pending/accepted/declined)
- ✅ Real-time notification badges in navbar
- ✅ Personal messages with invitations
- ✅ One-click accept/decline functionality
- ✅ Invitation history for users
- ✅ Secure authorization (organizers only)
- ✅ Guest management for accepted invitations
- ✅ RSVP details management
- ✅ Comprehensive test suite

### Security Features
- ✅ User authentication required for all actions
- ✅ Authorization checks (users can only manage their own events)
- ✅ CSRF protection on all forms
- ✅ Secure logout with POST method
- ✅ Database integrity with unique constraints

## API Endpoints

### Invitations
- `GET /event/<event_id>/invitations/` - List invitations for an event
- `GET /event/<event_id>/invitations/send/` - Send invitation form
- `POST /event/<event_id>/invitations/send/` - Create invitation
- `POST /invitations/<id>/cancel/` - Cancel pending invitation
- `GET /my-invitations/` - View user's invitations
- `POST /invitations/<id>/accept/` - Accept invitation
- `POST /invitations/<id>/decline/` - Decline invitation

### Guests
- `GET /event/<event_id>/guests/` - List confirmed guests
- `POST /guests/<id>/remove/` - Remove guest from event

### RSVP
- `GET /rsvp/<id>/edit/` - Edit RSVP details
- `POST /rsvp/<id>/edit/` - Update RSVP

## Database Models

### Core Models

**Invitation**
- Links an invitee (User) to an Event
- Status: pending, accepted, declined
- Tracks invited_at and responded_at timestamps
- Optional notes from organizer
- Unique constraint: one invitation per user per event

**Guest**
- Links a User to an Event (created when invitation is accepted)
- References the original Invitation
- Tracks when user was added as confirmed guest
- Unique constraint: one guest record per user per event

**RSVP**
- Linked to a Guest
- Status: pending, accepted, declined
- Tracks number_of_guests (attendees)
- Optional response_date and notes

**Event**
- Core event details (title, description, dates, venue, etc.)
- Links to event organizer (User)
- Tracks event type and status

## Troubleshooting

### Database Issues

**Problem:** `no such table: guests_invitation`

**Solution:**
```bash
# Delete database and recreate
rm db.sqlite3

# Run migrations
python manage.py migrate

# Create new superuser
python manage.py createsuperuser
```

### Logout Issue

**Problem:** "Method Not Allowed (GET): /accounts/logout/"

**Solution:** The logout has been fixed to use POST method for security. Click the logout button in the navbar.

### Migration Conflicts

**Problem:** Migration conflicts after model changes

**Solution:**
```bash
# Show current migration status
python manage.py showmigrations

# If needed, fake the migration
python manage.py migrate guests --fake zero
python manage.py migrate guests
```

### Missing Dependencies

**Problem:** Import errors or missing modules

**Solution:**
```bash
# Install/update all dependencies
pip install -r requirements.txt

# For development dependencies
pip install flake8 black isort
```

## Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/AmazingFeature`)
3. Follow the commit convention
4. Write tests for new features
5. Ensure all tests pass (`python manage.py test`)
6. Submit a Pull Request

## License

This project is for educational purposes.

## Support

For issues, questions, or contributions, please open an issue on the repository.
#

