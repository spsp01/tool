from django.shortcuts import render
from django.views.generic import TemplateView, View
from tool.forms import ExtractForm,ExtractUrlForm
from tool.utils import aExtract,gethtml

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
            links = aExtract(extractform)

        if form2.is_valid():
            extractform = form2.cleaned_data['urla']
            links = gethtml(extractform)

        return render(request, self.template_name, {'form': form,'form2':form2,'payload':links})