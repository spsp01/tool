from django.urls import path
from tool.views import Index, Extractor
from django.conf import settings
from django.conf.urls.static import static

app_name='toolseo'
urlpatterns = [
    path('', Index.as_view(), name='index' ),
    path('extractor', Extractor.as_view(), name='extractor' ),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)