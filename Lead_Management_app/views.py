from django.shortcuts import render
from Lead_Management_app.models import source_list, followup_history
from django.views.generic import ListView
# Create your views here.
def home(request):
    if request.method=="POST":
        start_date= request.POST.get('start_date')
        end_date = request.POST.get('end_date')
        comp_list =followup_history.objects.all()
        return render(request,'home.html',{'comp_list':comp_list})

class home_list(ListView):
    model = source_list
    context_object_name = 'context'

