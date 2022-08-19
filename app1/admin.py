from django.contrib import admin
import inspect
# Register your models here.

from app1 import models
for cls in dir(models):
	class_instance = getattr(models, cls)
	if inspect.isclass(class_instance):
		admin.site.register(class_instance)
