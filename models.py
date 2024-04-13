from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Blacklist(db.Model):
    __tablename__ = 'blacklist'

    email = db.Column(db.String(50), primary_key=True)
    app_uuid = db.Column(db.String(50), unique=True, nullable=False)
    blocked_reason = db.Column(db.String(255), nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    ip = db.Column(db.String(50), nullable=False)

    def __repr__(self):
        return f'<Blacklist {self.email}>'
