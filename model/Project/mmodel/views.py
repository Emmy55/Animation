from django.shortcuts import render

# Create your views here.
from .models import Pan



# Value1 = Pan()
# Value1.num = 1 
# Value1.title = "Emma"
# Value1.des = "He is a Senior Devoloper"


# Value2 = Pan()
# Value2.num = 2
# Value2.title = "Somzy"
# Value2.des = "He is a Junior Developer"

# Value3 = Pan()
# Value3.num = 3
# Value3.title = "Bimpe"
# Value3.des = "She is a Product Designer"
# Value4 = Pan()
# Value4.num = 4
# Value4.title = "Samuel"
# Value4.des = "He is a Graphic Designer"

# all = [Value1, Value2, Value3, Value4]



def index(request):
    box = Pan.objects.all
    return render(request, 'mmodel/index.html',{
    'try' : box
    })