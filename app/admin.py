from django.contrib import admin
from .models import Clients, Company, Position, Service, Statistic,PlayList,Portfolio,Team,Contact,Blog
# Register your models here.
class CompanyAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Company, CompanyAdmin)

class StatisticAdmin(admin.ModelAdmin):
    list_display = ['name','count']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Statistic,StatisticAdmin) 

class ServiceAdmin(admin.ModelAdmin):
    list_display = ['name','about']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Service,ServiceAdmin)

class PlayListAdmin(admin.ModelAdmin):
    list_display = ['cost','name','about','contact']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(PlayList,PlayListAdmin)

class ClientsAdmin(admin.ModelAdmin):
    list_display = ['name','position','about']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Clients,ClientsAdmin)

class PositionAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Position,PositionAdmin)

class TeamAdmin(admin.ModelAdmin):
    list_display = ['name','position']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Team,TeamAdmin)

class ContactAdmin(admin.ModelAdmin):
    list_display = ['address','phone','social','facebook','instagram','telegram','linkedin']
    list_per_page = 10
    search_fields = ['address']
admin.site.register(Contact,ContactAdmin)

class BlogAdmin(admin.ModelAdmin):
    list_display = ['name','about','description','date']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Blog,BlogAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    list_display = ['name']
    list_per_page = 10
    search_fields = ['name']
admin.site.register(Portfolio,PortfolioAdmin)    