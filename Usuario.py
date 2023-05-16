class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        return self
        
    def hacer_retiro(self,amount):
        self.balance_cuenta -= amount
        return self
        

# Crear instancias de la clase Usuario
guido = Usuario("Guido", "guido@example.com")
monty = Usuario("Monty", "monty@example.com")
vicente = Usuario("Vicente" , "vicente_chp@gmail.com")

print(guido.name)  # Salida: Guido
print(monty.name)  # Salida: Monty
print(vicente.name)  # Salida: Vicente


guido.hacer_deposito(100).hacer_deposito(200).hacer_deposito(100).hacer_retiro(200)

monty.hacer_deposito(350).hacer_deposito(100).hacer_retiro(200).hacer_retiro(200)

vicente.hacer_deposito(700).hacer_retiro(200).hacer_retiro(200).hacer_retiro(200)

print(guido.balance_cuenta) 
print(monty.balance_cuenta)  
print(vicente.balance_cuenta) 
