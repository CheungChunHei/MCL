import datetime
from flask import Markup, url_for
from sqlalchemy import Table, Column, Integer, String, ForeignKey, Date, Text
from sqlalchemy.orm import relationship
from flask_appbuilder import Model
from flask_appbuilder.models.mixins import ImageColumn

class Gender(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Country(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique = True, nullable=False)

    def __repr__(self):
        return self.name

class Department(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Function(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name


class Benefit(Model):
    id = Column(Integer, primary_key=True)
    name = Column(String(50), unique=True, nullable=False)

    def __repr__(self):
        return self.name

assoc_benefits_employee = Table('benefits_employee', Model.metadata,
                                  Column('id', Integer, primary_key=True),
                                  Column('benefit_id', Integer, ForeignKey('benefit.id')),
                                  Column('employee_id', Integer, ForeignKey('employee.id'))
)


def today():
    return datetime.datetime.today().strftime('%Y-%m-%d')


class EmployeeHistory(Model):
    id = Column(Integer, primary_key=True)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    employee_id = Column(Integer, ForeignKey('employee.id'), nullable=False)
    employee = relationship("Employee")
    begin_date = Column(Date, default=today)
    end_date = Column(Date)


class Employee(Model):
    id = Column(Integer, primary_key=True)
    full_name = Column(String(150), nullable=False)
    address = Column(Text(250), nullable=False)
    fiscal_number = Column(Integer, nullable=False)
    employee_number = Column(Integer, nullable=False)
    department_id = Column(Integer, ForeignKey('department.id'), nullable=False)
    department = relationship("Department")
    function_id = Column(Integer, ForeignKey('function.id'), nullable=False)
    function = relationship("Function")
    benefits = relationship('Benefit', secondary=assoc_benefits_employee, backref='employee')

    begin_date = Column(Date, default=datetime.date.today(), nullable=True)
    end_date = Column(Date, default=datetime.date.today(), nullable=True)

    def __repr__(self):
        return self.full_name

class MenuItem(Model):
    __tablename__ = 'menu_item'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    link = Column(String(150), nullable=False)
    menu_category_id = Column(Integer, ForeignKey('menu_category.id'), nullable=False)
    menu_category = relationship("MenuCategory")

class MenuCategory(Model):
    __tablename__ = 'menu_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)


class News(Model):
    __tablename__ = 'news'
    id = Column(Integer, primary_key=True)
    title = Column(String(50), nullable=False)
    content = Column(String(500), nullable=False)
    date = Column(Date, default=datetime.date.today(), nullable=True)
    newsCat_id = Column(Integer, ForeignKey('news_category.id'), nullable=False)
    newsCat = relationship("NewsCategory")

class NewsCategory(Model):
    __tablename__ = 'news_category'
    id = Column(Integer, primary_key=True)
    name = Column(String(50), nullable=False)
    
class Cinema(Model):
    __tablename__ = 'cinema'
    id = Column(Integer, primary_key=True)
    cinemaname = Column(String(50), nullable=False)
    area = Column(String(120), nullable=False)
    movie_id = Column(Integer, ForeignKey('movie.id'), nullable=False)
    movie = relationship("Movie")
    
class Movie(Model):
    __tablename__ = "movie"
    id = Column(Integer, primary_key=True)
    moviename = Column(String(50), nullable=True)
    movietype_id = Column(Integer, ForeignKey('movietype.id'), nullable=True)   
    movie_type = relationship("Movietype")
    photo = Column(ImageColumn(size=(300, 300, True), thumbnail_size=(30, 30, True)))
    
    def photo_img(self):
        im = ImageManager()
        if self.photo:
            return Markup('<a href="' + url_for('MovieView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="' + im.get_url(self.photo) +\
              '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('MovieView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')

    
    def photo_img_thumbnail(self):
        im = ImageManager()
        if self.photo:
            return Markup('<a href="' + url_for('MovieView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="' + im.get_url_thumbnail(self.photo) +\
              '" alt="Photo" class="img-rounded img-responsive"></a>')
        else:
            return Markup('<a href="' + url_for('MovieView.show',pk=str(self.id)) +\
             '" class="thumbnail"><img src="//:0" alt="Photo" class="img-responsive"></a>')
    
             
class Movietype(Model): 
    __tablename__ = "movietype"
    id = Column(Integer, primary_key=True)
    typename = Column(String(50), nullable=False)
    
class Language(Model):
    __tablename__ = 'language'
    id = Column(Integer, primary_key=True)
    languagename = Column(String(10), nullable=False)
    
class Loginuser(Model):
    __tablename__ = 'loginUser'
    id = Column(Integer, primary_key=True)
    name = Column(String(20), nullable=False)
    email = Column(String(50), nullable=False)
    phone = Column(Integer, nullable=False)
    
class Menu1(Model):
    __tablename__ = 'menu1'
    id = Column(Integer, primary_key=True)
    title = Column(String(10), nullable=False)
    
class Menu2(Model):
    __tablename__ = 'menu2'
    id = Column(Integer, primary_key=True)
    title = Column(String(10), nullable=False)
    
class Menu3(Model):
    __tablename__ = 'menu3'
    id = Column(Integer, primary_key=True)
    title = Column(String(10), nullable=False)
    
class Menu4(Model):
    __tablename__ = 'menu4'
    id = Column(Integer, primary_key=True)
    title = Column(String(10), nullable=False)
    
class Socialmedia(Model):
    __tablename__ = 'socialmedia'
    id = Column(Integer, primary_key=True)
    
class Menu5(Model):
    __tablename__ = 'menu4'
    id = Column(Integer, primary_key=True)
    title = Column(String(10), nullable=False)
    
class Menu6(Model):
    __tablename__ = 'menu4'
    id = Column(Integer, primary_key=True)
    title = Column(String(10), nullable=False)
    
class Cinemamovie(Model): 
    __tablename__ = "cinemamovie"
    id = Column(Integer, primary_key=True)
    cinemaname1 = Column(String(100), nullable=False)
    moviename = Column(String(100), nullable=False)
