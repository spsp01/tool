from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView,ListView
from tool.forms import ExtractForm,ExtractUrlForm,ExtractText, UploadFileForm,ExtractTwo
from tool.utils.utils import aExtract,gethtml,httpresponse,senutourl,getgooglelinks,getsitelinks,senutoposition, senutopositioncsv,getlinks,linksfromsitemap
from tool.utils.speedp import download, createurljson
from tool.utils.screaming import NameScreaming, readcsvraport, readcsvallraport
from tool.utils.position import getposition
from tool.utils.sfcli import startsf, getfile
from tool.utils.readlight import Lighthouseraport
from tool.utils.dolphin import getapi
from django.http import JsonResponse, HttpResponseRedirect, HttpResponse
from django.views.decorators.csrf import csrf_exempt
from tool.models import RaportScreaming, RaportScreamingtest, Client, RaportInlink


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
            links, alllinks, uniquelinks = getlinks(extractform)
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

class ScreamingFrog(ListView):
    template_name = 'tool/screamingfrog_list.html'
    model = RaportScreaming
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['clients'] = Client.objects.values_list('name',flat=True).distinct()
        return context


class RaportScreamingView(DetailView):
    model = RaportScreaming
    template_name = 'tool/screamingfrog_detail.html'
    def get_context_data(self, **kwargs):
         context = super().get_context_data(**kwargs)
         raport = context['object']
         resources = str(round(5*(1- raport.internal_blocked_by_robots/raport.total_url_encountered),1)).replace(',','.')
         url_sum = raport.uri_non_ascii + raport.uri_underscores + raport.uri_uppercase + raport.uri_duplicate + raport.uri_parameters + raport.uri_over_115
         codes = str(round(5 * (1 - (raport.resp_success / raport.resp_all/100)), 1)).replace(',', '.')
         if url_sum != 0:
             urladress = str(round(5 * (1- url_sum/6/raport.uri_all),1)).replace(',', '.')

         else:
             urladress = str(5.0)

         title_list = [raport.titles_over_65,raport.titles_below_30,raport.titles_over_571,
                       raport.titles_below_200,raport.titles_same_h1,raport.titles_multiple]
         title_average = sum(title_list)/len(title_list)/raport.titles_all

         title = str(round(5*(1- title_average-raport.titles_missing/raport.titles_all),1)).replace(',', '.')

         description_list = [raport.description_duplicate,raport.description_over_320,raport.description_below_70,
                             raport.description_over_1866,raport.description_below_400,
                             raport.description_multiple]
         description_average = sum(description_list)/len(description_list)/raport.description_all
         description = str(round(5*(1- description_average-raport.description_missing/raport.description_all),1)).replace(',', '.')

         h1_list = [raport.h1_duplicate, raport.h1_over_70, raport.h1_multiple,]
         h1_average = sum(h1_list)/len(h1_list)/raport.h1_all
         h1 = str(round(5*(1 - h1_average - raport.h1_missing/raport.h1_all),1)).replace(',', '.')
         raports_client = RaportScreaming.objects.filter(client=raport.client)
         context['add'] = {'zasoby':resources,'kody':codes, 'urladress': urladress,'title':title,'description':description,
                           'h1':h1, 'raports_client':raports_client,}
         return context


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
                                       external_all =data_raport[27][1],
                                       external_html =data_raport[28][1],
                                       external_javascript =data_raport[29][1],
                                       external_css =data_raport[30][1],
                                       external_images =data_raport[31][1],
                                       external_pdf =data_raport[32][1],
                                       external_flash = data_raport[33][1],
                                       external_other =data_raport[34][1],
                                       protocol_http = data_raport[39][1],
                                       protocol_https =data_raport[40][1],
                                       resp_all =data_raport[43][1],
                                       resp_blocked_robots =data_raport[44][1],
                                       resp_blocked_resource =data_raport[45][1],
                                       resp_no_resp =data_raport[46][1],
                                       resp_success =data_raport[47][1],
                                       resp_redirection =data_raport[48][1],
                                       resp_redirection_javascript =data_raport[49][1],
                                       resp_redirection_meta =data_raport[50][1],
                                       resp_client_error =data_raport[51][1],
                                       resp_server_error =data_raport[52][1],
                                       content_large_pages =data_raport[55][1],
                                       content_low_content_pages =data_raport[56][1],
                                       uri_all =data_raport[59][1],
                                       uri_non_ascii =data_raport[60][1],
                                       uri_underscores =data_raport[61][1],
                                       uri_uppercase = data_raport[62][1],
                                       uri_duplicate =data_raport[63][1],
                                       uri_parameters = data_raport[64][1],
                                       uri_over_115 = data_raport[65][1],
                                       titles_all = data_raport[68][1],
                                       titles_missing = data_raport[69][1],
                                       titles_duplicate = data_raport[70][1],
                                       titles_over_65 = data_raport[71][1],
                                       titles_below_30 = data_raport[72][1],
                                       titles_over_571 = data_raport[73][1],
                                       titles_below_200 =data_raport[74][1],
                                       titles_same_h1 =data_raport[75][1],
                                       titles_multiple =data_raport[76][1],
                                       description_all =data_raport[79][1],
                                       description_missing =data_raport[80][1],
                                       description_duplicate =data_raport[81][1],
                                       description_over_320 =data_raport[82][1],
                                       description_below_70 =data_raport[83][1],
                                       description_over_1866 =data_raport[84][1],
                                       description_below_400 =data_raport[85][1],
                                       description_multiple =data_raport[86][1],
                                       h1_all =data_raport[95][1],
                                       h1_missing =data_raport[96][1],
                                       h1_duplicate =data_raport[97][1],
                                       h1_over_70 =data_raport[98][1],
                                       h1_multiple =data_raport[99][1],
                                       h2_all =data_raport[102][1],
                                       h2_missing =data_raport[103][1],
                                       h2_duplicate =data_raport[104][1],
                                       h2_over_70 =data_raport[105][1],
                                       h2_multiple =data_raport[106][1],
                                       images_all =data_raport[109][1],
                                       images_over =data_raport[110][1],
                                       images_missing_alt =data_raport[111][1],
                                       dir_all = data_raport[115][1],
                                       dir_canonical =data_raport[116][1],
                                       dir_canonical_self =data_raport[117][1],
                                       dir_canonicalised =data_raport[118][1],
                                       dir_no_canonical =data_raport[119][1],
                                       dir_next_prev =data_raport[125][1],
                                       dir_index =data_raport[138][1],
                                       dir_noindex =data_raport[139][1],
                                       dir_follow =data_raport[140][1],
                                       dir_nofollow =data_raport[141][1],
                                       dir_none =data_raport[142][1],
                                       dir_noachive =data_raport[143][1],
                                       dir_nosnippet = data_raport[144][1],
                                       dir_noodp = data_raport[145][1],
                                       dir_noydir = data_raport[146][1],
                                       dir_noimageindex = data_raport[147][1],
                                       dir_notranslate = data_raport[148][1],
                                       dir_unavailable = data_raport[149][1],
                                       dir_refresh = data_raport[150][1],
                                       href_all = data_raport[153][1],
                                       href_missing_conf = data_raport[154][1],
                                       href_inconsistent_language = data_raport[157][1],
                                       href_noncanonical_conf = data_raport[158][1],
                                       href_noindex_conf = data_raport[159][1],
                                       href_incorrect_lanmguage_code = data_raport[160][1],
                                       href_multiple_entries = data_raport[161][1],
                                       href_missinf_self_ref =data_raport[162][1],
                                       href_non_using_canonical =data_raport[163][1],
                                       href_missing_xdefaults =data_raport[164][1],
                                       href_missing =data_raport[165][1],
                                       ajax_all =data_raport[168][1],
                                       ajax_hash =data_raport[169][1],
                                       ajax_without =data_raport[170][1],
                                       depth_0=data_raport[236][1],
                                       depth_1=data_raport[237][1],
                                       depth_2=data_raport[238][1],
                                       depth_3=data_raport[239][1],
                                       depth_4=data_raport[241][1],
                                       depth_5=data_raport[242][1],
									   depth_6 = data_raport[243][1],
                                       depth_7 = data_raport[244][1],
                                       depth_8 = data_raport[245][1],
                                       depth_9 = data_raport[246][1],
                                       depth_10 = 0,
                                       resp_1 =data_raport[270][1],
                                       resp_2 =data_raport[271][1],
                                       resp_3 =data_raport[272][1],
                                       resp_4 =data_raport[273][1],
                                       resp_5 =data_raport[274][1],
                                       resp_6 =data_raport[275][1],
                                       resp_7 =data_raport[276][1],
									   )
            rap1.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'tool/importraport.html', {'form': form})

def upload_raport_all(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        print(Client.objects.get(name='Ford'))
        if form.is_valid():
           csv_data = readcsvallraport(form.cleaned_data['file'])
           client = request.POST.get('client')
           date_crawled = request.POST.get('date_crawled')
           for index, i in enumerate(csv_data):
               if index > 0:
                   print(str(index)+' '+i[0]+', '+i[1]+', '+i[2])
                   rap_all = RaportInlink(client = Client.objects.get(id=1),
                                          date_crawled='2018-08-19',
                                          url_info=i[0],
                                          content=i[1],
                                          status_code=i[2],
                                          status=i[3],
                                          title = i[4],
                                          title_len = i[5],
                                          title_len_pix = i[6],
                                          description = i[10],
                                          desc_len = i[11],
                                          desc_len_pix = i[12],
                                          h1_1 = i[18],
                                          h1_1_len = i[19],
                                          h1_2 = i[20],
                                          h1_2_len = i[21],
                                          h2_1 = i[22],
                                          h2_1_len = i[23],
                                          h2_2 = i[24],
                                          h2_2_len = i[25],
                                          meta_robots = i[26],
                                          noindex = i[26],
                                          nofollow = i[26],
                                          meta_refresh = i[27],
                                          canonical = i[28],
                                          size = i[29],
                                          word_count = i[30],
                                          text_ratio = i[31],
                                          crawl_depth = i[32],
                                          inlinks = i[33],
                                          unique_inlinks = i[34],
                                          percent_total = i[35],
                                          outlinks = i[36],
                                          unique_outlinks = i[37],
                                          external_outlinks = i[38],
                                          unique_external_outlinks = i[39],
                                          response_time = i[41],
                                          last_modified = i[42],
                                          redirect_URI = i[43],
                                          redirect_type = i[44])
                   rap_all.save()
           return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'tool/raport_all_list.html', {'form': form})


class Clientraportlist(ListView):
    template_name = 'tool/raport_client_raport_list.html'
    model = RaportScreaming
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['raportlist'] = RaportScreaming.objects.filter(client__name=self.kwargs['client'])
        context['clients'] = Client.objects.values_list('name', flat=True).distinct()
        context['client'] = self.kwargs['client']
        return context

    # def get_queryset(self):
    #     self.client = get_object_or_404(RaportScreaming, name=self.kwargs['client'])
    #     return RaportScreaming.objects.filter(publisher=self.client)

@csrf_exempt
def positions(request):
    b=request.POST
    domain = b['domain']
    phrase = b['url']
    u = getposition(phrase, domain)
    data = {'d': u}
    return JsonResponse(data)


class PositionView(TemplateView):
    template_name = 'tool/positions.html'

    def get(self,request):
        form = ExtractText()
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = ExtractText(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['urlb']
            links= getsitelinks(extractform)

        return render(request, self.template_name,{'form': form,'links':links})


class ScreamignstartView(TemplateView):
    template_name = 'tool/screamingstart.html'

    def get(self,request):
        form = ExtractText()
        files = getfile()
        return render(request, self.template_name, {'form': form,'links':files})

    def post(self, request):
        form = ExtractText(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['urlb']
            startsf(extractform)

        return render(request, self.template_name,{'form': form,'links': 'OK' })

class LighthouseView(TemplateView):
    template_name = 'tool/lighthouse-raport.html'

    def get(self,request):
        raport = Lighthouseraport('E:\lighthouse\\axa.pl\\5-10-2018\\axa.pl-ubezpieczenie-zycie-i-zdrowie.json')

        content = {'summary': raport.readmetrics(),
                   'url':raport.readinfo(),
                   'metrics':raport.readproperty('metrics'),
                   'first_contentful_paint': raport.readproperty('first-contentful-paint'),
                   'first_meaningful_paint': raport.readproperty('first-meaningful-paint'),
                   'speed_index':raport.readproperty('speed-index'),
                   'interactive':raport.readproperty('interactive'),
                   'errors_in_console': raport.readproperty('errors-in-console'),
                   'is_on_https': raport.readproperty('is-on-https'),
                   'mobile_friendly':raport.readproperty('mobile-friendly'),
                   'robots_txt':raport.readproperty('robots-txt'),
                   'is_crawlable':raport.readproperty('is-crawlable'),
                   'without_javascript':raport.readproperty('without-javascript'),
                   'final_screenshot':raport.readproperty('final-screenshot'),
                   'network_requests': raport.readproperty('network-requests'),
                   }

        return render(request, self.template_name, {'content': content})


class SenutoPosition(TemplateView):
    template_name = 'tool/senuto-position.html'

    def get(self,request):
        form = ExtractTwo()
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = ExtractTwo(request.POST)

        if form.is_valid():

           domain = form.cleaned_data['urlb']
           phrase=form.cleaned_data['phrase']

           if request.POST['button'] == 'download':
             response = HttpResponse(senutopositioncsv(domain, phrase))
             response['Content-Disposition'] = "attachment; filename='pozycje.csv'"
             return response
           else:
              response= senutoposition(domain,phrase)
           return render(request, self.template_name,{'form': form,'content':response})

class SeleniumPosition(TemplateView):
    template_name = 'tool/senuto-position.html'

    def get(self,request):
        form = ExtractTwo()
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = ExtractTwo(request.POST)

        if form.is_valid():

           domain = form.cleaned_data['urlb']
           phrase=form.cleaned_data['phrase']
           response='a'
           return render(request, self.template_name, {'form': form, 'content': response})

class SenutoApi(TemplateView):
    template_name = 'tool/senuto-dolphin.html'

    def get(self,request):
        form = ExtractText()
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = ExtractText(request.POST)

        if form.is_valid():

           domain = form.cleaned_data['urlb']
           response= getapi(domain,'weekly','domain_seasonality')
           information = getapi(domain, 'weekly', 0)
           domain_competitors = getapi(domain, 'weekly', 'domain_competitors')
           phrases = getapi(domain, 'weekly', 'domain_keywords_top')
           return render(request, self.template_name,{'form': form,'content':response,'information':information,'domain_competitors':domain_competitors,'phrases':phrases})

class Sitemaplinks(TemplateView):
    template_name = 'tool/sitemaplinks.html'

    def get(self,request):
        form = ExtractUrlForm()
        return render(request, self.template_name, {'form': form,})

    def post(self, request):
        form = ExtractUrlForm(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['urla']
            sitemaplinks= linksfromsitemap(extractform)
            #print(sitemaplinks)

        return render(request, self.template_name,{'form': form,'payload':sitemaplinks})