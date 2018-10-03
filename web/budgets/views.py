from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import ListView, DetailView, CreateView
from django.urls import reverse_lazy
from .models import Budget, Transaction


class BudgetListView(LoginRequiredMixin, ListView):
    """View class quering list of budget objects for budget lsit html
    """
    template_name = 'budgets/budgets_list.html'
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')

    def get_context_data(self, **kwargs):
        """ customize default context
        """
        context = super().get_context_data(**kwargs)
        context['transactions'] = Transaction.objects.filter(
            user__username=self.request.user.username
        )
        return context

    def get_queryset(self):
        """ grabbing all the objects assigned to current user using username
        """
        return Budget.objects.filter(
            user__username=self.request.user.username
        )


class BudgetDetailView(LoginRequiredMixin, DetailView):
    """ View class quering requested budget object for budget detail html
    """
    template_name = 'budgets/budgets_detail.html'
    context_object_name = 'budgets'
    login_url = reverse_lazy('login')
    pk_url_kwarg = 'id'

    def get_queryset(self):
        """ query requested budget object
        """
        return Budget.objects.filter(
            user__username=self.request.user.username
        )
