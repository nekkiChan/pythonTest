import os
import subprocess

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

def install_postgresql(extract_folder, db_config):
    # PostgreSQLのbinディレクトリに移動
    bin_dir = os.path.join(extract_folder, "bin")
    os.chdir(bin_dir)
    
    # PostgreSQLのインストール
    os.system(f".\\initdb.exe -U postgres -A trust -E UTF8 -D ..\\data")
    os.system(f".\\pg_ctl.exe register -N postgresql-16.2-1 -U .\\postgres -D ..\\data -w")
    os.system(f".\\pg_ctl.exe start -D ..\\data")
    
    # 新しいユーザーを作成してデータベースの所有者とする
    # createuser_command = ["createuser", "-U", "postgres", "--superuser", "--no-password", db_config["DB_USER"]]
    # createuser_process = subprocess.Popen(createuser_command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    # stdout, stderr = createuser_process.communicate(input=db_config["DB_PASSWORD"].encode())
    # if stderr:
    #     print(stderr.decode())
    #     return
    # createdb_command = ["createdb", "-U", "postgres", "-O", db_config["DB_USER"], db_config["DB_NAME"]]
    # subprocess.run(createdb_command)

    print("PostgreSQL has been installed successfully!")

def initialize_postgresql(extract_folder, db_config):
    # PostgreSQLの初期化
    install_postgresql(extract_folder, db_config)
    # PostgreSQLのデータベース作成とポート番号の変更
    # create_database(extract_folder, db_config)

def create_database(extract_folder, db_config):
    # データベースがすでに存在するか確認
    result = subprocess.run(["psql", "-U", "postgres", "-lqt"], capture_output=True)
    if db_config["DB_NAME"] in result.stdout.decode():
        print(f"Database '{db_config['DB_NAME']}' already exists. Skipping database creation.")
        return
    
    # データベース作成
    subprocess.run(["createdb", "-U", "postgres", db_config["DB_NAME"]])
    print(f"Database '{db_config['DB_NAME']}' has been created successfully.")

def change_port(extract_folder, db_config):
    # postgresql.confファイルを編集してポート番号を変更
    postgresql_conf = os.path.join(extract_folder, "data", "postgresql.conf")
    with open(postgresql_conf, "r") as f:
        conf_lines = f.readlines()
    
    for i, line in enumerate(conf_lines):
        if line.startswith("port = "):
            conf_lines[i] = f"port = {db_config['DB_PORT']}\n"
    
    with open(postgresql_conf, "w") as f:
        f.writelines(conf_lines)
    
    print(f"Port number has been changed to {db_config['DB_PORT']}.")

def init_database():
    # .envファイルからデータベース設定を読み取る
    db_config = {
        "DB_NAME": os.getenv("DB_NAME"),
        "DB_PORT": os.getenv("DB_PORT"),
        "DB_USER": os.getenv("DB_USER"),
        "DB_PASSWORD": os.getenv("DB_PASSWORD")
    }
    
    # 開始ディレクトリを指定
    start_dir = os.getcwd()  # 現在のディレクトリから開始する例
        
    # buildディレクトリを探索
    build_dir = find_build_directory()
        
    if build_dir:
        print("buildディレクトリが見つかりました:", build_dir)
        # 解凍されたフォルダのパスを指定する
        extract_folder = os.path.join(build_dir, "postgresql-16.2-1-windows-x64-binaries\\pgsql\\")
        
        if all(db_config.values()):
            # PostgreSQLの初期化
            initialize_postgresql(extract_folder, db_config)
        else:
            print("DB_NAME、DB_PORT、DB_USER、DB_PASSWORDのいずれかが環境変数に設定されていません。")
    else:
        print("buildディレクトリが見つかりませんでした。")

# init_database()を呼び出して初期化を実行します
# init_database()
