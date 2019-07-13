## import modules here 
import pandas as pd
import numpy as np
import helper

################# Question 1 #################

# you can call helper functions through the helper module (e.g., helper.slice_data_dim0)

def buc_rec_optimized(df):# do not change the heading of the function
    dims = df.shape[1]
    tuples = df.shape[0]
    
    if tuples == 1:
        if dims > 1:
            name_list = list(df)
            length = 2**(dims-1)
            aa = np.array([['ALL']*len(name_list)]*length)
            last_name = name_list[-1]
            newdf = pd.DataFrame(aa,columns = name_list)
            newdf[last_name] = list(df[last_name])*length
            i = 0
            while i < dims - 1:
                parameter = int(length/(2**(i+1)))
                newdf[name_list[i]] = (list(df[name_list[i]])*parameter + ['ALL']*parameter)*(2**i)
                i = i + 1
                
            return newdf
        else:
            newdf = df.copy()
            return newdf
    
    else:
        
        if dims == 1:######这个地方有bug
            
            all_sum = sum(helper.project_data(df,0))####把他们按照不同的列来分开（A，B，M）
            value = np.array([all_sum])
            newdf = pd.DataFrame(value,columns = list(df))
            return newdf
            
        else:
            dim0_vals = set(helper.project_data(df,0).values)#####第0列上面的数值
            column_name = df.columns[0]
            newdf = pd.DataFrame(columns = list(df))
            for dim0_v in dim0_vals:
                sub_data = helper.slice_data_dim0(df,dim0_v)###切片按照第一列的每一个数
                i = buc_rec_optimized(sub_data)####剩余数据重来 sub_data前加上dim0_v
                i = i.reindex(columns = [column_name]+list(i))
                i = i.fillna(dim0_v)
                newdf = pd.concat([newdf,i])
            sub_data = helper.remove_first_dim(df)
            i = buc_rec_optimized(sub_data)#前面加上一列ALL
            i = i.reindex(columns = [column_name]+list(i))
            i = i.fillna('ALL')
            newdf = pd.concat([newdf,i])
            newdf.index = [x for x in range(0,len(newdf))]
            
            #newdf[df.columns[-1]] = newdf[df.columns[-1]].astype(int)
            return newdf
        
def read_data(filename):
    df = pd.read_csv(filename, sep='\t')
    return (df)   

################# Question 2 #################

def v_opt_dp(x, num_bins):# do not change the heading of the function
    if num_bins > len(x):
        matrix = num_bins*[[-1]*len(x)]
        bins = [[]]*num_bins
        return matrix,bins
    matrix = num_bins*[[]]
    bins = [[]]*num_bins
    # the case row one is different
    matrix[0]=matrix[0]+[-1]*(num_bins-1)
    bins[0] = bins[0]+[-1]*(num_bins-1)
    i = num_bins - 1
    while i < len(x)-1:
        sse_list = x[i:]
        bins[0].append([sse_list])
        avg = sum(sse_list)/len(sse_list)
        sse = 0
        for parameter in sse_list:
            sse = sse + (avg-parameter)**2
        matrix[0].append(sse)
        i = i + 1
    matrix[0].append(0)
    bins[0].append([[x[-1]]])
    #print(matrix[0],bins[0])
    ### row 2 and following    
    row = 2 
    while row <= num_bins:
        matrix[row-1]=matrix[row-1]+[-1]*(num_bins-row)
        bins[row-1]=bins[row-1]+[-1]*(num_bins-row)
        star_pos = num_bins-row####4-2=2
        end_pos = len(x) - row#####6-2=4
        step = star_pos
        while step < end_pos:
            sse_comp_list = []###生成一个sse的对比，从而选出最小的
            bin_comp_list=[]
            i = 0
            for sse_in_below in matrix[row-2][step+1:len(x)-row+2]:
                #print(matrix[row-2][step+1:len(x)-row+2],sse_in_below)
                sse_list = x[step:step+i+1]
                #print(sse_list,bins[row-2][step+1+i])
                bin_list = [sse_list]+bins[row-2][step+1+i]
                #print(bin_list)
                avg = sum(sse_list)/len(sse_list)
                sse_in_there = 0
                for element in sse_list:
                    sse_in_there = sse_in_there + (avg-element)**2
                new_sse = sse_in_below + sse_in_there
                #print(new_sse,sse_in_below,sse_in_there)
                sse_comp_list.append(new_sse)
                bin_comp_list.append(bin_list)
                i = i + 1
            #print(sse_comp_list,bin_comp_list) 
            matrix[row-1].append(min(sse_comp_list))
            bin_in=bin_comp_list[sse_comp_list.index(min(sse_comp_list))]
            bins[row-1].append(bin_in)
            #print(bins[row-1])
            step = step + 1
        matrix[row-1].append(0)
        bins[row-1].append([[x[-row]]]+bins[row-2][1-row])
        matrix[row-1]=matrix[row-1]+[-1]*(row-1)
        bins[row-1]=bins[row-1]+[-1]*(row-1)
        row = row + 1
    ####talk about bins
    
    return matrix,bins[-1][0]         
            
            
            
            
     # **replace** this line with your code