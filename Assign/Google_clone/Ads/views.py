from django.shortcuts import render

from django.http import HttpResponse

from .models import mode


# Create your views here.


# def sam1(request):
#     return render(request, "Ads/sign.html")

# def about(request):
#     return render(request, "Ema/about.html")


# first = mode()
# first.title = "Reputation, Respect, and Result"
# first.id = 1 
# first.des = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis fuga voluptates voluptatibus ea reiciendis dolore numquam ullam ratione molestiae a!"

# second = mode()
# second.title = "Reqeust, Quotation, Perspective"
# second.id = 2
# second.des = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus itaque in aspernatur atque. Eaque, nostrum?"

# third = mode()
# third.title = "Demand, Smart, Dorch"
# third.id = 3
# third.des = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto animi aliquam vero eaque eveniet."

# first1 = mode()
# first1.title = "Reputation, Respect, and Result"
# first1.id = 4
# first1.des = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis fuga voluptates voluptatibus ea reiciendis dolore numquam ullam ratione molestiae a!"

# second1 = mode()
# second1.title = "Reqeust, Quotation, Perspective"
# second1.id = 5
# second1.des = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus itaque in aspernatur atque. Eaque, nostrum?"

# third1 = mode()
# third1.title = "Demand, Smart, Dorch"
# third1.id = 6
# third1.des = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto animi aliquam vero eaque eveniet."

# fist = [first, second, third, first1, second1, third1]


def nite(request):
    fist = mode.objects.all
    return render(request, 'Ads/layout.html', {
        'train' : fist,
        
    })