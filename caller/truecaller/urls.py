from django.urls import path,include
from truecaller import views

from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('registeredUsers',views.UserProfileViewSet)
router.register('contacts',views.UserContactViewSet)
router.register('spam',views.SpamViewSet)
#router.register('globaldata',views.GlobalDatabase,basename='globaldata')

urlpatterns = [
    path('login/',views.UserLoginApiView.as_view()),
    path('',include(router.urls)),
    #path('globaldata/',views.GlobalDatabase.as_view()),

]