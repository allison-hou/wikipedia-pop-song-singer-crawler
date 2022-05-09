# 這是一個維基百科歌星的爬蟲專案


## 前言與動機
我想要學習如何用Python寫爬蟲，並應用到活中的場景。
此專案我決定設計一隻爬蟲程式，將我喜歡的歌手的維基資料爬下來!


## 功能介紹
只要輸入歌手的網址，維基百科歌星爬蟲就可以將出現在維基百科的歌手資料自動爬下來，存在一個 Python Dict 裡面，之後可以再用程式存成任何格式。


以下是這隻爬蟲會爬取的歌手資訊：照片、名字、生日、年齡、出生地、唱歌的類型。

## 如何使用
Step1. 先指定歌手 


```python
WIKI_URL = 'https://en.wikipedia.org/wiki/Ruel_(singer)'
```

Step2.  開啟Command line


Step3. 執行以下指令: `python crawler.py`


## 成果


以下是我的成果展現:

### 1.照片

![](Ruel.jpg)

### 2.爬下來的資料(姓名、照片的連結、生日、出生地、歌曲類型)

![](pic.jpg)

