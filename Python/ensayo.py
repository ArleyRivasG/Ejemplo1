caracteres = ""
caracteres= caracteres + "."
caracteres= caracteres + "-"
caracteres= caracteres + "-"


print(caracteres)

dicc_abecedario = {".-":"A", "-...":"B","-.-.":"C", "-..":"D", ".":"E",
                   "..-.":"F", "--.":"G", "....":"H", "..":"I", ".---":"J",
                   "-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O", ".--.":"P",
                   "--.-":"Q", ".-.":"R", "...":"S", "-":"T", "..-":"U", "...-":"V",
                   ".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z", "/":" "}
if (caracteres in dicc_abecedario):
    print(caracteres)
    print(dicc_abecedario[caracteres])