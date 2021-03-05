import uuid
from datetime import datetime

from app import db


class AbstractTimeStampModel(db.Model):
    __abstract__ = True
    id = db.Column(db.String(), default=uuid.uuid4(), primary_key=True)
    created_date = db.Column(db.DateTime(), default=datetime.utcnow())
    updated_date = db.Column(db.DateTime())


class Model(AbstractTimeStampModel):
    __abstract__ = True

    def save(self, commit=True):
        db.session.add(self)
        if commit:
            db.session.commit()

    @classmethod
    def create(cls, **kwargs):
        instance = cls(**kwargs)
        instance.save()
        return instance
