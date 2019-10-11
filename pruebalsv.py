class GFG:
    def numberofPosition(self, n, k, x, y, obstPosx, obstPosy):
        d11 = min(x-1, y-1)
        d12 = min(n-x, n-y)
        d21 = min(n-x, y-1)
        d22 = min(x-1, n-y)
	
        r1 = y-1
        r2 = n-y
        c1 = x-1
        c2 = n-x
	
        for i in range(0, k):
            if (x > obstPosx[i] and y > obstPosy[i] and x-obstPosx[i] == y-obstPosy[i]):
                d11 = min(d11, x-obstPosx[i]-1)
	
            if (obstPosx[i] > x and obstPosy[i] > y and obstPosx[i]-x == obstPosy[i]-y):
                d12 = min(d12, obstPosx[i]-x-1)
	
            if (obstPosx[i] > x and y > obstPosy[i] and obstPosx[i]-x == y-obstPosy[i]):
                d21 = min(d21, obstPosx[i]-x-1)
	
            if (x > obstPosx[i] and obstPosy[i] > y and x-obstPosx[i] == obstPosy[i]-y):
                d22 = min(d22, x-obstPosx[i]-1)
	
            if (x == obstPosx[i] and obstPosy[i] < y):
                r1 = min(r1, y-obstPosy[i]-1)
	
            if (x == obstPosx[i] and obstPosy[i] > y):
                r2 = min(r2, obstPosy[i]-y-1)
	
            if (y == obstPosy[i] and obstPosx[i] < x):
                c1 = min(c1, x-obstPosx[i]-1)
	
            if (y == obstPosy[i] and obstPosx[i] > x):
                c2 = min(c2, obstPosx[i]-x-1)
	
        return d11 + d12 + d21 + d22 + r1 + r2 + c1 + c2
	

n = 8 # Tamaño del tablero
k = 1 # numero de obstaculos
Qposx = 4 #Posicion de la reina x
Qposy = 4 # Posicion de la reina y
obstPosx = [3] # posicion de obstaculos x
obstPosy = [5] # y posicion de obstaculos y

# se instancia la clase
claseCFG = GFG()
print('POSICIÓN')
print(Qposx,Qposy)
print('--------------------')
print('NUMERO OBSTACULOS')
print(k)
print("--------------------")
print("OUTPUT")
print(claseCFG.numberofPosition(n, k, Qposx, Qposy, obstPosx, obstPosy))
