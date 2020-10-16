# Semantic-analysis-Pytorch

這是一款使用者能夠對隨機品牌進行評論的Web App，在評論時使用者能夠即時看到其輸入的情感分數，並提出1到5的評分。使用者若認為評分不對也能夠更改評分並進行提交。

為了建造這個Web App，必須遵循以下步驟:
- 蒐集資料以及使用者評論使用`Selenium` 和 `Scrapy`
- 使用`PyTorch`對這些資料進行深度訓練
- 建造Web App使用`Dash`
- 後端使用`Flask`資料庫使用`Postgres`
- 將app使用`Docker Compose`放入Docker
