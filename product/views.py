from django.shortcuts import render
from django.db.models import Q
from .models import Shangping,Brand
# Create your views here

def products(request,sp_id):
    sp=Shangping.objects.get(id=sp_id)
    ma=sp.manu
    context={'sp':sp,'ma':ma}
    return render(request,'product/产品详情.html',context)
def sp_all(request):
    brands=Brand.objects.all()
    shangpings=Shangping.objects.all().filter(status='1')
    context={'shangpings':shangpings,'brands':brands,}
    return render(request,'product/sp_all.html',context)

    
