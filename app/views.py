from flask_appbuilder import ModelView
from flask_appbuilder.fieldwidgets import Select2Widget
from flask_appbuilder.models.sqla.interface import SQLAInterface
from .models import Employee,Department, Function, EmployeeHistory, Benefit, MenuItem, MenuCategory, News, NewsCategory, Cinema, Movie, Movietype, Language, Loginuser, Menu1, Menu2, Menu3, Menu4, Socialmedia, Menu5, Menu6, Cinemamovie
from wtforms.ext.sqlalchemy.fields import QuerySelectField
from app import appbuilder, db
from flask_appbuilder.baseviews import expose, BaseView


def department_query():
    return db.session.query(Department)


class EmployeeHistoryView(ModelView):
    datamodel = SQLAInterface(EmployeeHistory)
    #base_permissions = ['can_add', 'can_show']
    list_columns = ['department', 'begin_date', 'end_date']


class EmployeeView(ModelView):
    datamodel = SQLAInterface(Employee)

    list_columns = ['full_name', 'department.name', 'employee_number']
    edit_form_extra_fields = {'department':  QuerySelectField('Department',
                                query_factory=department_query,
                                widget=Select2Widget(extra_classes="readonly"))}


    related_views = [EmployeeHistoryView]
    show_template = 'appbuilder/general/model/show_cascade.html'


class FunctionView(ModelView):
    datamodel = SQLAInterface(Function)
    related_views = [EmployeeView]


class DepartmentView(ModelView):
    datamodel = SQLAInterface(Department)
    related_views = [EmployeeView]


class BenefitView(ModelView):
    datamodel = SQLAInterface(Benefit)
    add_columns = ['name']
    edit_columns = ['name']
    show_columns = ['name']
    list_columns = ['name']

class MenuItemView(ModelView):
    datamodel = SQLAInterface(MenuItem)
    list_columns = ['id', 'name', 'link', 'menu_category_id']

class MenuCategoryView(ModelView):
    datamodel = SQLAInterface(MenuCategory)
    list_columns = ['id', 'name']

class NewsView(ModelView):
    datamodel = SQLAInterface(News)
    list_columns = ['id', 'title', 'content', 'date', 'newsCat_id']

class NewsCategoryView(ModelView):
    datamodel = SQLAInterface(NewsCategory)
    list_columns = ['id', 'name']

class NewsPageView(BaseView):
    default_view = 'local_news'

    @expose('/local_news/')
    def local_news(self):
        param1 = 'Local News'
        self.update_redirect()
        return self.render_template('news.html', param1 = param1)

    @expose('/global_news/')
    def global_news(self):
        param1 = 'Global News'
        self.update_redirect()
        return self.render_template('news.html', param1=param1)

class CinemaView(ModelView):
    datamodel = SQLAInterface(Cinema)
    list_columns = ['id', 'cinemaname','area', 'movie_id']
    
class MovieView(ModelView):
    datamodel = SQLAInterface(Movie)
    list_columns = ['id', 'moviename','movietype_id', 'photo', 'photo_img', 'photo_img_thumbnail']
    show_columns = ['photo_img','name']
    
class MovietypeView(ModelView):
    datamodel = SQLAInterface(Movietype)
    list_columns = ['id', 'typename']
    
class LanguageView(ModelView):
    datamodel = SQLAInterface(Language)
    list_columns = ['id', 'languagename']
    
class LoginuserView(ModelView):
    datamodel = SQLAInterface(Loginuser)
    list_columns = ['id', 'name', 'email', 'phone']
    
class Menu1View(ModelView):
    datamodel = SQLAInterface(Menu1)
    list_columns = ['id', 'title']
    
class Menu2View(ModelView):
    datamodel = SQLAInterface(Menu2)
    list_columns = ['id', 'title']
    
class Menu3View(ModelView):
    datamodel = SQLAInterface(Menu3)
    list_columns = ['id', 'title']

class Menu4View(ModelView):
    datamodel = SQLAInterface(Menu4)
    list_columns = ['id', 'title']

class SocialmediaView(ModelView):
    datamodel = SQLAInterface(Socialmedia)
    list_columns = ['id']
    
class Menu5View(ModelView):
    datamodel = SQLAInterface(Menu5)
    list_columns = ['id', 'title']

class Menu6View(ModelView):
    datamodel = SQLAInterface(Menu6)
    list_columns = ['id', 'title']
    
class CinemamovieView(ModelView):
    datamodel = SQLAInterface(Cinemamovie)
    list_columns = ['id', 'cinema', 'moviename1']
    
db.create_all()

""" Page View """
appbuilder.add_view(NewsPageView, 'Local News', category="News")
appbuilder.add_link("Global News", href="/newspageview/global_news/", category="News")

""" Custom Views """
appbuilder.add_view(MenuItemView, "MenuItem", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MenuCategoryView, "MenuCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsView, "News", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(NewsCategoryView, "NewsCategory", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(CinemaView, "Cinema", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MovieView, "Movie", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(MovietypeView, "Movietype", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(LanguageView, "Language", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(LoginuserView, "Loginuser", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(Menu1View, "Menu1", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(Menu2View, "Menu2", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(Menu3View, "Menu3", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(Menu4View, "Menu4", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(SocialmediaView, "Socialmedia", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(Menu5View, "Menu5", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(Menu6View, "Menu6", icon="fa-folder-open-o", category="Admin")
appbuilder.add_view(CinemamovieView, "Cinemamovie", icon="fa-folder-open-o", category="Admin")
