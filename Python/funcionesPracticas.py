
def capicua(numero):
    num_str= str(numero)
    list_num= list(num_str)
    list_rev = list_num.copy()
    list_rev.reverse()
#   print(list_num)
#   print(list_rev)
    if(list_num== list_rev):
        return True
    else:
        return False


capicua(51415)

def primer_digito_par (numero):
    """no incluyo el 0 porqué solo comparo el primer digito si es par"""
    lista_par = ["2", "4", "6", "8"]
    num_str= str(numero)
    if num_str[0] in lista_par:
        return True
    else:
        return False

primer_digito_par(547)


