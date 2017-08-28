from django.conf.urls import url

from . import views  # means that from the same directory you are currently in, import the views of this directory

app_name = 'user'

urlpatterns = [

    # www.spark.com/user/1
    url(r'^(?P<user_id>[0-9])+/$', views.profile_page, name='profile_page'),

    # www.spark.com/user/register
    url(r'^register/$', views.UserFormView.as_view(), name='register'),
]
