import pytest
from string_utils import StringUtils

SU = StringUtils()

@pytest.mark.parametrize('word, expected', [('hello', 'Hello'), ('world', 'World')] ) # Положительные проверки

def test_big_first_g(word, expected):
   res = SU.capitalize(word)
   assert res == expected
   print(res)

@pytest.mark.parametrize('word, expected', [('hello', 'hellO'), ('hello', 'hello'), ('world', 'Wrld')] ) # Негативыные проверки
@pytest.mark.xfail

def test_big_first_b(word, expected):
   res = SU.capitalize(word)
   assert res == expected
   print(res)

@pytest.mark.parametrize('word, expected', [('  hello', 'hello'), ('         world', 'world')] ) # Положительные проверки

def test_sp_g(word, expected):
   res = SU.trim(word)
   assert res == expected
   print(res)

@pytest.mark.parametrize('word, expected', [('hello  ', 'hello'), ('hel lo', 'hello')] ) # Негативыные проверки
@pytest.mark.xfail
def test_sp_b(word, expected):
   res = SU.trim(word)
   assert res == expected
   print(res)

@pytest.mark.parametrize('word, symbol', [('hello', 'h'), ('World', 'W')] ) # Положительные проверки

def test_sym_g(word, symbol):
   res = SU.contains(word, symbol)
   assert res == True
   print(res)

@pytest.mark.parametrize('word, symbol', [('hello', 'H'),('hello', 'w'), ('hello', ' ') ] ) # Негативыные проверки

def test_sym_b(word, symbol):
   res = SU.contains(word, symbol)
   assert res == False
   print(res)

@pytest.mark.parametrize('word, symbol, expected', [('hello', 'h', 'ello'), ('hello', 'z', 'hello'), ('world', 'world', ''), ('hello', 'l', 'heo') ] ) # Положительные проверки

def test_del_g(word, symbol, expected):
   res = SU.delete_symbol(word, symbol)
   assert res == expected
   print(res)

@pytest.mark.parametrize('word, symbol, expected', [('hello', 'H', 'ello'), ('hello', '', 'hello' )] ) # Негативыные проверки  ## баг 1, строка 1 ('hello', '', 'hello')
@pytest.mark.xfail
def test_del_b(word, symbol, expected):
   res = SU.delete_symbol(word, symbol)
   assert res == expected
   print(res)