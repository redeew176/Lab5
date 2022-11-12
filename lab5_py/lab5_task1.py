from pprint import pprint

num_dict = [{'dec': i,
             'bin': bin(i),
             'oct': oct(i),
             'hex': hex(i)} for i in range(0, 16)]

pprint(num_dict)