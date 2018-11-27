from django.urls import path
from tool.views import Index, Extractor,Httpheader,Senutourl,Googletop, Googlesite, profile, \
    Speedpage,ScreamingFrog,RaportScreamingView,upload_file,upload_raport_all,Clientraportlist, positions,PositionView, ScreamignstartView,SenutoPosition,LighthouseView,SenutoApi,Sitemaplinks
from django.conf import settings
from django.conf.urls.static import static

app_name='toolseo'
urlpatterns = [
    path('', Index.as_view(), name='index' ),
    path('extractor', Extractor.as_view(), name='extractor' ),
    path('httpheader', Httpheader.as_view(), name='httpheader' ),
    path('senuto', Senutourl.as_view(), name='senuto' ),
    path('senutoposition', SenutoPosition.as_view(), name='senutoposition' ),
    path('googletop', Googletop.as_view(), name='googletop' ),
    path('googlesite', Googlesite.as_view(), name='googlesite' ),
    path('api',profile, name='profile'),
    path('apiposition',positions,name='positionapi'),
    path('speedp',Speedpage.as_view(), name='speedp'),
    path('position',PositionView.as_view(), name='position'),
    path('raportlist',ScreamingFrog.as_view(), name='screaming'),
    path('raport/<int:pk>',RaportScreamingView.as_view(), name='raport-detail'),
    path('raport/<client>',Clientraportlist.as_view(), name='raport-client'),
    path('raportupload',upload_file, name='raport'),
    path('raportallupload',upload_raport_all, name='raportall'),
    path('screamingstart',ScreamignstartView.as_view(), name='screamingstart'),
    path('lighthouse',LighthouseView.as_view(), name='lighthouse'),
    path('senutoapi',SenutoApi.as_view(), name='senutoapi'),
    path('sitemaplinks', Sitemaplinks.as_view(), name='sitemaplinks' ),
    ]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)+static(settings.STATIC_URL, document_root=settings.MEDIA_URL)
