from flask import Flask, request, jsonify
from flask_cors import CORS
from waitress import serve
import settings
import dict
import mecab
import openai_api

def changeKatakana(text: str) -> str:
	if text == "":
		# 空文字の場合はそのまま返す
		return text
	elif text in dict.dictionary:
		# 辞書に存在する場合は辞書の値を返す
		return dict.dictionary[text].split("//")[0]
	else:
		# 辞書に存在しない場合はOpenAI APIを呼び出してカタカナ変換を行う
		result = openai_api.changeKatakana(text)
		if result == "":
			print("OpenAI API returned an empty response.")
			return text
		else:
			# 辞書に追加
			dict.add_word(text, result)
			return result

def translate(text:str) -> str:
	token = mecab.tokenize_with_pos(text)
	result = ""
	for i in range(len(token)):
		if token[i][1] == "名詞":
			token[i] = (changeKatakana(token[i][0]), token[i][1])
		result += token[i][0]
	return result

def translate2(text:str) -> list:
	token = mecab.tokenize_with_pos(text)
	result = []
	for i in range(len(token)):
		if token[i][1] == "名詞":
			changed_text = changeKatakana(token[i][0])
			if token[i][0] == changed_text:
				result.append({
					"text": token[i][0],
					"type": "original",
					"pos": token[i][1],
				})
			else:
				result.append({
					"text": changed_text,
					"type": "changed",
					"original": token[i][0],
					"pos": token[i][1],
				})
		else:
			result.append({
				"text": token[i][0],
				"type": "original",
				"pos": token[i][1],
			})
	return result

# Flaskアプリケーションのインスタンスを作成
app = Flask(__name__)

# 特定のWebサイトからのリクエストを許可
CORS(app, resources={
	r"/*": {"origins": [
		"http://localhost:5500",
		"https://tamakagi-14-it-11.github.io",
	]}
})

@app.route('/', methods=['GET'])
def index():
	"""動作確認用"""
	return "Flask app is running!"

@app.route('/api/', methods=['POST'])
def api():
	"""カタカナ変換API"""
	data = request.json
	# データが存在し、'text'キーが含まれているか確認
	if not data or 'text' not in data:
		response = {
			'status': 'error',
			'message': 'Invalid input',
		}
		return jsonify(response), 400

	text = data['text']
	processed_text = translate(text)
	response = {
		'status': 'success',
		'data': processed_text,
	}
	return jsonify(response)

@app.route('/api2/', methods=['POST'])
def api2():
	"""カタカナ変換API2"""
	data = request.json
	# データが存在し、'text'キーが含まれているか確認
	if not data or 'text' not in data:
		response = {
			'status': 'error',
			'message': 'Invalid input',
		}
		return jsonify(response), 400

	text = data['text']
	processed_text = translate2(text)
	response = {
		'status': 'success',
		'data': processed_text,
	}
	return jsonify(response)

if __name__ == '__main__':
	# app.run(port=settings.PORT, debug=True)
	serve(app, port=settings.PORT)

# if __name__ == "__main__":
# 	text = "アジェンダをコンセンサスして、フィードバックをリマインド。プロアクティブにコミットメントをマネジメントし、プロジェクトのスキームをブラッシュアップ。リスクマネジメントもスムーズにオペレーションし、クオリティのアセスメントをエビデンスベースでレビューする。"
# 	response = openai_api.changeKatakana(text)
# 	print(response)
