from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.shortcuts import get_object_or_404, redirect
from django.shortcuts import render

from employee.models import Employee
from .forms import PayrollForm
from .models import Payroll


@login_required
def payroll_list(request):
    employees = Employee.objects.all()
    return render(request, "payroll/payroll_list.html", {"employees": employees})


@login_required
def payroll_create(request, id):  # Add 'id' as an argument
    employee = get_object_or_404(Employee, pk=id)  # Now 'id' is passed correctly

    if request.method == "POST":
        form = PayrollForm(request.POST)
        if form.is_valid():
            payroll = form.save(commit=False)
            payroll.employee = employee
            payroll.save()
            messages.success(request, "Payroll created successfully-")
            return redirect("payroll_list")
    else:
        form = PayrollForm()
    return render(
        request, "payroll/payroll_form.html", {"form": form, "employee": employee}
    )


@login_required
def payroll_update(request, id):
    payroll = get_object_or_404(Payroll, id=id)
    if request.method == "POST":
        form = PayrollForm(request.POST, instance=payroll)
        if form.is_valid():
            form.save()
            messages.success(request, "Payroll updated successfully-")
            return redirect("payroll_list")

    else:
        form = PayrollForm(instance=payroll)
    return render(request, "payroll/payroll_form.html", {"form": form})


@login_required
def payroll_delete(request, id):
    payroll = get_object_or_404(Payroll, id=id)
    payroll.delete()
    messages.success(request, "Payroll deleted successfully.")
    return redirect("payroll_list")
