#あなたは S と名付けられたポケモンを捕まえました。このポケモンは、餌を1回与えるごとに名前が変わるという特徴があります。
#具体的には、餌を与える度に、名前の先頭に a を付け加えたものが、新しい名前になります。
#今、あなたはこのポケモンを N 回強化しました。ポケモンの名前を出力しなさい。
#制約・Sは英小文字のみからなる文字列 , ・1 <= N <= 100
S = input()
N = int(input())
for i in range (N):
    N += 1
print("a"*i+S)