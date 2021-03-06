# paper-lintrules
paper-lintrulesはtextlint等の校正ツールを組み合わせて論文執筆をサポートするツールです。

（GitHub ActionsがAction in Actionをサポートするまで設定をダウンロードで代用するためのリポジトリです。）

## 使い方
自分の論文リポジトリの一番上の階層で、
``` bash
$ curl -sSf https://raw.githubusercontent.com/dbgroup-nagoya-u/paper-lintrules/main/update.bash | bash
```
を実行すると設定ファイルがダウンロードされます。
ダウンロードした設定ファイルを全てcommitし、Pull Requestを作成すると校正ツールが起動します。

### 注意事項
厳しい指摘がたくさん行われるので、コメント数が増えてページが重くなる場合があります。
ページが重い場合はPull Requestを一旦Closeして、同じブランチをもとに別のPull Requestを作成してください。
同様の理由で、Reviewerに添削をお願いする前に別のPull Requestを作成してください。

## ルールのバグ報告
- 論文執筆時に明らかにおかしいルールを発見した
- 指摘されていないが、プログラムで発見可能な新しいルールを考えた

場合は、今後のために例文を書いて[ここから](https://github.com/dbgroup-nagoya-u/paper-lintrules/issues/new?assignees=&labels=bug&template=bug-report.md&title=)報告をしてください。
