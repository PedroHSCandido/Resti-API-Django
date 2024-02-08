from ast import Return
import imp
from django.http import JsonResponse
from django.shortcuts import get_object_or_404

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import mixins
from rest_framework import generics
from agenda import serializers

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

# Create your views here.

class AgendamentoDetail(
    mixins.RetrieveModelMixin, #detalhar objeto
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    generics.GenericAPIView
):
    queryset = Agendamento.objects.all()

    def get(self,request, *args, **kwargs):
        return self.retrieve(request, args, kwargs)
    
    def patch(self,request, *args, **kwargs):
        return self.update(request, args, kwargs)
    
    def delete(self,request, *args, **kwargs):
        return self.destroy(request, args, kwargs)
    '''   if request.method == "PUT": #SO EDITA TODOS OS DADOS
        obj = get_object_or_404(Agendamento, id=id)
        serializer = AgendamentoSerializer(data = request.data)
        if serializer.is_valid(): #valida os dados
            validated_data = serializer.validated_data
            obj.nome_cliente = validated_data.get("nome_cliente", obj.nome_cliente)
            obj.email_cliente = validated_data.get("email_cliente", obj.email_cliente)
            obj.telefone_cliente = validated_data.get("data_horario", obj.telefone_cliente) 
            obj.save
            return JsonResponse(serializer.data, status=200)'''

class AgendamentoList(
    mixins.ListModelMixin,
    mixins.CreateModelMixin,
    generics.GenericAPIView,
):
    queryset = Agendamento.objects.all()
    serializer_class = AgendamentoSerializer
    def get(self, request, *args, **kwargs):
        return self.list(request, *args, **kwargs)#Listagem de modelo precisando ser mostrado quem e o modelo e qual o serializer
        '''request.method== "GET": #Verifica se foi feita uma requisição GET ou POST
        qs = Agendamento.objects.filter(evento_cancelado=False) #Armazena os agendamentos na qs com o agendamento cancelado seja false
        serializer = AgendamentoSerializer(qs, many= True) #Serializa os objetos presentes na QS
        return JsonResponse(serializer.data, safe=False) #Retorna os objetos em formato JSON'''
    
    def post(self, request, *args, **kwargs):
        return self.create(request, *args, **kwargs)
        '''data = request.data #Pega os dados enviados pelo usuario
        serializer = AgendamentoSerializer(data=data) #serializa a data
        if serializer.is_valid(): #valida os dados
            serializer.save()
            return JsonResponse(serializer.data, status=201)#Rentorna o objeto criado e serializado com o status 201
        return JsonResponse(status=400)#Apresenta o erro e o codigo 400 '''

     