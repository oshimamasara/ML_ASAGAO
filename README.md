<img src="https://pythonchannel.com/media/github/Flask-ML-Sample.jpg" width="100%">

git clone https://github.com/oshimamasara/Flask_ML.git

朝顔の成長データ参考　http://www.fuso-bc.jp/23/78/（株式会社 扶桑商会さま）


## ML APP RUN

1. cd Flask_ML
2. virtualenv env
3. source env/bin/activate
4. 確認 pip freeze
5. pip install -r requirements.txt
6. python graph.py
7. python train.py
8. python api.py
9. 別のターミナルで Flask_ML ディレクトリに移動
10. source env/bin/activate
11. python app.py
12. http://127.0.0.1:5111
13. 仮想環境おわり　deactivate

