
### 検索ツールサンプル
### これをベースに課題の内容を追記してください

# 検索ソース
#source=["ねずこ","たんじろう","きょうじゅろう","ぎゆう","げんや","かなお","ぜんいつ"]
with open("data.csv", encoding="utf-8")as f:
    source = f.read().split()
print(source)
### 検索ツール
def search():
    word =input("鬼滅の登場人物の名前を入力してください >>> ")
    
    ### ここに検索ロジックを書く
    if word in source:
        print("{}が見つかりました".format(word))
    else:
        print("{}は存在しませんでした".format(word))
        source.append(word)
    print(source)

if __name__ == "__main__":
    search()
