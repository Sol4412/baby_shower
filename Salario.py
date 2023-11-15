#https://replit.com/join/updugpxysx-sol-veronicaver
num_vent=float(input("Dime las ventas"))
comi=0
if num_vent <3500: 
   comi=0.07
elif 3500  <= comi <= 7000:
  comi=0.1
elif num_vent > 7000:
  comi=0.15
while True:  
  vendedor= input("Hay vendedor?").lower()

  if vendedor=="no":
    break 
  elif vendedor== "si":
   nom= input("Nombre del vendedor..")
  salario= float(input("Cual es el salario base?"))
  total= float(input("Dame el total de ventas"))
  total_s= comi+ salario
  print(f"{nom} tiene un salario de {salario} y ventas de {total}. El sueldo total es:{total_s}")
