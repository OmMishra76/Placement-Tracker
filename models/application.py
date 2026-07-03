from models import db
from datetime import datetime

class Application(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)

    company = db.Column(db.String(120), nullable=False)
    role = db.Column(db.String(120), nullable=False)
    job_link = db.Column(db.String(500))
    apply_date = db.Column(db.Date)
    deadline = db.Column(db.Date)
    status = db.Column(db.String(50), default='Applied')
    resume_version = db.Column(db.String(80))
    notes = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def __repr__(self):
        return f"<Application {self.company} - {self.role}>"