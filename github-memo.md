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

