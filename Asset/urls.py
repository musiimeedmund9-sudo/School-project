"""
URL configuration for Asset project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/6.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include

from Assets.views import sign_up_view
from Assets.views import add_employee_view,edit_employee_view,delete_employee_view
from Assets.views import add_store_view,edit_store_view,delete_store_view
from Assets.views import add_asset_view,edit_asset_view,delete_asset_view
from Assets.views import add_stock_view,edit_stock_view,delete_stock_view
from Assets.views import add_stock_item_view,edit_stock_item_view,delete_stock_item_view
from Assets.views import add_requisition_view,edit_requisition_view,delete_requisition_view
from Assets.views import add_requisition_item_view,edit_requisition_item_view,delete_requisition_item_view

urlpatterns = [
    path('admin/', admin.site.urls),
     path('',add_employee_view,name='employee_home_page'),
    
    path('sign_up',sign_up_view,name='sign_up_page'),
    path('accounts',include('django.contrib.auth.urls')),
    path('sign_up',sign_up_view,name='sign_up_page'),

    path('add_employee/',add_employee_view,name="add_employee_page"),
    path('edit_employee/<int:employee_id>/',edit_employee_view,name="edit_employee_page"),
    path('delete_employee/<int:employee_id>/',delete_employee_view,name="delete_employee_page"),

    path('add_store/',add_store_view,name="add_store_page"),
    path('edit_store/<int:store_id>/',edit_store_view,name="edit_store_page"),
    path('delete_store/<int:store_id>/',delete_store_view,name="delete_store_page"),

    path('add_asset/',add_asset_view,name="add_asset_page"),
    path('edit_asset/<int:asset_id>/',edit_asset_view,name="edit_asset_page"),
    path('delete_asset/<int:asset_id>/',delete_asset_view,name="delete_asset_page"),

    path('add_stock/',add_stock_view,name="add_stock_page"),
    path('edit_stock/<int:stock_id>/',edit_stock_view,name="edit_stock_page"),
    path('delete_stock/<int:stock_id>/',delete_stock_view,name="delete_stock_page"),

    path('add_stock_item/',add_stock_item_view,name="add_stock_item_page"),
    path('edit_stock_item/<int:stock_item_id>/',edit_stock_item_view,name="edit_stock_item_page"),
    path('delete_stock_item/<int:stock_item_id>/',delete_stock_item_view,name="delete_stock_item_page"),

    path('add_requisition/',add_requisition_view,name="add_requisition_page"),
    path('edit_requisition/<int:requisition_id>/',edit_requisition_view,name="edit_requisition_page"),
    path('delete_requisition/<int:requisition_id>/',delete_requisition_view,name="delete_requisition_page"),

    path('add_requisition_item/',add_requisition_item_view,name="add_requisition_item_page"),
    path('edit_requisition_item/<int:requisition_item_id>/',edit_requisition_item_view,name="edit_requisition_item_page"),
    path('delete_requisition_item/<int:requisition_item_id>/',delete_requisition_item_view,name="delete_requisition_item_page"),
]