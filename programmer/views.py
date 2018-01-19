from django.shortcuts import render
from django.views.generic import View
from .models import Programmer


class HomeView(View):
    def get(self, request):

        qs = Programmer.objects.all()

        context = {
            'object_list': qs,
        }

        return render(request, 'programmer/home.html', context)
