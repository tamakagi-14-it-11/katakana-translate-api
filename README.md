# katakana-translate-api

[katakana-translate](https://github.com/tamakagi-14-it-11/katakana-translate)のためののAI翻訳用APIサーバー

## 必要なアプリケーション

- [Git](https://git-scm.com/) (コードのダウンロードのみに使用)
- [Python](https://www.python.org/downloads/) (Python 3.12.9で動作確認済み)

## ChatGPTについて

OpenAIのAPIからChatGPTを使用しているため、OpenAIのAPI keyが必要です。

## セットアップ手順

### 1. リポジトリのクローン

```bash
git clone https://github.com/tamakagi-14-it-11/katakana-translate-api.git
cd katakana-translate-api
```

### 2. 仮想環境の作成

```bash
python -m venv venv
```

### 3. 仮想環境の有効化

OSによってコマンドが違います。

- **Windows (PowerShell)**

```powershell
venv\Scripts\Activate.ps1
```

- **Windows (cmd)**

```cmd
venv\Scripts\activate
```

- **Linux**

```bash
source venv/bin/activate
```

### 4. 必要なモジュールのインストール

```bash
pip install -r requirements.txt
```

### 5. 環境変数の設定

`.env.example` を元に `.env` ファイルを作成し、必要な値を設定してください。

```bash
cp .env.example .env
```

`.env` 内の各値を適切に設定してください。

> [!WARNING]
> 必ず `OPENAI_API_KEY` にOpenAIのAPI keyを入力してください。

### 6. プログラムの実行

```bash
python main.py
```

### 7. APIサーバーの起動確認

任意のブラウザまたは[curl](https://github.com/curl/curl)でAPIのURL(例: `http://127.0.0.1:5000/` )にアクセスし、 `Flask app is running!` と表示されたら成功

## 注意事項

- プログラムの実行やモジュールのインストールは、仮想環境を有効化した後に行ってください。
- モジュールを追加でインストールしたら、その後必ず以下のコマンドを実行し、 `requirements.txt` を更新してください。

```bash
pip freeze > requirements.txt
```
