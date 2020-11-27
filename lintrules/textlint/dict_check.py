import re
from collections import defaultdict
relativity_path = "./lintrules/textlint/"
#↓既存の辞書（検査されない）
exsisted_path = ["WEB+DB_PRESS.yml","techbooster.yml","textlint-prh-kanji-hiragana.yml","lab.yml","textlint-prh-noun.yml","typo.yml"]
#↓追加する辞書
new_path =  ["ieice.yml"]

flag = False
expecteds = set()
patterns = set()

for p in exsisted_path:
    with open(relativity_path + p) as f:
        for i in f:
            if re.match(".*expected:",i):
                expecteds.add(i.split()[-1])
                flag = False
            elif re.match(".*patterns?:",i):
                if re.match('patterns?:',i.split()[-1]):
                    flag = True
                else:
                    patterns.add(re.split("[:|-]\s+",i)[-1].split('\n')[0])
                    flag = False
            elif not(re.match("\s+\-",i)):
                flag = False
            elif flag:
                patterns.add(re.split("[:|-]\s+",i)[-1].split('\n')[0])

line = 1
flag = False

for p in new_path:
    line = 1
    print(p)
    with open(relativity_path + p) as f:
        for i in f:
            if re.match(".*expected:",i):
                flag = False
                ex = re.split("[:-]\s+",i)[-1].split('\n')[0]
                if ex in patterns:
                    print("\033[31m","Found CONFLICTED expected in",p,"at line",line,":",ex,"\033[0m")
                elif ex in expecteds:
                    print("Found duplicated expected in",p,"at line",line,":",ex)
                else:
                    expecteds.add(ex)
            elif re.match(".*patterns?:",i):
                if re.match('patterns?:',i.split()[-1]):
                    flag = True
                else:
                    flag = False
                    pt = re.split("[:-]\s+",i)[-1].split('\n')[0]
                    if pt in expecteds:
                        print("\033[31m","Found CONFLICTED pattern  in",p,"at line",line,":",pt,"\033[0m")
                    elif pt in patterns:
                        print("Found duplicated pattern  in",p,"at line",line,":",pt)
                    else:
                        patterns.add(pt)
            elif not(re.match("\s+\-",i)):
                flag != False
            elif flag:
                pt = i.split()[-1]
                if pt in expecteds:
                    print("\033[31m","Found CONFLICTED pattern in",p,"at line",line,":",pt,"\033[0m")
                elif pt in patterns:
                    print("Found duplicated pattern in",p,"at line",line,":",pt)
                else:
                    patterns.add(pt)
            line += 1