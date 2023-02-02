class No:
    def __init__(self, dado):
        self.dado = dado
        self.esquerda = None
        self.direita = None

    def __str__(self):
        return str(self.dado)
        
padrão = "valor padrão"

class ArvoreBinariaBusca:
    def __init__(self, dado = None, no = None):
        #se for passado um nó para construir uma subarvore
        if no:
            self.raiz = no 

        elif dado: 
            no = No(dado)   
            self.raiz = no
        
        else: self.raiz = None

    def inserir(self, dado):
        pai = None
        temp = self.raiz

        #loop para achar o lugar do dado
        while temp != None:
            pai = temp

            if dado < temp.dado:
                temp = temp.esquerda
                
            else:
                temp = temp.direita

        if pai is None:
            #se não tiver nenhum nó, o nó inserido vira a raiz
            self.raiz = No(dado)
       
        elif dado < pai.dado:
            pai.esquerda = No(dado)
         
        else:
            pai.direita = No(dado)

    def buscar(self, value, node = padrão):
        #define que se nenhum valor for passado no nodo, é iniciado pela raiz
        if node == padrão:
            node = self.raiz
        if node is None:
            return print("\nvalor não encontrado na arvore")
        if node.dado == value:
            return ArvoreBinariaBusca(node)
        if value < node.dado:
            return self.buscar(value, node.esquerda)
        return self.buscar(value, node.direita)

    def min(self, nodo=padrão):
        if nodo == padrão:
            nodo = self.raiz

        while nodo.esquerda:
            nodo = nodo.esquerda
        return nodo.dado 

    def remover(self, valor, nodo =0):
        if nodo == 0:
            nodo = self.raiz

        if nodo == None: return nodo

        if valor < nodo.dado:
            nodo.esquerda = self.remover(valor, nodo.esquerda)
        elif valor > nodo.dado:
            nodo.direita = self.remover(valor, nodo.direita)

        else:
            if nodo.esquerda == None:
                return nodo.direita
            elif nodo.direita == None:
                return nodo.esquerda
            else: 
                substituto = self.min(nodo.esquerda)
                nodo.dado = substituto
                #remove o substituto da subarvore 
                nodo.direita = self.remover(substituto, nodo.direita)

        return nodo

    def print_em_ordem(self, node=None):
        if node is None:
            node = self.raiz
        
        if node.esquerda:
            self.print_em_ordem(node.esquerda)

        print(node, end=' ')
        if node.direita:
            self.print_em_ordem(node.direita)
        







values = [61, 89, 66, 43, 51, 16, 55, 11, 79, 77, 82, 32]
tree = ArvoreBinariaBusca()
for v in values:
    tree.inserir(v)

#tree.remover(89)
r = tree.min()
#print(r)

#tree.print_em_ordem()
tree.print_em_ordem()

b = tree.buscar(50)
if b != None:
    print('\n' ,b.raiz.dado, "encontrado")
