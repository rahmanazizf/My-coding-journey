import numpy as np
import find_largest as fl

#function to calculate statistics
def calculator(a_list):
    arr = []
    stat_dict = {}
    x = 0
    if len(a_list) == 9:
        for _ in range(3):
            arr.append(a_list[x:x+3]) #storing list contains 3 elements each in arr
            x += 3
        
        nump_arr = np.array(arr)
#storing function in dictionary to be used in the following loop
        ops = {"mean":np.average, "variance":np.var, "standard deviation":np.std, "max":np.max, "min":np.min, "sum":np.sum}

        for lab in ops.keys():
            for op in ops.values():
                stat_dict[lab] = stat_dict.get(lab, [[op(nump_arr[i][0:3]) for i in range(3)],
                [op(nump_arr[0:3][i]) for i in range(3)], 
                (sum([op(nump_arr[i][0:3]) for i in range(3)])+sum([op(nump_arr[0:3][i]) for i in range(3)]))])
        return stat_dict       
    else:
        return "List must contain nine number"

print(calculator([0,1,2,3,4,5,6,7,8]))


