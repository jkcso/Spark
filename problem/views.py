from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from django.views.generic.edit import FormMixin

from .forms import *


def problem_page(request, problem_id):
    problem = Problem.objects.get(pk=problem_id)

    return render(request, 'problem/problem_page.html', {'problem': problem})


def upvote(request, problem_id):
    problem = Problem.objects.get(pk=problem_id)
    problem.up_vote()

    return render(request, 'problem/problem_page.html', {'problem': problem})


def downvote(request, problem_id):
    problem = Problem.objects.get(pk=problem_id)
    problem.down_vote()

    return render(request, 'problem/problem_page.html', {'problem': problem})


def sol_upvote(request, problem_id, solution_id):
    problem = Problem.objects.get(pk=problem_id)
    solution = problem.solution_set.get(pk=solution_id)
    solution.up_vote()

    return render(request, 'problem/solution_page.html', {'problem': problem, 'solution': solution})


def sol_downvote(request, problem_id, solution_id):
    problem = Problem.objects.get(pk=problem_id)
    solution = problem.solution_set.get(pk=solution_id)
    solution.down_vote()

    return render(request, 'problem/solution_page.html', {'problem': problem, 'solution': solution})


def index(request):
    top_rated = get_top_rated_problems()
    newest_probs = get_newest_problems()

    return render(request, 'problem/index.html', {'top_rated': top_rated,
                                         'newest_probs': newest_probs
    })


def create_solution(request, problem_id):
    form = SolutionForm(request.POST or None)
    problem = get_object_or_404(Problem, pk=problem_id)
    if form.is_valid():
        solution = form.save(commit=False)
        solution.problem = problem
        # solution.file = request.FILES['file']
        solution.save()
        solution.alert_subscribers(request.build_absolute_uri())
        return solution_page(request, problem.id, solution.id)
    context = {
        'problem': problem,
        'form': form,
    }
    return render(request, 'problem/create_solution.html', context)


def subscribe(request, problem_id):
    form = SubscriberForm(request.POST or None)
    problem = get_object_or_404(Problem, pk=problem_id)
    if form.is_valid():
        subscriber = form.save(commit=False)
        subscriber.problem = problem
        subscriber.save()
        return render(request, 'problem/problem_page.html', {'problem': problem})
    context = {
        'problem': problem,
        'form': form,
    }
    return render(request, 'problem/subscribe.html', context)


def solution_page(request, problem_id, solution_id):
    problem = Problem.objects.get(pk=problem_id)
    solution = problem.solution_set.get(pk=solution_id)
    return render(request, 'problem/solution_page.html', {'problem': problem, 'solution': solution})


class ProblemCreate(CreateView):
    model = Problem
    fields = ['title', 'description']


class SolutionCreate(CreateView):
    model = Solution
    fields = ['description']


# Filters result after search.
class FilteredListView(FormMixin, ListView):
    def get_form_kwargs(self):
        return {
          'initial': self.get_initial(),
          'prefix': self.get_prefix(),
          'data': self.request.GET or None
        }

    def get(self, request, *args, **kwargs):
        self.object_list = self.get_queryset()

        form = self.get_form(self.get_form_class())

        if form.is_valid():
            self.object_list = form.filter_queryset(request, self.object_list)

        context = self.get_context_data(form=form, object_list=self.object_list)
        return self.render_to_response(context)


# used for search filtering and also displaying all problems of the site.
problem_list = FilteredListView.as_view(
    form_class=ProblemSearchForm,
    template_name='../templates/problem/problem_list.html',
    queryset=Problem.objects.all(),
    paginate_by=12
)
