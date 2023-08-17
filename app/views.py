from django.shortcuts import render
from django.views.generic import ListView
from django.contrib.auth.models import User
from .models import Company,Statistic,Service,PlayList,Clients,Position,Team,Contact,Blog,Portfolio
# Create your views here
def index(request):
    company = Company.objects.all()
    statistic = Statistic.objects.all()
    service = Service.objects.all()
    playlist = PlayList.objects.all()
    clients = Clients.objects.all()
    team = Team.objects.all()
    contact = Contact.objects.all()
    portfolio = Portfolio.objects.all()
    contex = {
        'Company':company,
        'Statistic':statistic,
        'Service':service,
        'Playlist':playlist,
        'Clients':clients,
        'Team':team,
        'Contact':contact,
        'Portfolio':portfolio,
    }
    return render(request,['index.html'],contex)
class AboutViews(ListView):
    model = Company
    template_name = 'about.html'
    context_object_name = 'About'

class TeamViews(ListView):
    model = Team
    template_name = 'Team.html'
    context_object_name = 'Team'

class ServiceViews(ListView):
    model = Service
    template_name = 'service.html'
    context_object_name = 'Service'

class BlogViews(ListView):
    model = Blog
    template_name = 'blog.html'
    context_object_name = 'blog'

class ContactViews(ListView):
    model = Contact
    template_name = 'contact.html'
    context_object_name = 'Contact'