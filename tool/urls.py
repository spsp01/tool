from django.urls import path
from tool.views import Index, Extractor,Httpheader,Senutourl,Googletop, Googlesite, profile, Speedpage,ScreamingFrog,RaportScreamingView,upload_file
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
    path('api',profile, name='profile'),
    path('speedp',Speedpage.as_view(), name='speedp'),
    path('raportlist',ScreamingFrog.as_view(), name='screaming'),
    path('raport/<int:pk>',RaportScreamingView.as_view(), name='raport-detail'),
    path('raportupload',upload_file, name='raport'),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.STATIC_URL, document_root=settings.MEDIA_URL)