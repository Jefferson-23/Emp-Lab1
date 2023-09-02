from django.shortcuts import render

def sumar(request, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    resultado = num1 + num2
    operacion_texto = 'suma'
    return render(request, 'tarea/resultado.html', {'operacion_texto': operacion_texto, 'num1': num1, 'num2': num2, 'resultado': resultado})

def restar(request, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    resultado = num1 - num2
    operacion_texto = 'resta'
    return render(request, 'tarea/resultado.html', {'operacion_texto': operacion_texto, 'num1': num1, 'num2': num2, 'resultado': resultado})

def multiplicar(request, num1, num2):
    num1 = int(num1)
    num2 = int(num2)
    resultado = num1 * num2
    operacion_texto = 'multiplicación'
    return render(request, 'tarea/resultado.html', {'operacion_texto': operacion_texto, 'num1': num1, 'num2': num2, 'resultado': resultado})

