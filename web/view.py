from django.contrib.auth import get_user_model, authenticate, login, logout
from django.shortcuts import render, redirect

from web.forms import RegistrationForm, AuthForm, InventoryForm, KindOfSportForm
from web.models import Inventory, KindOfSport

User = get_user_model()


def main_view(request):
    inventory = Inventory.objects.all()
    return render(request, 'web/example.html', {
        'inventory': inventory
    })


def registration_view(request):
    form = RegistrationForm()
    is_success = False
    if request.method == 'POST':
        form = RegistrationForm(data=request.POST)
        if form.is_valid():
            user = User(username=form.cleaned_data["username"],
                        email=form.cleaned_data["email"]
                        )
            user.set_password(form.cleaned_data["password"])
            user.save()
            print(form.cleaned_data)
            is_success = True
    return render(request, 'web/registration.html', {
        "form": form, "is_success": is_success
    })


def auth_view(request):
    form = AuthForm()
    if request.method == "POST":
        form = AuthForm(data=request.POST)
        if form.is_valid():
            user = authenticate(**form.cleaned_data)
            if user is None:
                form.add_error(None, 'Введены неверные данные')
            else:
                login(request, user)
                return redirect('main')
    return render(request, 'web/auth.html', {"form": form})


def logout_view(request):
    logout(request)
    return redirect('main')


def inventory_edit_view(request, id=None):
    inventory = Inventory.objects.get(id=id) if id is not None else None
    form = InventoryForm(instance=inventory)
    if request.method == "POST":
        form = InventoryForm(data=request.POST, instance=inventory)
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, 'web/inventory_form.html', {"form": form})


def kind_of_sport_view(request):
    kind_of_sport = KindOfSport.objects.all()
    form = KindOfSportForm()
    if request.method == "POST":
        form = KindOfSportForm(data=request.POST)
        if form.is_valid():
            form.save()
            return redirect('kind_of_sport')
    return render(request, 'web/kind_of_sport_form.html', {"kind_of_sport": kind_of_sport, "form": form})


def kind_of_sport_delete(request, id):
    sport = KindOfSport.objects.get(id=id)
    sport.delete()
    return redirect('kind_of_sport')