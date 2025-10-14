# Event Planning Platform - Django Implementation Plan (Beginner Level)

## Project Overview

A beginner-friendly Django web application for event planners to manage events, track guest lists, handle RSVPs, manage budgets, and coordinate with vendors.

## Target Users

- Event Planners
- Corporate Event Coordinators
- Wedding Planners
- Small Organizations

## Technical Stack

### Backend
- **Framework**: Django 5.0+
- **Database**: SQLite (development) with abstraction layer for easy PostgreSQL migration
- **Authentication**: Django's built-in auth system
- **Email**: Gmail SMTP

### Frontend
- **Template Engine**: Django Templates
- **CSS Framework**: Bootstrap 5
- **JavaScript**: Vanilla JS (minimal)

## Database Design

### Core Models

#### 1. User (extends Django AbstractUser)
- username
- email
- first_name
- last_name
- role (planner, guest)
- phone_number

#### 2. Event
- title
- description
- event_type (wedding, corporate, party, other)
- status (planning, confirmed, completed, cancelled)
- start_date
- end_date
- venue
- location
- max_capacity
- created_by (FK to User)
- created_at
- updated_at

#### 3. Guest
- event (FK to Event)
- first_name
- last_name
- email
- phone_number
- created_at

#### 4. RSVP
- guest (FK to Guest)
- status (pending, accepted, declined)
- number_of_guests
- response_date
- notes

#### 5. BudgetItem
- event (FK to Event)
- category (venue, catering, decoration, other)
- name
- estimated_cost
- actual_cost
- status (planned, paid, pending)
- payment_date

#### 6. Vendor
- name
- category (catering, photography, decoration, other)
- contact_person
- email
- phone_number
- notes

#### 7. EventVendor
- event (FK to Event)
- vendor (FK to Vendor)
- service_description
- contract_amount
- status (pending, confirmed, completed)

## Django Apps Structure

```
event_planning_platform/
├── config/                    # Project settings
│   ├── settings.py
│   ├── urls.py
│   └── wsgi.py
├── accounts/                  # User authentication
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── events/                    # Event management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── guests/                    # Guest and RSVP management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── budget/                    # Budget tracking
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
├── vendors/                   # Vendor management
│   ├── models.py
│   ├── views.py
│   ├── forms.py
│   └── urls.py
└── core/                      # Shared utilities
    ├── db.py                  # Database abstraction
    └── utils.py
```

## Implementation Phases

### Phase 1: Foundation (Week 1)
- Django project setup
- User authentication (login, register, logout)
- Base templates with Bootstrap 5
- Dashboard skeleton

### Phase 2: Event Management (Week 2)
- Event CRUD operations
- Event list and detail views
- Event status management

### Phase 3: Guest Management (Week 3)
- Guest CRUD operations
- RSVP system
- Guest list views

### Phase 4: Budget Tracking (Week 4)
- Budget items CRUD
- Budget summary view
- Simple charts

### Phase 5: Vendor Management (Week 5)
- Vendor CRUD operations
- Event-vendor assignment
- Vendor list views

### Phase 6: Polish & Deployment (Week 6)
- UI improvements
- Form validation
- Basic email notifications
- Documentation

## Key Features

### 1. User Authentication
- Registration
- Login/Logout
- Profile management

### 2. Event Management
- Create/Edit/Delete events
- View event details
- Track event status
- List all events

### 3. Guest Management
- Add guests to events
- Track RSVPs
- View guest lists
- Send email invitations

### 4. Budget Tracking
- Add budget items
- Track expenses
- View budget summary
- Calculate totals

### 5. Vendor Management
- Manage vendor database
- Assign vendors to events
- Track vendor contracts
- View vendor lists

## Database Abstraction

All database operations will use Django ORM with:
- Abstract base classes for models
- Manager classes for complex queries
- QuerySet methods for reusability
- Easy migration path to PostgreSQL

## Email Configuration

Using Gmail SMTP:
- EMAIL_BACKEND: django.core.mail.backends.smtp.EmailBackend
- EMAIL_HOST: smtp.gmail.com
- EMAIL_PORT: 587
- EMAIL_USE_TLS: True

## Timeline

**Total Duration**: 6 weeks
**Difficulty Level**: Beginner
**Prerequisites**: Basic Python and Django knowledge

## Success Metrics

- Working user authentication
- CRUD operations for all models
- Responsive UI with Bootstrap
- Email notifications working
- Clean, readable code following SOLID principles
