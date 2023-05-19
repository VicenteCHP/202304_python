class UsuarioBancario:
    def __init__(self, name, tasa_interes):
        self.name = name
        self.tasa_interes = tasa_interes
        self.balance_cuenta = 0

    def hacer_deposito(self, amount):
        self.balance_cuenta += amount
        return self

    def hacer_retiro(self, amount):
        self.balance_cuenta -= amount
        return self
    
    def mostrar_balance_usuario(self):
        print(f"Usuario: {self.name} - Balance: {self.balance_cuenta}")
        
    def generar_interes(self):
        if self.balance_cuenta > 0:
            self.balance_cuenta += (self.balance_cuenta * self.tasa_interes)
        return self

Vicente = UsuarioBancario("Vicente", 0.01)
Vicente .hacer_deposito(10000).hacer_deposito(20000).hacer_deposito(10000).hacer_retiro(2000).mostrar_balance_usuario()
Vicente .generar_interes()
Vicente.mostrar_balance_usuario()

Rod = UsuarioBancario("Vicente", 0.01)
Rod .hacer_deposito(100000000).hacer_deposito(20000).hacer_retiro(2000).hacer_retiro(2000).hacer_retiro(2000).hacer_retiro(2000).mostrar_balance_usuario()
Rod .generar_interes()
Rod.mostrar_balance_usuario()