from django.shortcuts import get_object_or_404, render
from .models import Question, Choice
from django.urls import reverse
from django.http import HttpResponseRedirect
from django.views import generic

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))
#----------------------------------------------------------------------------------
#----------------------------------------------------------------------------------
from django.http.response import JsonResponse
from datetime import datetime
from django.db.models.functions import Extract, Trunc
from django.db.models import DateTimeField
from polls.models import Experiment
from django.core import serializers

# /extract/?lookup_name=xxx
def polls_extract(request):
    payload = request.GET.get('lookup_name')
    start = datetime(2015, 6, 15)
    end = datetime(2015, 7, 2)
    Experiment.objects.create(
        start_datetime=start, start_date=start.date(),
        end_datetime=end, end_date=end.date())
    experiments = Experiment.objects.filter(start_datetime__year=Extract('end_datetime', payload))
    return JsonResponse({"res": serializers.serialize("json", experiments)})

# /trunc/?kind=xxx
def polls_trunc(request):
    payload = request.GET.get('kind')
    start = datetime(2015, 6, 15)
    end = datetime(2015, 7, 2)
    Experiment.objects.create(
        start_datetime=start, start_date=start.date(),
        end_datetime=end, end_date=end.date())
    experiments = Experiment.objects.filter(start_datetime__date=Trunc('start_datetime', payload))
    return JsonResponse({"res": serializers.serialize("json", experiments)})