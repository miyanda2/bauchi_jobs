from django.db.models import (
	Model, 
	TextField,
	

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

	    

	def __unicode__(self):
        # add __str__() if using Python 3.x
		return self.title