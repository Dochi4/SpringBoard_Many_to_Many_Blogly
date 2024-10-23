"""Models for Blogly."""

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def connect_db(app):
    db.app = app 
    db.init_app(app)

default_img = "https://static.vecteezy.com/system/resources/thumbnails/009/292/244/small/default-avatar-icon-of-social-media-user-vector.jpg"

class User(db.Model):
    """User Model"""
    __tablename__ = 'users'

    def __repr__(self):
        u = self
        return f"<User id={u.id}, first_name={u.first_name}, last_name={u.last_name}, image_url={u.image_url}>"

    id = db.Column(db.Integer, 
                    primary_key=True,
                    autoincrement=True)
    
    first_name = db.Column(db.String(50), 
                           nullable=False)
    
    last_name = db.Column(db.String(50),
                           nullable=False)
    
    image_url = db.Column(db.String, 
                          nullable=False, 
                          default=default_img)


class Post(db.Model):
    """Post Model"""
    __tablename__ = 'posts'

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)
    
    title = db.Column(db.String(50), 
                      nullable=False)
    
    content = db.Column(db.Text, 
                        nullable=False)
    
    created_at = db.Column(db.DateTime, 
                           server_default=db.func.now())

    user_id = db.Column(db.Integer, 
                        db.ForeignKey('users.id'))
    
    user = db.relationship('User', 
                           backref='posts')


class Tag(db.Model):
    """Tag Model"""
    __tablename__ = 'tags'

    id = db.Column(db.Integer, 
                   primary_key=True, 
                   autoincrement=True)

    name = db.Column(db.Text, 
                     nullable=False, 
                     unique=True)

    posts = db.relationship('Post', 
                            secondary='post_tags', 
                            backref='tags')


class PostTag(db.Model):
    """Join table for Post and Tag"""
    __tablename__ = 'post_tags'

    post_id = db.Column(db.Integer, db.ForeignKey('posts.id'), 
                        primary_key=True)
    
    tag_id = db.Column(db.Integer, db.ForeignKey('tags.id'), 
                       primary_key=True)
