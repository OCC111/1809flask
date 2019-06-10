from app import db

from .baseModel import BaseModel



class Category(BaseModel,db.Model):
    __tablename__ = 'category'
    id = db.Column(db.Integer,primary_key=True)
    name = db.Column(db.String(50),nullable=False)
    weight = db.Column(db.Integer,nullable=False)
    status = db.Column(db.Integer,nullable=False)
    food = db.relationship('Food',backref='category')


    @property
    def status_desc(self):
        return self.status

    def __repr__(self):
        return self.name



class Food(BaseModel,db.Model):
    __tablename__ = 'food'

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    price = db.Column(db.Numeric(10,2), nullable=False)
    main_image = db.Column(db.String(256), nullable=False)
    summary = db.Column(db.String(2000), nullable=False)
    stock = db.Column(db.Integer, nullable=False)
    tags = db.Column(db.String(256), nullable=False)
    status = db.Column(db.Integer, nullable=False)
    month_count = db.Column(db.Integer, nullable=False)
    total_count = db.Column(db.Integer, nullable=False)
    view_count = db.Column(db.Integer, nullable=False)
    comment_count = db.Column(db.Integer, nullable=False)

    cat_id = db.Column(db.Integer,db.ForeignKey('category.id'))




















