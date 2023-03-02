cad = [['Maria', 29], ['Pedeo', 90], ['Polam', 28]]
grand = peque = c = 0
for p in cad:
      if c == 0:
        grand = 1
        peque = 1 
      if cad[c][1] > grand:
        grand = cad[0][1]
      if cad[c][1] < grand:
        peque = cad[c][1]
      c+=1  

print(grand)
print(peque)