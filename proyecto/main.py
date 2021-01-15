import sys


clients = [
    {
        'name': 'Pablo',
        'company': 'Google',
        'email': 'pablo@google.com',
        'position': 'Software engineer',
    },
    {
        'name': 'Ricardo',
        'company': 'Facebook',
        'email': 'pablo@facebook.com',
        'position': 'Data engineer',
    },
]


# Creamos nuevos clientes
def create_client(client):
    global clients

    # control de existencia del cliente en la lista
    if client not in clients:
        clients.append(client)
        #clients += client_name
        #_add_comma()
    else:
        print('Client already is in the client\'s list' )

# Listamos los clientes 
def list_clients():
    for idx, client in enumerate(clients):
        print('{uid} | {name} | {company} | {email} | {position}'.format(
            uid=idx,
            name=client['name'],
            company=client['company'],
            email=client['email'],
            position=client['position']))
        #print('{}: {}'.format(idx, client['name']))

#    global clients

#    print(clients)


def update_client(client_name, updated_name):       # Declaracion anterior
    global clients

    if client_name in clients:
        index = clients.index(client_name)
        clients[index] = updated_name
        #clients = clients.replace(client_name + ',', update_client_name + ',') 
    else:
        print('client is not in clients list')
         
# Eliminar cliente
def delete_client(client_name):
    global clients

    if client_name in clients:
        clients.remove(client_name)
        #clients = clients.replace(client_name + ',', '')
    else:
        print('Client is not clients list')


# Buscar cliente
def search_client(client_name):
   # clients_list = clients.split(',')

    for client in clients:
        if client != client_name:
            continue 
        else:
            return True


# Agrega comoa, para separar los nombres
# def _add_comma():
#    global clients
# 
#    clients += ','

#metodo

def _get_client_field(field_name):
    field = None

    while not field:
        field = input('Wha is the client {}? '.format(field_name))

    return field

def _get_client_name():
    client_name = None

    while not client_name:
        client_name = input('whats is the client name? ')

        if client_name == 'exit':
            client_name = None
            break

    if not client_name:
        sys.exit()


    return client_name
    #return input('What is the client name? ')


# Mensaje de bienvenida
def _print_welcome():
    print('WELCOME TO PLATZI VENTAS')
    print('*' * 50)
    print('What woul you like to do today?')
    print('[C]reate client')
    print('[L]ist client')
    print('[U]pdate client')
    print('[D]elete client')
    print('[S]earch client')

    print('*' * 50)


if __name__ == '__main__':
    _print_welcome()    # Llamamos la funcion _print_welcome

    command = input()
    command = command.upper()

    if command == 'C':
        client = {
            'name': _get_client_field('name'),
            'company': _get_client_field('company'),
            'email': _get_client_field('email'),
            'position': _get_client_field('position'),
        }
        create_client(client)
        list_clients()
    elif command == 'L':
        list_clients()
    elif command == 'U':  # Actualizar
        client_name = _get_client_name()
        update_client_name = input('What is the updated client name? ')

        update_client(client_name, updated_name)
        list_clients()
    elif command == 'D':
        client_name = _get_client_name()
        delete_client(client_name)
        list_clients()
    elif command == 'S':
        client_name = _get_client_name()
        found = search_client(client_name)

        if found:
            print('The client is in the client\'s list')
        else:
            print('The client: {} is not in our client\'s list'.format(client_name))
    else:
        print('invalid command')

# repetir codigo

   # list_clients()
#
   # create_client('david')
   # 
   # list_clients()
#
   # print(clients)

