from datetime import datetime

#今年の年を取得
cyear = datetime.now().year

#人を定義
a = cyear - 1981
dora = cyear - 2012

#結果表示
print('今年は', cyear, '年')
print('Aさんは今年', a, '歳')
print('doraさんは今年', dora, '歳')
