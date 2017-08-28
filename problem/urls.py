from django.conf.urls import url
from . import views  # means that from the same directory you are currently in, import the views of this directory

app_name = 'problem'

urlpatterns = [

    url(r'^list/$', views.problem_list, name='problem_list'),

    # www.spark.com/problem/
    url(r'^$', views.index, name='index'),

    # www.spark.com/problem/1
    url(r'^(?P<problem_id>[0-9]+)/$', views.problem_page, name='problem_page'),

    # www.spark.com/problem/1/upvote/
    url(r'^(?P<problem_id>[0-9]+)/upvote/$', views.upvote, name='prob_upvote'),

    url(r'^(?P<problem_id>[0-9]+)/downvote/$', views.downvote, name='prob_downvote'),

    # www.spark.com/problem/1/solution/1
    url(r'^(?P<problem_id>[0-9]+)/solution/(?P<solution_id>[0-9]+)/$', views.solution_page, name='solution_page'),

    # www.spark.com/problem/1/solution/1/upvote/
    url(r'^(?P<problem_id>[0-9]+)/solution/(?P<solution_id>[0-9]+)/upvote/$', views.sol_upvote, name='sol_upvote'),

    url(r'^(?P<problem_id>[0-9]+)/solution/(?P<solution_id>[0-9]+)/downvote/$', views.sol_downvote, name='sol_downvote'),

    url(r'^(?P<problem_id>[0-9]+)/subscribe/$', views.subscribe,
        name='subscribe'),

    # www.spark.com/problem/form
    url(r'^form/$', views.ProblemCreate.as_view(), name='problem-form'),

    # www.spark.com/problem/1/sol-form
    url(r'^(?P<problem_id>[0-9]+)/sol-form/$', views.SolutionCreate.as_view(), name='solution-form'),

    url(r'^(?P<problem_id>[0-9]+)/create_solution/$', views.create_solution, name='create_solution'),

]