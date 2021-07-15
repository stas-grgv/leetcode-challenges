import re
def get_int(s:str)->int:
    pattern = '^\W*(x*(-?\d+))'
    s = re.search(pattern, s)
    try:
        s = int(s.group(0))
        print(s)
        if s in range(-2**31, (2**31)-1):
            return s
        elif s < -2**31:
            s = -2**31
        elif s >= 2**31:
            s = 2**31 - 1
        return s
    except:
        s = 0
        return s
    
print(get_int("     -42"))