from django.contrib.sessions import serializers
from django.http import HttpResponse
from django.template import RequestContext
from django.shortcuts import render_to_response
from TranslatorManager.models import Client,JobType,ClientJob
import logging,sys
from TranslatorManager.forms import ClientForm,AddJobForm


logger = logging.getLogger(__name__)

# Create your views here.
def index(request):
    # Request the context of the request.
    # The context contains information such as the client's machine details, for example.
    context = RequestContext(request)

    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage is the same as {{ boldmessage }} in the template!
    context_dict = {'clients': Client.objects.all()}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.
    return render_to_response('index.html', context_dict, context)

def jobs(request):
    context = RequestContext(request)
    context_dict = Client.objects.all()
    jobs  = ClientJob.objects.all()
    paymentInfo = JobType.objects.all()

    #totalPrice = 0.0
    #if jobs[0].service == "Translation":
    #    totalPrice += paymentInfo[0].words_new * jobs[0].words_new + paymentInfo[0].words_fuzzy85 * jobs[0].words_fuzzy85 + paymentInfo[0].words_match * jobs[0].words_match + paymentInfo[0].words_rep * jobs[0].words_rep + paymentInfo[0].words_ice * jobs[0].words_ice

    form = AddJobForm()

    totalPrice = calc_DTP(1, 'Localeyes')
    return render_to_response('jobs.html', {'clients': context_dict, 'price':totalPrice, 'form': form}, context)

def add_job(request):
    context = RequestContext(request)


    if request.method == 'POST':
        form = AddJobForm(request.POST)

        #allClients = Client.objects.get(clientName=form.clientName)
        if form.is_valid():
            #newJob = \
            form.save(commit=True)
            #newJob.key_field = form.client #CLIENT ID FROM FORM
            form.save()

            return jobs(request)
        else:
            print form.errors
    else:
        form = AddJobForm()

    return render_to_response('jobs.html', {'form': form}, context)

def completed(request):
    context = RequestContext(request)
    context_dict = {'boldmessage': "I am bold font from the context"}
    return render_to_response('completed.html', context_dict, context)

def clients(request):
    context = RequestContext(request)
    context_dict = {'clients': Client.objects.all()}

    return render_to_response('clients.html',context_dict , context)

def add_client(request):
    context = RequestContext(request)
    context_dict = Client.objects.all()

    if request.method == 'POST':
        form = ClientForm(request.POST)

        if form.is_valid():
            form.save(commit=True)

            return clients(request)
        else:
            print form.errors
    else:
        form = ClientForm()

    return render_to_response('clients.html', {'form': form, 'clients': context_dict}, context)

def all_clients(request, client):
    print >> sys.stderr, "PENIS"
    logger.debug("MURT")
    logger.info("INFO")
    current_client = Client.objects.get(clientName=client)
    logger.debug(current_client)
    allClients = Client.objects.all().filter(clientName=current_client)
    logger.debug(allClients)
    json_models = serializers.serialize("json", allClients)
    return HttpResponse(json_models, mimetype="application/javascript")


def calc_DTP(jobID, clientInput):
    TRANSLATION = 'Translation'
    REVIEW = 'Review'
    DTP = 'DTP'

    client = Client.objects.get(clientName=clientInput) #Get only the relevant client
    clientJob  = ClientJob.objects.get(client=client, id=jobID)   #Get all the jobs for this client
    clientJobTypes = JobType.objects.get(client=client, service=DTP) #Get the clientJobTypes for this client

    totalPrice = 0.0
    #for job in clientJobTypes:
    totalPrice += clientJob.hours_Spent*clientJobTypes.pay_hourly

    if clientJob.pay_rush > 0:
        totalPrice = totalPrice*(1+(clientJob/100))

    return totalPrice