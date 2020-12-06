from django.contrib import admin
from Lead_Management_app.models import source_list, followup_history
# Register your models here.

class SourceAdmin(admin.ModelAdmin):
    list_display = ['id','source','contact_person_name','address','person_number','current_stage']


class FollowUpAdmin(admin.ModelAdmin):
    list_display = ['source_id','date_of_follow_up','response','medium']


admin.site.register(source_list,SourceAdmin)
admin.site.register(followup_history,FollowUpAdmin)
