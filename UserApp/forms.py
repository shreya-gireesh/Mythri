from django import forms
from django.core.exceptions import ValidationError
from UserApp.models import *


class MembershipForm(forms.ModelForm):
    class Meta:
        model = MemberModel
        fields = [
            'member_name',
            'mailid',
            'gender',
            'mobile_no',
            'whatsapp_no',
            'address',
            'pincode',
            'dob',
            'blood_group',
            'employment',
            'unit',
            'user_role',
            'nominee_name',
            'nominee_address',
            'nominee_dob',
            'nominee_mobileno',
            'relation_with_member',
        ]
        widgets = {
            'member_name': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Name'}),
            'mailid': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Mail Id'}),
            'gender': forms.Select( attrs={'class': 'form-select form-control'}),
            'mobile_no': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Mobile Number'}),
            'whatsapp_no': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Whatsapp Number'}),
            'address': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Address'}),
            'pincode': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Pincode'}),
            'dob': forms.DateInput(attrs={'class': 'form-control form-control-user', 'type': 'date'}),
            'blood_group': forms.Select( attrs={'class': 'form-select form-control'}),
            'employment': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Employment'}),
            'unit': forms.Select( attrs={'class': 'form-select form-control'}),
            'user_role': forms.Select( attrs={'class': 'form-select form-control'}),
            'nominee_name': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nominee Name'}),
            'nominee_address': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nominee Address'}),
            'nominee_dob': forms.DateInput(attrs={'class': 'form-control form-control-user', 'type': 'date'}),
            'nominee_mobileno': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nominee Name'}),
            'relation_with_member': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Nominee Name'}),
        }



class AddMemberForm(forms.ModelForm):
    class Meta:
        model = MemberFamilyModel
        fields = [
            'member',
            'name',
            'age',
            'gender',
            'relation',
            'education',
            'employment',
        ]
        widgets ={
            'member':forms.Select(attrs={'class': 'form-select form-control'}),
            'name': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Name'}),
            'age': forms.NumberInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Age'}),
            'gender': forms.Select(attrs={'class': 'form-select form-control'}),
            'relation':forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Relationship'}),
            'education': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Education'}),
            'employment': forms.TextInput(attrs={'class': 'form-control form-control-user', 'placeholder': 'Employment'}),
        }


class UnitForm(forms.ModelForm):
    class Meta:
        model = UnitModel
        fields = ['unit_name',
                  'region',
                  'zone',
                  'area',
                  'created_by',
                  ]
        widgets = {
            'unit_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Unit Name',
            }),
            'region': forms.Select(attrs={
                'class': 'form-select form-control',
                'placeholder': 'Enter Region',
            }),
            'zone': forms.Select(attrs={
                'class': 'form-select form-control',
                'placeholder': 'Enter Zone',
            }),
            'area': forms.Select(attrs={
                'class': 'form-select form-control',
                'placeholder': 'Enter Area',
            }),
            'created_by': forms.Select(attrs={
                'class': 'form-select form-control',
            }),

        }



class RegionForm(forms.ModelForm):
    class Meta:
        model = RegionModel
        fields = ['region_name', 'region_code']

        # Add widgets for customizing the appearance of form fields
        widgets = {
            'region_name': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter Region Name',

            }),
            'region_code': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter Region Code',

            }),
        }


# Form for ZoneModel
class ZoneForm(forms.ModelForm):
    class Meta:
        model = ZoneModel
        fields = ['zone_name', 'zone_code']

        # Add widgets for customizing the appearance of form fields
        widgets = {
            'zone_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Zone Name',
            }),
            'zone_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Zone Code',
            }),
        }


# Form for AreaModel
class AreaForm(forms.ModelForm):
    class Meta:
        model = AreaModel
        fields = ['area_name', 'area_code']

        # Add widgets for customizing the appearance of form fields
        widgets = {
            'area_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Area Name',
            }),
            'area_code': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Enter Area Code',
            }),
        }


class UserForm(forms.ModelForm):
    class Meta:
        model = UserModel
        fields = ['user_first_name',
                  'user_last_name',
                  'user_mail',
                  'user_password',
                  'user_phoneno'
                  ]
        widgets = {
            'user_first_name': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter First Name',
            }),
            'user_last_name': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter Last Name',
            }),
            'user_mail': forms.EmailInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter Email',
            }),
            'user_password': forms.PasswordInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter Password',
            }),
            'user_phoneno': forms.TextInput(attrs={
                'class': 'form-control form-control-user',
                'placeholder': 'Enter Phone No',
            }),
        }