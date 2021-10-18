

dicc_abecedario = {".-":"A", "-...":"B","-.-.":"C", "-..":"D", ".":"E",
                   "..-.":"F", "--.":"G", "....":"H", "..":"I", ".---":"J",
                   "-.-":"K", ".-..":"L", "--":"M", "-.":"N", "---":"O", ".--.":"P",
                   "--.-":"Q", ".-.":"R", "...":"S", "-":"T", "..-":"U", "...-":"V",
                   ".--":"W", "-..-":"X", "-.--":"Y", "--..":"Z", "/":" "}


def traductor_a_espanol(mensaje_a_traducir):

  caracteres = ""
  mensaje_traducido=""

  for i in  range(0, len(mensaje_a_traducir)):
      new_letra=False
      print(i)


      if (mensaje_a_traducir[i]!= " "):
          caracteres= caracteres + mensaje_a_traducir[i]
          print(caracteres)
      elif((mensaje_a_traducir[i]==" ")):
          new_letra=True

      if i==(len(mensaje_a_traducir)-1):
          new_letra = True


      if ((new_letra) and (caracteres in dicc_abecedario)):

           print(dicc_abecedario[caracteres])
           mensaje_traducido = mensaje_traducido + dicc_abecedario[caracteres]
           caracteres=""

      elif((new_letra) and (caracteres not in dicc_abecedario)):
           print("caracter no encontrado")
           caracteres=""


  return print(mensaje_traducido)


traductor_a_espanol(".... . -- --- ... / . -. -.-. --- -. - .-. .- -.. --- / ..- -. .- / .--. .-.. .- -. - .- / -. ..- -. -.-. .- / .- -. - . ... / ...- .. ... - .-")










