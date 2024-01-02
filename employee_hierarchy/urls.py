from django.urls import path, include
from .views import EmployeeHierarchyView, EmployeeListView, \
    ajax_search, ajax_load_subordinates, employee_delete

urlpatterns = [
    path('hierarchy/', EmployeeHierarchyView.as_view(), name='employee_hierarchy'),
    path('list/', EmployeeListView.as_view(), name='employee_list'),
    path('search/', ajax_search, name='ajax_search'),
    path('hierarchy/ajax/load-subordinates/<int:employee_id>/', ajax_load_subordinates, name='ajax_load_subordinates'),
    path('delete/<int:employee_id>/', employee_delete, name='employee_delete'),
]