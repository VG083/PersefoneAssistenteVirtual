def linha(tam = 49):
    return '-'*tam


def cabecalho():
    '''
    """
    -> Essa função exibe um cabeçalho centralizado
    :param msg: Recebe o texto do cabeçalho
    '''
    print('\033[41m', linha(), '\033[m')
    print('\033[41m', '                    Perséfone                    ', '\033[m')
    print('\033[41m', linha(), '\033[m')

def falaPersefone(msg):
    '''
    """
    -> Essa função exibe uma fala da Perséfone
    :param msg: Recebe o texto do cabeçalho
    '''
    print('\033[31m>>', msg, '\033[m')

def falaUsuario(msg):
    '''
    """
    -> Essa função exibe uma fala do usuário
    :param msg: Recebe o texto do cabeçalho
    '''
    print('\033[33mComando:', msg, '\033[m')

