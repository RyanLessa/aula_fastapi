from pydantic import BaseModel
from typing import List, Optional


# Schema de saída para Group
class GroupBase(BaseModel):
    name: str


class GroupCreate(GroupBase):
    pass

# Schema de saída para User
class UserBase(BaseModel):
    username: str


class GroupResponse(GroupBase):
    id: int
    users: List[UserBase] = []  # Lista de usernames associados

    class Config:
        from_attributes = True


class UserCreate(UserBase):
    group_id: int  # Associar o usuário a um grupo


class UserResponse(UserBase):
    id: int
    group: Optional[GroupBase] = None  # Detalhes do grupo

    class Config:
        from_attributes = True
