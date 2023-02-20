from django.shortcuts import render

# Create your views here.
from .models import Same

sound = Same()
sound.name = "Iphone"
sound.id = 1
sound.des = "This is a good product to sample at anytime Lorem ipsum dolor sit amet consectetur adipisicing elit. Porro laborum aliquid consectetur est soluta, quibusdam accusantium necessitatibus aut iste reprehenderit sapiente architecto voluptate eligendi fugiat reiciendis illo sint ad doloribus molestias placeat exercitationem quo unde quisquam. Maiores, quia."

nound = Same()
nound.name
nound.id = 2

def shop(request):
    return render(request, 'ecomm/layout.html')
def shop1(request):
    return render(request, 'ecomm/shop.html', {
        'sounds' : sound,
        'nounds' : nound
    })
def shop1(request):
    return render(request, 'ecomm/shop.html', {
        'sounds' : sound,
        'nounds' : nound
    })