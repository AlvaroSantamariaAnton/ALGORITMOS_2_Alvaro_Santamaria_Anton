import functools

"""
En este código, 'functools.partial' se utiliza para crear versiones especializadas de los métodos 
'apply_discount' y 'calculate_tax' con ciertos parámetros predefinidos (el descuento del 20% y la tasa de impuesto del 21%, respectivamente). 
Luego, estas funciones parcialmente configuradas se utilizan para calcular los precios con descuentos y tasas de impuestos predefinidos.
"""

class SimpleOperations:
    def apply_discount(self, price, discount):
        """Aplica un descuento al precio dado y retorna el nuevo precio."""
        discounted_price = price * (1 - discount)
        return discounted_price

    def calculate_tax(self, price, tax_rate):
        """Calcula y agrega el impuesto al precio dado."""
        taxed_price = price * (1 + tax_rate)
        return taxed_price

# Crear una instancia de SimpleOperations
operations = SimpleOperations()

# Configurar funciones con descuentos y tasas de impuestos predefinidos utilizando functools.partial.
twenty_percent_discount = functools.partial(operations.apply_discount, discount=0.20)
vat_tax = functools.partial(operations.calculate_tax, tax_rate=0.21)

# Usar las funciones preconfiguradas.
original_price = 100
discounted_price = twenty_percent_discount(original_price)
final_price = vat_tax(discounted_price)

print("Precio original:", original_price)
print("Precio con descuento del 20%:", discounted_price)
print("Precio final con impuesto del 21%:", final_price)