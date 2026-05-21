# 呼び出してみる
print('はじめてのPython')

# 変数に代入
hello = 'はじめてのPythonを変数に代入したよ'
print(hello)

# List
pokemon_list = ['ヒトカゲ','ゼニガメ','フシギダネ']
print(pokemon_list)

## 配列追加
pokemon_list.append('ピカチュウ')
print(pokemon_list)

# Tuple 上書き不可
pokemon_tuple = ('ヒトカゲ','ゼニガメ','フシギダネ')
print(pokemon_tuple)

# Set 順不同で重複削除
pokemon_set = {'ヒトカゲ','ゼニガメ','フシギダネ','フシギダネ'}
print(pokemon_set)

# 条件分岐
monster_ball = True
if monster_ball:
  print('モンスターボールをなげますか？')
else:
  print('モンスターボールを持っていない...。')

