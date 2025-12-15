from django.shortcuts import render
def eff(request):
    d = int(request.POST.get('Distancetravelled', 0))
    v = int(request.POST.get('fuel', 0))
    e = d/v if request.method == 'POST' else 0
    print("Distance=",d)
    print("Volume=",v)
    print("Mileage=",e)
    return render(request, 'mathapp/math.html', {'d': d, 'v': v, 'e': e})
