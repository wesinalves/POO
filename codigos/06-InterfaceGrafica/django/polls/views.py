from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, HttpResponseRedirect

from polls.models import Question, Choice
from django.db.models import F
from django.urls import reverse, reverse_lazy
from django.views import generic
from django.utils import timezone

# Create your views here.

class IndexView(generic.ListView):
    template_name = 'polls/index.html'
    context_object_name = 'latest_question_list'

    def get_queryset(self):
        return Question.objects.filter(pub_date__lte=timezone.now()).order_by('-pub_date')[:5]

class DetailView(generic.DetailView):
    model = Question
    template_name = 'polls/detail.html'

class QuestionCreateView(generic.edit.CreateView):
    model = Question
    fields = ['question_text', 'pub_date']

class QuestionUpdateView(generic.edit.UpdateView):
    model = Question
    fields = ['question_text', 'pub_date']

class QuestionDeleteView(generic.edit.DeleteView):
    model = Question
    success_url = reverse_lazy('polls:index')


class ChoiceCreateView(generic.edit.CreateView):
    model = Choice
    fields = ['question', 'choice_text', 'votes']

class ChoiceUpdateView(generic.edit.CreateView):
    model = Choice
    fields = ['question', 'choice_text', 'votes']

class ResultsView(generic.DetailView):
    model = Question
    template_name = 'polls/results.html'

def vote(request, question_id):
    question = get_object_or_404(Question, pk = question_id)
    if request.method != 'POST':
        return HttpResponse("Method not allowed", status = 405)
    
    try:
        selected_choice = question.choice_set.get(pk = request.POST['choice'])
    except (KeyError, Choice.DoesNotExist):
        return render(request, 'polls/detail.html', {
            'question': question,
            'error_message': "You didn't select a choice.",
        })
    else:
        selected_choice.votes = F('votes') + 1
        selected_choice.save()
    return HttpResponseRedirect(reverse('polls:results', args=(question.id,)))


