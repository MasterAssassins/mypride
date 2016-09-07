from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from .models import Emp
from django.contrib.auth import authenticate, login, logout
from django.views.generic import View
from .forms import EmpForm, UserForm


def index(request):
    if not request.user.is_authenticated():
        return render(request, 'employee/login.html')
    else:
        all_employees = Emp.objects.all()
    data = {'all_employees': all_employees}
    return render(request, 'employee/index.html', data)


def detail(request, pk):
    employee_details = get_object_or_404(Emp, pk=pk)
    context = {'employee_details': employee_details}
    return render(request, 'employee/detail.html', context)


def add_emp(request):
    form = EmpForm(request.POST or None)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {"form": form}
    return render(request, 'employee/add_form.html', context)


def update_emp(request, pk=None):
    employee_details = get_object_or_404(Emp, pk=pk)
    form = EmpForm(request.POST or None, instance=employee_details)
    if form.is_valid():
        instance = form.save(commit=False)
        instance.save()
        return HttpResponseRedirect(instance.get_absolute_url())
    context = {
        "employee_details": employee_details,
        "form": form
    }
    return render(request, 'employee/add_form.html', context)


def delete_emp(request, pk=None):
    employee_details = get_object_or_404(Emp, pk=pk)
    employee_details.delete()
    return redirect("employee:index")


class UserFormView(View):
    form_class = UserForm
    template_name = 'employee/registration_form.html'

    # get form data
    def get(self, request):
        form = self.form_class(None)
        return render(request, self.template_name, {'form':form})

    # process form data
    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            user = form.save(commit=False)

            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user.set_password(password)
            user.save()

            # Authentication
            user = authenticate(username=username, password=password)

            if user is not None:
                if user.is_active:
                    login(request, user)
                    return redirect('employee:index')
        context = {'form': form}
        return render(request, self.template_name, context)


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                all_employees = Emp.objects.all()
                return render(request, 'employee/index.html', {'all_employees': all_employees})
            else:
                return render(request, 'employee/login.html', {'error_message': 'Your account has been disabled'})
        else:
            return render(request, 'employee/login.html', {'error_message': 'Invalid login'})
    return render(request, 'employee/login.html')


def logout_user(request):
    logout(request)
    form = UserForm(request.POST or None)
    context = {
        "form": form,
    }
    return render(request, 'employee/login.html', context)

