#Recursividad para calcular el factorial de un número.

def factorial(n):
    """Calcula el factorial de un número dado.
    
    Parameters
    ----------
    n : int
        Número entero al que se le calculará el factorial.
        
    Returns
    -------
    int
        El factorial del número dado.
        
    Example
    -------
    factorial(5)
    120
    """
    #Código a realizar.
    """
    En esta implementación, la función 'factorial' utiliza recursión para calcular el factorial de un número entero no negativo 'n'. 
    En el caso base, si 'n' es igual a 0, la función retorna 1, ya que por definición el factorial de 0 es 1. 
    En el paso recursivo, si 'n' es mayor que 0, la función retorna 'n * factorial(n - 1)', 
    lo que calcula el factorial multiplicando 'n' por el factorial del número 'n - 1'. 
    Este proceso continúa hasta que se alcanza el caso base.
    """
    
    # Caso base: si n es 0, retorna 1
    if n == 0:
        return 1
    # Paso recursivo: si n > 0, retorna n * factorial(n-1)
    else:
        return n * factorial(n - 1) 

def main():
    print("=================================================================.")
    print("Test Case 1: Check the Factorial of 5.")
    print("=================================================================.")
    print("The factorial of 5 is: ", factorial(5))

if __name__ == "__main__":
    main()
    