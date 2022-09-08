from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.urls import reverse
from .models import Question, Choice
from django.views import generic


# Class Based Views ---
class IndexView(generic.ListView):
    template_name = "questions/index.html"
    context_object_name = "latest_question_list"

    def get_queryset(self):
        # Retorna las ultimas 5 preguntas publicadas.
        return Question.objects.order_by("-pub_date")[:5]


class DetailView(generic.DetailView):
    model = Question
    template_name = "questions/detail.html"


# Hereda de  DetailView
class ResultView(DetailView):
    template_name = "questions/results.html"



# Function Based View --
def vote(request, question_id):
    question = get_object_or_404(Question, pk=question_id)
    try:
        selected_choice = question.choice_set.get(pk=request.POST["choice"])
    except (KeyError, Choice.DoesNotExist):
        return render(request, "questions/detail.html", {
            "question": question,
            "error_message": "No elegiste una respuesta"
        })
    else:
        selected_choice.votes += 1
        selected_choice.save()
        return HttpResponseRedirect(reverse("questions:results", args=(question.id,)))