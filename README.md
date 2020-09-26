# test desu.
GitHub ActionsがAction in Actionをサポートするまで設定をダウンロードで代用するためのレポジトリのサンプル

名前はtextlintにこだわらずに、paper-lintrulesとかが良さそう

paper.txtがテスト用にありますが、消しても良いかもしれません

リポジトリを作成し直した際に、TODOはissueに移行します。

使い方
卒論リポジトリで、`curl -sf https://raw.githubusercontent.com/dbgroup-nagoya-u/test-public-textlint-settings/master/update.bash | bash -s`と打つと、textlint等の設定が更新される。（実際には`template-latex`にこれを実行してくれるファイルがあるはず）

## TODO
- バグ報告のリンクをどこかに出しておく
  - このリポジトリの存在は卒論リポジトリから見えないから
  - github actionsで最後にコメントを付け加える等
- そもそもタグを毎回つけないといけないが、これも自動にする
  - github actionsで可能
  - ただし、branch名等の情報からタグをつけるようにしか設定できないので、実質手動と変わらない？
    - issueのresolveみたいな感じでpull requestのコメントに tag #v0.1.1 と書いたら動くようになってほしい
- draftcheckも管理して書き換えたいがライセンスがついていないのでどうすればよいか調べる
- template-latexリポジトリにダウンロードスクリプトを追加
- このリポジトリの削除
- （ただし、あまりこだわりすぎない！）
