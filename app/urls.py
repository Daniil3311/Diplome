
from django.contrib import admin
from django.urls import include, path

urlpatterns =[
    path(r'admin/', admin.site.urls),
    path('api/v1/', include('app1.urls', namespace='app1')),

]


