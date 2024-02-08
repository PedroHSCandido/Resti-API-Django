from django.urls import path
from agenda.views import AgendamentoDetail, AgendamentoList 

app_name = 'agenda'
urlpatterns = [
    path('agendamentos', AgendamentoList.as_view),
    path('agendamentos/<int:pk>/', AgendamentoDetail.as_view)

]