# test desu.
GitHub ActionsがAction in Actionをサポートするまで設定をダウンロードで代用するためのサンプルレポジトリ

名前はtextlintにこだわらずに、paper-lintrulesとかが良さそう

paper.txtがテスト用にありますが、消しても良いかもしれません

リポジトリを作成し直した際に、TODOはissueに移行します。

使い方
卒論リポジトリで、`curl -sf https://raw.githubusercontent.com/dbgroup-nagoya-u/test-public-textlint-settings/master/update.bash | bash -s`と打つと、textlint等の設定が更新される。（実際には`template-latex`にこれを実行してくれるファイルがあるはず）

## TODO
- バグ報告のリンクをどこかに出しておく
- 最新バージョンができるたびに毎回uddate.bashを書き換える必要があるが、APIでなんとかする
- そもそもタグを毎回つけないといけないが、これも自動にする
- あまりこだわりすぎない
- draftcheckも管理したい
- template-latexリポジトリにダウンロードスクリプトを追加
