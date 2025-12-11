EXPECTED_BAKE_TIME = 40
PREPARATION_TIME = 2

def bake_time_remaining(elapsed_bake_time):
    
    """Calculate the bake time remaining.

    :param elapsed_bake_time: int - baking time already elapsed.
    :return: int - remaining bake time (in minutes) derived from 'EXPECTED_BAKE_TIME'.

    Function that takes the actual minutes the lasagna has been in the oven as
    an argument and returns how many minutes the lasagna still needs to bake
    based on the `EXPECTED_BAKE_TIME`.
    """

    return EXPECTED_BAKE_TIME - elapsed_bake_time

def preparation_time_in_minutes(number_of_layers):

    """
    :param number_of_layers: int - número de camadas da lasanha
    :return: int - tempo total de preparação baseado em PREPARATION_TIME

    A função recebe o número de camadas da lasanha e retorna os minutos necessários para preparar todas as camadas levando em consideração que o tempo para preparar 1 camada é de PREPARATION_TIME minutos.
    
    """
    return number_of_layers*PREPARATION_TIME

def elapsed_time_in_minutes(number_of_layers, elapsed_bake_time):

    """
    :param number_of_layers: int - número de camadas da lasanha
    :param elapsed_bake_time: int - tempo (em minutos) de cozimento decorrido
    :return: int - tempo total de preparação somado ao cozimento atual

    A função recebe o número de camadas da lasanha, o tempo (em minutos) decorrido de cozimento e retorna o tempo (em minutos) decorrido, levando em consideração que o tempo para preparar 1 camada é de PREPARATION_TIME minutos.
    
    """
    
    return PREPARATION_TIME*number_of_layers+elapsed_bake_time
