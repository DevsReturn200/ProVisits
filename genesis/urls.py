from django.contrib import admin
from django.urls import path, re_path
from django.conf import settings
from django.conf.urls.static import static

from app import views

from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    
    ############################################################
    ######################## Users Urls ########################
    ############################################################
    path('dashboard/', views.Dashboard, name=''),
    path('analytics/', views.Analytics, name=''),
    path('membership/', views.Membership, name=''),
    path('settings/', views.Settings, name=''),
    path('closeaccount/', views.CloseAccount, name=''),
    path('changepassword/', views.ChangePassword, name=''),
    path('getmembership/<str:tp>/', views.GetMemberShip, name=''),
    path('cards/', views.Cards, name=''),
    path('products/', views.Products, name=''),
    path('product/<str:PID>/', views.Product, name=''),
    path('addproduct/', views.AddProduct, name=''),
    path('editproduct/<str:PID>/', views.EditProduct, name=''),
    path('deleteproduct/<str:PID>/', views.DeleteProduct, name=''),
    path('messages/', views.Messages, name=''),
    path('message/<str:messageID>/', views.Message, name=''),
    path('addnewcard/', views.AddNewCard, name=''),
    path('editcard/<str:cardname>/', views.EditCard, name=''),
    path('deletecard/<str:cardname>/', views.DeleteCard, name=''),

    ############################################################
    ######################## Global Urls #######################
    ############################################################
    path('', views.HomePage, name=''),
    path('about/', views.AboutPage, name=''),
    path('testimonials/', views.TestimonialsPage, name=''),
    path('contactus/', views.ContactUsPage, name=''),
    path('signin/', views.SignInPage, name=''),
    path('signup/', views.SignUpPage, name=''),
    path('logout/', views.logout, name=''),
    path('manifesto/', views.Manifesto, name=''),
    path('productt/', views.Productt, name=''),
    path('bugs/', views.Bugs, name=''),
    path('card/<str:cardname>/', views.ViewCard, name=''),
    path('sourcecode/', views.SourceCode, name=''),
    path('profile/<str:username>/', views.Profile, name=''),
    ############ Payment Handler ################
    path('paymenthandler/', views.paymenthandler, name='paymenthandler'),

    # REST UNDEFINED PATTERNS
    # re_path(r'^.*/$', views.send_bad_request, name='bad-route'),
]

urlpatterns += static(settings.MEDIA_URI,document_root=settings.MEDIA_ROOT)