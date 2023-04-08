from django.urls import path
from .views import *


urlpatterns = [
    # path('admin/', admin.site.urls),

    path('register/', user_register, name='user-register'),

]
