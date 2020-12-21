from app import db


class User(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(24), unique=True, nullable=False)
    email = db.Column(db.String(50), unique=True, nullable=False)

    def __init__(self, user_name, email):
        self.user_name = user_name
        self.email = email

    def __repr__(self):
        return '<user: {}>'.format(self.user_name)

    @staticmethod
    def get_user_all():
        return User.query.all()

    @staticmethod
    def get_user_by_id(id):
        return User.query.filter_by(id=id).first()

    @staticmethod
    def get_unser_by_name(name):
        return User.query.filter_by(user_name=name).first()

    def add_item(self):
        db.session.add(self)
        db.session.commit()
