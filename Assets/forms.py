from django import forms

from Assets.models import Employee, Store, Asset, Stock, StockItem, Requisition, RequisitionItem


class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'


class StoreForm(forms.ModelForm):
    class Meta:
        model = Store
        fields = '__all__'


class AssetForm(forms.ModelForm):
    class Meta:
        model = Asset
        fields = '__all__'


class StockForm(forms.ModelForm):
    class Meta:
        model = Stock
        fields = '__all__'


class StockItemForm(forms.ModelForm):
    class Meta:
        model = StockItem
        fields = '__all__'


class RequisitionForm(forms.ModelForm):
    class Meta:
        model = Requisition
        fields = '__all__'


class RequisitionItemForm(forms.ModelForm):
    class Meta:
        model = RequisitionItem
        fields = '__all__'