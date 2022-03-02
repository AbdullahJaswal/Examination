from .views import *

from django.urls import path

app_name = 'product'

urlpatterns = [
    # Topic
    path('topic/', TopicList.as_view(), name='topicList'),
    path('topic/<int:pk>/', TopicDetail.as_view(), name='topicDetail'),

    # SubTopic
    path('subtopic/', SubTopicList.as_view(), name='subTopicList'),
    path('subtopic/<int:pk>/', SubTopicDetail.as_view(), name='subTopicDetail'),

    # Question
    path('question/', QuestionList.as_view(), name='questionList'),
    path('question/<int:pk>/', QuestionDetail.as_view(), name='questionDetail'),

    # Answer
    path('answer/', AnswerList.as_view(), name='answerList'),
    path('answer/<int:pk>/', AnswerDetail.as_view(), name='answerDetail'),

    # # Nested (Category)
    # path(
    #     'category/<int:cat>/product/',
    #     CategoryProductList.as_view(),
    #     name='categoryProductList'
    # ),

    # # Nested (Subject)
    # path(
    #     'subject/<int:sub>/product/',
    #     SubjectProductList.as_view(),
    #     name='subjectProductList'
    # ),

    # # Nested (Category Subject)
    # path(
    #     'category/<int:cat>/subject/<int:sub>/product/',
    #     CategorySubjectProductList.as_view(),
    #     name='categorySubjectProductList'
    # ),
]
