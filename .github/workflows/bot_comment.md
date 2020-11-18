このPull Requestではtextlintが走ります。
適宜`update-paper-lintrules.bash`を使用してtextlintの設定を更新してください。

### 執筆手順


- [ ] **textlintを参考に、可能な限り執筆・修正**
最初はReviewerを追加せず、このDraft Pull Requestで執筆・修正を続けてください。可能な限りtextlintが指摘を行います。
漢字や送り仮名に対する微妙な指摘については[ここ](https://www.ieice.org/jpn/shiori/pdf/furoku_d.pdf)とか[ここ](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kakuki/14/pdf/jyouyou_kanjihyou.pdf)も参考にすると良いでしょう。
Review commentの数が100に近づくとページの表示が重くなります。適宜Draft Pull RequestをCloseし，別のDraft Pull Requestで作業を続けてください。
- [ ] **`.github/workflows/textlint.yml`と`.github/workflows/comment-open-pull-request.yml`を削除**
修正が完了し、Reviewerに添削をお願いできる状況になったら、上記ファイルを削除し，commitしてください。以降のcommitに対してはtextlintによる指摘が行われなくなります。
- [ ] **このDraft Pull RequestをClose**
- [ ] **Pull Requestを作成**
元のDraft Pull RequestをCloseし、新たに（通常の）Pull Requestを作成してください。Reviewerに先生を追加し、先生からの指摘をもとに執筆・修正を続けてください。

### バグ報告

おかしな指摘・指摘されていないが今後プログラムで指摘可能なルールを発見した場合は、
今後のために[こちら](https://github.com/dbgroup-nagoya-u/paper-lintrules/issues/new?assignees=&labels=&template=bug-report.md&title=)から指摘をお願いします。


執筆頑張ってください！
