# django_short_url
使用django實現縮網址



## 1. DEMO


DEMO影片 : [Youtube Demo影片](https://www.youtube.com/watch?v=FVlnKGUPJMw)<br>
[![Django縮網址結果](https://1.bp.blogspot.com/-MjN2vAzBPb4/XsGD-CHepHI/AAAAAAAAHjA/HEx3eXjazcwbKXd138mYJa9gyUl4uTIbgCK4BGAsYHg/url_shortner.png)](https://www.youtube.com/watch?v=FVlnKGUPJMw "Django縮網址結果")




## 2. 說明

使用hashids套件，可以使用時間戳來產生unique id<br>
於是用取得縮網址當下的時間戳來產生unique id<br>
才可確保縮網址不會重複<br>
並將縮網址與原本的網址存於sqlite之中<br>
當使用者在瀏覽器輸入短網址後<br>
會到縮網址伺服器中尋找對應的原來網址<br>
並將使用者重新導向網址<br>



## 3. 部署

使用docker部署

### 1. 安裝docker最新版本

### 2. 建立docker images

確認當前路徑在專案底下(要有Dockerfile那層)

```
[cabie@centosclean shorturl]$ docker build -t shorturl .
```

### 3. 確認images建立

```
[cabie@centosclean shorturl]$ sudo docker images
REPOSITORY                                                          TAG                 IMAGE ID            CREATED             SIZE
shorturl                                                            latest              bb25271c73f1        11 minutes ago      260MB
```


### 4. run container

```
[cabie@centosclean shorturl]$ sudo docker run -it -d -p 8000:8000 --name=django-shorturl shorturl:latest python /django/manage.py runserver 0.0.0.0:8000
f062d95c8a0136bcc274550db8465bd95314da53b54795b204310a48fa02795a
```

```
[cabie@centosclean shorturl]$ sudo docker ps
[sudo] password for cabie: 
CONTAINER ID        IMAGE               COMMAND                  CREATED             STATUS              PORTS                    NAMES
f062d95c8a01        shorturl:latest     "python /django/mana…"   5 minutes ago       Up 5 minutes        0.0.0.0:8000->8000/tcp   django-shorturl
```


### 5. 開啟瀏覽器

開啟瀏覽器輸入 http://{你的伺服器ip}:8000/docs<br>
eg: http://192.168.50.106:8000/docs/<br>

![](https://imgbox.com/Pl3oSmJr)








