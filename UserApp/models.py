from django.db import models

# Create your models here.
class UserModel(models.Model):
    user_id = models.AutoField(primary_key = True)
    user_first_name = models.CharField(max_length=100)
    user_last_name = models.CharField(max_length=100, null=True, blank=True)
    user_mail = models.EmailField()
    user_password = models.CharField(max_length=100)
    user_phoneno = models.CharField(max_length=15, null=True, blank=True)
    is_superadmin = models.BooleanField(default=False)
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        return f"{self.user_first_name} {self.user_last_name}"

# for adding State
class ZoneModel(models.Model):
    zone_id = models.AutoField(primary_key = True)
    zone_name = models.CharField(max_length=100)
    zone_code = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        # Convert region_name and region_code to uppercase before saving
        if self.zone_name:
            self.zone_name = self.zone_name.upper()
        if self.zone_code:
            self.zone_code = self.zone_code.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.zone_name

# for adding District
class RegionModel(models.Model):
    region_id = models.AutoField(primary_key = True)
    region_name = models.CharField(max_length=100)
    region_code = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        # Convert region_name and region_code to uppercase before saving
        if self.region_name:
            self.region_name = self.region_name.upper()
        if self.region_code:
            self.region_code = self.region_code.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.region_name

# for adding Panchayat
class AreaModel(models.Model):
    area_id = models.AutoField(primary_key = True)
    area_name = models.CharField(max_length=100)
    area_code = models.CharField(max_length=50, null=True)
    created_at = models.DateTimeField(null=True)

    def save(self, *args, **kwargs):
        # Convert region_name and region_code to uppercase before saving
        if self.area_name:
            self.area_name = self.area_name.upper()
        if self.area_code:
            self.area_code = self.area_code.upper()
        super().save(*args, **kwargs)

    def __str__(self):
        return self.area_name

class BloodGroupModel(models.Model):
    group_id = models.AutoField(primary_key = True)
    group_name = models.CharField(max_length=100)

    def __str__(self):
        return self.group_name


class UserRole(models.Model):
    user_id = models.AutoField(primary_key= True)
    user_role = models.CharField(max_length=100)

    def __str__(self):
        return self.user_role

class GenderModel(models.Model):
    gender_id = models.AutoField(primary_key = True)
    gender = models.CharField(max_length=100)

    def __str__(self):
        return self.gender

class UnitModel(models.Model):
    unit_id = models.AutoField(primary_key=True)
    affliation_number = models.CharField(max_length=50, null=True, unique=True)
    unit_name = models.CharField(max_length=100)
    region = models.ForeignKey(RegionModel, on_delete=models.SET_NULL, null=True, blank=True)
    zone = models.ForeignKey(ZoneModel, on_delete=models.SET_NULL,null=True, blank=True)
    area = models.ForeignKey(AreaModel, on_delete=models.SET_NULL, null=True, blank=True)
    created_by = models.ForeignKey(UserModel, on_delete=models.SET_NULL, related_name='unit_admin', null=True, blank=True)
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.unit_name

class MemberModel(models.Model):
    member_id =models.AutoField(primary_key = True)
    admission_no = models.CharField(max_length=100)
    member_name = models.CharField(max_length=100)
    mailid = models.EmailField(null=True, blank=True)
    gender = models.ForeignKey(GenderModel, on_delete=models.SET_NULL, null=True, blank=True)
    mobile_no = models.CharField(max_length=50, null=True, blank=True)
    whatsapp_no = models.CharField(max_length=50, null=True, blank=True)
    address = models.CharField(max_length=100, null=True, blank=True)
    pincode = models.CharField(max_length=10, null=True, blank=True)
    dob = models.DateField(null=True, blank=True)
    blood_group = models.ForeignKey(BloodGroupModel, on_delete=models.SET_NULL, null=True, blank=True)
    employment = models.CharField(max_length=100, null=True, blank=True)
    unit = models.ForeignKey(UnitModel, on_delete=models.SET_NULL, null=True, blank=True)
    user_role = models.ForeignKey(UserRole, on_delete=models.SET_NULL, null=True, blank=True)
    nominee_name = models.CharField(max_length=100, null=True, blank=True)
    nominee_address = models.CharField(max_length=100, null=True, blank=True)
    nominee_dob = models.DateField(null=True, blank=True)
    nominee_mobileno = models.CharField(max_length=50, null=True, blank=True)
    relation_with_member = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.member_name

    def total_members(self):
        # Count members related to this unit via MemberModel
        return MemberModel.objects.filter(unit=self).count()

class MemberFamilyModel(models.Model):
    family_id = models.AutoField(primary_key = True)
    member = models.ForeignKey(MemberModel, on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    age =models.IntegerField(null=True, blank=True)
    gender = models.ForeignKey(GenderModel, on_delete=models.SET_NULL, null=True)
    relation = models.CharField(max_length=100)
    education = models.CharField(max_length=100, null=True, blank=True)
    employment = models.CharField(max_length=100, null=True, blank=True)
    created_at = models.DateTimeField(null=True)

    def __str__(self):
        return self.name

# class ActivityModel(models.Model):
#     activity_id = models.AutoField(primary_key = True)
#     user = models.ForeignKey(UserModel, on_delete=models.SET_NULL, null=True, blank=True)
#     activity = models.CharField(max_length=100, null=True)
#     at_time = models.DateTimeField(null=True)
#
#     def __str__(self):
#         return f"{self.user.user_first_name}{self.activity}"
