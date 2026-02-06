# Technical Decisions

##  Database Structure
A relational database model was selected to ensure:
- Data consistency
- Clear relationships (users, subscriptions, configs)
- Easy migration to more powerful databases later

Initial core entities:
- User
- Subscription
- Config / Outbound (future)

##  SQLite for MVP
SQLite was chosen for the MVP phase because:
- Zero configuration
- File-based and portable
- Perfect for early-stage development and testing
- Easy migration path to PostgreSQL/MySQL later

This decision prioritizes speed of development over scalability.

##  Timezone-Aware UTC Datetimes
All timestamps are stored as timezone-aware UTC datetimes.

Reasoning:
- Avoid ambiguity across servers and regions
- Prevent bugs related to daylight saving time
- Industry best practice for backend systems

Implementation uses:
`datetime.now(timezone.utc)` instead of deprecated `datetime.utcnow()`

This convention must be respected across the entire backend.

##  ORM & Database
- Chose SQLAlchemy over raw SQL for maintainability
- Started with SQLite for fast iteration
- Will migrate to PostgreSQL later

##  User identity
- telegram_id is unique
- Duplicate users are checked before insert
- Avoids IntegrityError in production

##  Table creation
- Using Base.metadata.create_all() for MVP
- Alembic deferred to later phase