from django.shortcuts import render
from .models import *
from .forms import DisasterReportForm
from django.utils.timezone import now
import pygeoip
from django.http import HttpResponse

# Create your views here.


def report_disaster(request):
	x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
	if x_forwarded_for:
		ip = x_forwarded_for.split(',')[0]
	else:
		ip = request.META.get('REMOTE_ADDR')
	if ip == '127.0.0.1':
		pin = "683565"
	else:
		GEOIP = pygeoip.GeoIP("/absolute_path/GeoIP.dat", pygeoip.MEMORY_CACHE)
		pass
	if request.method == 'POST':
		form = DisasterReportForm(request.POST)
		if form.is_valid():
			date = now().date()
			d_type = form.cleaned_data['disaster_type']
			alert = form.cleaned_data['alert']
			profile = Profile.objects.get(user=request.user)
			place = Place.objects.get(pincode=pin)
			disaster = Disaster(record_date=date, disaster_type=d_type, alert=alert, verified=False, reported_by=profile,place=place)
			disaster.save()
	else:
		form = DisasterReportForm()
	return render(request, 'report_disaster.html', locals())


def mark_affected(request,disaster_id):
	disaster = Disaster.objects.get(id=disaster_id)
	request.session['marked'] = disaster_id
	disaster.count +=1 
	disaster.save()
	return HttpResponse("marked!")


def current_disasters(request):
	disasters = Disaster.objects.filter(verified=True)
	return render(request, 'disasters.html', locals())


def view_affected(request,disaster_id):
	disaster = Disaster.objects.get(id=disaster_id)
	return render(request,'analysis.html',locals())
