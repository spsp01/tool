from django.shortcuts import render
from django.views.generic import TemplateView, View, DetailView,ListView
from tool.forms import ExtractForm,ExtractUrlForm,ExtractText, UploadFileForm
from tool.utils.utils import aExtract,gethtml,httpresponse,senutourl,getgooglelinks,getsitelinks
from tool.utils.speedp import download, createurljson
from tool.utils.screaming import NameScreaming, readcsvraport, readcsvallraport
from django.http import JsonResponse, HttpResponseRedirect
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

class ScreamingFrog(ListView):
    template_name = 'tool/screamingfrog_list.html'
    model = RaportScreaming
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
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
                                       external_all =data_raport[26][1],
                                       external_html =data_raport[27][1],
                                       external_javascript =data_raport[28][1],
                                       external_css =data_raport[29][1],
                                       external_images =data_raport[30][1],
                                       external_pdf =data_raport[31][1],
                                       external_flash = data_raport[32][1],
                                       external_other =data_raport[33][1],
                                       protocol_http = data_raport[37][1],
                                       protocol_https =data_raport[38][1],
                                       resp_all =data_raport[41][1],
                                       resp_blocked_robots =data_raport[42][1],
                                       resp_blocked_resource =data_raport[43][1],
                                       resp_no_resp =data_raport[44][1],
                                       resp_success =data_raport[45][1],
                                       resp_redirection =data_raport[46][1],
                                       resp_redirection_javascript =data_raport[47][1],
                                       resp_redirection_meta =data_raport[48][1],
                                       resp_client_error =data_raport[49][1],
                                       resp_server_error =data_raport[50][1],
                                       content_large_pages =data_raport[53][1],
                                       content_low_content_pages =data_raport[54][1],
                                       uri_all =data_raport[57][1],
                                       uri_non_ascii =data_raport[58][1],
                                       uri_underscores =data_raport[59][1],
                                       uri_uppercase = data_raport[60][1],
                                       uri_duplicate =data_raport[61][1],
                                       uri_parameters = data_raport[62][1],
                                       uri_over_115 = data_raport[63][1],
                                       titles_all = data_raport[66][1],
                                       titles_missing = data_raport[67][1],
                                       titles_duplicate = data_raport[68][1],
                                       titles_over_65 = data_raport[69][1],
                                       titles_below_30 = data_raport[70][1],
                                       titles_over_571 = data_raport[71][1],
                                       titles_below_200 =data_raport[72][1],
                                       titles_same_h1 =data_raport[73][1],
                                       titles_multiple =data_raport[74][1],
                                       description_all =data_raport[77][1],
                                       description_missing =data_raport[78][1],
                                       description_duplicate =data_raport[79][1],
                                       description_over_320 =data_raport[80][1],
                                       description_below_70 =data_raport[81][1],
                                       description_over_1866 =data_raport[82][1],
                                       description_below_400 =data_raport[83][1],
                                       description_multiple =data_raport[84][1],
                                       h1_all =data_raport[93][1],
                                       h1_missing =data_raport[94][1],
                                       h1_duplicate =data_raport[95][1],
                                       h1_over_70 =data_raport[96][1],
                                       h1_multiple =data_raport[97][1],
                                       h2_all =data_raport[100][1],
                                       h2_missing =data_raport[101][1],
                                       h2_duplicate =data_raport[102][1],
                                       h2_over_70 =data_raport[103][1],
                                       h2_multiple =data_raport[104][1],
                                       images_all =data_raport[107][1],
                                       images_over =data_raport[108][1],
                                       images_missing_alt =data_raport[109][1],
                                       dir_all = data_raport[113][1],
                                       dir_canonical =data_raport[114][1],
                                       dir_canonical_self =data_raport[115][1],
                                       dir_canonicalised =data_raport[116][1],
                                       dir_no_canonical =data_raport[117][1],
                                       dir_next_prev =data_raport[118][1],
                                       dir_index =data_raport[119][1],
                                       dir_noindex =data_raport[120][1],
                                       dir_follow =data_raport[121][1],
                                       dir_nofollow =data_raport[122][1],
                                       dir_none =data_raport[123][1],
                                       dir_noachive =data_raport[124][1],
                                       dir_nosnippet = data_raport[125][1],
                                       dir_noodp = data_raport[126][1],
                                       dir_noydir = data_raport[127][1],
                                       dir_noimageindex = data_raport[128][1],
                                       dir_notranslate = data_raport[129][1],
                                       dir_unavailable = data_raport[130][1],
                                       dir_refresh = data_raport[131][1],
                                       href_all = data_raport[134][1],
                                       href_missing_conf = data_raport[135][1],
                                       href_inconsistent_language = data_raport[136][1],
                                       href_noncanonical_conf = data_raport[137][1],
                                       href_noindex_conf = data_raport[138][1],
                                       href_incorrect_lanmguage_code = data_raport[139][1],
                                       href_multiple_entries = data_raport[140][1],
                                       href_missinf_self_ref =data_raport[141][1],
                                       href_non_using_canonical =data_raport[142][1],
                                       href_missing_xdefaults =data_raport[143][1],
                                       href_missing =data_raport[144][1],
                                       ajax_all =data_raport[147][1],
                                       ajax_hash =data_raport[148][1],
                                       ajax_without =data_raport[149][1],
                                       depth_0=data_raport[180][1],
                                       depth_1=data_raport[181][1],
                                       depth_2=data_raport[182][1],
                                       depth_3=data_raport[183][1],
                                       depth_4=data_raport[184][1],
                                       depth_5=data_raport[185][1],
									   depth_6 = data_raport[186][1],
                                       depth_7 = data_raport[187][1],
                                       depth_8 = data_raport[188][1],
                                       depth_9 = data_raport[189][1],
                                       depth_10 = data_raport[190][1],
                                       resp_1 =data_raport[215][1],
                                       resp_2 =data_raport[216][1],
                                       resp_3 =data_raport[217][1],
                                       resp_4 =data_raport[218][1],
                                       resp_5 =data_raport[219][1],
                                       resp_6 =data_raport[220][1],
                                       resp_7 =data_raport[221][1],
									   )
            rap1.save()
            return HttpResponseRedirect('/')
    else:
        form = UploadFileForm()
    return render(request, 'tool/importraport.html', {'form': form})

def upload_raport_all(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
           csv_data = readcsvallraport(form.cleaned_data['file'])
           date_crawled = '2018-08-02'
           client = 'Axa'
           for i in csv_data:

               print(i)
    else:
        form = UploadFileForm()
    return render(request, 'tool/raport_all_list.html', {'form': form})