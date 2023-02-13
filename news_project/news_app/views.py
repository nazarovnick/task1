from django.shortcuts import render
from news_app.models import news_model


# Create your views here.
def index_page(request):

    news = news_model.objects.all()

    context = {
                'news' : news,
               }

    return render(request = request, template_name = 'index.html', context = context)