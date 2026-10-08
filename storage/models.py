
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, nullable=False, index=True)
    tier_level = Column(Integer, default=1) 
    #Tier 1: No Data Structures, no Algorithms, Tier (Not Leader Eligible)
    #Tier 2: Data Structures, no Algorithms
    #Tier 3: Both Data Structures and Algorithms 
    leader = Column(Boolean, default=False)
    is_active = Column(Boolean, default=True)
    submissions = relationship("Submission", back_populates="user", cascade="all, delete-orphan")

class Submission(Base):
    __tablename__ = "submissions"
    id = Column(Integer, primary_key=True, index=True)
    title_slug = Column(String, nullable=False, index=True)
    title = Column(String, nullable=False)
    timestamp = Column(Integer, nullable=False)
    user_id = Column(Integer, ForeignKey("users.id"), nullable=False)
    user = relationship("User", back_populates="submissions")
