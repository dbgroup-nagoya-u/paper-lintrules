このPull Requestではtextlintが走ります。
適宜`update-paper-lintrules.bash`を使用してtextlintの設定を更新してください。

### 執筆手順

必ず上から順番に行いましょう。各手順が終わったらチェックをつけてください。

- [ ] **textlintを参考に、可能な限り執筆・修正：**
最初はReviewerを追加せず、このDraft Pull Requestで執筆・修正を続けてください。可能な限りtextlintが指摘を行います。
漢字や送り仮名に対する微妙な指摘については、[電子情報通信学会の資料（1ページ）](https://www.ieice.org/jpn/shiori/pdf/furoku_d.pdf)や[常用漢字一覧表 - 文化庁](https://www.bunka.go.jp/kokugo_nihongo/sisaku/joho/joho/kakuki/14/pdf/jyouyou_kanjihyou.pdf)を参考にしてください。
Review commentの数が100に近づくとページの表示が重くなります。適宜Draft Pull RequestをCloseし、別のDraft Pull Requestで作業を続けてください。
- [ ] **参考文献のタイトルに含まれる固有名詞を`{}`で囲う**
Bibtexでは、タイトルの文字が自動的に大文字や小文字に変換されます。固有名詞をそのままの文字で残すため、それらを波括弧で囲んでください。textlintからの指摘は行われないので注意してください。
（例）`title={... {MySQL}}`
- [ ] **`.github/workflows/textlint.yml`と`.github/workflows/comment-open-pull-request.yml`を削除し、commitをpush：**
修正が完了し、Reviewerに添削をお願いできる状況になったら、上記ファイルを削除してcommitをpushしてください。以降のcommitに対してはtextlintによる指摘が行われなくなります。
- [ ] **このDraft Pull RequestをClose**
- [ ] **Pull Requestを作成：**
元のDraft Pull RequestをCloseし、新たに（通常の）Pull Requestを作成してください。Reviewerに共著者を追加し、共著者からの指摘や議論をもとに執筆・修正を続けてください。
共著者の追加方法は[ここ](https://github.com/dbgroup-nagoya-u/template-latex/tree/main#%E5%9F%B7%E7%AD%86%E3%81%AE%E6%B5%81%E3%82%8C)を見てください。

### バグ報告

おかしな指摘・指摘されていないが今後プログラムで指摘可能なルールを発見した場合は、
今後のために[こちら](https://github.com/dbgroup-nagoya-u/paper-lintrules/issues/new?assignees=&labels=&template=bug-report.md&title=)から指摘をお願いします。


執筆頑張ってください！
