class ListaSequencial:
  # o unico dado requerido da lista é o tamanho
  def __init__(self, tamanhoMaximo): 
    
    # aqui vamos tirar vantagem da estrutura da linguagem
    self.lista = []

    # eu preciso saber quem será o proximo nodo
    self.proximoNodo = 0

    # eu tenho que saber até onde posso navegar na minha lista
    self.tamanhoMaximo = tamanhoMaximo - 1 

  def inserir_nodo(self, nodo):
    # verificar se ja estou no maximo da minha lista
    if self.proximoNodo > self.tamanhoMaximo:
      print("Olha, ja deu heim? Lista está no maximo!")
      return
    
    # fazer um append na lista
    self.lista.append(None)
    self.lista[self.proximoNodo] = nodo

    # atualizar o indice do proximo nodo
    self.proximoNodo = self.proximoNodo + 1

  def tamanho(self):
    print(len(self.lista))

  def acessar_no_pelo_indice(self, indice):

    # sabe se é um indice valido
    if indice <= self.tamanhoMaximo:
      # se for, arrocha
      return print(self.lista[indice])
    else:
      # se nao, xinga
      print("Esse indice nao existe: " + str(indice))

  # facil
  def acessar_no_pelo_valor(self, valor):
    if valor not in self.lista:
        print(f"este valor '{valor}', não existe na lista")
    else:
        v = self.lista.index(valor)
        return print(self.lista[v])
  # facil
  def imprimir(self):
    return print(self.lista)
  
  # medio
  def inserir_na_posicao(self, posiçao, elemento):
    if posiçao > len(self.lista):
        print("Esta posição ultrapassa o tamanho maximo da lista")
    elif self.proximoNodo > self.tamanhoMaximo:
      print("Olha, ja deu heim? Lista está no maximo!")
    else:
        self.proximoNodo +=1 
        return self.lista.insert(posiçao, elemento)

  # medio++
  def remover(self, valor):
    if valor not in self.lista:
        print("este valor não existe na lista, impossivel remover")
    else:
        return self.lista.remove(valor)

lista = ListaSequencial(10)
lista.inserir_nodo("Artur")
lista.inserir_nodo("Fabio")
lista.inserir_nodo("Sideral")
lista.inserir_nodo("Gustavo")
lista.inserir_nodo("Joao")
lista.inserir_nodo("Wilson")
lista.inserir_nodo("Yuri")

lista.tamanho()
lista.imprimir()

lista.acessar_no_pelo_valor("Joao")
lista.acessar_no_pelo_indice(6)
lista.inserir_na_posicao(3, "Claudinaldo")

lista.imprimir()
lista.remover("Joao")
lista.imprimir()