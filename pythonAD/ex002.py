palavra = "garrafas"

for num_bebidas in range(99, 0 ,-1):
    print(num_bebidas, palavra, "de cerveja na parede.")

    print(num_bebidas, palavra, "de cerveja")

    print("derruba uma.")
    
    print("passa outra")

    if num_bebidas == 1:
        print("sem mais garrafas de cerveja na parede")
    else:
        novo_num = num_bebidas - 1
        if novo_num == 1:
            palavra = "garrafa"
        print(novo_num, palavra, "de cerveja na parede.")
print()
            
    