"""exam URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""

from django.conf.urls import url
from.import views
urlpatterns = [
   url(r'^$', views.index, name='index'),
   url(r'^register', views.register, name='register'),
   url(r'^recoverpassword', views.recoverpassword, name='recoverpassword'),
   url(r'^regform_submit', views.regform_submit, name='regform_submit'),
   url(r'^loginform_submit', views.loginform_submit, name='loginform_submit'),
   url(r'^login', views.login, name='login'),
   url(r'^teacher_dashboard', views.teacher_dashboard, name='teacher_dashboard'),
   url(r'^student_dashboard', views.student_dashboard, name='student_dashboard'),
   url(r'^create_test', views.create_test, name='create_test'),
   url(r'^createtest_name', views.createtest_name, name='createtest_name'),
   url(r'^createtest_submit/(?P<index>[-\w]+)/(?P<i>[-\w]+)/$', views.createtest_submit, name='createtest_submit'),
   url(r'^question_submit/(?P<index>[-\w]+)/(?P<i>[-\w]+)/$', views.question_submit, name='question_submit'),
   url(r'^submit_test/(?P<index>[-\w]+)/$', views.submit_test, name='submit_test'),
   url(r'^attempt_test/(?P<index>[-\w]+)/$', views.attempt_test, name='attempt_test'),
   url(r'^give_test', views.give_test, name='give_test'),
   url(r'^view_test1', views.view_test1, name='view_test1'),
   url(r'^view_test2', views.view_test2, name='view_test2'),
   url(r'^view_results_t1', views.view_results_t1, name='view_results_t1'),
   url(r'^searchtestresults', views.searchtestresults, name='searchtestresults'),
   url(r'^findtestresults', views.findtestresults, name='findtestresults'),
   url(r'^view_results_t2/(?P<index>[-\w]+)/$', views.view_results_t2, name='view_results_t2'),
   url(r'^view_results_s1', views.view_results_s1, name='view_results_s1'),
   url(r'^view_results_s2/(?P<index>[-\w]+)/$', views.view_results_s2, name='view_results_s2'),
   url(r'^performance_graph/(?P<index>[-\w]+)/$', views.performance_graph, name='performance_graph'),
]
