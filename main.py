import pandas as pd
import openpyxl
import numpy as np

df = pd.read_excel ('golf shots.xlsx',dtype = {"club": str,"shot type": str,
                            "outcome":str,"distance": float, "out of bounds":bool,}) #place "r" before the path string to address special character, such as '\'. Don't forget to put the file name at the end of the path + '.xlsx'
arr=df.to_numpy()
fairway_distance_list=[]
for x in arr:
  if ((x[0]=='driver') and (x[2]=='fairway')):
      fairway_distance_list.append(x[3])
fairway_distance_arr = np.array(fairway_distance_list)

print('25% ')
print(np.quantile(fairway_distance_arr,0.25))
print('50% ')
print(np.mean(fairway_distance_arr))
print('75% ')
print(np.quantile(fairway_distance_arr,0.75))