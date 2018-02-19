from django.shortcuts import get_object_or_404, redirect
from django.views.generic import CreateView, UpdateView
from .forms import ProgForm
from .models import Programmer


class HomeView(CreateView):
    form_class = ProgForm
    template_name = 'programmer/home.html'

    def form_valid(self, form):
        return super(HomeView, self).form_valid(form)

    def get_queryset(self):
        return Programmer.objects.all()

    def get_context_data(self, *args, **kwargs):
        context = super(HomeView, self).get_context_data(*args, **kwargs)

        qs = Programmer.objects.all()

        context['object_list'] = qs
        context['submit_btn'] = 'Create'
        return context


class UpdateProgView(UpdateView):
    form_class = ProgForm
    template_name = 'programmer/update.html'

    def get_object(self, queryset=None):
        obj, created = Programmer.objects.get_or_create(id=self.kwargs['pk'])
        return obj

    def get_context_data(self, *args, **kwargs):
        context = super(UpdateProgView, self).get_context_data(*args, **kwargs)
        context['submit_btn'] = 'Update'
        return context


def doc_delete(request, pk=None):
    instance = get_object_or_404(Programmer, id=pk)
    instance.delete()
    return redirect("/")
