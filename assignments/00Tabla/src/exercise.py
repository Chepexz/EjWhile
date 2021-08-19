import os

def main():
    os.system("clear")
    #escribe tu código abajo de esta línea
    x = .5
    print("     x         y       z") 
    print(f"{'x':>7} {'y':>7}  {'z':>7} ") 
    print("___________________________")
    while x <= 10:
        y = 3*x**2+7*x-15
        z = y - 2 * x ** 2

        print(f"{x:8.2f} {y:8.2f} {z:8.2f}")
        
        x += .5

if __name__=='__main__':
    main()
