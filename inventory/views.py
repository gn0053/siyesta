import json
from django.contrib.auth.decorators import login_required
from django.shortcuts import render
from django.http import HttpResponse, JsonResponse
from django.db.models import Q, F, Case, When, FloatField
from .models import Item
from .forms import ItemForm, itemId
from .export import generate_inventory_report

@login_required
def index(request): 
    return render(request, 'inventory.html')

@login_required
def load_inventory(request):
    rows = []
    
    total_records = 0
    start = int(request.POST['start'])
    length = int(request.POST['length'])
    total = Item.objects.all().count()
    model_obj = None
    if request.POST['search[value]']:
        model_obj = Item.objects.all().annotate(
            unit_prices = Case(
                When(Q(item_price__exact=0) | Q(unit_per_item__exact=0), then=0.0),
                default=F("item_price") / F("unit_per_item")
            )
        ).filter(
            Q(item_name__icontains=request.POST['search[value]'])|
            Q(item_price__icontains=request.POST['search[value]'])|
            Q(unit_per_item__icontains=request.POST['search[value]'])|
            Q(description__icontains=request.POST['search[value]'])|
            Q(unit_prices__icontains=request.POST['search[value]'])
        )[start:length]
    else:
        model_obj = Item.objects.all().annotate(
            unit_prices = Case(
                When(Q(item_price__exact=0) | Q(unit_per_item__exact=0), then=0.0),
                default=F("item_price") / F("unit_per_item")
            )
        )[start:length]
    # if request.POST['search[value]']:
    #     model_obj = Item.objects.filter(
    #         Q(item_name__icontains=request.POST['search[value]'])|
    #         Q(item_price__icontains=request.POST['search[value]'])|
    #         Q(unit_per_item__icontains=request.POST['search[value]'])|
    #         Q(description__icontains=request.POST['search[value]'])
    #         # Q(unit_price__icontains=request.POST['search[value]'])
    #     )[start:length]
    # else:
    #     model_obj = Item.objects.all()[start:length]
    
    for qobj in model_obj:
        total_records += 1
        item = [
            qobj.id,
            qobj.item_name,
            qobj.item_price,
            qobj.unit_per_item,
            qobj.unit_prices,
            qobj.description,
            qobj.is_active,
            qobj.is_deleted,
        ]
        rows.append(item)
    data = {
        "draw":request.POST['draw'],
        "recordsTotal":total,
        "recordsFiltered":total_records,
        "data":rows,
    }
    return HttpResponse(json.dumps(data), content_type='application/json')

@login_required
def remove_item(request):
    status = "Success"
    form = itemId(request.POST)
    if request.method == "POST" and form.is_valid():
        id = form.cleaned_data['question_id']
        item_row = Item.objects.get(pk=int(id))
        item_row.is_deleted = True
        item_row.save()
    else:
        status = "Failed"
    return JsonResponse({'Status':status})

@login_required
def restore_item(request):
    status = "Success"
    form = itemId(request.POST)
    if request.method == "POST" and form.is_valid():
        id = form.cleaned_data['question_id']
        item_row = Item.objects.get(pk=int(id))
        item_row.is_deleted = False
        item_row.save()
    else:
        status = "Failed"
    return JsonResponse({'Status':status})

@login_required
def save_item(request):
    form = ItemForm(request.POST)
    if request.method == "POST" and form.is_valid():
        id = form.cleaned_data['id']
        item_name = form.cleaned_data['item_name']
        item_price = form.cleaned_data['item_price']
        unit_per_item = form.cleaned_data['unit_per_item']
        description = form.cleaned_data['description']
        if(int(id) == 0):
            Item.objects.create(
                item_name=item_name,
                item_price=item_price,
                unit_per_item=unit_per_item,
                description=description,
            )
        else:
            item_row = Item.objects.get(pk=int(id))
            item_row.item_name = item_name
            item_row.item_price = item_price
            item_row.unit_per_item = unit_per_item
            item_row.description = description
            item_row.save()
    return JsonResponse({'data':'test'})

@login_required
def change_status(request):
    if request.method == "POST":
        print(request.POST)
        if request.POST['id'].isdigit():
            id = request.POST['id']
            item_row = Item.objects.get(pk=int(id))
            if request.POST['status'] == 'false':
                item_row.is_active = False
            else:
                item_row.is_active = True
            item_row.save()

    return JsonResponse({'data':'test'})

@login_required
def exportItems(request):
    response = HttpResponse(content_type='application/vnd.ms-excel')
    response['Content-Disposition'] = 'attachment;filename="test_file.xlsx"'
    output = generate_inventory_report()
    response.write(output.getvalue())
    return response