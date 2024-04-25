# メモ

## 環境変数設定について

以下のコマンドを実施し、.envファイルを生成

``
pip install python-dotenv
``

[参考](https://zenn.dev/nakashi94/articles/9c93b6a58acdb4)

## exe化にあたって

以下のコマンドを実施

``
git clone https://github.com/pyinstaller/pyinstaller.git
cd pyinstaller/bootloader
python ./waf distclean all
pip install wheel
cd pyinstaller
pip install .
pyinstaller main.py --onefile --noconsole
``

## postgresqlについて

以下のコマンドを実施

``
pip install psycopg2
``

[参考](https://asameshicode.com/python-psycopg2/)
