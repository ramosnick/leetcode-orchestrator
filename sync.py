
from core.leetcode_client import get_recent_submissions
from storage.database import SessionLocal
from storage.models import User, Submission
from sqlalchemy import select

def get_or_create_user(db : Session, username: string):
    
    statement = select(User).where(User.username == username)
    results = db.execute(statement).scalars().one_or_none()

    if results is None:
        results = User(username=username)
        db.add(results)
        db.commit()
        db.refresh(results)

    return results

#Testing:
if __name__ == "__main__":
    
    db  = SessionLocal()

    try:
        michael = "Seymomic"
        nathan = "NStevens"
        ashton = ""
        nick = "ramosnick"

        user1 = get_or_create_user(db, michael)
        print(f"Run 1-> UserID: {user1.id}, Username: {user1.username}")

        user2 = get_or_create_user(db, michael)
        print(f"Run 2-> UserID: {user2.id}, Username: {user2.username}")

        if(user1.id != user2.id):
            print("Error, you duplicated a user")

    finally:
        db.close()
