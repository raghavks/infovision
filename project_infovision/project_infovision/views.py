from django.shortcuts import render, get_object_or_404
import json
import config
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.views.decorators.csrf import csrf_exempt


##
from django.shortcuts import render_to_response
from django.template import RequestContext
#
from models import Discoverorgdata,Companylist
def index(request):
    # latest_question_list = Question.objects.order_by('-pub_date')[:5]
    # template = loader.get_template('index.html')
    # context = {
    #     'latest_question_list': latest_question_list,
    # }
    # return HttpResponse(template.render(context, request))
    return render(request, 'index.html',{"json_data":json.dumps(config.json_data)})
def recentvisitors(request):
    records = Discoverorgdata.objects.all().only('company_name', 'website', 'description')
    return render(request, 'result.html', {"data": records[:10]})


def topvisitors(request):
    records = Discoverorgdata.objects.all().only('company_name', 'website', 'description')
    return render(request, 'result.html', {"data": records[:10]})



def getData(request):
    records = Discoverorgdata.objects.all().only('company_name', 'website','description')

    return render(request, 'result.html', {"data":records[:10]})

@csrf_exempt
def freeSearch(request):
    if request.method=="POST":

        searchdata = request.POST.get('search')
        records = Discoverorgdata.objects(company_name__icontains=searchdata)
        page = request.GET.get('page', 1)
        paginator = Paginator(records, 10)
        try:
            companies = paginator.page(page)
        except PageNotAnInteger:
            companies = paginator.page(1)
        except EmptyPage:
            companies = paginator.page(paginator.num_pages)

        company_list = []
        for i in Companylist.objects.all():
            # print i.text
            company_list.append((i.text).encode('utf-8'))
        json_dumps = json.dumps(company_list)

        print "saldkldm", paginator.num_pages
        return render(request, 'freesearch.html', {"data": companies, "company": json_dumps, 'paginator': paginator,'stylecheck':paginator.num_pages,'search_term':searchdata}, )

    else:
        records = Discoverorgdata.objects.all().only('company_name', 'website','description')
        # autocomplete_company = Companylist.objects.all()

        page = request.GET.get('page', 1)

        paginator = Paginator(records, 10)
        try:
            companies = paginator.page(page)
        except PageNotAnInteger:
            companies = paginator.page(1)
        except EmptyPage:
            companies = paginator.page(paginator.num_pages)

        company_list=[]
        for i in Companylist.objects.all():
            print i.text
            company_list.append((i.text).encode('utf-8'))
        json_dumps = json.dumps(company_list)

        print "saldkldm",paginator.num_pages
        return render(request, 'freesearch.html', {"data":companies,"company":json_dumps,'paginator':paginator,'stylecheck':paginator.num_pages},)


def getCompanyInfo(request):
    id = request.GET.get('id')
    data=None
    for i in Discoverorgdata.objects(id=id):
        data=  i
    print data.employee_details

    data_list=[]

    # import random
    # for data in Discoverorgdata.objects.all():
    #     data_list.append({"text": data.company_name, "count": random.randint(1, 100)})
    #
    # print "*"*100
    # print json.dumps(data_list)
    # print "*"*100

    return render(request, 'company_template.html', {"record":data})
