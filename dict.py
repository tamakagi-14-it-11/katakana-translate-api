import os
import csv
import settings

dict_path = settings.DICT_PATH
dict_path_auto = settings.DICT_PATH_AUTO

def csv_to_dict(csv_file_paths: list) -> dict:
	"""複数のCSVファイルを読み込み、辞書に変換する関数"""
	result_dict = {}
	try:
		for csv_file_path in csv_file_paths:
			if not os.path.exists(csv_file_path):
				print(f"Skipping non-existent file: {csv_file_path}")
				continue
			with open(csv_file_path, 'r', encoding='utf-8') as file:
				csv_reader = csv.reader(file)
				next(csv_reader) # ヘッダー行をスキップ
				for row in csv_reader:
					if len(row) >= 2: # 少なくとも2列あることを確認
						key = row[0]
						value = row[1]
						result_dict[key] = value
					else:
						print(f"Skipping row with insufficient columns: {row}")
						continue
		return result_dict
	except Exception as e:
		print(f"エラーが発生しました: {e}")
		return {}

dictionary = csv_to_dict([dict_path_auto, dict_path])

def add_word_to_autoDict(csv_file_path:str, word: str, paraphrase: str) -> None:
	"""辞書に単語とその言い換えを追加する関数"""
	try:
		if not os.path.exists(csv_file_path):
			# ファイルが存在しない場合は新規作成
			os.makedirs(os.path.dirname(csv_file_path), exist_ok=True)
			with open(csv_file_path, 'w', encoding='utf-8', newline='') as file:
				csv_writer = csv.writer(file)
				# ヘッダー行を追加
				csv_writer.writerow(["Word", "Paraphrase"])
			print(f"Created new file: {csv_file_path}")
		with open(csv_file_path, 'a', encoding='utf-8', newline='') as file:
			csv_writer = csv.writer(file)
			csv_writer.writerow([word, paraphrase])
	except Exception as e:
		print(f"エラーが発生しましたa: {e}")

def add_word(word: str, paraphrase: str) -> None:
	"""辞書に項目を追加する関数"""
	if word and paraphrase:
		dictionary[word] = paraphrase
		# 辞書に追加した内容をCSVファイルに保存
		add_word_to_autoDict(dict_path_auto, word, paraphrase)
		print(f"Added '{word}' with paraphrase '{paraphrase}' to the dictionary.")
	else:
		print("Please provide both the word and its paraphrase.")

if __name__ == "__main__":
	print("辞書の内容:")
	for key, value in dictionary.items():
		print(f"{key}: {value}")
	# add_word_to_autoDict(dict_path_auto, "テスト", "試験")
