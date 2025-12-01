import settings
from openai import OpenAI

client = OpenAI(
	api_key=settings.OPENAI_API_KEY,
)

def generate_response(model:str, temperature:float, systemPrompt:str, prompt:str) -> str:
	try:
		completion = client.chat.completions.create(
			model=model,
			temperature=temperature,
			messages=[
				{"role": "system", "content": systemPrompt},
				{"role": "user", "content": prompt},
			],
		)
		return completion.choices[0].message.content
	except Exception as e:
		return f"An error occurred: {str(e)}"

def changeKatakana(text:str) -> str:
	return generate_response(settings.MODEL, settings.TEMPERATURE, settings.SYSTEM_PROMPT, text)

if __name__ == "__main__":
	text = "アジェンダをコンセンサスして、フィードバックをリマインド。プロアクティブにコミットメントをマネジメントし、プロジェクトのスキームをブラッシュアップ。リスクマネジメントもスムーズにオペレーションし、クオリティのアセスメントをエビデンスベースでレビューする。"
	response = changeKatakana(text)
	print(response)
