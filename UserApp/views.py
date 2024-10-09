from django.shortcuts import render, redirect, get_object_or_404
from datetime import datetime, date
from django.contrib import messages
from django.db.models import Count
from UserApp.forms import *
from UserApp.models import *


# Create your views here.
def home(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    else:
        admin = UserModel.objects.get(user_id=user)
        if admin.user_last_name:
            admin_name = f"{admin.user_first_name} {admin.user_last_name}"
        else:
            admin_name = f"{admin.user_first_name}"
        allusers = UserModel.objects.filter(is_superadmin=False)
        members = MemberModel.objects.all()
        region = RegionModel.objects.all()
        area = AreaModel.objects.all()
        units = UnitModel.objects.filter(created_at__date=date.today())
        unit_count = UnitModel.objects.all().count()
        members_count = MemberModel.objects.all().count()
        zone_counts = ZoneModel.objects.all().count()
        region_counts = region.count()
        area_counts = area.count()
        return render(request, 'index.html', {'users': allusers, 'username': admin_name,
                                              'regions': region, 'areas': area, 'total_unit': unit_count,
                                              'units': units,
                                              'members': members, 'admin': admin, 'total_members': members_count,
                                              'zone_counts': zone_counts, 'region_counts': region_counts,
                                              'area_counts': area_counts})


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')
        try:
            admin = UserModel.objects.get(user_mail=email, user_password=password)
            request.session['user'] = admin.user_id
            request.session.set_expiry(3600)
            return redirect('/')
        except UserModel.DoesNotExist:
            return render(request, 'login.html', {'error': "User not found"})
    return render(request, 'login.html')

def membership_form(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    admin = UserModel.objects.get(user_id=user)
    if admin.user_last_name:
        admin_name = f"{admin.user_first_name} {admin.user_last_name}"
    else:
        admin_name = f"{admin.user_first_name}"
    today = datetime.now().date()
    limit_exceeded = False
    if request.method == 'POST':
        form = MembershipForm(request.POST, request.FILES)
        if form.is_valid():
            admission_form = form.save(commit=False)
            unit = admission_form.unit
            member_count = MemberModel.objects.filter(unit=admission_form.unit).count()

            if member_count >= 20:
                limit_exceeded = True
                return render(request, 'create.html', {'username': admin_name,'form': form, 'limit_exceeded': limit_exceeded})
            numeric_part = unit.affliation_number[-4:]
            member_no = member_count + 1
            admission_form.admission_no = f'{numeric_part}/{member_no}'
            admission_form.created_at = today  # Set the admin field from the logged-in user
            admission_form.save()
            # Check which button was clicked and redirect accordingly
            if 'addnew' in request.POST:
                messages.success(request, 'Member added successfully. Add a new member.')
                return redirect('membership-form')  # Reload the form to add a new member
            elif 'submit' in request.POST:
                return redirect('membership-form')  # Redirect to the homepage
    else:
        form = MembershipForm()
    return render(request, 'create.html', {'username': admin_name,'form': form, 'limit_exceeded': limit_exceeded})


def addmember(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    admin = UserModel.objects.get(user_id=user)
    if admin.user_last_name:
        admin_name = f"{admin.user_first_name} {admin.user_last_name}"
    else:
        admin_name = f"{admin.user_first_name}"
    today = datetime.now().date()
    if request.method == 'POST':
        form = AddMemberForm(request.POST, request.FILES)
        if form.is_valid():
            admission_form = form.save(commit=False)
            admission_form.created_at = today  # Set the admin field from the logged-in user
            admission_form.save()
            return redirect('/')  # Redirect to a relevant page after submission
    else:
        form = AddMemberForm()
    return render(request, 'addmember.html', {'form': form, 'username': admin_name})


def addarea(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    admin = UserModel.objects.get(user_id=user)
    if admin.user_last_name:
        admin_name = f"{admin.user_first_name} {admin.user_last_name}"
    else:
        admin_name = f"{admin.user_first_name}"
    area_form = AreaForm()
    area = AreaModel.objects.all()
    area_count = area.count()
    if 'area_name' in request.POST:
        area_form = AreaForm(request.POST)
        if area_form.is_valid():
            area_form.save()
            return redirect('areas')
    context = {
        'area_form': area_form,
        'areas': area,
        'area_count': area_count,
        'username':admin_name
    }
    return render(request, 'area.html', context)


def addregion(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    admin = UserModel.objects.get(user_id=user)
    if admin.user_last_name:
        admin_name = f"{admin.user_first_name} {admin.user_last_name}"
    else:
        admin_name = f"{admin.user_first_name}"
    region_form = RegionForm()
    regions = RegionModel.objects.all()
    region_count = regions.count()
    if 'region_name' in request.POST:
        region_form = RegionForm(request.POST)
        if region_form.is_valid():
            region_form.save()
            return redirect('regions')
    context = {
        'region_form': region_form,
        'regions': regions,
        'region_count': region_count,
        'username': admin_name,
    }
    return render(request, 'regions.html', context)

def addzone(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    admin = UserModel.objects.get(user_id=user)
    if admin.user_last_name:
        admin_name = f"{admin.user_first_name} {admin.user_last_name}"
    else:
        admin_name = f"{admin.user_first_name}"
    # Initialize empty forms

    zone_form = ZoneForm()

    zones = ZoneModel.objects.all()
    zone_count = zones.count()
    if request.method == 'POST':
        # Handle Region Form Submission
         # Replace with the URL where you want to redirect after successful submission

        # Handle Zone Form Submission
        if 'zone_name' in request.POST:
            zone_form = ZoneForm(request.POST)
            if zone_form.is_valid():
                zone_form.save()
                return redirect('zones')  # Replace with the URL where you want to redirect after successful submission

    context = {
        'zone_form': zone_form,
        'zones': zones,
        'zone_count': zone_count,
        'username': admin_name,
    }
    return render(request, 'addregion.html', context)

def delete_zone(request, zone_id):
    zone = get_object_or_404(ZoneModel, pk=zone_id)
    if request.method == 'POST':
        zone.delete()
        return redirect('zones')  # Adjust the redirect based on your URL name for the user list page
    return redirect('zones')

def delete_region(request, region_id):
    region = get_object_or_404(RegionModel, pk=region_id)
    if request.method == 'POST':
        region.delete()
        return redirect('regions')  # Adjust the redirect based on your URL name for the user list page
    return redirect('regions')

def delete_area(request, area_id):
    area = get_object_or_404(AreaModel, pk=area_id)
    if request.method == 'POST':
        area.delete()
        return redirect('areas')  # Adjust the redirect based on your URL name for the user list page
    return redirect('areas')

def delete_member(request, member_id):
    member = get_object_or_404(MemberModel, pk=member_id)
    if request.method == 'POST':
        member.delete()
        return redirect('members')  # Adjust the redirect based on your URL name for the user list page
    return redirect('members')

def delete_unit(request, unit_id):
    unit = get_object_or_404(UnitModel, pk=unit_id)
    if request.method == 'POST':
        unit.delete()
        return redirect('units')  # Adjust the redirect based on your URL name for the user list page
    return redirect('units')

def delete_user(request, user_id):
    user = get_object_or_404(UserModel, pk=user_id)
    if request.method == 'POST':
        user.delete()
        return redirect('/')  # Adjust the redirect based on your URL name for the user list page
    return redirect('/')


def generate_uniqueno(zone_no, region_no, area_no):
    counts = UnitModel.objects.all().count()
    unique_no = str(counts + 1001)
    zone = ZoneModel.objects.get(zone_id = zone_no)
    region = RegionModel.objects.get(region_id = region_no)
    area = AreaModel.objects.get(area_id = area_no)
    unique_code = f"{zone.zone_code}{region.region_code}{area.area_code}{unique_no}"
    return unique_code


def unitcreation(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    admin = UserModel.objects.get(user_id=user)
    if admin.user_last_name:
        admin_name = f"{admin.user_first_name} {admin.user_last_name}"
    else:
        admin_name = f"{admin.user_first_name}"
    today = datetime.now()
    if request.method == 'POST':
        form = UnitForm(request.POST, request.FILES)
        if form.is_valid():
            unit_form = form.save(commit=False)
            uniqueno = generate_uniqueno(unit_form.zone.zone_id, unit_form.region.region_id, unit_form.area.area_id)

            unit_form.affliation_number = uniqueno
            unit_form.created_by = admin
            unit_form.created_at = today  # Set the admin field from the logged-in user
            unit_form.save()  # Now save the unit instance to the database
            form.save_m2m()
            return redirect('/')  # Redirect to a relevant page after submission
    else:
        form = UnitForm()
    return render(request, 'unitcreation.html', {'form': form, 'username': admin_name})


def createuser(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    admin = UserModel.objects.get(user_id=user)
    if admin.user_last_name:
        admin_name = f"{admin.user_first_name} {admin.user_last_name}"
    else:
        admin_name = f"{admin.user_first_name}"
    today = datetime.now().date()
    if request.method == 'POST':
        form = UserForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user_form.created_at = today  # Set the admin field from the logged-in user
            user_form.save()
            return redirect('/')
    else:
        form = UserForm()
    return render(request, 'createuser.html', {'form': form, 'username': admin_name})


def members(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    admin = UserModel.objects.get(user_id=user)
    if admin.user_last_name:
        admin_name = f"{admin.user_first_name} {admin.user_last_name}"
    else:
        admin_name = f"{admin.user_first_name}"
    members = MemberModel.objects.all()
    return render(request, 'members.html', {'members':members, 'username': admin_name})


def units(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    admin = UserModel.objects.get(user_id=user)
    if admin.user_last_name:
        admin_name = f"{admin.user_first_name} {admin.user_last_name}"
    else:
        admin_name = f"{admin.user_first_name}"
    units = UnitModel.objects.all()
    return render(request, 'units.html', {'units':units, 'username': admin_name})


def unitspage(request, unit_id):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    admin = UserModel.objects.get(user_id=user)
    if admin.user_last_name:
        admin_name = f"{admin.user_first_name} {admin.user_last_name}"
    else:
        admin_name = f"{admin.user_first_name}"

    # Fetch the specific unit by its ID
    unit = UnitModel.objects.get(unit_id=unit_id)
    allmembers = MemberModel.objects.filter(unit = unit)
    president = allmembers.filter(user_role__user_role='President')
    vice_president = allmembers.filter(user_role__user_role='Vice President')
    secretary = allmembers.filter(user_role__user_role='Secretary')
    jointsecretary = allmembers.filter(user_role__user_role='Joint Secretary')
    treasurer = allmembers.filter(user_role__user_role='Treasurer')
    members = allmembers.filter(user_role__user_role='Member')

    if request.method == 'POST':
        # Populate the form with POST data and the current unit instance
        form = UnitForm(request.POST, instance=unit)
        # Validate the form
        if form.is_valid():
            unit_form = form.save(commit=False)

            unit_form.created_by = admin
            # Save the form, which will update the unit
            form.save()
            return redirect('units')  # Redirect to the appropriate page after saving
    else:
        # If not posting, just populate the form with the unit instance for editing
        form = UnitForm(instance=unit)
    context={
        'form': form,
        'president': president,
        'vice_president': vice_president,
        'secretary':secretary,
        'joint_secretary':jointsecretary,
        'treasurer':treasurer,
        'members': members,
        'username': admin_name
    }
    # Render the form and pass it to the template
    return render(request, 'unitpage.html', context)


def report(request):
    user = request.session.get('user', None)
    if user is None:
        return redirect('/login')
    admin = UserModel.objects.get(user_id=user)
    if admin.user_last_name:
        admin_name = f"{admin.user_first_name} {admin.user_last_name}"
    else:
        admin_name = f"{admin.user_first_name}"
    units = UnitModel.objects.annotate(total_members=Count('membermodel'))
    zones = ZoneModel.objects.all()
    regions = RegionModel.objects.all()
    areas = AreaModel.objects.all()
    zone = request.GET.get('zone')
    region = request.GET.get('region')
    area = request.GET.get('area')

    if zone:
        units = units.filter(zone_id=zone)
    if region:
        units = units.filter(region_id=region)
    if area:
        units = units.filter(area_id=area)

    context = {
        'units': units,
        'zones': zones,
        'regions': regions,
        'areas': areas,
        'zone': zone,
        'region': region,
        'area': area,
        'username': admin_name,
    }

    return render(request, 'report.html', context)

def logout(request):
    del request.session['user']
    return redirect('/')