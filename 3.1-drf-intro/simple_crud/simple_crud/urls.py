from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from measurements import views

# TODO: настройте роутер и подключите `ProjectViewSet` и `MeasurementViewSet`

router = DefaultRouter()
router.register('project', views.ProjectViewSet, basename='project')
router.register('measurement', views.MeasurementViewSet, basename='measurement')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/v1/', include(router.urls))
]
