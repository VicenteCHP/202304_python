class CuentaBancaria:
    def __init__(self, tasa_interes):
        self.balance = 0
        self.tasa_interes = tasa_interes

    def hacer_deposito(self, amount):
        self.balance += amount

    def hacer_retiro(self, amount):
        if self.balance >= amount:
            self.balance -= amount
        else:
            print("No hay suficientes fondos en la cuenta.")
            
    def generar_interes(self):
        if self.balance > 0:
            self.balance += (self.balance * self.tasa_interes)

    def mostrar_balance(self):
        return self.balance



class Usuario:
    def __init__(self, name, email, tasa_interes):
        self.name = name
        self.email = email
        self.cuenta = CuentaBancaria(tasa_interes)  # Pasar la tasa de interés al crear una instancia de CuentaBancaria

    def hacer_deposito(self, amount):
        self.cuenta.hacer_deposito(amount)
        return self

    def hacer_retiro(self, amount):
        self.cuenta.hacer_retiro(amount)
        return self

    def generar_interes(self):
        self.cuenta.generar_interes()
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name} - Saldo: {self.cuenta.mostrar_balance()}")


# Crear instancias de la clase Usuario
usuario1 = Usuario("Guido", "guido@example.com", 0.03)
usuario1.hacer_deposito(100).hacer_deposito(200).hacer_deposito(100).hacer_retiro(200).generar_interes().mostrar_balance_usuario()

usuario2 = Usuario("Monty", "monty@example.com", 0.03)
usuario2.hacer_deposito(350).hacer_deposito(100).hacer_retiro(200).hacer_retiro(200).generar_interes().mostrar_balance_usuario()

usuario3 = Usuario("Vicente", "vicente_chp@gmail.com", 0.03)
usuario3.hacer_deposito(700).hacer_retiro(200).hacer_retiro(200).generar_interes().mostrar_balance_usuario()
