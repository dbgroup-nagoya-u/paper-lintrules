# test-public-textlint-settings
GitHub ActionsがAction in Actionをサポートするまで設定をダウンロードで代用するためのリポジトリのサンプル

名前はtextlintにこだわらずに、paper-lintrulesとかが良さそう

paper.txtがテスト用にありますが、消しても良いかもしれません

リポジトリを作成し直した際に、TODOはissueに移行します。

## 使い方
卒論リポジトリで、`curl -sf https://raw.githubusercontent.com/dbgroup-nagoya-u/test-public-textlint-settings/master/update.bash | bash -s`と打つと、textlint等の設定が更新される。（実際には`template-latex`にこれを実行してくれるファイルがあるはず）

## TODO
- 初回コメントの改善
- 超コメントが出てページが重くなる場合の対処
  - Pull RequestをCloseしてもブランチは残るのでPull Requestを再作成でOK？
  - review前にtextlintは切る等は初回コメントに書く
- draftcheckも管理して書き換えたいがライセンスがついていないのでどうすればよいか調べる
- textlint設定ファイルを一つのディレクトリに封じ込める
  - textlint --config testlint-rules/.textlintrc
  - textlint.jsonでも読み込むらしい
- textlintの設定を厳しくする
  - [これとか](https://github.com/prismatix-jp/techdoc-ja/blob/develop/usage.md#textlint-%E8%A8%AD%E5%AE%9A%E4%BE%8B)を参考に
  - prhの辞書を増やす
- B4研修+卒論を使って明らかに違うルールを削除
- リポジトリ名変更時に影響箇所全部を変更
- 移行&&完成後、template-latexリポジトリにダウンロードスクリプトを追加
- このリポジトリの削除
- （ただし、あまりこだわりすぎない！）
