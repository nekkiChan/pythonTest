import tkinter as tk
from dotenv import load_dotenv

import os

def find_build_directory():
    # 指定されたディレクトリまたはその親ディレクトリにbuildディレクトリがあるか確認
    current_dir = os.getcwd()
    while current_dir:
        build_dir = os.path.join(current_dir, "build")
        if os.path.isdir(build_dir):
            return build_dir
        # 親ディレクトリに移動
        current_dir = os.path.dirname(current_dir)
    
    # ルートディレクトリまで探索しても見つからない場合はNoneを返す
    return None

def install_postgresql(extract_folder):
    # PostgreSQLのbinディレクトリに移動
    bin_dir = os.path.join(extract_folder, "bin")
    os.chdir(bin_dir)
    
    # PostgreSQLのインストール
    os.system(".\\initdb.exe -U postgres -A trust -E UTF8 -D ..\\data")
    os.system(".\\pg_ctl.exe register -N postgresql-16.2-1 -U .\\postgres -D ..\\data -w")
    os.system(".\\pg_ctl.exe start -D ..\\data")
    
    print("PostgreSQL has been installed successfully!")
    

# 開始ディレクトリを指定
start_dir = os.getcwd()  # 現在のディレクトリから開始する例
    
# buildディレクトリを探索
build_dir = find_build_directory()
    
if build_dir:
    print("buildディレクトリが見つかりました:", build_dir)
    # 解凍されたフォルダのパスを指定する
    extract_folder = os.path.join(build_dir, "postgresql-16.2-1-windows-x64-binaries\\pgsql\\")
    # PostgreSQLのインストール
    install_postgresql(extract_folder)
else:
    print("buildディレクトリが見つかりませんでした。")

# .envファイルの内容を読み込見込む
load_dotenv()

from controllers.TestController import TestController

def main():
    root = tk.Tk()
    app = TestController(root)
    root.mainloop()

if __name__ == "__main__":
    main()