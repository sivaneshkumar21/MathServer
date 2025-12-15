# Ex.04 Design a Website for Server Side Processing
## Date:
15/12/2025
## AIM:
To create a web page to calculate vehicle mileage and fuel efficiency using server-side scripts.

## FORMULA:
M = D / F
<br> M --> Mileage (in km/l)
<br> D --> Distance Travelled (in km)
<br> F --> Fuel Consumed (in l)

## DESIGN STEPS:

### Step 1:
Clone the repository from GitHub.

### Step 2:
Create Django Admin project.

### Step 3:
Create a New App under the Django Admin project.

### Step 4:
Create python programs for views and urls to perform server side processing.

### Step 5:
Create a HTML file to implement form based input and output.

### Step 6:
Publish the website in the given URL.

## PROGRAM:
~~~
math.html
<html>
    <head>
        <title>Vehicle Mileage</title>
    </head>
    <style>
        .box
        {
            margin-top: 10%;
            margin-left: 25%;
            margin-right:25%;
            border: 8px  aquamarine; 
            background-color: red;
            text-align: center; 
        }
    </style>
    <body>
        <div class="box">
        <h1> Calculator for Fuel Efficiency </h1>
        <h3>SIVANESH KUMAR.N</h3>
        <h3>25001283</h3>
        <br>
        <form method="POST">
            {% csrf_token %}
            <label>DISTANCE: </label>
            <input type="text" name="Distancetravelled" value="{{d}}" required> Km
            <br><br>
            <label>Volume Of Fuel: </label>
            <input type="text" name="fuel" value="{{v}}" required> L
            <br><br>
            <input type="submit" value="Calculate">
            <br><br>
            <label>Efficiency: </label>
            <input type="text" name="Fuel Efficiency" value="{{e}}"> Km/L
        </form>
        </div>
    </body>
</html>



views.py

from django.shortcuts import render
def eff(request):
    d = int(request.POST.get('Distancetravelled', 0))
    v = int(request.POST.get('fuel', 0))
    e = d/v if request.method == 'POST' else 0
    print("Distance=",d)
    print("Volume=",v)
    print("Mileage=",e)
    return render(request, 'mathapp/math.html', {'d': d, 'v': v, 'e': e})



urls.py
from django.urls import path
from mathapp import views
urlpatterns = [
    path('', views.eff, name='eff'),
]
~~~
## OUTPUT - SERVER SIDE:
![alt text](<Screenshot (36).png>)


## OUTPUT - WEBPAGE:
![alt text](<Screenshot (35).png>)


## RESULT:
The a web page to calculate vehicle mileage and fuel efficiency using server-side scripts is created successfully.
