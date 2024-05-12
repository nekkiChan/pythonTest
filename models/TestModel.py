# model/test_model.py

import json
import os
import re
import pprint

class TestModel:
    def __init__(self):
        self.name = ""
        self.data_path = os.path.join(os.path.dirname(__file__), 'data', 'data.json')
        self.load_data()
        self.find_code()
        
    def find_code(self):
        
        prescription_text = """
                            31,1112
                            51,20231028
                            101,1,1,,3
                            111,1,1,,１日４回、毎食後・就寝前服用,4
                            201,1,1,1,2,620160301,,4,1,g
                            101,2,2,,10
                            111,2,1,,発熱時服用,
                            201,2,1,1,7,1149019F1ZZZ,【般】ロキソプロフェンＮａ錠６０ｍｇ,1,1,T
                            101,3,1,,10
                            111,3,1,,１日３回、毎食後服用,3
                            201,3,1,1,7,2316020F1ZZZ,【般】ビフィズス菌錠１２ｍｇ,3,1,T
                            """
        variables = {
            "top": 201,
        }       
        tag_dict = {
            4: 'コード',
            6: '毎',
            7: '量',
            8: '単位',
        }
            
        pattern = re.compile(r"{top},(.*?)\n".format(**variables))
        tags = pattern.findall(prescription_text)

        value = []
        for tag in tags:
            value_dict = {}
            tag_array = re.split(',', tag)
            for i, tag_value in enumerate(tag_array):
                if i in tag_dict:
                    value_dict[tag_dict[i]] = tag_value
                    continue
            value.append(value_dict)
        pprint.pprint(value)   
                        
    def find_directory(self, dir_name):
        # 指定されたディレクトリまたはその親ディレクトリにbuildディレクトリがあるか確認
        current_dir = os.getcwd()
        while current_dir:
            dir = os.path.join(current_dir, dir_name)
            if os.path.isdir(dir):
                return dir
            # 親ディレクトリに移動
            current_dir = os.path.dirname(current_dir)
        
        # ルートディレクトリまで探索しても見つからない場合はNoneを返す
        return current_dir
    
    def set_name(self, name):
        self.name = name
        self.save_data()

    def get_greeting(self):
        return f"Hello, {self.name}" if self.name else "Hello!"

    def load_data(self):
        if os.path.exists(self.data_path):
            try:
                with open(self.data_path, 'r') as file:
                    data = json.load(file)
                    if isinstance(data, list):
                        # 既存データがリストの場合、最後の要素を取得
                        self.name = data[-1].get('name', '')
                    else:
                        # 既存データがリストでない場合、新しいリストを作成
                        self.name = data.get('name', '')
            except json.JSONDecodeError:
                print("Error decoding JSON. Using default data.")
        else:
            print("JSON file does not exist. Using default data.")

    def save_data(self):
        # 読み込んだ既存データを取得
        existing_data = []
        if os.path.exists(self.data_path):
            with open(self.data_path, 'r') as file:
                try:
                    existing_data = json.load(file)
                except json.JSONDecodeError:
                    print("Error decoding JSON. Using default data.")

        # 新しいデータを追加
        existing_data.append({'name': self.name})

        # ファイルに保存
        with open(self.data_path, 'w') as file:
            json.dump(existing_data, file, indent=2)
