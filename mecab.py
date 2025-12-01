import MeCab

tagger = MeCab.Tagger()

def tokenize_with_pos(text):
	nodes = tagger.parseToNode(text)
	tokens = []
	while nodes:
		if nodes.surface:
			tokens.append((nodes.surface, nodes.feature.split(",")[0]))
		nodes = nodes.next
	return tokens

def filter_pos(tokens, pos_list):
	return [token for token, pos in tokens if pos in pos_list]

# このファイルを直接実行した場合のみ実行
if __name__ == "__main__":
	text = input("Enter text: ")
	tokens_with_pos = tokenize_with_pos(text)
	nouns = filter_pos(tokens_with_pos, ["名詞"])
	print(nouns) # 名詞のみ出力
	# print(tagger.parse(text)) # 形態素解析結果を出力
