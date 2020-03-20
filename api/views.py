# -*- coding: utf-8 -*-
from __future__ import unicode_literals

# import Responses
from httplib2 import Response
# from rest_framework.decorators import api_view
from rest_framework.decorators import api_view
from rest_framework.response import Response
from api.ethereum import ethereum
instance=ethereum()
# Create your views here.
@api_view(['GET', 'POST'])
def getAccount(request):
    phase=request.data['phrase'];
    address=instance.getAccount(phase)

    if request.method == 'POST':
        return Response({"status": 2000, "account": address})
    return Response({"message": "oppps something went wrong try to contact admin"})
@api_view(['GET', 'POST'])
def getAccountList(request):

    list=instance.getAccountList()

    if request.method == 'GET':
        return Response({"status": 2000, "accountList": list})
    return Response({"message": "oppps something went wrong try to contact admin"})