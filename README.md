# openai-api-manga

環境
・Python3.8
・arm64

1.Pythonの仮想環境作成
python -m venv ~/venv/openai-api-manga
source ~/venv/openai-api-manga

2.必要なライブラリのインストール
#openaiライブラリをインストール
pip install openai

#requestsライブラリのインストール
pip install requests

3.OpenAIのAPI有効化
#openaiのAPIキーを設定
(openai-img-gene)export OPENAI_API_KEY='your_api_key_here'

4.（必要に応じて）image-vision-gene-manga.pyの内容変更
・n_pagesにページ数を指定
・world_buildingに漫画の設定を記載
・promptを変更

5.image-vision-gene-manga.pyの実行
#実行
python image-vision-gene-manga.py
