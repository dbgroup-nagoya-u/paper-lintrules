# test desu.
GitHub ActionsがAction in Actionをサポートするまで設定をダウンロードで代用するためのサンプルレポジトリ

名前はtextlintにこだわらずに、paper-lintrulesとかが良さそう

paper.txtがテスト用にありますが、消しても良いかもしれません

リポジトリを作成し直した際に、TODO等は移行します。

使い方
卒論リポジトリで、`curl -sf https://raw.githubusercontent.com/dbgroup-nagoya-u/test-public-textlint-settings/master/update.bash | bash -s`と打つと、textlint等の設定が更新される。（実際には`template-latex`にこれを実行してくれるファイルがあるはず）
