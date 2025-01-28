from sqlalchemy.orm import Session
from .models import Group, User, Migrations
from .database import engine
from .schemas import GroupCreate, UserCreate

Migrations.migrations(engine)


# CRUD para Group
def create_group(db: Session, group: GroupCreate):
    new_group = Group(name=group.name)
    db.add(new_group)
    db.commit()
    db.refresh(new_group)
    return new_group


def get_groups(db: Session):
    groups = db.query(Group).all()

    print(groups)

    return groups


def get_group_by_id(db: Session, group_id: int):
    return db.query(Group).filter(Group.id == group_id).first()


def delete_group(db: Session, group_id: int):
    group = db.query(Group).filter(Group.id == group_id).first()
    if group:
        db.delete(group)
        db.commit()
    return group


# CRUD para User
def create_user(db: Session, user: UserCreate):
    new_user = User(username=user.username, group_id=user.group_id)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


def get_users(db: Session):
    return db.query(User).all()


def get_user_by_id(db: Session, user_id: int):
    return db.query(User).filter(User.id == user_id).first()


def delete_user(db: Session, user_id: int):
    user = db.query(User).filter(User.id == user_id).first()
    if user:
        db.delete(user)
        db.commit()
    return user
