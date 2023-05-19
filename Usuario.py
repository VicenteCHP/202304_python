class Usuario:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        return self

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        return self

    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name} - Saldo: {self.balance_cuenta}")


# Crear instancias de la clase Usuario
usuario1 = Usuario("Guido", "guido@example.com")
usuario1.hacer_deposito(100).hacer_deposito(200).hacer_deposito(100).hacer_retiro(200).mostrar_balance_usuario()

usuario2 = Usuario("Monty", "monty@example.com")
usuario2.hacer_deposito(350).hacer_deposito(100).hacer_retiro(200).hacer_retiro(200).mostrar_balance_usuario()

usuario3 = Usuario("Vicente", "vicente_chp@gmail.com")
usuario3.hacer_deposito(700).hacer_retiro(200).hacer_retiro(200).mostrar_balance_usuario()
