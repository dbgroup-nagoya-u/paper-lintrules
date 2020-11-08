このPull Requestではtextlintが走ります。
適宜`update-paper-lintrules.bash`を使用してtextlintの設定を更新してください。

### 執筆の流れ

1. 最初はReviewerを追加せず、このDraft Pull Requestで執筆・修正を続けてください。可能な限りtextlintが指摘を行います。
- Review commentの数が100に近づくとページの表示が重くなります。適宜Draft Pull RequestをCloseし，別のDraft Pull Requestで作業を続けてください。
1. 修正が完了し、Reviewerに添削をお願いできる状況になったら、
`.github/workflows/textlint.yml`と`.github/workflows/comment-open-pull-request.yml`を削除し，commitしてください。
以降のcommitに対してはtextlintによる指摘が行われなくなります。
1. 元のDraft Pull RequestをCloseし、新たに（通常の）Pull Requestを作成してください。Reviewerに先生を追加し、先生からの指摘をもとに執筆・修正を続けてください。

### やることリスト

すべて終えてから先生にReviewをお願いしましょう！

- [ ] textlintを参考に，可能な限り執筆・修正
- [ ] `.github/workflows/textlint.yml`と`.github/workflows/comment-open-pull-request.yml`を削除
- [ ] このDraft Pull RequestをClose

### 参考

- [常用漢字表・送り仮名について](https://www.ieice.org/jpn/shiori/pdf/furoku_d.pdf)
- [常用漢字一覧表](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kakuki/14/pdf/jyouyou_kanjihyou.pdf)

### バグ報告

おかしな指摘・指摘されていないが今後プログラムで指摘可能なルールを発見した場合は、
今後のために[こちら](https://github.com/dbgroup-nagoya-u/paper-lintrules/issues/new?assignees=&labels=&template=bug-report.md&title=)から指摘をお願いします:smiley:


執筆頑張ってください！
