class Conta:

  def __init__(self, numero, titular, saldo, limite):
    print("construindo objeto...")
    self.__numero = numero
    self.__titular = titular
    self.__saldo = saldo
    self.__limite = limite


  def deposita(self, valor):
    self.__saldo += valor


  def saca(self, valor):
    if self.__pode_sacar(valor):
      self.__saldo -= valor
    else:
      print("Saldo não suviciente para esse valor")


  def __pode_sacar(self, valor):
    return valor <= (self.__saldo + self.__limite)


  def extrato(self):
    print(f"Saldo de: {self.__saldo}. (Titular {self.__titular})")


  def transfere(self, valor, conta):
    self.saca(valor)
    conta.deposita(valor)


  @property
  def limite(self):
    return self.__limite


  @limite.setter
  def limite(self, limite):
    self.__limite = limite


  @property
  def saldo(self):
    return self.__saldo


  @staticmethod
  def codigo_banco():
    return "001"


  # def get_saldo(self):
  #   return self.__saldo

  # def set_limite(self, limite):
  #   self.__limite = limite
    