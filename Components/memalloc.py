class __allocatebuffer:
    def __init__(self, adress: str, sizet: int|None=None) -> None:
        if sizet == None:
            sizet = 1
        
        self.sizet = sizet
        self.adress_hex = adress
        self.adress_int = int(adress, 16)
        
        self.type = None
        self.valuebuff = [0 for _ in range(sizet)]
    
    
    def set_type(self, type: str) -> None:
        self.type = type
    
    def set_value(self, buffer: int, value: int) -> None:
        self.valuebuff[buffer] = value

__ndadresslist = []
__freelist = []
def __getnextfreeadress() -> int:
    return max(__ndadresslist) + 1


def malloc(size_t: int) -> __allocatebuffer:
    allocbuf = __allocatebuffer(hex(__getnextfreeadress()), size_t)
    __ndadresslist.append(allocbuf.adress_int)
    return allocbuf

def mmap(adress: str, size_t: int) -> __allocatebuffer:
    allocbuf = __allocatebuffer(adress, size_t)
    __ndadresslist.append(allocbuf.adress_int)
    return allocbuf

def free(adress: __allocatebuffer) -> None:
    adress.set_type('undefined')
    __freelist.append(adress.adress_int)
    __ndadresslist.remove(adress.adress_int)

def realloc(adress: __allocatebuffer, size_t: int) -> __allocatebuffer:
    free(adress)
    return mmap(adress.adress_hex, size_t)