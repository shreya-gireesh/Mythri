from django.contrib import admin
from UserApp.models import *

# Register your models here.
admin.site.register(UserModel)
admin.site.register(RegionModel)
admin.site.register(ZoneModel)
admin.site.register(AreaModel)
admin.site.register(UnitModel)
admin.site.register(BloodGroupModel)
admin.site.register(GenderModel)
admin.site.register(UserRole)
admin.site.register(MemberModel)