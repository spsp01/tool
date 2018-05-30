from django.shortcuts import render
from django.views.generic import TemplateView, View
from tool.forms import ExtractForm,ExtractUrlForm,ExtractText
from tool.utils.utils import aExtract,gethtml,httpresponse,senutourl
from tool.utils.scrapegoogle import top50g,geturltext

class Index(TemplateView):
    template_name = 'tool/index.html'

    def get(self, request):
        return render(request, self.template_name, {'active':'home',})

class Extractor(TemplateView):
    template_name = 'tool/extractor.html'

    def get(self,request):
        form = ExtractForm()
        form2 = ExtractUrlForm()
        return render(request,self.template_name,{'form':form,'form2':form2,'active':'extractor'})

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

        return render(request, self.template_name, {'form': form,'form2':form2,'payload':links,'alllinks':alllinks,'uniquelinks':uniquelinks, 'active':'extractor'})


class Httpheader(TemplateView):
    template_name = 'tool/httpheader.html'

    def get(self,request):
        form = ExtractUrlForm()
        return render(request, self.template_name, {'form': form,'active':'httpheader'})

    def post(self, request):
        form = ExtractUrlForm(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['urla']
            httpresp= httpresponse(extractform)
        return render(request, self.template_name,{'form': form,'payload':httpresp,'active':'httpheader'})

class Senutourl(TemplateView):
    template_name = 'tool/senuto.html'

    def get(self,request):
        form = ExtractText()
        return render(request, self.template_name, {'form': form,'active':'senuto'})

    def post(self, request):
        form = ExtractText(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['urlb']
            keywordspair= senutourl(extractform)
        return render(request, self.template_name,{'form': form,'keywordspair':keywordspair,'active':'senuto'})

class Googletop(TemplateView):
    template_name = 'tool/googletop.html'

    def get(self,request):
        form = ExtractText()
        return render(request, self.template_name, {'form': form,'active':'googletop'})

    def post(self, request):
        form = ExtractText(request.POST)
        if form.is_valid():
            extractform = form.cleaned_data['urlb']
            keywordspair= geturltext(extractform)
        return render(request, self.template_name,{'form': form,'payload':keywordspair,'active':'googletop'})