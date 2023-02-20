from django.shortcuts import render

# Create your views here.


def home(request):
    return render(request, 'Try/home.html')


def sub(request):
    return render(request, 'Try/sub.html')


def ans(request):
    return render(request, 'Try/adans.html')


# def sub(request):
#     return render(request, 'Try/sub.html')


def mult(request):
    return render(request, 'Try/mult.html')


# def div(request):
#     return render(request, 'Try/div.html')


# def squa(request):
#     return render(request, 'Try/square.html')
# def sqrt(request):
#     return render(request, 'Try/sqrt.html')

def ans(request):
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) + int(value2)
    return render(request, 'Try/adans.html', {
        'ans' : total
    })
def ans1(request):
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) - int(value2)
    return render(request, 'Try/adans.html', {
        'ans' : total
    })
def ans2(request):
    value1 = request.GET['first']
    value2 = request.GET['second']
    total = int(value1) * int(value2)
    return render(request, 'Try/adans.html', {
        'ans' : total
    })
# def ansbook2(request):
#     value1 = request.GET['first']
#     value2 = request.GET['second']
#     total = int(value1) * int(value2)
#     return render(request, 'Try/ansbook.html', {
#         'ans' : total
#     })
# def ansbook3(request):
#     value1 = request.GET['first']
#     value2 = request.GET['second']
#     total = int(value1) / int(value2)
#     return render(request, 'Try/ansbook.html', {
#         'ans' : total
#     })
# def ansbook4(request):
#     value1 = request.GET['first']
#     value2 = request.GET['second']
#     total = int(value1) ** int(value2)
#     return render(request, 'Try/ansbook.html', {
#         'ans' : total
#     })
# def ansbook5(request):
#     value1 = request.GET['first']
#     # value2 = request.GET['second']
#     total = math.sqrt(int(value1))
#     return render(request, 'Try/ansbook.html', {
#         'ans' : total
#     })