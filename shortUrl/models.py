from django.db import models

# Create your models here.
import requests
import json
import sys
import sqlite3
import traceback
from pprint import pprint
from hashids import Hashids
from datetime import datetime
import socket


from django.shortcuts import redirect
from django.urls import reverse



class ShortUrl(models.Model):
    
    # INPUT 條件
    short_url = models.TextField()
    class Meta:
        db_table = "shortUrl"







def getShortUrl(**kwargs):
    '''
    取得縮網址
    '''
    
    try:
        
        
        # requests json
        url = kwargs.get('url')

        
        # 建立資料庫與連線
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        
        
        
        # 利用當下時間創立
        hashids = Hashids(salt = "random str", alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890")
        myID = hashids.encode(int(datetime.today().timestamp())) 

        
        # insert新的縮網址資料
        sql_insert = ("INSERT INTO shorturl (id,url) VALUES ('{}','{}')").format(myID,url)
        c.execute(sql_insert)
        conn.commit()
        
        
        # 組合成縮網址
        local_ip = socket.gethostbyname(socket.gethostname())
        short_url = "http://" + local_ip + ":8000/shortUrl/get_short_url/" + myID

        
        
        # 組合JSON
        res_json = { 
                    "status":200,
                    "msg":"Success",
                    "url": url,
                    "shorturl": short_url
                    }
        

        return res_json
        


    
    
    
    
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

        print("異常處理訊息")
        #logging.debug(res_json)
        
        return res_json



    
    
    
    
    





def getLongUrl(**kwargs):
    '''
    取得原來網址
    '''
    
    try:
        
        
        # requests json
        url = kwargs.get('url')
        print("輸入的URL : ",url)
        
        # 建立資料庫
        conn = sqlite3.connect('mydatabase.db')
        c = conn.cursor()
        
        
        
        
        # select
        sql_select = ("select id,url from shorturl where id = '{}'").format(url)
        c.execute(sql_select)
        res = c.fetchall()
        res_json = [list(row) for row in res]

        
        # 組合JSON
        res_json = { 
                    "status":200,
                    "msg":"Success",
                    "original_url": res_json[0][1]
                    }
        

        return res_json

    
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
        


