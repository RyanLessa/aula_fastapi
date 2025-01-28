from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from .database import get_db
from .schemas import GroupCreate, GroupResponse, UserCreate, UserResponse
from .controllers import create_group, get_groups, get_group_by_id, delete_group, create_user, get_users, get_user_by_id, delete_user

router = APIRouter()


@router.post('/groups/', response_model=GroupResponse)
def create_group_endpoint(group: GroupCreate, db: Session = Depends(get_db)):
    return create_group(db, group)


@router.get('/groups/', response_model=list[GroupResponse])
def get_groups_endpoint(db: Session = Depends(get_db)):
    return get_groups(db)


@router.get('/groups/{group_id}', response_model=GroupResponse)
def get_group_endpoint(group_id: int, db: Session = Depends(get_db)):
    group = get_group_by_id(db, group_id)

    if not group:
        raise HTTPException(status_code=404, detail="Group not found")
    return group


@router.delete('/groups/{group_id}')
def delete_group_endpoint(group_id: int, db: Session = Depends(get_db)):
    group = delete_group(db, group_id)

    if not group:
        raise HTTPException(status_code=404, detail="Group not found")

    return {"message": "Group deleted successfully"}


@router.post('/users/', response_model=UserResponse)
def create_user_endpoint(user: UserCreate, db: Session = Depends(get_db)):
    return create_user(db, user)


@router.get('/users/', response_model=list[UserResponse])
def get_users_endpoint(db: Session = Depends(get_db)):
    return get_users(db)


@router.get('/users/{user_id}', response_model=UserResponse)
def get_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = get_user_by_id(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return user


@router.delete('/users/{user_id}')
def delete_user_endpoint(user_id: int, db: Session = Depends(get_db)):
    user = delete_user(db, user_id)

    if not user:
        raise HTTPException(status_code=404, detail="User not found")
    return {"message": "User deleted successfully"}
