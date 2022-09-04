# -*- coding: utf-8 -*-
"""
Created on Sat Sep  3 23:49:58 2022

@author: FierceBird//ZiyahVirani
"""

import matplotlib.pyplot as plt
import psutil as p 
app_name_dict = {}
count = 0 
for process in p.process_iter():
    count = count+1
    if count <= 6 :
        name = process.name()
        cpu_usage = p.cpu_percent()
        print(" name : " ,name, "--cpu usage : ", cpu_usage)
        app_name_dict.update({name:cpu_usage})
        keymax=max(app_name_dict,key=app_name_dict.get)
        keymin=min(app_name_dict,key=app_name_dict.get)
        name_list = [keymax,keymin]
        print(name_list)
        app=app_name_dict.values()
        max_app=max(app)
        print(" maximum : ",max_app)
        min_app=min(app)
        print("minimum : ", min_app)
        max_min_list=[max_app,min_app]

plt.figure(figsize=(15,7))
plt.xlabel("Min-Max Cpu Consumption")
plt.ylabel("Usage")
plt.bar(name_list,max_min_list,width=0.6,color=("purple","blue"))
plt.show()



