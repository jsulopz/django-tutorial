from django.http import HttpResponse


def view_for_products(request):
    return HttpResponse("This function will render `html` code that makes you see this <p style='color: red'>text in red</p>.")

def new_view(request):
    return HttpResponse('This is the <strong>new view</strong>')