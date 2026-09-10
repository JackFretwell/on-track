from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import BigInteger, Text, JSON, DateTime, func

class Base(DeclarativeBase):
    pass

class RawEvent(Base):
    __tablename__ = "raw_events"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    received_at: Mapped[object] = mapped_column(DateTime(timezone=True), server_default=func.now())
    msg_type: Mapped[str] = mapped_column(Text)
    train_id: Mapped[str] = mapped_column(Text, nullable=True)
    payload: Mapped[dict] = mapped_column(JSON)
