from .models import Ticket
from .forms import NewTicket, EditTicket
from django.shortcuts import render, reverse, HttpResponseRedirect, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib import messages
# from .decorators import allowed_users
from django.contrib.auth.decorators import login_required
from custom_user.models import CustomUser
from django.views.generic.detail import DetailView

@login_required(login_url='login')
def home(request):
    items = Ticket.objects.all()
    assigned_tickets = Ticket.objects.filter(status="IN PROGRESS")
    new_tickets = Ticket.objects.filter(status="NEW")
    completed_tickets = Ticket.objects.filter(status="DONE")
    invalid_tickets = Ticket.objects.filter(status="INVALID")
    return render(request, 'index.html', {'data': items,
     'assigned_tickets': assigned_tickets,
     'new_tickets': new_tickets,
     'completed_tickets': completed_tickets,
     'invalid_tickets': invalid_tickets})



@login_required(login_url='login')
def detail(request, id):
    item = Ticket.objects.get(id=id)
    return render(request, 'detail.html', {'data': item})


# def sortedx(request):
#     html = "index.html"
#     data = Ticket.objects.all().order_by("-time_filled")
#     return render(request, html, {"data": data})


# def sortedt(request):
#     html = "index.html"
#     data = Ticket.objects.all().order_by("status").reverse()
#     return render(request, html, {"data": data})



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

@login_required()
def user_detail_view(request, id):
    user = None
    submitted_tickets = None
    assigned_tickets = None
    closed_tickets = None

    try:
        user = CustomUser.objects.get(id=id)
        submitted_tickets = Ticket.objects.filter(created_by=user)
        assigned_tickets = Ticket.objects.filter(user_assigned=user)
        closed_tickets = Ticket.objects.filter(completed_by=user)
        title = Ticket.objects.get(title=title)

    except Exception as e:
        print(e)
    
    return render(request, 'user_detail.html', {
        'user': user,
        'submitted_tickets': submitted_tickets,
        'assigned_tickets': assigned_tickets,
        'closed_tickets': closed_tickets
    })
#