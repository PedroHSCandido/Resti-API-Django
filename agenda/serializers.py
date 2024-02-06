from rest_framework import serializers

"""Um serializer é uma classe que converte dados complexos, como objetos Python, em tipos de dados que podem ser 
facilmente renderizados em JSON, XML, ou outros formatos, e vice-versa"""

class AgendamentoSerializer(serializers.Serializer):
    data_horario = serializers.DateTimeField()
    nome_cliente = serializers.CharField(max_length = 200)
    email_cliente = serializers.EmailField()
    telefone_cliente = serializers.CharField(max_length = 20)