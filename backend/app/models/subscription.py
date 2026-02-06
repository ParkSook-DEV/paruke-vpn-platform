from datetime import datetime, timezone, timedelta

from sqlalchemy import Column, Integer, DateTime, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.ext.hybrid import hybrid_property

from app.core.database import Base


class Subscription(Base):
    __tablename__ = "subscriptions"

   
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey("users.id"))

    
    start_at = Column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc)
    )

    end_at = Column(
        DateTime(timezone=True),
        nullable=False
    )

    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
        nullable=False,
    )

    # ---------- factory ----------
    @classmethod
    def create(cls, user_id: int, days: int) -> "Subscription":
        now = datetime.now(timezone.utc)
        return cls(
            user_id=user_id,
            start_at=now,
            end_at=now + timedelta(days=days),
        )

    # ---------- computed ----------
    @hybrid_property
    def is_active(self):
        if self.end_at is None:
            return False
        return self.end_at.replace(tzinfo=timezone.utc) > datetime.now(timezone.utc)

    @property
    def status(self) -> str:
        return "active" if self.is_active else "expired"