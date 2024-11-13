#listcomp
symbols = "Дима лох"
symnol_codes = [ord (symbol) for symbol in symbols]
print(symnol_codes) # Список

symbols = "Дима лох"
symnol_codes = (ord (symbol) for symbol in symbols)
print(symnol_codes) # Генератор 
