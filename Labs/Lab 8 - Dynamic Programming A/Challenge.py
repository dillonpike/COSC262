from functools import lru_cache

def routes(input_list):
    n_streets, n_avenues = input_list.pop(0)
    
    @lru_cache
    def route_inner(street, avenue):
        if (street, avenue) in input_list:
            return 0
        elif (street, avenue) == (n_streets - 1, n_avenues - 1) :
            return 1
        elif street == n_streets - 1:
            return route_inner(street, avenue + 1)
        elif avenue == n_avenues - 1:
            return route_inner(street + 1, avenue)
        else:
            return route_inner(street, avenue + 1) + route_inner(street + 1, avenue)
    return route_inner(0, 0)
        
        

i = 1
inp = -1
input_list = []
while inp != "0 0":
    inp = input()
    if inp == "0 0":
        if len(input_list) == 0:
            break
        else:
            print(f"Map {i}: {routes(input_list)}")
            i += 1
            input_list = []
            inp = -1
    else:
        inp = inp.split()
        input_list.append((int(inp[0]), int(inp[1])))   