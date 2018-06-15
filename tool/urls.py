from django.urls import path
from tool.views import Index, Extractor,Httpheader,Senutourl,Googletop, Googlesite
from django.conf import settings
from django.conf.urls.static import static

app_name='toolseo'
urlpatterns = [
    path('', Index.as_view(), name='index' ),
    path('extractor', Extractor.as_view(), name='extractor' ),
    path('httpheader', Httpheader.as_view(), name='httpheader' ),
    path('senuto', Senutourl.as_view(), name='senuto' ),
    path('googletop', Googletop.as_view(), name='googletop' ),
    path('googlesite', Googlesite.as_view(), name='googlesite' ),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)