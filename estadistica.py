#https://replit.com/join/jdhrhlncyv-sol-veronicaver
anml=input("Hay animales?").lower()
menor_2=0
entre2_menor5=0
entre5_menor10=0
may_igual10=0
total=0

while anml=="si":
  edad=int(input("Que edad tiene el animal? "))
  if edad <2:
    menor_2+=1
  elif 2 <=edad <5:
    entre2_menor5+=1
  elif   5 <= edad <10:
    entre5_menor10+=1
  elif edad <=10:
    may_igual10+=1
  total+=1
  anml = input("Hay más animales? ").lower()  
if total > 0:
    p_menor2 = (menor_2/ total) * 100
    p_entre2_y_5 = (entre2_menor5 / total) * 100
    p_entre5_y_10 = (entre2_menor5 / total) * 100
    p_mayorigual_10 = (may_igual10 / total) * 100
print(f"Número de animales registrados: {total},Menor a 2 años: {menor_2} ({p_menor2}% del total,Entre 2 y 5 años: {entre2_menor5} ({p_entre2_y_5}% del total,Entre 5 y 10 años: {entre5_menor10} ({p_entre5_y_10}% del total),Mayor o igual a 10 años: {may_igual10} ({p_mayorigual_10}% del total") 
