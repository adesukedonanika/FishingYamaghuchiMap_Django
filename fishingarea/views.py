from django.views import generic

# Create your views here.

class IndexView(generic.TemplateView):
    templete_name="index.html"