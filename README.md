# Paruke VPN Platform

## Overview
Automated, backend-first VPN subscription platform built with FastAPI and Telegram Bot for scalable and automated sales.

## Features
- FastAPI backend with clean project structure
- User management and subscription logic
- Timezone-aware UTC datetime handling
- Telegram bot integration (MVP)
- Fully documented architecture and technical decisions

## Architecture
- Backend-first design prioritizing business logic and automation
- FastAPI for async and performant APIs
- SQLite for MVP development, easy migration to MySQL/PostgreSQL
- venv for isolated Python environment
- UTC timezone standard for all timestamps

## Tech Stack
- Python 3.12
- FastAPI
- SQLite (development), with future migration to MySQL/PostgreSQL
- Telegram Bot

## Documentation
- [Architecture](docs/architecture.md)
- [Decisions](docs/decisions.md)
- [Roadmap](docs/roadmap.md)

## Status
Phase 1: Backend Skeleton (Day 1)
- FastAPI backend initialized
- User model & UTC datetime convention implemented
- Project documentation & README completed

Phase 2: Backed Foundation
- SQLAlchemy setup with SQLite (paruke.db)
- User & Subscription models
- Relationship between User and Subscription
- End-to-end test endpoint
- Unique constraint handling for telegram_id

##  Developer(s)
ParkSook-DEV