# -*- coding: utf-8 -*-
from __future__ import absolute_import, unicode_literals

from django.conf.urls import url

from . import views

urlpatterns = [
    url(
        regex=r'^$',
        view=views.QuestionListView.as_view(),
        name='list'
    ),

    url(
        regex=r'^(?P<pk>[0-9]+)/$',        
        view=views.QuestionDetailView.as_view(),
        name='detail'
    ),

    url(
        regex=r'^(?P<pk>[0-9]+)/results/$',        
        view=views.QuestionResultsView.as_view(),
        name='results'
    ),

     url(
        regex=r'^(?P<question_id>[0-9]+)/vote/$',        
        view=views.vote,
        name='vote'
    ),

]