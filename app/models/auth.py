from app import db


class Auth(db.Model):
    __table_args__ = {'extend_existing': True}

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.String(80),
                        db.ForeignKey('user.id'),
                        nullable=False)

    passwd = db.Column(db.String(24), nullable=False)

    def __init__(self, user_id, passwd):
        self.user_id = user_id
        self.passwd = passwd

    def __repr__(self):
        return '<auth: {}>'.format(self.user_id)

    @staticmethod
    def get_by_id(id):
        return Auth.query.filter_by(id=id).first()

    def add_item(self):
        db.session.add(self)
        db.session.commit()
