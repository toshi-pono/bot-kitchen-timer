# bot-kitchen-timer

キッチンタイマー BOT for traQ．[AiotraQ](https://github.com/toshi-pono/aiotraq) を使ったサンプル Bot です．

## デプロイ方法 for Neoshowcase

### 1. requirements.lock から requirements.txt を生成

```bash
make generate
```

### 2. デプロイ

環境変数を設定する

- `BOT_ACCESS_TOKEN`: Bot のアクセストークン
- `BOT_VERIFICATION_TOKEN`: Bot の検証トークン
- `PYTHONPATH`: `src`ディレクトリのパス(たぶん`/workspace/ns-repo/src`)を追加

URL は `https://{{好きなURL}} -> 8080/TCP` に設定する

実行するコマンドは Procfile で指定する
