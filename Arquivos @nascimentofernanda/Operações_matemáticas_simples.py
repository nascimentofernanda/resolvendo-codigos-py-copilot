#Descrição: Vamos solicitar como entrada dois números e depois vamos realizar uma operação simples entre eles.

número1=float(input("Digite um número: "))
número2=float(input("Digite um número: "))

soma=número1+número2
subtração=número1-número2
multiplicação=número1*número2
divisão=número1/número2

print(f"{número1}+{número2}={soma}")
print(f"{número1}-{número2}={subtração}")
print(f"{número1}*{número2}={multiplicação}")
print(f"{número1}/{número2}={divisão}")
