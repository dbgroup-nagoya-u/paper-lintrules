# test-public-textlint-settings
GitHub ActionsがAction in Actionをサポートするまで設定をダウンロードで代用するためのリポジトリのサンプル

リポジトリを作成し直した際に、TODOはissueに移行します。

## 使い方
卒論リポジトリで、`curl -sf https://raw.githubusercontent.com/dbgroup-nagoya-u/test-public-textlint-settings/master/update.bash | bash -s`を閉じ込めたファイル`hoge.bash`を実行すると、textlint等の設定が更新される。

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
- リポジトリ名変更
  - textlintにとらわれない名前が良さそうpaper-lintrulesとか
- リポジトリ名変更時に影響箇所全部を変更
- 移行&&完成後、`template-latex`リポジトリにダウンロードスクリプトを追加
``` bash
#!/bin/bash
# Check if command exists.
ESC=$(printf '\033')
RED="${ESC}[31m"
if ! command -v curl &> /dev/null
then
    echo "curl could not be found."
    printf "Type ${RED}%s${ESC}[m\n" 'sudo apt install curl'
    exit
fi
curl -sf https://raw.githubusercontent.com/dbgroup-nagoya-u/test-public-textlint-settings/master/update.bash | bash -s
```
- このリポジトリの削除
- （ただし、あまりこだわりすぎない！）
