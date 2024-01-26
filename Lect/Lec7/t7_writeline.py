# Построчная запись в файл
text = ['1Lorem ipsum dolor sit amet, consectetur adipisicing elit.',
'2Consequatur debitis explicabo laboriosam sint suscipit temporibus veniam?',
'3Accusantium alias amet fugit iste neque non odit quia saepe totam velit?', ]
with open('new_data.txt', 'a', encoding='utf-8') as f:
    f.writelines('\n'.join(text))