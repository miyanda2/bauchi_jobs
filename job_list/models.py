from django.db.models import (
	Model, 
	TextField,
	ImageField,

)
from django.conf import settings

# Create your models here.
class JobListing(Model):
	title = TextField(null=True, blank = True)
	company_name = TextField(null=True, blank = True)
	description = TextField(null=True, blank = True)


	def url(self):
        # returns a URL for either internal stored or external image url
		if self.externalURL:
			return self.externalURL
		else:
            # is this the best way to do this??
			return os.path.join('/',settings.MEDIA_URL, os.path.basename(str(self.image)))

	def image_tag(self):
        # used in the admin site model as a "thumbnail"
		return mark_safe('<img src="{}" width="150" height="150" />'.format(self.url()) )
		image_tag.short_description = 'Image'    

	def __unicode__(self):
        # add __str__() if using Python 3.x
		return self.title