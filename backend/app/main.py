from fastapi import FastAPI, Depends
from app.core.database import engine, Base, SessionLocal
from app.models.user import User
from app.models.subscription import Subscription
from sqlalchemy.orm import Session

app = FastAPI()

Base.metadata.create_all(bind=engine)


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.get("/test-subscription")
def test_subscription():
    sub = Subscription.create(user_id=1, days=30)

    return {
        "user_id": sub.user_id,
        "start_at": sub.start_at,
        "end_at": sub.end_at,
        "active": sub.is_active,
        "status": sub.status,
    }

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@app.get("/test-end-to-end")
def test_end_to_end(db: Session = Depends(get_db)):
    telegram_id = "test_telegram_123"

    # 1️⃣ اگر User وجود داشت، بگیرش
    user = db.query(User).filter(User.telegram_id == telegram_id).first()

    # 2️⃣ اگر نبود، بساز
    if not user:
        user = User(telegram_id=telegram_id)
        db.add(user)
        db.commit()
        db.refresh(user)

    # 3️⃣ ساخت Subscription
    sub = Subscription.create(user_id=user.id, days=30)
    db.add(sub)
    db.commit()
    db.refresh(sub)

    return {
        "user_id": user.id,
        "telegram_id": user.telegram_id,
        "subscription": {
            "start_at": sub.start_at,
            "end_at": sub.end_at,
            "active": sub.is_active,
            "status": sub.status,
        }
    }