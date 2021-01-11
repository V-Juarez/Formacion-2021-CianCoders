



clients = 'pablo,ricardo,'

# Creamos nuevos clientes
def create_client(client_name):
    global clients
    
    # control de existencia del cliente en la lista
    if client_name not in clients:
        clients += client_name
        _add_comma()
    else:
        print('Client already is in the client\'s list' )

# Listamos los clientes 
def list_clients():
    global clients

    print(clients)

# Agrega comoa, para separar los nombres
def _add_comma():
    global clients

    clients += ','

# Mensaje de bienvenida
def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What woul you like to do today?')
    print('[C]reate client')
    print('[D]elete client')


if __name__ == '__main__':
    _print_welcome()    # Llamamos la funcion _print_welcome

    command = input()

    if command == 'C':
        client_name = input('What is the client name? ')
        create_client(client_name)
        list_clients()
    elif command == 'D':
        pass
    else:
        print('invalid command')

    list_clients()

    create_client('david')
    
    list_clients()

    print(clients)

