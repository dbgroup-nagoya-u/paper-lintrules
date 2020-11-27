grep -P -rn '(?<!\\url{)(\bhttps?://)[^\s.]+\.[-A-Za-z0-9+&@#/%?=~_|!:,.;]+' * \
| grep .bib \
| cut -d: -f1,2 \
| sed -e "s|\$| URLは\`\\\url\` コマンドで囲います.|"

grep -P -rn 'pages[ ,　]*?=.*?[0-9][ ,　]*?-[ ,　]*?[0-9]' * \
| grep .bib \
| cut -d: -f1,2 \
| sed -e "s|\$| 数値範囲は\`--\` を使用します.|"

