
from django.urls import path
from .views import CoursesViewSet
urlpatterns = [
   
    path('courses', CoursesViewSet.as_view({
        'get':'list',
        'post':'create',      
    })),
    
    path('courses/<str:pk>', CoursesViewSet.as_view({
        'get':'retrieve',
        'put':'update',
        'delete':'destroy'
    }))
    
    # path('', CoursesViewSet.as_view())
]
