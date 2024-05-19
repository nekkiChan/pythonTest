import tkinter as tk
import os 
from dotenv import load_dotenv

# .envファイルの内容を読み込見込む
load_dotenv()

from controllers.TestController import TestController

def main():
    root = tk.Tk()
    app = TestController(root)
    # ウィンドウの初期サイズを設定
    # アイコンファイルのフルパスを解決
    script_dir = os.path.dirname(os.path.abspath(__file__))
    icon_path = os.path.join(script_dir, 'image', 'asset', 'icon.ico')

    # デバッグ用出力：パスと存在確認
    print(f"スクリプトのディレクトリ: {script_dir}")
    print(f"アイコンのパス: {icon_path}")
    print(f"アイコンが存在するか: {os.path.isfile(icon_path)}")

    # アイコンファイルが存在するか確認して設定
    if os.path.isfile(icon_path):
        root.iconbitmap(icon_path)
    else:
        print(f"アイコンファイルが見つかりません: {icon_path}")
    root.mainloop()

if __name__ == "__main__":
    main()