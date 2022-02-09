from django.shortcuts import render

from django.http import HttpResponse
from rango.models import Page
# Import the Category model
from rango.models import Category, Page
def index(request):
    return HttpResponse("Rango says hey there partner!")

def index(request):
    category_list = Category.objects.order_by('-likes')[:5]
    context_dict = {}

    pages = Page.objects.order_by('-views')[:5]
    # Construct a dictionary to pass to the template engine as its context.
    # Note the key boldmessage matches to {{ boldmessage }} in the template!
    context_dict = {'boldmessage': 'Crunchy, creamy, cookie, candy, cupcake!'}

    # Return a rendered response to send to the client.
    # We make use of the shortcut function to make our lives easier.
    # Note that the first parameter is the template we wish to use.

    context_dict['categories'] = category_list
    context_dict['pages'] = pages


    return render(request, 'rango/index.html', context=context_dict)

def about(request):
    return HttpResponse("Rango says here is the about page.")

def about(request):
    
    return render(request, 'rango/about.html',)

def show_category(request, category_name_slug):
    context_dict = {}

    try:
        category = Category.objects.get(slug=category_name_slug)
        pages = Page.objects.filter(category=category)
        context_dict['pages'] = pages
        context_dict['category'] = category

    except Category.DoesNotExist:
        context_dict['Category'] = None
        context_dict['pages'] = None
    
    return render(request, 'rango/category.html', context=context_dict)
