from app import db


class Session(db.Model):
    __table_args__ = {'extend_existing': True}
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    session = db.Column(db.String(250), unique=True, nullable=False)
    status = db.Column(db.Boolean, nullable=False)

    def __init__(self, user_id, session, status):
        self.user_id = user_id
        self.session = session
        self.status = status

    def __repr__(self):
        return '<session: {}>'.format(self.session)

    @staticmethod
    def get_session_all():
        return Session.query.all()

    @staticmethod
    def get_session_by_id(id):
        return Session.query.filter_by(user_id=id).first()

    def add_session(self):
        db.session.add(self)
        db.session.commit()
