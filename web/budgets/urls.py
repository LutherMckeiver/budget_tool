from django.urls import path
from .views import BudgetListView, BudgetDetailView


urlpatterns = [
    path('budget', BudgetListView.as_view(), name='budget_list'),
    path('budget/<int:id>', BudgetDetailView.as_view(), name='budget_detail')
]
