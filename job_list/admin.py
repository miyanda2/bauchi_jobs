from django.contrib import admin
from .models import JobListing


# Register your models here.
class JobListingAdmin(admin.ModelAdmin):
	list_display = ['title', 'description', 'company_name', ]

	#fields = ( 'image_tag','title','description','image','externalURL', )
    
admin.site.register(JobListing, JobListingAdmin)
admin.site.site_header = 'Online Job Admin Dashboard'