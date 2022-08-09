import numpy as np

#function to calculate statistics
def calculate(a_list):
    arr = []
    stat_dict = {}
    x = 0
    try:
        for _ in range(3):
            arr.append(a_list[x:x+3]) #storing list contains 3 elements each in arr
            x += 3
        
        nump_arr = np.array(arr, dtype=int, ndmin=2)
#storing function in dictionary to be used in the following loop
        ops = {"mean":np.average, "variance":np.var, "standard deviation":np.std, "max":np.max, "min":np.min, "sum":np.sum}

        for lab, op in ops.items():
            stat_dict[lab] = stat_dict.get(lab, [[op(nump_arr[0:3, i]) for i in range(3)],
            [op(nump_arr[i, 0:3]) for i in range(3)],
            op(nump_arr)])
        return stat_dict      
    except:
        raise ValueError("List must contain nine numbers.")

print(calculate([9,1,5,3,3,3,2,9,0]))

