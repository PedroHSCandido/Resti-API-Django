from django.urls import path
from agenda.views import agendamento_detail, agendamento_list


urlspatterns = [
    path('agendamentos', agendamento_list),
    path('agendamentos/<init:id>/', agendamento_detail)

]