import os
import csv
from datetime import datetime
import settings

log_path = settings.LOG_PATH

# 初回ならヘッダ行を作成
if not os.path.exists(log_path):
	with open(log_path, mode='w', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow(["DateTime", "Text"])

now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

def writeLog(text):
	with open(log_path, mode='a', newline='', encoding='utf-8') as f:
		writer = csv.writer(f)
		writer.writerow([now, text])
