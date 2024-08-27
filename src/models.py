import os
import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.orm import relationship, declarative_base
from sqlalchemy import create_engine
from eralchemy2 import render_er


Base = declarative_base()

class User(Base):
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    username = Column(String)
    email = Column(String)
    password = Column(String)
    bio = Column(String)
    profile_pic = Column(String)

class Post(Base):
    __tablename__ = 'posts'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='posts')
    caption = Column(String)


class Media(Base):
    __tablename__ = 'media'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post', backref='media')
    media_type = Column(String)
    media_url = Column(String)

class Like(Base):
    __tablename__ = 'likes'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post', backref='likes')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='likes')

class Comment(Base):
    __tablename__ = 'comments'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post', backref='comments')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='comments')
    comment_text = Column(String)

class Favorite(Base):
    __tablename__ = 'favorites'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post', backref='favorites')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='favorites')

class Share(Base):
    __tablename__ = 'shares'
    id = Column(Integer, primary_key=True)
    post_id = Column(Integer, ForeignKey('posts.id'))
    post = relationship('Post', backref='shares')
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='shares')

class InstagramState(Base):
    __tablename__ = 'instagram_states'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship('User', backref='instagram_states')
    state_type = Column(String)
    state_text = Column(String)
    def to_dict(self):
        return {}

## Draw from SQLAlchemy base
try:
    result = render_er(Base, 'diagram.png')
    print("Success! Check the diagram.png file")
except Exception as e:
    print("There was a problem genering the diagram")
    raise e
