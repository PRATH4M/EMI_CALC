from django.shortcuts import render
from django.http import JsonResponse, HttpResponseBadRequest

def emi_calculator_view(request):
    return render(request, 'calculator/emi_calculator.html')

def calculate_emi(request):
    try:
        principal = float(request.GET.get('principal', 0))
        rate = float(request.GET.get('rate', 0))
        time = float(request.GET.get('time', 0))

        if principal <= 0 or rate <= 0 or time <= 0:
            return HttpResponseBadRequest("Invalid input values")

        rate = rate / (12 * 100)
        time = time * 12

        emi = (principal * rate * ((1 + rate) ** time)) / ((1 + rate) ** time - 1)
        return JsonResponse({'emi': emi})
    except ValueError:
        return HttpResponseBadRequest("Invalid input values")
