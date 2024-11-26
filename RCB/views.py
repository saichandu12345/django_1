from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Captain(request):
    return HttpResponse('''<p style=color:white;background-color:blue;>The  RCB Squad for Ipl 2025:</p>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Virat Kohli</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Rajat patidar</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Philip Salt</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Liam Livingstone</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Tim David</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Padikkal</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Shafford</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Betchell</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Krunal Pandhya</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Hazelwood</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Bhuvaneshwar</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Yash Dhayal</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Suyash Sharma</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Swapnil singh</h1>
                        <h1 style=color:black;background-color:red;padding:10px;border-radius:10px;>Lungi ingndi</h1>
                        ''')