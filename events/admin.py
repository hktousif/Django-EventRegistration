from django.contrib import admin

# Register your models here.
from .models import *

admin.site.register(CoordinatorsModel)
admin.site.register(ProtocolsModel)
admin.site.register(EventsModel)
admin.site.register(AboutModel)
admin.site.register(GalleryModel)
admin.site.register(ContactModel)
admin.site.register(HomeSlidesModel)
