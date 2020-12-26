from django.shortcuts import render
from django.views.generic import View
from .models import *
import requests
from .tasks import *
from django.http import JsonResponse
import json


class StatusDescriptor:
    def __set_name__(self, owner_class, property_name):
        self.property_name = property_name

    def __set__(self, instance, value):
        key = '_' + self.property_name
        r = requests.get(value)
        setattr(instance, key, r.status_code)


    def __get__(self, instance, owner):
        key = '_' + self.property_name
        return getattr(instance, key, None)


class Main(View):
    status = Status_Descriptor()

    def get(self, request):
        all_urls = Url.objects.all()
        urls = {}
        if all_urls:
            for url in all_urls:
                name = url.url_name
                self.status = url.url_name
                urls[name] = self.status
        return render(request, 'url_check/index.html', context={'urls': urls})



class AjaxHandler(View):

    def post(self, request):
        if request.is_ajax():
            interval = int(json.loads(request.POST.get('interval')))
            q_url = request.POST.get('url')
            flag = request.POST.get('flag')
            test.delay(interval)
            if q_url:
                url = Url.objects.get(url_name__iexact = q_url)
                if flag == '1':
                    url.url_checker = False
                elif flag == '2':
                    url.url_checker = True
                url.save()
            context ={}
            items = Url.objects.all().values()
            for item in items:
                context[item['url_name']] = item['url_status']
            return JsonResponse(context, safe=False)
        return render(request, 'url_check/index.html')
