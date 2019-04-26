# github memo.

### clone exist github "private" repo with username, password
可以使用https的方式去提供username, password

- `git clone https://maloyang:mygithubpassword@github.com/maloyang/project.git`

### clone exist github "public" repo
- `git clone https://github.com/maloyang/project.git`


### push
以一個新專案開始為例：

- `git init` 
- `git add .`
- `git status` 看狀態
- `git commit -m "new solar"` 放入本地端的git repo中
- `git remote add origin https://github.com/maloyang/eg00020.git` 設定遠端的repo專案
- `git push -u origin master` 推送出去


若有修改要上傳
- `git commit -m "test"`
- `git push -u origin master` 再次推送出去

### pull
若使一台電腦已有clone過，想要follow上目前的新進度

- `git pull` 就可以了
- 但如果pull不過來(也許你已有動過部份東西了)，我們又只是想全部pull進來，用 `git reset --hard HEAD`


----
## 重新測試private的github repo

- 在github新增一個private repo.
- 下指令 `git clone https://github.com/maloyang/xxxxxx` 下載repo.資料
- `git add .` 加入所有的東西
- `git commit -m "new web"` 對這次的變更加commit
- 推到github上 `git push origin master`
- 到這邊就搞定了!!

### 到GCP上想要把剛剛在電腦上寫好的並上傳github的網頁，下載到GCP中
- 下 `git clone https://github.com/maloyang/xxxxxx` 因為GCP上還沒有輸入github的帳密，所以它會問你
```
Cloning into 'xxxxxx'...
Username for 'https://github.com': xxxxxx@gmail.com
Password for 'https://xxxxxx@gmail.com@github.com': 
remote: Enumerating objects: 214, done.
remote: Counting objects: 100% (214/214), done.
remote: Compressing objects: 100% (193/193), done.
remote: Total 214 (delta 14), reused 211 (delta 14), pack-reused 0
Receiving objects: 100% (214/214), 1.72 MiB | 9.06 MiB/s, done.
Resolving deltas: 100% (14/14), done.
```
- 這樣就可以很容易同步了
