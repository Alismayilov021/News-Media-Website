from app import db
from datetime import datetime

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.Text, nullable=False)
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # Relationships
    article = db.relationship('Article', backref=db.backref('comments', lazy=True))
    author = db.relationship('User', backref=db.backref('comments', lazy=True))

    def __init__(self, content, article_id, author_id):
        self.content = content
        self.article_id = article_id
        self.author_id = author_id

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'article_id': self.article_id,
            'author_id': self.author_id,
            'author': self.author.username,  # Assuming the User model has a 'username' field
            'created_at': self.created_at
        }
