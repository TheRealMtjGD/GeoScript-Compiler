import psroot
#import valueparser

def ismath(_Math: str) -> bool:
    for i in ['+', '-', '*', '/']:
        if i in _Math:
            return True
    return False


def MathParser(_Math: str) -> psroot.ParserObject:
    parserobject = psroot.ParserObject()
    parserobject.define_opcode('MATH')
    
    operations = []
    opsplit = []
    
    __operation__ = ''
    for i in ['+', '-', '*', '/']:
        if i in _Math:
            operations.append(i)
    
    for i in operations:
        if len(operations) == 1:
            ms = _Math.split(i)
            opsplit.append(ms[0])
            opsplit.append(ms[1])
            break
        
        else:
            preopsplit = []
            ms = _Math.split(i)
            preopsplit.append(ms[0])
            preopsplit.append(ms[1])
            
            if not __operation__ == '':
                preopsplit[0][preopsplit[0].find(__operation__)] = chr(9)
                preopsplit[0] = preopsplit[0].split(chr(9), 1)
                preopsplit[0] = preopsplit[0][1]
            
            print(preopsplit)
            
            preopsplit[1][preopsplit[1].rfind(__operation__)] = chr(9)
            preopsplit[1] = preopsplit[1].split(chr(9), 1)
            preopsplit[1] = preopsplit[1][0]
            
            opsplit.extend(preopsplit)
    
    return [operations, opsplit]

#print(MathParser('87+9/8'))