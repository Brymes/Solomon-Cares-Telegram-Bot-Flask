from datetime import datetime
from extensions import db


class Clients(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    order_id = db.Column(db.Integer(), unique=True)

    user_id = db.Column(db.String())
    # first_name = db.Column(db.String(80))
    # last_name = db.Column(db.String(80))
    # dob = db.Column(db.String())

    client_data = db.Column(db.Text())

    created_at = db.Column(db.DateTime(), default=datetime.utcnow())

    service_type = db.Column(db.String())

    amount_paid = db.Column(db.Integer())
    time_paid = db.Column(db.DateTime())
    has_paid = db.Column(db.Boolean(), default=False)

    completed_at = db.Column(db.DateTime())
    service_completed = db.Column(db.Boolean(), default=False)

    order_canceled = db.Column(db.Boolean(), default=False)

    def data(self):
        return {
            'id': self.id,
            'order_id': self.order_id,
            'user_id': self.user_id,
            'client_data': self.client_data,
            'self.created_at': self.created_at,
            'service_type': self.service_type,
            'amount_paid': self.amount_paid,
            'time_paid': self.time_paid,
            'has_paid': self.has_paid,
            'completed_at': self.completed_at,
            'service_completed': self.service_completed,
            'order_canceled': self.order_canceled
        }

    @classmethod
    def get_by_order_id(cls, order_id):
        return cls.query.filter_by(order_id=order_id).first()

    @classmethod
    def get_by_user_id(cls, user_id):
        return cls.query.filter_by(user_id=user_id).all()

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Admin(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    user_id = db.Column(db.String(), nullable=False)

    @classmethod
    def get_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()


class Commands(db.Model):

    id = db.Column(db.Integer(), primary_key=True)
    command = db.Column(db.String())
    command_desc = db.Column(db.String())

    
    @classmethod
    def get_all(cls):
        return cls.query.all()

    def save(self):
        db.session.add(self)
        db.session.commit()

    def delete(self):
        db.session.delete(self)
        db.session.commit()
