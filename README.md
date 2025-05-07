# titanic-survival-app
Titanic 存活預測應用程式範例([參考文件](https://www.kaggle.com/competitions/titanic))。

將訓練好的 Titanic 存活預測訓練模型製作成網頁應用程式。

# 測試環境設定
1. [建議] 先建立虛擬環境
2. 在虛擬環境中安裝需要的套件

   `pip install --no-cache -r requirements.txt`

# 測試本機應用程式
1. 執行 app.py

   `python app.py`

2. 開啟瀏覽器並前往 [http://127.0.0.1:8080](http://127.0.0.1:8080)

3. 結束執行

    `Ctrl + c`

# 測試 Docker 應用程式
1. 以 Dockerfile 建立映像檔

   `docker image build -t titanic:latest .`
2. 建立容器

   `docker container run -d --name titanic -p 8080:8080 titanic:latest`

3. 開啟瀏覽器並前往 [http://127.0.0.1:8080](http://127.0.0.1:8080)

# 練習
1. 將此應用程式部署到 Azure Virtual Machine。
2. 將此應用程式部署到 Azure Contrainer Instance。
3. 將此應用程式部署到 Azure Function 。

# 更新模型
1. 修改並執行 train_model.py

   `python train_model.py`