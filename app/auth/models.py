from app import db
from core.abstract_models import Model

group_permissions = db.Table(
    'group_permission',
    db.Column('group_id', db.String(), db.ForeignKey('groups.id')),
    db.Column('permission_id', db.String(), db.ForeignKey('permissions.id'))
)

user_groups = db.Table(
    'user_groups',
    db.Column('group_id', db.String(), db.ForeignKey('groups.id')),
    db.Column('user_id', db.String(), db.ForeignKey('users.id'))
)

user_permissions = db.Table(
    'user_permissions',
    db.Column('permission_id', db.String(), db.ForeignKey('permissions.id')),
    db.Column('user_id', db.String(), db.ForeignKey('users.id'))
)


class Permission(Model):
    __tablename__ = "permissions"
    name = db.Column(db.String(), nullable=False, unique=True)
    codename = db.Column(db.String())

    def __repr__(self):
        return F"<Permission({self.name})>"


class Group(Model):
    __tablename__ = "groups"
    name = db.Column(db.String(), nullable=False, unique=True)
    permissions = db.relationship("Permission", lazy="dynamic", secondary="group_permission")

    def __repr__(self):
        return F"<Group({self.name})>"


class User(Model):
    __tablename__ = "users"
    username = db.Column(db.String(), nullable=False, unique=True)
    first_name = db.Column(db.String(), nullable=False)
    last_name = db.Column(db.String(), nullable=False)
    email = db.Column(db.String(), nullable=False, unique=True)
    password = db.Column(db.String(), nullable=False)
    is_active = db.Column(db.Boolean(), default=False)
    last_login = db.Column(db.DateTime())

    is_superuser = db.Column(db.Boolean(), default=False)
    groups = db.relationship("Group", lazy="dynamic", secondary="user_groups")
    permissions = db.relationship("Permission", lazy="dynamic", secondary="user_permissions")

    def __repr__(self):
        return  F"<User({self.username})>"