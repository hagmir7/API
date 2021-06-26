from django.http.response import JsonResponse
from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import *
from .serializers import *
from django.http import JsonResponse


@api_view(['GET'])
def home(request):
    data = []
    posts = Post.objects.all()
    for item in posts:
        data_list = {
            'id': item.id,
            'pk': item.pk,
            'user': f'{item.user.first_name} {item.user.last_name}',
            'name': item.name,
            'image': item.image.url,
            'description': item.description[0:40] + "...",
            'views': item.views.count()
        }
        data.append(data_list)
    return Response({'items':data})


@api_view(['GET'])
def detail(request, id):
    item = Post.objects.get(id=id)

    # get traphic
    x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
    if x_forwarded_for:
        ip = x_forwarded_for.split(',')[0]
    else:
        ip = request.META.get('REMOTE_ADDR')
    if IpAddress.objects.filter(name=ip).exists():
        item.views.add(IpAddress.objects.get(name=ip))
    else:
        IpAddress.objects.create(name=ip)
        item.views.add(IpAddress.objects.get(name=ip))

    data = []
    if request.user.is_authenticated:
        print('Yes')
    else:
        print('No')


    data_list = {
            'id': item.id,
            'pk': item.pk,
            'user': f'{item.user.first_name} {item.user.last_name}',
            'name': item.name,
            'image': item.image.url,
            'description': item.description,
            'views': item.views.count(),
            'data': item.data.strftime('%d-%m-%Y / %H:%M'),
    }
    print(item.views.count())
    data.append(data_list)
    return Response({'list':data})
