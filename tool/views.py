from django.shortcuts import render
from django.views.generic import TemplateView, View
from tool.forms import ExtractForm,ExtractUrlForm,ExtractText, UploadFileForm
from tool.utils.utils import aExtract,gethtml,httpresponse,senutourl,getgooglelinks,getsitelinks
from tool.utils.speedp import download, createurljson
from tool.utils.screaming import NameScreaming, readcsvraport
from django.http import JsonResponse
from django.http import HttpResponse, HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from tool.models import RaportScreaming, RaportScreamingtest, Client


class Index(TemplateView):
    template_name = 'tool/index.html'

class Extractor(TemplateView):
    template_name = 'tool/extractor.html'

    def get(self,request):
        form = ExtractForm()
        form2 = ExtractUrlForm()
        return render(request,self.template_name,{'form':form,'form2':form2})

    def post(self, request):
        form = ExtractForm(request.POST)
        form2 = ExtractUrlForm(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['extract']
            links, alllinks, uniquelinks = aExtract(extractform)


        if form2.is_valid():
            extractform = form2.cleaned_data['urla']
            links, alllinks, uniquelinks = gethtml(extractform)
            print(alllinks)
            print(uniquelinks)

        return render(request, self.template_name, {'form': form,'form2':form2,'payload':links,'alllinks':alllinks,'uniquelinks':uniquelinks})


class Httpheader(TemplateView):
    template_name = 'tool/httpheader.html'

    def get(self,request):
        form = ExtractUrlForm()
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = ExtractUrlForm(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['urla']
            httpresp= httpresponse(extractform)
        return render(request, self.template_name,{'form': form,'payload':httpresp})

class Senutourl(TemplateView):
    template_name = 'tool/senuto.html'

    def get(self,request):
        form = ExtractText()
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = ExtractText(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['urlb']
            keywordspair= senutourl(extractform)

        return render(request, self.template_name,{'form': form,'keywordspair':keywordspair})

class Googletop(TemplateView):
    template_name = 'tool/googletop.html'

    def get(self,request):
        form = ExtractText()
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = ExtractText(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['urlb']
            links= getgooglelinks(extractform)
        return render(request, self.template_name,{'form': form,'links':links})

class Googlesite(TemplateView):
    template_name = 'tool/googlesite.html'

    def get(self,request):
        form = ExtractText()
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = ExtractText(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['urlb']
            links= getsitelinks(extractform)

        return render(request, self.template_name,{'form': form,'links':links})

class Speedpage(TemplateView):
    template_name = 'tool/pagespeed.html'

    def get(self,request):
        form = ExtractText()
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = ExtractText(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['urlb']
            links= getsitelinks(extractform)

        return render(request, self.template_name,{'form': form,'links':links})

class ScreamingFrog(TemplateView):
    template_name = 'tool/screamingfrog.html'

    def get(self,request):
        name = NameScreaming.service()
        summary = NameScreaming.summary()
        internal =NameScreaming.internal()
        response_codes = NameScreaming.response_codes()
        uri = NameScreaming.uri()
        page_titles = NameScreaming.page_titles()
        meta_description = NameScreaming.meta_description()
        h1 = NameScreaming.h1()
        h2 = NameScreaming.h2()
        images = NameScreaming.images()

        return render(request, self.template_name, {'name':name,'summary': summary,'internal':internal,'response_codes':response_codes,
                                                    'uri':uri,'page_titles':page_titles,'meta_description':meta_description,
                                                    'h1':h1,'h2':h2,'images':images})


class RaportScreamingView(TemplateView):
    template_name = 'tool/importraport.html'

    def get(self,request):
        name= 'Kuba'
        return render(request, self.template_name, {'name':name,})

@csrf_exempt
def profile(request):
    b=request.POST
    for i in b:
        b = download(i)
        #html = "<html><body> " + b + " </body></html>"
        c = b.split(';')
        print(c[0])
        data = {'d': b}
        return JsonResponse(data)
    #return HttpResponse(html)

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            client =request.POST.get('client')
            print(request.POST.get('date_crawled'))
            data_raport = readcsvraport(form.cleaned_data['file'])

            rap1 = RaportScreaming(client= Client.objects.get(name=client),
                                       date_crawled =request.POST.get('date_crawled'),
                                       total_url_encountered = data_raport[6][1],
                                       total_url_crawled = data_raport[7][1],
                                       internal_blocked_by_robots = data_raport[8][1],
                                       external_blocked_by_robots = data_raport[9][1],
                                       total_internal_url = data_raport[12][1],
                                       total_external_url =data_raport[13][1],
                                       internal_all =data_raport[16][1],
                                       internal_html =data_raport[17][1],
                                       internal_javascript =data_raport[18][1],
                                       internal_css =data_raport[19][1],
                                       internal_images =data_raport[20][1],
                                       internal_pdf =data_raport[21][1],
                                       internal_flash =data_raport[22][1],
                                       internal_other =data_raport[23][1],
                                       external_all =1,
                                       external_html =1,
                                       external_javascript =1,
                                       external_css =1,
                                       external_images =1,
                                       external_pdf =1,
                                       external_flash =1,
                                       external_other =1,
                                       protocol_http =1,
                                       protocol_https =1,
                                       resp_all =1,
                                       resp_blocked_robots =1,
                                       resp_blocked_resource =1,
                                       resp_no_resp =1,
                                       resp_success =1,
                                       resp_redirection =1,
                                       resp_redirection_javascript =1,
                                       resp_redirection_meta =1,
                                       resp_client_error =1,
                                       resp_server_error =1,
                                       content_large_pages =1,
                                       content_low_content_pages =1,
                                       uri_all =1,
                                       uri_non_ascii =1,
                                       uri_underscores =1,
                                       uri_uppercase = 1,
                                       uri_duplicate =1,
                                       uri_parameters = 1,
                                       titles_all = 1,
                                       titles_missing = 1,
                                       titles_duplicate = 1,
                                       titles_over_65 = 1,
                                       titles_below_30 = 1,
                                       titles_over_571 = 1,
                                       titles_below_200 =1,
                                       titles_same_h1 =1,
                                       titles_multiple =1,
                                       description_all =1,
                                       description_missing =1,
                                       description_duplicate =1,
                                       description_over_320 =1,
                                       description_below_70 =1,
                                       description_over_1866 =1,
                                       description_below_400 =1,
                                       description_multiple =1,
                                       h1_all =1,
                                       h1_missing =1,
                                       h1_duplicate =1,
                                       h1_over_70 =1,
                                       h1_multiple =1,
                                       h2_all =1,
                                       h2_missing =1,
                                       h2_duplicate =1,
                                       h2_over_70 =1,
                                       h2_multiple =1,
                                       images_all =1,
                                       images_over =1,
                                       images_missing_alt =1,
                                       dir_all =1,
                                       dir_canonical =1,
                                       dir_canonical_self =1,
                                       dir_canonicalised =1,
                                       dir_no_canonical =1,
                                       dir_next_prev =1,
                                       dir_index =1,
                                       dir_noindex =1,
                                       dir_follow =1,
                                       dir_nofollow =1,
                                       dir_none =1,
                                       dir_noachive =1,
                                       dir_nosnippet =1,
                                       dir_noodp =1,
                                       dir_noydir =1,
                                       dir_noimageindex =1,
                                       dir_notranslate =1,
                                       dir_unavailable =1,
                                       dir_refresh =1,
                                       href_all =1,
                                       href_missing_conf =1,
                                       href_inconsistent_language =1,
                                       href_noncanonical_conf =1,
                                       href_incorrect_lanmguage_code =1,
                                       href_multiple_entries =1,
                                       href_missinf_self_ref =1,
                                       href_non_using_canonical =1,
                                       href_missing_xdefaults =1,
                                       href_missing =1,
                                       ajax_all =1,
                                       ajax_hash =1,
                                       ajax_without =1,
                                       depth_0 =1,
                                       depth_1 =1,
                                       depth_2 =1,
                                       depth_3 =1,
                                       depth_4 =1,
                                       depth_5 =1,
                                       depth_6 =1,
                                       depth_7 =1,
                                       depth_8 =1,
                                       depth_9 =1,
                                       depth_10 =1,
                                       resp_1 =1,
                                       resp_2 =1,
                                       resp_3 =1,
                                       resp_4 =1,
                                       resp_5 =1,
                                       resp_6 =1,
                                       resp_7 =1,)
            rap1.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'tool/importraport.html', {'form': form})