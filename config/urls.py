"""config URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.1/topics/http/urls/
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
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


admin.site.site_header = "Администрирование Art-Vostorg.ru"
admin.site.index_title = "Администрирование вашего сайта"
admin.site.site_title = "Административный сайт Art-Vostorg.ru"

urlpatterns = [
    path('', include('art_vostorg.urls')),
    path('admin/', admin.site.urls),
]

urlpatterns += [
    # 'неявные' view из auth app (шаблоны лежат в /templates/registration)
    path("users/", include("django.contrib.auth.urls")),
    # остальные view и шаблоны пользователей лежат в users app
    path("users/", include("users.urls")),
]

urlpatterns += [
    path('tinymce/', include('tinymce.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += [
#     path('__debug__/', include('debug_toolbar.urls')),
    ]
