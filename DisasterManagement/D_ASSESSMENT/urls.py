from django.urls import path
from .views import *

urlpatterns = [

path('report', report_disaster),
path('mark/<int:disaster_id>', mark_affected, name="mark"),
path('', current_disasters),
path('analysis/<int:disaster_id>', view_affected, name='analysis'),

]