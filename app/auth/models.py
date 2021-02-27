from app import db
from datetime import datetime
from core.abstract_models import BaseModel

group_permissions = db.Table(
    db.Column('group_id', db.String(), db.ForeignKey('groups.id')),
    db.Column('permission_id', db.String(), db.ForeignKey('permissions.id'))
)

user_groups = db.Table(
    db.Column('group_id', db.String(), db.ForeignKey('groups.id')),
    db.Column('permission_id',db.String(),db.ForeignKey('users.id'))
)

user_permissions = db.Table(
    db.Column('permission_id', db.String(), db.ForeignKey('permissions.id')),
    db.Column('user_id', db.String(), db.ForeignKey('users.id'))
)


class Permission(BaseModel):
    __tablename__ = "permissions"
    name = db.Column(db.String(), nullable=False, unique=True)
    codename = db.Colun(db.String())


class Group(BaseModel):
    __tablename__ = "groups"
    name = db.Column(db.String(), nullable=False, unique=True)
    permissions = db.relationship(secondary=group_permissions)


class User(BaseModel):
    username = db.Column(db.String(), nullable=False, unique=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False)
    password = db.Column(db.String(), nullable=False)
    is_active = db.Column(db.Boolean(), default=False)
    last_login = db.Column(db.DateTime())

    is_superuser = db.Column(db.Boolean(), default=False)
    groups = db.relationship(secondary=user_groups)
    permissions = db.relationship(secondary=user_permissions)


