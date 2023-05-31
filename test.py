from datetime import datetime

#今年の年を取得
current_year = datetime.now().year

#人を定義
a = current_year - 1981
dora = current_year - 2012

#結果表示
print('今年は', current_year, '年')
print('Aさんは今年', a, '歳になります')
print('doraさんは今年', dora, '歳になります')
