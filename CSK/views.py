from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def Team(request):
    return HttpResponse('''<p style=color:black;background-color:blue;>The  CSK Squad for Ipl 2025:</p>
                        <h1 style=color:black;background-color:yellow;padding:10px;border-radius:10px;>Ruturaj Gaikwad</h1>
                        <h1 style=color:black;background-color:yellow;padding:10px;border-radius:10px;>MS dhoni</h1>
                        <h1 style=color:black;background-color:yellow;padding:10px;border-radius:10px;>Ravindra jadeja</h1>
                        <h1 style=color:black;background-color:yellow;padding:10px;border-radius:10px;>Ravichandran Ashwin</h1>
                        ''')