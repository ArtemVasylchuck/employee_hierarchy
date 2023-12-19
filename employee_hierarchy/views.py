from django.contrib.auth.decorators import login_required, permission_required
from django.http import JsonResponse
from django.shortcuts import render, get_object_or_404, redirect
from django.template.loader import render_to_string
from django.views.generic import ListView
from .models import Employee


class EmployeeHierarchyView(ListView):
    model = Employee
    template_name = 'employee_hierarchy.html'

    def get_queryset(self, query=None):
        return Employee.objects.filter(manager__isnull=True)


class EmployeeListView(ListView):
    model = Employee
    template_name = 'employee_list.html'
    paginate_by = 10

    def get_queryset(self, query=None):
        query = self.request.GET.get('search')
        if query:
            return Employee.objects.filter(name__icontains=query) \
                   | Employee.objects.filter(position__icontains=query) \
                   | Employee.objects.filter(email__icontains=query)

        ordering = self.get_ordering()
        return Employee.objects.all().order_by(ordering)

    def get_ordering(self):
        ordering = self.request.GET.get('ordering')
        valid_ordering = ['name', 'position', 'hire_date', 'email']
        if ordering in valid_ordering:
            return ordering

        return 'name'


def ajax_search(request):
    query = request.GET.get('search')
    employees = EmployeeListView.get_queryset(query)
    html = render_to_string('employee_list.html', {'object_list': employees})

    return JsonResponse({'html': html})


def ajax_load_subordinates(request, employee_id):
    employee = Employee.objects.get(id=employee_id)
    subordinates = employee.subordinates.all()
    html = render_to_string('employee_item.html',
                            {'employee': employee, 'subordinates': subordinates, 'load_on_demand': True})

    return JsonResponse({'html': html})


@login_required
@permission_required('app.delete_employee')
def employee_delete(request, employee_id):
    employee = get_object_or_404(Employee, id=employee_id)
    employee.delete()

    return redirect('employee_list')
