from django.http import JsonResponse
from django.shortcuts import get_object_or_404
from rest_framework.decorators import api_view
from rest_framework.response import Response

from agenda.models import Agendamento
from agenda.serializers import AgendamentoSerializer

# Create your views here.

@api_view(http_method_names=["GET", "PUT", "DELETE"])
def agendamento_detail(request, id):
    obj = get_object_or_404(Agendamento, id=id)
    if request.method== "GET": #Verifica se foi feita uma requisição GET ou POST
        serializer = AgendamentoSerializer(obj)
        return JsonResponse(serializer.data)
    
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
    
    if request.method == "PACTH":#EDITA O OBJETO PARCIALMENTE
        serializer = AgendamentoSerializer(obj, data = request.data, partial=True)
        if serializer.is_valid(): #valida os dados
            serializer.save
            return JsonResponse(serializer.data, status=200)
        return JsonResponse(status=400)#Apresenta o erro e o codigo 400
    
    if request.method== "DELETE":
        obj.evento_cancelado = True
        return Response(status=204)

@api_view(http_method_names=["GET", "POST"])
def agendamento_list(request):
    if request.method== "GET": #Verifica se foi feita uma requisição GET ou POST
        qs = Agendamento.objects.filter(evento_cancelado=False) #Armazena os agendamentos na qs com o agendamento cancelado seja false
        serializer = AgendamentoSerializer(qs, many= True) #Serializa os objetos presentes na QS
        return JsonResponse(serializer.data, safe=False) #Retorna os objetos em formato JSON

    if request.method == "POST": #Verifica se foi feita uma requisição GET ou POST 
        data = request.data #Pega os dados enviados pelo usuario
        serializer = AgendamentoSerializer(data=data) #serializa a data
        if serializer.is_valid(): #valida os dados
            serializer.save()
            return JsonResponse(serializer.data, status=201)#Rentorna o objeto criado e serializado com o status 201
        return JsonResponse(status=400)#Apresenta o erro e o codigo 400
    