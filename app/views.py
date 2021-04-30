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
        
class menuView(BaseView):
    default_view = 'ticketing'
    
    @expose('/ticketing/')
    def ticketing(self):
        param1 = 'Ticketing'
        self.update_redirect()
        return self.render_template('ticketing.html', param1=param1)
        
    @expose('/coomingsoon/')
    def comingsoon(self):
        param1 = 'Comming soon'
        self.update_redirect()
        return self.render_template('coomingsoon.html', param1=param1)
        
    @expose('/festandpro/')
    def festandpro(self):
        param1 = 'Festival & Programes'
        self.update_redirect()
        return self.render_template('festandpro.html', param1=param1)
        
    @expose('/proandnews/')
    def proandnews(self):
        param1 = 'Promotion & News'
        self.update_redirect()
        return self.render_template('proandnews.html', param1=param1)
        
    @expose('/events/')
    def events(self):
        param1 = 'Events'
        self.update_redirect()
        return self.render_template('events.html', param1=param1)
    
    @expose('/screen/')
    def screen(self):
        param1 = 'Screen'
        self.update_redirect()
        return self.render_template('screen.html', param1=param1)

class cinemaareaView(BaseView):
    default_view = 'k11'
    
    @expose('/k11/')
    def k11(self):
        param1 = 'K11 Art House'
        self.update_redirect()
        return self.render_template('k11.html', param1=param1)
        
    @expose('/beafestival/')
    def beafestival(self):
        param1 = 'Bea Festival Suite'
        self.update_redirect()
        return self.render_template('beafestival.html', param1=param1)
        
    @expose('/windsor/')
    def windsor(self):
        param1 = 'Winsor'
        self.update_redirect()
        return self.render_template('windsor.html', param1=param1)
        
class menu99View(BaseView):
    default_view = 'aboutus'
    
    @expose('/aboutus/')
    def aboutus(self):
        param1 = 'About us'
        self.update_redirect()
        return self.render_template('aboutus.html', param1=param1)
        
    @expose('/contactus/')
    def contactus(self):
        param1 = 'Contact us'
        self.update_redirect()
        return self.render_template('contactus.html', param1=param1)

    @expose('/career/')
    def career(self):
        param1 = 'Career'
        self.update_redirect()
        return self.render_template('career.html', param1=param1)

    @expose('/faq/')
    def faq(self):
        param1 = 'FAQ'
        self.update_redirect()
        return self.render_template('faq.html', param1=param1)

    @expose('/personalinf/')
    def personalinf(self):
        param1 = 'Personal Information Colletion Statement'
        self.update_redirect()
        return self.render_template('personalinf.html', param1=param1)
        
    @expose('/privacypolicy/')
    def privacypolicy(self):
        param1 = 'Privacy Policy'
        self.update_redirect()
        return self.render_template('privacypolicy.html', param1=param1)
        
    @expose('/termofuse/')
    def termofuse(self):
        param1 = 'Term Of Use'
        self.update_redirect()
        return self.render_template('termofuse.html', param1=param1)

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
appbuilder.add_view(menuView, 'Ticketing', category="Menu")
appbuilder.add_link("Comming soon", href="/menuview/coomingsoon/", category="Menu")
appbuilder.add_link("Festival & Programes", href="/menuview/festandpro/", category="Menu")
appbuilder.add_link("Promotions & News", href="/menuview/proandnews/", category="Menu")
appbuilder.add_link("Events", href="/menuview/events/", category="Menu")
appbuilder.add_link("Screen AD", href="/menuview/screen/", category="Menu")
appbuilder.add_view(cinemaareaView, 'K11 Art House', category="Cinemaarea")
appbuilder.add_link("Bea Festival Suite", href="/cinemaareaview/beafestival/", category="Cinemaarea")
appbuilder.add_link("Windsor", href="/cinemaareaview/windsor/", category="Cinemaarea")
appbuilder.add_view(menu99View, 'About Us', category="More")
appbuilder.add_link("Contact us", href="/menu99view/contactus/", category="More")
appbuilder.add_link("Career", href="/menu99view/career/", category="More")
appbuilder.add_link("FAQ", href="/menu99view/faq/", category="More")
appbuilder.add_link("Personal Information Collection Statement", href="/menu99view/personalinf/", category="More")
appbuilder.add_link("Privacy Policy Statement", href="/menu99view/privacypolicy/", category="More")
appbuilder.add_link("Term Of Use", href="/menu99view/termofuse/", category="More")

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
