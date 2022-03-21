"""smartnotes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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


urlpatterns = [
    # The Codes Below is How we Link up Every App Created to the Main Project URLS
    # Settings, so that, the Project Identifies all the URL's from Every Individuall
    # Applications and Runs THem without Errors.
    path('admin/', admin.site.urls),
    path('', include('home.urls')), # App URLS in the HOME APP Created
    path('smart/', include('notes.urls')), # All URL's from the Notes app created


]
