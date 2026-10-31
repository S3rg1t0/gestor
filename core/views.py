from django.shortcuts import render, HttpResponse

from core.models import Question


# Create your views here.

def question_view(request):

    return HttpResponse(
        "<h1> Sargento Torreznillo </h1>"
        "<p>Quieres comer palomitas con tu maridito </p>"
    )


