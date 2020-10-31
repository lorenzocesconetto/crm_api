from rest_framework import viewsets
from api.models import Customer
from api.serializers import CustomerSerializer
from django.views import generic
from .utils import render_react


class CustomerViewSet(viewsets.ReadOnlyModelViewSet):
    """
    This viewset automatically provides 'list' and 'detail' actions.
    """
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class IndexView(generic.ListView):
    model = Customer
    template_name = 'front/list.html'
    context_object_name = 'items'
    paginate_by = 20
    ordering = ['id']


class DetailView(generic.DetailView):
    model = Customer
    template_name = 'front/detail.html'
    context_object_name = 'item'


def new_page(request):
    return render_react(request, "list")
