import os

# プロジェクトの相対パス
base_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

def sqlite_db():
    return os.path.join(base_path, "dialy.db")

class AppColor:
    def base():
        return "rgba(239,237,218,1)"
    
    def accent():
        return "rgba(147,129,118,1)"
    
    def sub():
        return "rgba(182,200,155)"