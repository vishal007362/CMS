from django.contrib import admin
from .models import Staff, Role, Doctor, Specialization

admin.site.register(Staff)
admin.site.register(Role)
admin.site.register(Doctor)
admin.site.register(Specialization)
