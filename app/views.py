from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
from app.forms import *
def insert_contact(request):
    ECFO=ContactForm()
    d={'ECFO':ECFO}
    if request.method =='POST':
        FDO=ContactForm(request.POST)
        if FDO.is_valid():
            return HttpResponse(str(FDO.cleaned_data))
        else:
            return HttpResponse('invalid data')
    return render(request,'contact.html',d)

def insert_Topic(request):
    ETFO=TopicForm()
    d={'ETFO':ETFO}
    if request.method =='POST':
        TNO=TopicForm(request.POST)
        if TNO.is_valid():
            tname=TNO.cleaned_data['topic_name']
            TO=Topic.objects.get_or_create(topic_name=tname)
            if TO[1]:
                return HttpResponse(f'{tname} data is inserted')
            else:
                return HttpResponse(f'{tname} is all ready present')
        else:
            return HttpResponse('Invalid data')
    return render(request,'inset_Topicform.html',d)


def insert_Webpage(request):
    EWFO=WebpageForm()
    d={'EWFO':EWFO}
    if request.method == 'POST':
        WNO=WebpageForm(request.POST)
        if WNO.is_valid():
            tname=WNO.cleaned_data['topic_name']
            Name=WNO.cleaned_data['name']
            Url=WNO.cleaned_data['url']
            LTO=Topic.objects.get(topic_name=tname)
            WTO=Webpage.objects.get_or_create(topic_name=LTO, name=Name , url=Url)
            if WTO[1]:
                return HttpResponse(f'{tname} data is inserted')
            else:
                return HttpResponse(f'{tname} is all ready present')
        else:
            return HttpResponse('invalid data') 
    return render(request,'insert_Webpageform.html',d) 

def insert_access(request):
    EAFO=AccessRecordform()
    d={'EAFO':EAFO}
    if request.method=='POST':
        ARNO=AccessRecordform(request.POST)
        if ARNO.is_valid():
            name=ARNO.cleaned_data['name']
            autor=ARNO.cleaned_data['autor']
            date=ARNO.cleaned_data['date']
            LWO=Webpage.objects.get(name=name)
            ATO=AccessRecords.objects.get_or_create(name=LWO,autor=autor,date=date) 
            if ATO[1]:  
                return HttpResponse(f'{autor} data is inserted')
            else:
                return HttpResponse(f'{autor} is all ready present') 
        else:
            return HttpResponse(f' data is invalid')   
    return render(request,'insert_AccessRecord.html',d)