# django_short_url
使用django實現縮網址



## 1. DEMO


<iframe width="560" height="315" src="https://www.youtube.com/embed/FVlnKGUPJMw" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture" allowfullscreen></iframe>



## 2. 說明

使用hashids套件，可以使用時間戳來產生unique id
於是用取得縮網址當下的時間戳來產生unique id
才可確保縮網址不會重複
並將縮網址與原本的網址存於sqlite之中
當使用者在瀏覽器輸入短網址後
會到縮網址伺服器中尋找對應的原來網址
並將使用者重新導向網址

