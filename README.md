# Heroku-memo

## 好文記錄

- [用 Heroku 部署網站 from djangogirlstaipei](http://djangogirlstaipei.herokuapp.com/tutorials/deploy-to-heroku/?os=windows)


## 基本操作 - 建立一個新的APP

可以參考[這邊](https://devcenter.heroku.com/articles/creating-apps)

- 如果你已有一個現成的專案：(基本組成為app.py , Procfile , requirements.txt)
  - 先在指令列進到專案資料夾用 `git init` 建立git的基本檔案
  - 再下指令 `git add .` 把資料夾中的所有檔案加入
  - 喔! 因為我的git這電腦上剛裝好，所以git它會提醒你要先做git的基本config，因此只要下
  `git config --global user.email "you@example.com"` 和 `git config --global user.name "Your Name"`
  這樣就可以了，其中email, "Your Name"的部份要填你自己的mail, name...
  - 再下一次 `git add .` 就正常了
  - 下指令 `heroku apps:create my-webapi` 可以建立app (這邊要注意名稱可以用"-"，但是不能使用"_")
  ```
  Creating ⬢ my-webapi... done
  https://my-webapi.herokuapp.com/ | https://git.heroku.com/my-webapi.git
  ```
  - 下指令 `git commit -am "first version"` 把所有東西加入要上傳的差異清單，並加入註解
  - 下指令 `git push heroku master` 就可以把專案app發佈了，過程如下
```
Enumerating objects: 5, done.
Counting objects: 100% (5/5), done.
Delta compression using up to 4 threads
Compressing objects: 100% (3/3), done.
Writing objects: 100% (5/5), 988 bytes | 494.00 KiB/s, done.
Total 5 (delta 0), reused 0 (delta 0)
remote: Compressing source files... done.
remote: Building source:
remote:
remote: -----> Python app detected
remote: -----> Installing python-3.6.7
remote: -----> Installing pip
remote: -----> Installing SQLite3
remote: -----> Installing requirements with pip

.......

remote: -----> Discovering process types
remote:        Procfile declares types -> web
remote:
remote: -----> Compressing...
remote:        Done: 44.8M
remote: -----> Launching...
remote:        Released v3
remote:        https://my-webapi.herokuapp.com/ deployed to Heroku
remote:
remote: Verifying deploy... done.
To https://git.heroku.com/my-webapi.git
 * [new branch]      master -> master
```

----

## 如果換一台電腦要進行剛剛的專案，但電腦是沒有存在此專案

- 先安裝git
  - 一樣要像前面下指令：`git config --global user.email "you@example.com"` 和 `git config --global user.name "Your Name"`+
  
  
- 再安裝heroku tool belt
- 登入Heroku
  - `heroku login`


- 把專案clone回來
  - `heroku git:clone -a mk-digital-service`


- 程式編輯好後，再使用以下指令就可以再push回傳
```
$ git add .
$ git commit -am "make it better"
$ git push heroku master
```
