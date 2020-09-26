# test-public-textlint-settings
GitHub ActionsがAction in Actionをサポートするまで設定をダウンロードで代用するためのリポジトリのサンプル

名前はtextlintにこだわらずに、paper-lintrulesとかが良さそう

paper.txtがテスト用にありますが、消しても良いかもしれません

リポジトリを作成し直した際に、TODOはissueに移行します。

## 使い方
卒論リポジトリで、`curl -sf https://raw.githubusercontent.com/dbgroup-nagoya-u/test-public-textlint-settings/master/update.bash | bash -s`と打つと、textlint等の設定が更新される。（実際には`template-latex`にこれを実行してくれるファイルがあるはず）

## TODO
- 初回コメントの改善
- そもそもタグを毎回つけないといけないが、これも自動にする
  - github actionsで可能
  - ただし、branch名等の情報からタグをつけるようにしか設定できないので、実質手動と変わらない？
    - issueのresolveみたいな感じでpull requestのコメントに tag #v0.1.1 と書いたら動くようになってほしい
- draftcheckも管理して書き換えたいがライセンスがついていないのでどうすればよいか調べる
- 移行&&完成後、template-latexリポジトリにダウンロードスクリプトを追加
- このリポジトリの削除
- （ただし、あまりこだわりすぎない！）
