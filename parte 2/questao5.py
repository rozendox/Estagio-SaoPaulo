def inverter_string(s):
    resultado = ""
    for char in s:
        resultado = char + resultado
    return resultado

string_exemplo = "Exemplo"
string_invertida = inverter_string(string_exemplo)
print("String original:", string_exemplo)
print("String invertida:", string_invertida)
