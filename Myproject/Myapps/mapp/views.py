from django.shortcuts import render




def ans(request):
    van = request.GET['wowo']
    vab = request.GET['wowi']
    total = int(van) + int(vab)
    return render(request, "mapp/answer2.html", {
        'ans' : total
    })




def name2(request):
    return render(request, "mapp/smarter.html")


def name(request):
    return render(request, "mapp/smart.html")

