# django_short_url
使用django實現縮網址



## 1. DEMO

[![Django縮網址結果](https://1.bp.blogspot.com/-MjN2vAzBPb4/XsGD-CHepHI/AAAAAAAAHjA/HEx3eXjazcwbKXd138mYJa9gyUl4uTIbgCK4BGAsYHg/url_shortner.png)](https://www.youtube.com/watch?v=FVlnKGUPJMw "Django縮網址結果")




## 2. 說明

使用hashids套件，可以使用時間戳來產生unique id
於是用取得縮網址當下的時間戳來產生unique id
才可確保縮網址不會重複
並將縮網址與原本的網址存於sqlite之中
當使用者在瀏覽器輸入短網址後
會到縮網址伺服器中尋找對應的原來網址
並將使用者重新導向網址

