from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
import math
from .models import Choice,Question
from django.template import loader
from django.urls import reverse
from .models import Movie,Actor
from django.db.models import Q

# Create your views here.

def aboutus(request):
    return render(request, 'about-us/about-us.html')

def start(request):
    return render(request, 'about-us/start.html')


def polls(request):
    latest_question_list = Question.objects.order_by('-pub_date')[:5]
    template = loader.get_template('polls/index.html')
    context = {
        'latest_question_list': latest_question_list,
    }
    return HttpResponse(template.render(context, request))

def detail(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/detail.html', {'question': question})

def results(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    return render(request, 'polls/results.html', {'question': question})

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('results', args=(question.id,)))

def movies(request):
    movies_list = Movie.objects.all()
    context = {'movies_list': movies_list}
    return render(request, 'about-us/movies.html', context)

def actors(request):
    actors_list = Actor.objects.all()
    context = {'actors_list': actors_list}
    return render(request, 'about-us/actors.html', context)

def whole_list(request, model, page):
    if page is None:
        return render(request, './about-us/404.html')
    page = int(page)
    objects = model.objects.all()
    total_page = int(math.ceil(len(objects) / 10))
    if page > total_page:
        return render(request, './about-us/404.html')
    last_item_index = 10 * page if page != total_page else len(objects)
    pages = []
    end_distance = total_page - page
    start_page_num = page - 5 if end_distance >= 5 else page - 10 + end_distance
    end_page_num = page + 5 if page > 5 else 10
    for i in range(start_page_num, end_page_num + 1):
        if 1 <= i <= total_page:
            pages.append(i)
    data = {'items': objects[10 * (page - 1):last_item_index], 'current_page': page, 'page_number': total_page,
            'pages': pages}
    return render(request, '{}_list.html'.format(model.get_name()), data)

def base(request):
    return render(request, 'about-us/base.html')

def search(request):
    sc = request.GET.get('search', None)
    context = None
    if sc:
        print(sc)
        movies_list = Movie.objects.filter(Q(name__icontains=sc))
        context = {'movies_list': movies_list}

    return render(request, 'about-us/movielist.html', context)