from .models import Ticket
from .forms import NewTicket, EditTicket
from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# from .decorators import allowed_users
from django.contrib.auth.decorators import login_required


@login_required(login_url='login')
def home(request):
    item = Ticket.objects.all()
    return render(request, 'index.html', {'data': item})


@login_required(login_url='login')
def detail(request, id):
    item = Ticket.objects.get(id=id)
    return render(request, 'detail.html', {'data': item})


def sortedx(request):
    html = "index.html"
    data = Ticket.objects.all().order_by("-time_filled")
    return render(request, html, {"data": data})


def sortedt(request):
    html = "index.html"
    data = Ticket.objects.all().order_by("status").reverse()
    return render(request, html, {"data": data})



@login_required(login_url='login')
def ticket_add(request):
    html = 'createTicket.html'

    if request.method == 'POST':
        form = NewTicket(request.POST)

        if form.is_valid():
            data = form.cleaned_data
            Ticket.objects.create(
                title=data['title'],
                description=data['description'],
                created_by=request.user,
                status="NEW"
            )

            return HttpResponseRedirect(reverse("home"))

    form = NewTicket()

    return render(request, html, {'form': form})



@login_required(login_url='login')
def edit_tick(request, id):
    html = 'editTicket.html'
    instance = Ticket.objects.get(id=id)
    if request.method == 'POST':
        form = EditTicket(request.POST, instance=instance)
        if form.is_valid():
            form.save(commit=False)
            if instance.status == "DONE":
                instance.completed_by = request.user
                instance.user_assigned = None
            elif instance.status == "IN PROGRESS":
                instance.user_assigned = request.user
                instance.completed_by = None
            elif instance.status == "INVALID":
                instance.completed_by = None
                instance.user_assigned = None
            elif instance.status == "NEW":
                instance.completed_by = None
                instance.user_assigned = None
            instance.save()
            # instance.save(commit=False)
            # instance.completed_by = request.user
            return HttpResponseRedirect(reverse("home"))
    # form.save(commit=false) after add the attr and call .save on instance
    form = EditTicket(instance=instance)

    return render(request, html, {'form': form})


def loginPage(request):
    html = 'login.html'
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("home")
        else:
            messages.info(request, 'Username or password is incorrect.')
    return render(request, html)


def logoutUser(request):
    logout(request)
    return redirect('login')
# user click btn to claim ticket
# admin create tik not assigned
# then edit title des, set status,
