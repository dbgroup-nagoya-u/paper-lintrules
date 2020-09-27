### Message from github-actions bot
このPull Requestではtextlintが走ります:rocket:
適宜`./update.bash`を使用してtextlintの設定を更新してください。

### 執筆の流れ

1. 最初はReviewerを追加せず、このPull Requestで執筆と修正を続けてください。可能な限りtextlintが指摘を行います。
1. 修正が完了し、Reviewerに添削をお願いできる状況になったら、
`./github/workflows/textlint.yml`を削除してください。
以降のcommitに対してはtextlintによる指摘が行われなくなります。
1. Reviewerを追加する際は同じブランチ（通常は`develop`）に対して別のプルリクエストを作成し、そこでReviewを開始してください。
- Review commentの数が100に近づくとページの表示が重くなります。
Textlintの修正が多い場合・Review前にはプルリクエストを切り替えると快適に作業ができます。

### バグ報告
おかしな指摘・指摘されていないが今後プログラムで指摘可能なルールを発見した場合は、
今後のために[こちら](https://github.com/dbgroup-nagoya-u/test-public-textlint-settings/issues/new?assignees=&labels=&template=bug-report.md&title=)から指摘をお願いします:smiley:


執筆頑張ってください！
