from django.shortcuts import render, redirect
from .models import Car
from .forms import CarCreateForm, CarUpdateForm


def home(request):

	context={}

	return render(request, 'home.html', context)

def car_list(request):
	cars = Car.objects.all()
	context = {
		"cars": cars,
	}
	return render(request, 'car_list.html', context)


def car_detail(request, car_id):
	car = Car.objects.get(id=car_id)
	context = {
		"car": car,
	}
	return render(request, 'car_detail.html', context)


def car_create(request):

	form=CarCreateForm()
	if request.method == "POST":
		form= CarCreateForm(request.POST, request.FILES or None)
		if form.is_valid():
			car= form.save(commit=False)
			car.save()

	context = {
		"form": form,
		}
	return render(request, 'create-page.html', context)


def car_update(request, car_id):

	car_obj= Car.objects.get(id=car_id)
	form=CarUpdateForm()
	if request.method == "POST":
		form= CarUpdateForm(request.POST, instance= car_obj)
		if form.is_valid():
			form.save()
			return redirect('car-list')
	context = { 
		"car_obj": car_obj,
		"form": form,
	}
	return render(request,'car-update.html',context)


def car_delete(request, car_id):
	#Complete Me
	car_obj= Car.objects.get(id= car_id)
	car_obj.delete()
	return render('car-list')








