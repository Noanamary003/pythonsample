from django.contrib import admin
from . models import model1
from . models import model2
from . models import model3
from . models import cartmodel
# Register your models here.
admin.site.register(model1)
admin.site.register(model2)
admin.site.register(model3)
admin.site.register(cartmodel)
