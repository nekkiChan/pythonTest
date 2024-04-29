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

def install_postgresql(extract_folder, db_user, db_password):
    # PostgreSQLのbinディレクトリに移動
    bin_dir = os.path.join(extract_folder, "bin")
    os.chdir(bin_dir)
    
    # PostgreSQLのインストール
    os.system(f".\\initdb.exe -U postgres -A trust -E UTF8 -D ..\\data")
    os.system(f".\\pg_ctl.exe register -N postgresql-16.2-1 -U .\\postgres -D ..\\data -w")
    os.system(f".\\pg_ctl.exe start -D ..\\data")
    
    # 新しいユーザーを作成してデータベースの所有者とする
    subprocess.run(["createuser", "-U", "postgres", "--superuser", "--no-password", db_user], input=db_password.encode())
    subprocess.run(["createdb", "-U", "postgres", "-O", db_user, "mydatabase"])

    print("PostgreSQL has been installed successfully!")

def initialize_postgresql(extract_folder, db_user, db_password):
    # PostgreSQLの初期化
    install_postgresql(extract_folder, db_user, db_password)
    # PostgreSQLのデータベース作成とポート番号の変更
    create_database(extract_folder)

def create_database(extract_folder):
    # データベースがすでに存在するか確認
    result = subprocess.run(["psql", "-U", "postgres", "-lqt"], capture_output=True)
    if b"mydatabase" in result.stdout:
        print("Database 'mydatabase' already exists. Skipping database creation.")
        return
    
    # データベース作成
    subprocess.run(["createdb", "-U", "postgres", "mydatabase"])
    print("Database 'mydatabase' has been created successfully.")

def change_port(extract_folder):
    # postgresql.confファイルを編集してポート番号を変更
    postgresql_conf = os.path.join(extract_folder, "data", "postgresql.conf")
    with open(postgresql_conf, "r") as f:
        conf_lines = f.readlines()
    
    for i, line in enumerate(conf_lines):
        if line.startswith("port = "):
            conf_lines[i] = "port = 5433\n"  # 5433にポート番号を変更する例
    
    with open(postgresql_conf, "w") as f:
        f.writelines(conf_lines)
    
    print("Port number has been changed to 5433.")

def init_database():
    # 開始ディレクトリを指定
    start_dir = os.getcwd()  # 現在のディレクトリから開始する例
        
    # buildディレクトリを探索
    build_dir = find_build_directory()
        
    if build_dir:
        print("buildディレクトリが見つかりました:", build_dir)
        # 解凍されたフォルダのパスを指定する
        extract_folder = os.path.join(build_dir, "postgresql-16.2-1-windows-x64-binaries\\pgsql\\")
        # .envファイルからDB_USERとDB_PASSWORDを読み取る
        db_user = os.getenv("DB_USER")
        db_password = os.getenv("DB_PASSWORD")
        if db_user and db_password:
            # PostgreSQLの初期化
            initialize_postgresql(extract_folder, db_user, db_password)
        else:
            print("DB_USERとDB_PASSWORDが環境変数に設定されていません。")
    else:
        print("buildディレクトリが見つかりませんでした。")

