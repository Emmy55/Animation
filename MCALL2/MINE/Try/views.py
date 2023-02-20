from django.shortcuts import render

import math
# Create your views here.
def lay(request):
    return render(request, 'Try/layout.html')


def sel(request):
    return render(request, 'Try/select.html')


def ads(request):
    return render(request, 'Try/adds.html')


def sub(request):
    return render(request, 'Try/sub.html')


def mult(request):
    return render(request, 'Try/mult.html')


def div(request):
    return render(request, 'Try/div.html')


def squa(request):
    return render(request, 'Try/square.html')
def sqrt(request):
    return render(request, 'Try/sqrt.html')
def simul(request):
    return render(request, 'Try/simult.html')
def quad(request):
    return render(request, 'Try/quad.html')
# def varia(request):
#     return render(request, 'Try/selvaria.html')
def selvaria(request):
    return render(request, 'Try/selvaria.html')
def direct(request):
    return render(request, 'Try/direct.html')
def inverse(request):
    return render(request, 'Try/inverse.html')


def ansbook(request):
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) + int(value2)
    
    return render(request, 'Try/ansbook.html', {
        'ans' : total
    })
def ansbook1(request):
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) - int(value2)
    return render(request, 'Try/ansbook.html', {
        'ans' : total
    })
def ansbook2(request):
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) * int(value2)
    return render(request, 'Try/ansbook.html', {
        'ans' : total
    })
def ansbook3(request):
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) / int(value2)
    return render(request, 'Try/ansbook.html', {
        'ans' : total
    })
def ansbook4(request):
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) ** int(value2)
    return render(request, 'Try/ansbook.html', {
        'ans' : total
    })
def ansbook5(request):
    value1 = request.GET['first']
    # value2 = request.GET['second']
    total = math.sqrt(int(value1))
    return render(request, 'Try/ansbook.html', {
        'ans' : total
    })
def ansbook6(request):
    value1 = int(request.GET['first'])
    value2 = int(request.GET['second'])
    value3 = int(request.GET['third'])
    value4 = int(request.GET['forth'])
    value5 = int(request.GET['fifth'])
    value6 = int(request.GET['sixth'])
    mult1 = value1*value5
    mult1 = int(mult1)
    mult2 = value4*value2
    mult2 = int(mult2)
    sub = (mult1 - mult2)
    mult12 = value3*value5
    mult22 = value6*value2
    sub2 = (mult12 - mult22)
    mult13 = value1*value6
    mult23 = value4*value3
    sub3 = (mult13 - mult23)
    div = sub2 / sub
    div2 = sub3 / sub
    # total = math.sqrt(int(value1))
    return render(request, 'Try/anssbook.html', {
        'ans' : div,
        'ans1' : div2
    })

def ansbook7(request):  
    value1 = float(request.GET['first'])
    value2 = float(request.GET['second'])
    value3 = float(request.GET['third'])
    nat1 = value2 * -1
    nat2 = value2**2
    nat3 = (nat2) - (4*value1*value3)
    nat4 = math.sqrt(nat3)
    nat5 = 2*value1
    nat6 = nat1 + nat4
    nat7 = nat1 - nat4
    ans1 = nat6/nat5
    ans2 = nat7/nat5
    return render(request, 'Try/anssbook.html', {
        'ans' : ans1,
        'ans1' :ans2 
    })

def ansbook8(request):
    a1 = int(request.GET['first'])
    b1 = int(request.GET['second'])
    a2 = int(request.GET['third'])
    b2 = int(request.GET['forth'])
    bin = b1*a2
    bin1 = b2*a1
    if b2 == 0:
        total = bin/a1
        total1 = a1/b1
    elif a1 == 0:
            total = (bin/b2)
            total1 = (a2/b2)
    elif b1 == 0:
            total = (bin1/a2)
            total1 = (a2/b2)
    elif a2 == 0:
            total = (bin1/b1)
            total1 = (a1/b1)
        
    return render(request, 'Try/varans.html',{
        'ans' : total,
        'ans1' : total1
    } )


def ansbook9(request):
    a1 = int(request.GET['first'])
    b1 = int(request.GET['second'])
    a2 = int(request.GET['third'])
    b2 = int(request.GET['forth'])
    k1 = a1*b1
    k2 = a2*b2
    if a2 == 0:
        total = (k1/b2) 
        total1 = (k1)
    elif b2 == 0:
            total = (k1/a2)
            total1 = (k1)
    elif a1 == 0:
            total = (k2/b1)
            total1 = (k2)
    elif b1 == 0:
            total = (k2/a1)
            total1 = (k2)
    return render(request, 'Try/varans.html', {
        'ans' : total,
        'ans1' : total1
    })