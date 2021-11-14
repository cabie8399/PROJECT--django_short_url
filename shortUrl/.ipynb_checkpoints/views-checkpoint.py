from django.shortcuts import render
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import viewsets, status
from django.http import HttpResponse
from drf_yasg.utils import swagger_auto_schema
from django.shortcuts import redirect
from django.urls import reverse


import json
from pprint import pprint
import logging
import sqlite3

# 取得縮網址
from shortUrl.models import getShortUrl
from shortUrl.serializers import ShortUrlSerializer


# 取得原來網址
from shortUrl.models import getLongUrl





class ShortUrlViewset(viewsets.ViewSet):
    
    
    @swagger_auto_schema(
        operation_summary='取得縮網址',
        request_body=ShortUrlSerializer,
       
    )
    @action(detail=False,methods=['post'],url_path='get_short_url')
    def short_url(self, request):
        '''
        # INPUT



        ```json
        {    
          "url":"http://www.google.com"   
        }
        ```



        # OUTPUT



        ```json
        {
          "status": 200,
          "msg": "Success",
          "url": "http://www.google.com",
          "shorturl": "http://192.168.50.106:8000/shortUrl/get_short_url/MDOOM6ZO"
        }
        ```
        

        '''
        
        url = request.data.get('url')
        
        
        
        res = getShortUrl(url=url)
        
        return Response(res, status=status.HTTP_200_OK)



    
    
    
    
    
    
    



    @swagger_auto_schema(
        operation_summary='導向原網址'
    )
    @action(detail=False,methods=['get'],url_path='get_short_url/(\w+)')
    def original_url(self, request,url):

        try:
        
            # 建立資料庫
            conn = sqlite3.connect('mydatabase.db')
            c = conn.cursor()


            # select
            sql_select = ("select id,url from shorturl where id = '{}'").format(url)
            c.execute(sql_select)
            res = c.fetchall()
            res_json = [list(row) for row in res]

            return redirect(res_json[0][1])


        except Exception as e:
        
            error_class = e.__class__.__name__ #取得錯誤類型
            detail = e.args[0] #取得詳細內容
            cl, exc, tb = sys.exc_info() #取得Call Stack
            lastCallStack = traceback.extract_tb(tb)[-1] #取得Call Stack的最後一筆資料
            fileName = lastCallStack[0] #取得發生的檔案名稱
            lineNum = lastCallStack[1] #取得發生的行號
            funcName = lastCallStack[2] #取得發生的函數名稱

            res_json = {  
                        "debug":str(lineNum)+"L,filename:"+fileName+","+str(detail),
                        "status":500,
                        "detail":str(e),
                        "msg":"failed"
                        }

            return res_json








