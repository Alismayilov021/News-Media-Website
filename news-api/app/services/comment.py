from app import db
from datetime import datetime

class Comment(db.Model):
    __tablename__ = 'comments'

    id = db.Column(db.Integer, primary_key=True)
    content = db.Column(db.String(500), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    # Foreign key to link the comment to an article
    article_id = db.Column(db.Integer, db.ForeignKey('articles.id'), nullable=False)
    # Foreign key to link the comment to a user
    author_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=False)

    # Relationships
    article = db.relationship('Article', back_populates='comments')
    author = db.relationship('User', back_populates='comments')

    def __init__(self, content, article_id, author_id):
        self.content = content
        self.article_id = article_id
        self.author_id = author_id

    def __repr__(self):
        return f'<Comment {self.id} - {self.content[:20]}...>'

    def to_dict(self):
        return {
            'id': self.id,
            'content': self.content,
            'created_at': self.created_at,
            'updated_at': self.updated_at,
            'author_id': self.author_id,
            'article_id': self.article_id,
            'author': self.author.to_dict() if self.author else None
        }
