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

class Location(Base):
    __tablename__ = "locations"
    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    stanox: Mapped[str] = mapped_column(Text, index=True, nullable=True, unique=True)
    uic: Mapped[str] = mapped_column(Text, nullable=True)
    three_alpha: Mapped[str] = mapped_column(Text, nullable=True)
    tiploc: Mapped[str] = mapped_column(Text, nullable=True)
    nlc : Mapped[str] = mapped_column(Text, nullable=True)
    nlc_description: Mapped[str] = mapped_column(Text, nullable=True)
