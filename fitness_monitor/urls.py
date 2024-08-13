# myproject/urls.py

from django.contrib import admin
from django.urls import path, include
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi
from .views import home  # Importa a nova view



"""
URL Configuration for MyProject.

This file contains the URL patterns for the project, including the admin site,
API routes, and documentation views using Swagger UI and ReDoc.

The URL patterns include:
- The home page view.
- The Django admin site.
- The API routes included from the 'api' app.
- Swagger UI for API documentation.
- ReDoc for alternative API documentation.

Each URL pattern is associated with a view or a schema view to provide
appropriate responses for various endpoints.

Schema View Configuration:
- Title: "API de Monitoramento de Atividades Físicas"
- Version: 'v1'
- Description: Documentation for the API monitoring physical activities.
- Terms of Service: URL to the terms of service.
- Contact: Email address for API contact.
- License: Name of the license used for the API.

"""
# Configuração do Schema View para Swagger UI
schema_view = get_schema_view(
    openapi.Info(
        title="API de Monitoramento de Atividades Físicas",
        default_version='v1',
        description="Documentação da API para monitoramento de atividades físicas",
        terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="contact@yourapi.local"),
        license=openapi.License(name="BSD License"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    path('', home, name='home'), 
    path('admin/', admin.site.urls),
    path('api/', include('api.urls')), 
    path('swagger/', schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    path('redoc/', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
]
