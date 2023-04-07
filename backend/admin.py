from django.contrib import admin
from .models import *

admin.site.register(User)
admin.site.register(Project)
admin.site.register(Room)
admin.site.register(Report_Safety)
admin.site.register(Report_Quality)
admin.site.register(Safety_issue)
admin.site.register(Quality_issue)