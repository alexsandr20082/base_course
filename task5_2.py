name = "Александр Шерстобоев"  
name_with_underscores_upper = '_'.join(name) + '_'
ascii_codes_upper = [ord(char) for char in name_with_underscores_upper.upper()]

print("Строка в верхнем регистре:", name_with_underscores_upper.upper())
print("ASCII коды для верхнего регистра:", ascii_codes_upper)

name_with_underscores_lower = '_'.join(name) + '_'
ascii_codes_lower = [ord(char) for char in name_with_underscores_lower.lower()]

print("Строка в нижнем регистре:", name_with_underscores_lower.lower())
print("ASCII коды для нижнего регистра:", ascii_codes_lower)

all_ascii_codes = ascii_codes_upper + ascii_codes_lower
max_value = max(all_ascii_codes)
min_value = min(all_ascii_codes)

print("Наибольшее значение из всех ASCII кодов:", max_value)
print("Наименьшее значение из всех ASCII кодов:", min_value)