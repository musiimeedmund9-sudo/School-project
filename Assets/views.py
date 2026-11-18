from django.shortcuts import render, redirect,get_object_or_404
from django.http import HttpResponseRedirect

from Assets.forms import EmployeeForm,StoreForm,AssetForm,StockForm,StockItemForm,RequisitionForm,RequisitionItemForm
from Assets.forms import Employee,Store,Asset,Stock,StockItem,Requisition,RequisitionItem
from django.contrib.auth.forms import UserCreationForm

def add_employee_view(request):
    message = ''
    if request.method =="POST":
        employee_form = EmployeeForm(request.POST)

        if employee_form.is_valid():
            employee_form.save()

            message= "Employee added successfully"
    else:
        employee_form = EmployeeForm() 

    employees = Employee.objects.all()        


    context ={
        'form':employee_form,
        'msg' :message,
        'employees': employees
    }    
    return render (request,"add_employee.html",context) 



def edit_employee_view(request,employee_id):
        employee = Employee.objects.get(id=employee_id)
        message = ""


        if request.method =="POST":
            employee_form =EmployeeForm(request.POST, instance=employee)
            

            if employee_form.is_valid():
                employee_form.save()
                message = "Changes saved successfully"

            else:
                message= "Form is Invalid Data"    

        else:
            employee_form = EmployeeForm(instance=employee)


        context={
            'form': employee_form,
            'employee':employee,
            'message': message
            
        }   
        return render(request,'edit_employee.html',context)  
   
def delete_employee_view (request, employee_id):
    employee = Employee.objects.get(id=employee_id)

    employee.delete()

    return redirect(add_employee_view)


def add_store_view(request):
    message = ''
    if request.method =="POST":
        store_form = StoreForm(request.POST)

        if store_form.is_valid():
            store_form.save()

            message= "Store added successfully"
    else:
        store_form = StoreForm() 

    stores = Store.objects.all()        


    context ={
        'form':store_form,
        'msg' :message,
        'stores': stores
    }    
    return render (request,"add_store.html",context) 



def edit_store_view(request,store_id):
        store = Store.objects.get(id=store_id)
        message = ""


        if request.method =="POST":
            store_form =StoreForm(request.POST, instance=store)
            

            if store_form.is_valid():
                store_form.save()
                message = "Changes saved successfully"

            else:
                message= "Form is Invalid Data"    

        else:
            store_form = StoreForm(instance=store)


        context={
            'form': store_form,
            'store':store,
            'message': message
            
        }   
        return render(request,'edit_store.html',context)  
   
def delete_store_view (request, store_id):
    store = Store.objects.get(id=store_id)

    store.delete()

    return redirect(add_store_view)


def add_asset_view(request):
    message = ''
    if request.method =="POST":
        asset_form = AssetForm(request.POST)

        if asset_form.is_valid():
            asset_form.save()

            message= "Asset added successfully"
    else:
        asset_form = AssetForm() 

    assets = Asset.objects.all()        


    context ={
        'form':asset_form,
        'msg' :message,
        'assets': assets
    }    
    return render (request,"add_asset.html",context) 



def edit_asset_view(request,asset_id):
        asset = Asset.objects.get(id=asset_id)
        message = ""


        if request.method =="POST":
            asset_form =AssetForm(request.POST, instance=asset)
            

            if asset_form.is_valid():
                asset_form.save()
                message = "Changes saved successfully"

            else:
                message= "Form is Invalid Data"    

        else:
            asset_form = AssetForm(instance=asset)


        context={
            'form': asset_form,
            'asset':asset,
            'message': message
            
        }   
        return render(request,'edit_asset.html',context)  
   
def delete_asset_view (request, asset_id):
    asset = Asset.objects.get(id=asset_id)

    asset.delete()

    return redirect(add_asset_view)


def add_stock_view(request):
    message = ''
    if request.method =="POST":
        stock_form = StockForm(request.POST)

        if stock_form.is_valid():
            stock_form.save()

            message= "Stock added successfully"
    else:
        stock_form = StockForm() 

    stocks = Stock.objects.all()        


    context ={
        'form':stock_form,
        'msg' :message,
        'stocks': stocks
    }    
    return render (request,"add_stock.html",context) 



def edit_stock_view(request,stock_id):
        stock = Stock.objects.get(id=stock_id)
        message = ""


        if request.method =="POST":
            stock_form =StockForm(request.POST, instance=stock)
            

            if stock_form.is_valid():
                stock_form.save()
                message = "Changes saved successfully"

            else:
                message= "Form is Invalid Data"    

        else:
            stock_form = StockForm(instance=stock)


        context={
            'form': stock_form,
            'stock':stock,
            'message': message
            
        }   
        return render(request,'edit_stock.html',context)  
   
def delete_stock_view (request, stock_id):
    stock = Stock.objects.get(id=stock_id)

    stock.delete()

    return redirect(add_stock_view)


def add_stock_item_view(request):
    message = ''
    if request.method =="POST":
        stock_item_form = StockItemForm(request.POST)

        if stock_item_form.is_valid():
            stock_item_form.save()

            message= "Stock item added successfully"
    else:
        stock_item_form = StockItemForm() 

    stock_items = StockItem.objects.all()        


    context ={
        'form':stock_item_form,
        'msg' :message,
        'stock_items': stock_items
    }    
    return render (request,"add_stock_item.html",context) 



def edit_stock_item_view(request,stock_item_id):
        stock_item = StockItem.objects.get(id=stock_item_id)
        message = ""


        if request.method =="POST":
            stock_item_form =StockItemForm(request.POST, instance=stock_item)
            

            if stock_item_form.is_valid():
                stock_item_form.save()
                message = "Changes saved successfully"

            else:
                message= "Form is Invalid Data"    

        else:
            stock_item_form = StockItemForm(instance=stock_item)


        context={
            'form': stock_item_form,
            'stock_item':stock_item,
            'message': message
            
        }   
        return render(request,'edit_stock_item.html',context)  
   
def delete_stock_item_view (request, stock_item_id):
    stock_item = StockItem.objects.get(id=stock_item_id)

    stock_item.delete()

    return redirect(add_stock_item_view)


def add_requisition_view(request):
    message = ''
    if request.method =="POST":
        requisition_form = RequisitionForm(request.POST)

        if requisition_form.is_valid():
            requisition_form.save()

            message= "Requisition added successfully"
    else:
        requisition_form = RequisitionForm() 

    requisitions = Requisition.objects.all()        


    context ={
        'form':requisition_form,
        'msg' :message,
        'requisitions': requisitions
    }    
    return render (request,"add_requisition.html",context) 



def edit_requisition_view(request,requisition_id):
        requisition = Requisition.objects.get(id=requisition_id)
        message = ""


        if request.method =="POST":
            requisition_form =RequisitionForm(request.POST, instance=requisition)
            

            if requisition_form.is_valid():
                requisition_form.save()
                message = "Changes saved successfully"

            else:
                message= "Form is Invalid Data"    

        else:
            requisition_form = RequisitionForm(instance=requisition)


        context={
            'form': requisition_form,
            'requisition':requisition,
            'message': message
            
        }   
        return render(request,'edit_requisition.html',context)  
   
def delete_requisition_view (request, requisition_id):
    requisition = Requisition.objects.get(id=requisition_id)

    requisition.delete()

    return redirect(add_requisition_view)


def add_requisition_item_view(request):
    message = ''
    if request.method =="POST":
        requisition_item_form = RequisitionItemForm(request.POST)

        if requisition_item_form.is_valid():
            requisition_item_form.save()

            message= "Requisition item added successfully"
    else:
        requisition_item_form = RequisitionItemForm() 

    requisition_items = RequisitionItem.objects.all()        


    context ={
        'form':requisition_item_form,
        'msg' :message,
        'requisition_items': requisition_items
    }    
    return render (request,"add_requisition_item.html",context) 



def edit_requisition_item_view(request,requisition_item_id):
        requisition_item = RequisitionItem.objects.get(id=requisition_item_id)
        message = ""


        if request.method =="POST":
            requisition_item_form =RequisitionItemForm(request.POST, instance=requisition_item)
            

            if requisition_item_form.is_valid():
                requisition_item_form.save()
                message = "Changes saved successfully"

            else:
                message= "Form is Invalid Data"    

        else:
            requisition_item_form = RequisitionItemForm(instance=requisition_item)


        context={
            'form': requisition_item_form,
            'requisition_item':requisition_item,
            'message': message
            
        }   
        return render(request,'edit_requisition_item.html',context)  
   
def delete_requisition_item_view (request, requisition_item_id):
    requisition_item = RequisitionItem.objects.get(id=requisition_item_id)

    requisition_item.delete()

    return redirect(add_requisition_item_view)


def sign_up_view(request ):
    if request.method =="POST":
        sign_up_form =UserCreationForm(request.POST)
        if sign_up_form .is_valid ():
            sign_up_form.save()
            return redirect('login') 
            message ='User created sucessfully'

        else:
            message = 'something went wrong '  
                      

    else:
        sign_up_form = UserCreationForm()


    context = {
    'form':sign_up_form
}

    return render(request,'registration/sign_up.html',context)