
#from .forms import InputForm
#from .models import STATES_DICT, CURRENCY_DICT

import geopandas as gpd, folium
from geopy import Nominatim

import seaborn as sns
sns.set(font_scale = 1.7)

from io import BytesIO

# Create your views here.
import matplotlib.pyplot as plt, numpy as np
import geopandas as gpd
import pandas as pd
import fiona
from shapely.geometry import Point
from os.path import join
from django.conf import settings
from django.http import HttpResponse, Http404, HttpResponseRedirect
from django.core.urlresolvers import reverse_lazy
from django.shortcuts import render
from .forms import InputForm
from .models import STATION_DICT

def home(request):
    return render(request, "home.html", {"title": "Danger: Biking in Chicago"})

def map(request):
    return render(request, "map.html", {"title": "Map"})

def presentation(request):
    return render(request, "presentation.html", {"title": "Presentation"})

def about(request):
    return render(request, "about.html", {"title": "About"})


def csv(request, station = None):


   filename = join(settings.STATIC_ROOT, 'myapp/map_data.csv')

   df = pd.read_csv(filename)

   if station: df = df[df["station"] == int("Station ID")]

   table = df.to_html(float_format = "%.3f", classes = "table table-striped", index_names = False)
   table = table.replace('border="1"','border="0"')
   table = table.replace('style="text-align: right;"', "") # control this in css, not pandas.

   return HttpResponse(table)

def plot(request):

    station = request.GET.get('station', '')
    if not station: station = request.POST.get('station', '494')

    params = {'form_action' : reverse_lazy('myapp:plot'), 
              'form_method' : 'get', 
              'form' : InputForm({'station' : station}),
              'station' : STATION_DICT[station],
              "title" : "Divvy Crime Map",
              "pic_source" : reverse_lazy("myapp:pic", kwargs = {'station' : station})}

    return render(request, 'plot.html', params)

def pic(request, station = None):

   data_file = join(settings.STATIC_ROOT, 'myapp/join_data.csv')
   divvy_data = pd.read_csv(data_file)
   divvy_data = divvy_data[divvy_data["FROM STATION ID"] == int(station)]
   divvy_data['Type_Counts'] = divvy_data.groupby("Primary Type")["FROM STATION ID"].transform('count')
   result = divvy_data[["Primary Type","Type_Counts"]].drop_duplicates(keep='first')
   ax = result.plot(kind = "bar", legend = False, rot = 90, figsize=(40,15), x = "Primary Type", y = "Type_Counts")

   # write bytes instead of file.
   from io import BytesIO
   figfile = BytesIO()

   # this is where the color is used.
   try: ax.get_figure().savefig(figfile, format = 'png', bbox_inches='tight')
   except ValueError: raise Http404("No such color")

   figfile.seek(0) # rewind to beginning of file
   return HttpResponse(figfile.read(), content_type="image/png")
