# SQLAlchemy Models
from sqlalchemy import ForeignKey, Column
from sqlalchemy.orm import DeclarativeBase, relationship

# Optional Imports
from sqlalchemy import String, Integer, Boolean, TIMESTAMP, text

# SQLAlchemy base model
class Base(DeclarativeBase):
    pass

# Samples (edit from here)
class Sample(Base):
    __tablename__ = "samples"
    sample_id = Column(Integer, primary_key=True, nullable=False)
    string_field = Column(String, nullable=False)
    int_field = Column(Integer, nullable=True)
    timestamp_field = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))
    bool_field = Column(Boolean, server_default='TRUE', nullable=False)

    owner_id = Column(Integer, ForeignKey("users.id", ondelete="CASCADE"), nullable=False)
    owner = relationship("User", back_populates="sample")
    
class CompositeSample(Base):
    __tablename__ = "composite_samples"
    sample_id = Column(Integer, primary_key=True, nullable=False)
    user_id = Column(Integer, primary_key=True, nullable=False)

class User(Base):
    __tablename__ = "users"
    user_id = Column(Integer, primary_key=True, nullable=False)
    email = Column(String, nullable=False, unique=True)
    password = Column(String, nullable=False)
    created_at = Column(TIMESTAMP(timezone=True), nullable=False, server_default=text('now()'))