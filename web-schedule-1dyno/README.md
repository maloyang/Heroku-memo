# Heroku-memo - 使用一個dyno同時可以有web & schedule的服務

## 重點在於執行web服務要另外使用os的comamnd去跑!

- `os.system('gunicorn -w 2 app:app')`
- 本來web的服務是使用 app.run() 來執行… 但web有起來，schedule卻不會動，不知道是怎麼了，明明在log中有看到另一個worker啟動了!

## 這樣就可以省掉一個dyno的費用，只要花一半的錢就可以同時有一個schedule的服務
