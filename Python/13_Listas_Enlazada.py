"""13_Listas _Enlazadas;
la cantidad de nodos en una list5a no es fija y puede crecer, Son dinamicas en su tamañano y su contenido"""


class node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next


class linked_list:
    def __init__(self):
        self.head = None
        self.len = 0

    # Método para verificar si la lista está vacía
    def is_empty(self):
        return self.head == None

    # Método imprimir el tamaño de la lista
    def size_list(self):
        print('Longitud lista:', self.len)

    # Método agrega al final
    def add_end(self, data):
        if self.head == None:
            self.head = node(data)
        else:
            curr = self.head
            while curr.next != None:
                curr = curr.next
            curr.next = node(data)
        self.len += 1

    # Método que imprima la lista
    def print_list(self):
        node= self.head
        while node != None:
            print(node.data, end = " => ")
            node=node.next
        print("\n")

    #metodo para agregar elementos en el frente de la linked list
    def add_at_front(self, data):
        self.head = node(data, self.head)
        self.len += 1

# Método para agregar elementos en una posición especifica de la linked list
    def add_at_position(self, data, position):
        curr = self.head
        curr_pos = 0
        if self.head != None:
            while curr != None and curr_pos != position:
                node_replace = curr
                curr = curr.next
                curr_pos += 1
            node_replace.next = node(data, curr)
        else:
            self.add_at_front(data)
        self.len += 1

# Método para eleminar nodos
    def delete_node(self, value):

        curr = self.head
        prev = None
        while curr != None and curr.data != value:
            prev = curr
            curr = curr.next
        if prev == None:
            self.head = curr.next
        elif curr:
            prev.next = curr.next
            curr.next = None
        self.len -= 1


lis = linked_list()
lis.add_end(10)
lis.size_list()
lis.add_end(20)
lis.size_list()
lis.add_end(15)
lis.add_end(23)
lis.print_list()
lis.add_at_front(8)
lis.print_list()
lis.add_at_position(80, 3)
lis.print_list()
lis.delete_node(20)
lis.print_list()