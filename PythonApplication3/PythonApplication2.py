#-*- coding:cp1251 -*-
from string import punctuation
 
text = '''�������� ���������, ������� ��������� ����� � ������� ��� �����: 
�������� ����� ������������� � ����� �������. 
�������� ���������� ������� �� Python'''
 
tbl = str.maketrans('', '', punctuation)
words = text.translate(tbl).lower().split()
print(max(words, key=len))
print(max(set(words), key=lambda x: words.count(x)))

