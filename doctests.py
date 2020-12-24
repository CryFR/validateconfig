import pathlib
import doctest


def vfile(args):  # file - проверка наличия имени файла
    """
    >>> vfile([True, 'file', 'file']) #файла нет
    True
    >>> vfile([False, 'file', 'file']) #файла нет
    False
    >>> vfile([True, 'file', 'config.txt']) #файл есть
    False
    >>> vfile([False, 'file', 'config.txt']) #файл есть
    True
    """
    fname = pathlib.Path(args[2])
    if args[0] == True:
        if fname.is_file():
            return False
        else:
            return True
    else:
        if fname.is_file():
            return True
        else:
            return False


doctest.testmod()
