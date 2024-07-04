# views.py

from django.contrib.auth.decorators import login_required
from django.contrib.auth import login, logout
from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render, redirect
import math

# Calculator operations
def add(number1, number2):
    return number1 + number2

def subtract(number1, number2):
    return number1 - number2

def multiply(number1, number2):
    return number1 * number2

def divide(number1, number2):
    if number2 != 0:
        return number1 / number2
    else:
        raise ValueError('Error: Division by zero')

def modulus(number1, number2):
    return number1 % number2

def power(number1, number2):
    return number1 ** number2

def square_root(number):
    if number >= 0:
        return math.sqrt(number)
    else:
        raise ValueError('Square root of a negative number is undefined')

def percent(number1, number2):
    return (number1 * number2) / 100

OPERATIONS = {
    'add': add,
    'subtract': subtract,
    'multiply': multiply,
    'divide': divide,
    'modulus': modulus,
    'power': power,
    'sqrt': square_root,
    'percent': percent
}

# Calculator view
@login_required
def calculator_view(request):
    result = None
    error = None
    if request.method == 'POST':
        try:
            number1_str = request.POST.get('number1', '').strip()
            number2_str = request.POST.get('number2', '').strip()
            number1 = float(number1_str) if number1_str else 0
            number2 = float(number2_str) if number2_str else 0
            operation = request.POST.get('operation')
            if operation in OPERATIONS:
                if operation == 'sqrt':
                    result = OPERATIONS[operation](number1)
                else:
                    result = OPERATIONS[operation](number1, number2)
            else:
                error = 'Error: Invalid operation'
        except ValueError as e:
            error = str(e)
    return render(request, 'calculator.html', {'result': result, 'error': error})

# Login view
def login_view(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('calculator')
    else:
        form = AuthenticationForm()
    return render(request, 'login.html', {'form': form})

# Logout view
def logout_view(request):
    if request.method == 'POST':
        logout(request)
        return redirect('login')
