from . import psroot

def TypeChecker(value: str) -> str|None:
    if value.startswith('"'):
        if value.endswith('"'):
            return 'LiteralString'
        else:
            return None
    else:
        try:
            int(value)
            return 'int64'
        except ValueError:
            try:
                float(value)
                return 'float64'
            except ValueError:
                if value == "True":
                    return 'bool'
                elif value == "False":
                    return 'bool'
                elif value.startswith('g::'):
                    return 'gj:group'
                elif value.startswith('c::'):
                    return 'gj:counter'
                elif value.startswith('o::'):
                    return 'gj:object'
                else:
                    try:
                        int(value, 16)
                        return 'pointer64'
                    except ValueError:
                        return None

def ValueParser(_Value: str) -> psroot.ParserObject:
    parser_object = psroot.ParserObject()
    parser_object.define_opcode('VALUE')
    
    gtype = TypeChecker(_Value)
    if gtype == None:
        parser_object.define_operand({'errtype': True, 'message': f'Value "{_Value}" has no descernable type | GSParser ValueParser'})
        return parser_object
    
    elif gtype == 'LiteralString':
        buffsize = len(_Value) - 2
        valuebuff = [i for i in _Value]
        valuebuff.pop(0)
        valuebuff.pop(-1)
        
        parser_object.define_operand({'errtype': False, 'type': gtype, 'value': valuebuff, 'buffsize': buffsize, 'ascii-str': [ord(i) for i in valuebuff]})
        return parser_object
    
    elif gtype == 'int64':
        parser_object.define_operand({'errtype': False, 'type': gtype, 'value': _Value, 'hexadecimal': hex(int(_Value))})
        return parser_object
    elif gtype == 'float64':
        parser_object.define_operand({'errtype': False, 'type': gtype, 'value': _Value})
        return parser_object
    
    elif gtype == 'bool':
        parser_object.define_operand({'errtype': False, 'type': gtype, 'value': _Value})
        return parser_object
    
    elif gtype == 'gj:group':
        parser_object.define_operand({'errtype': False, 'type': gtype, 'value': _Value})
        return parser_object
    elif gtype == 'gj:counter':
        parser_object.define_operand({'errtype': False, 'type': gtype, 'value': _Value})
        return parser_object
    elif gtype == 'gj:object':
        objectgj = _Value.split(',')
        parser_object.define_operand({'errtype': False, 'type': gtype, 'value': objectgj, 'id': objectgj[2], 'coordinates': [objectgj[3], objectgj[5]]})
        return parser_object
    
    elif gtype == 'pointer64':
        parser_object.define_operand({'errtype': False, 'type': gtype, 'value': _Value, 'intager': int(_Value, 16)})
        return parser_object