## import modules here 
import pandas as pd
import numpy as np
import copy

################# Question 1 #################
# def v_opt_dp(x, num_bins):# do not change the heading of the function

#     global _x, _num_bins, dp_matrix, dp_index

#     dp_matrix = [[-1 for i in range(len(x))] for j in range(num_bins)]
#     dp_index = [[-1 for i in range(len(x))] for j in range(num_bins)]
#     _x = x
#     _num_bins = num_bins
#     _v_opt_dp(0, num_bins-1) #bin is 0-3

#     start = dp_index[-1][0]
#     pre_start = start
#     bins = [x[:start]]
#     for i in range(len(dp_index)-2, 0, -1):
#         start = dp_index[i][start]
#         bins.append(x[pre_start:start])
#         pre_start = start
#     bins.append(x[pre_start:])
#     return dp_matrix, bins

# def _v_opt_dp(mtx_x, remain_bins): #mtx_x is the index of x, we will put
#                                     #all element behind it to the reamin bin
    
#     global _x, _num_bins, dp_matrix, dp_index
    
#     if( _num_bins - remain_bins - mtx_x < 2) and (len(_x) - mtx_x > remain_bins):
#         _v_opt_dp(mtx_x+1, remain_bins)
#         if(remain_bins == 0):
#             dp_matrix[remain_bins][mtx_x] = np.var(_x[mtx_x:])*len(_x[mtx_x:])
#             return 

#         _v_opt_dp(mtx_x, remain_bins - 1)  

#         min_list = [dp_matrix[remain_bins-1][mtx_x+1]]

#         for i in range(mtx_x+2, len(_x)):
#             min_list.append(dp_matrix[remain_bins-1][i] + (i - mtx_x)*np.var(_x[mtx_x:i])) 

#         dp_matrix[remain_bins][mtx_x] = min(min_list)
#         dp_index[remain_bins][mtx_x] = min_list.index(min(min_list)) + mtx_x +1

def sse(l):
    return np.var(l)*len(l)
    # a = np.array(l)
    # E = np.mean(a)
    # SSE = 0
    # for i in a:
    #     SSE += (i-E)**2
    # if(SSE == 0.0):
    #     SSE = 0
    # return SSE

def v_opt_dp(x, b):# do not change the heading of the function
    matrix = [([-1]*len(x)) for p in range(b)]
    #base
    base = b
    bin_buff = [(-1) for p in range(len(x))]
    while(base <= len(x)):
        matrix[0][base-1] = sse(x[base-1:])
        bin_buff[base-1] = x[base-1:]
        base += 1
    #body
    base = 1
    #outer loop around bins
    while(base < b):
        #location of the element in current row
        current = b-base -1
        #loop around current row
        while(current < len(x)-base):
            #loop around last row
            d = {}
            last = current + 1
            l1 = x[current:]
            cache = []
            while(last <  len(x)-base + 1):
                temp = x[current:last]
                sum_sse = sse(temp) + matrix[base-1][last]
                if(isinstance(bin_buff[last][0],list)):
                    s = copy.deepcopy(bin_buff[last])
                    s.insert(0,temp)
                    d[sum_sse] = s
                else:
                    d[sum_sse] = [temp,bin_buff[last]]
                cache.append(sum_sse)
                last += 1
                
            matrix[base][current] = min(cache)
            bin_buff[current] = d[min(cache)]
            current += 1
        bin_buff[-base] = -1
        base += 1
    return matrix,bin_buff[0]
