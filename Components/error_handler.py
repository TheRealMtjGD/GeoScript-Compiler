def gstraceback(lineint: int, archline: str, file: str) -> dict[str]:
    return {
        "li": lineint,
        "al": archline,
        "f": file
    }


def throw_error(error: str, description: str, gstb: dict) -> None:
    print(f'Traceback error in compilaton')
    print(f'  File {gstb['f']}, {gstb['li']}')
    print(f'    {gstb['al']}')
    
    print('    ', end='')
    for _ in range(len(gstb['al'])):
        print('^', end='')
    print('\n')
    
    print(f'[{error}]: {description}')
    exit(1)

def throw_warning(error: str, description: str, gstb: dict) -> None:
    print(f'warning | [{error}]: {description}')
    print(f'  File {gstb['f']}, {gstb['li']}')
    print(f'    {gstb['al']}')
    
    print('    ', end='')
    for _ in range(len(gstb['al'])):
        print('^', end='')
    print('\n')
    exit(1)

def raise_compiler_error(error: str, args: tuple[str], sline: str, file: str, line: int) -> None:
    print('A client side exception has occured | Language: Python 3.12.1 64-Bit Win32')
    print(f'  File {file}, {line}')
    print(f'    {sline}')
    print('    ', end='')
    for _ in sline:
        print('^', end='')
    print('')
    
    print('')
    print(f'[{error}]: {' '.join(args)}')