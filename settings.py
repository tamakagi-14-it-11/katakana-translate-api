import os
import sys
from dotenv import load_dotenv

load_dotenv()

# 必須の環境変数のリスト
required_vars = [
	"OPENAI_API_KEY",
	"MODEL",
	"TEMPERATURE",
	"SYSTEM_PROMPT",
	"LOG_PATH",
	"DICT_PATH",
	"DICT_PATH_AUTO",
	"PORT",
]

# 環境変数が設定されているか確認
missing_vars = []
for var in required_vars:
	if os.getenv(var) is None:
		missing_vars.append(var)

# 不足している環境変数がある場合はエラーメッセージを表示して終了
if missing_vars:
	print(f"エラー: 以下の必須環境変数が設定されていません: {', '.join(missing_vars)}")
	print("環境変数を.envファイルに設定するか、システム環境変数として設定してください。")
	sys.exit(1)

OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
MODEL = os.getenv("MODEL")
TEMPERATURE = float(os.getenv("TEMPERATURE"))
SYSTEM_PROMPT = os.getenv("SYSTEM_PROMPT")
LOG_PATH = os.getenv("LOG_PATH")
DICT_PATH = os.getenv("DICT_PATH")
DICT_PATH_AUTO = os.getenv("DICT_PATH_AUTO")
PORT = int(os.getenv("PORT"))

# print(f"設定が読み込まれました: {OPENAI_API_KEY}, {MODEL}, {TEMPERATURE}, {SYSTEM_PROMPT}, {LOG_PATH}")
