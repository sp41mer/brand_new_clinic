from django.core.urlresolvers import reverse
from django.shortcuts import render, get_object_or_404

# Create your views here.

from django.http import HttpResponse, Http404, HttpResponseRedirect

def landing(request):
    return render(request, 'brand_new_clinic/index.html')