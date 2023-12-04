from django.contrib.auth import get_user_model, authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, get_object_or_404

from web.forms import RegistrationForm, AuthForm, InventoryForm, KindOfSportForm
from web.models import Inventory, KindOfSport

User = get_user_model()

@login_required
def main_view(request):
    inventory = Inventory.objects.filter(user = request.user).order_by('-rating')
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


@login_required
def inventory_edit_view(request, id=None):
    inventory = get_object_or_404(Inventory, user = request.user, id=id) if id is not None else None;
    form = InventoryForm(instance=inventory, initial={"user": request.user})
    if request.method == "POST":
        form = InventoryForm(data=request.POST, instance=inventory, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect("main")
    return render(request, 'web/inventory_form.html', {"form": form})


@login_required
def inventory_delete(request, id):
    inventory = get_object_or_404(id=id, user=request.user)
    inventory.delete()
    return redirect("main")

@login_required
def kind_of_sport_list(request):
    kind_of_sport = KindOfSport.objects.filter(user=request.user)
    return render(request, 'web/kind_of_sport_list.html', {"kind_of_sport": kind_of_sport})


@login_required
def kind_of_sport_edit(request, id=None):
    sport = get_object_or_404(KindOfSport, user=request.user, id=id) if id is not None else None
    form = KindOfSportForm(instance=sport, initial={"user": request.user})
    if request.method == "POST":
        form = KindOfSportForm(data=request.POST, instance=sport, initial={"user": request.user})
        if form.is_valid():
            form.save()
            return redirect('kind_of_sport_list')
    return render(request, 'web/kind_of_sport_form.html', {"form": form})


@login_required
def kind_of_sport_delete(request, id):
    sport = get_object_or_404(id=id, user=request.user)
    sport.delete()
    return redirect('kind_of_sport_list')
