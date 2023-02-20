from django.shortcuts import render

from .models import mode
# Create your views here.

first = mode()
first.title = "Reputation, Respect, and Result"
first.id = 1 
first.des = "Lorem, ipsum dolor sit amet consectetur adipisicing elit. Omnis fuga voluptates voluptatibus ea reiciendis dolore numquam ullam ratione molestiae a!"

second = mode()
second.title = "Reqeust, Quotation, Perspective"
second.id = 2
second.des = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Minus itaque in aspernatur atque. Eaque, nostrum?"

third = mode()
third.title = "Demand, Smart, Dorch"
third.id = 3
third.des = "Lorem ipsum dolor sit amet, consectetur adipisicing elit. Architecto animi aliquam vero eaque eveniet."

fist = [first, second, third]
def nite(request):
    return render(request, 'Practice/nite.html', {
        'train' : fist,
        
    })