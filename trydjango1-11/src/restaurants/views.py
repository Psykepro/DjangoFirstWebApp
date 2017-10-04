import random
from django.db.models import Q
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.views import View
from django.views.generic import TemplateView, ListView, DetailView, CreateView


from .forms import RestaurantCreateForm, RestaurantLocationCreateForm
from .models import RestaurantLocation

def restaurant_create_view(request):
    form = RestaurantLocationCreateForm(request.POST or None)
    errors = None
    if form.is_valid():
        if request.user.is_authenticated():
            instance = form.save(commit=False)
            # customize
            # like a pre_save
            instance.owner = request.user
            instance.save()
            # like a post_save
            return HttpResponseRedirect("/restaurants/")
        else:
            return HttpResponseRedirect("/login/")
    if form.errors:
        errors = form.errors
    template_name = 'restaurants/form.html'
    context = {
        'form': form,
        'errors':errors
    }
    return render(request, template_name, context)

def restaurant_list_view(request):
    template_name = 'restaurants/restaurants_list.html'
    queryset = RestaurantLocation.objects.all()
    context = {
        'object_list': queryset
    }
    return render(request, template_name, context)

class RestaurantListView(ListView):
    template_name = 'restaurants/restaurants_list.html'

    def get_queryset(self):
        slug = self.kwargs.get('slug')
        if slug:
            queryset = RestaurantLocation.objects.filter(
                    Q(category__iexact=slug) |
                    Q(category__icontains=slug)
                )
        else:
            queryset = RestaurantLocation.objects.all()

        return queryset

class RestaurantDetailView(DetailView):
    template_name = 'restaurants/restaurants_detail.html'
    queryset = RestaurantLocation.objects.all()
    # def get_context_data(self, *args, **kwargs):
    #     context = super(RestaurantDetailView, self).get_context_data(*args, **kwargs)
    #     return context

    # def get_object(self, *args, **kwargs):
    #     rest_id = self.kwargs.get('rest_id')
    #     obj = get_object_or_404(RestaurantLocation, id=rest_id)
    #     return obj

class RestaurantCreateView(CreateView):
    form_class = RestaurantLocationCreateForm
    template_name = 'restaurants/form.html'
    success_url = '/restaurants/'
    
    def form_valid(self, form):
        instance = form.save(commit=False)
        instance.owner = self.request.user
        return super(RestaurantCreateView,self).form_valid(form)