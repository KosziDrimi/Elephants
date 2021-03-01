# -*- coding: utf-8 -*-
"""
Created on Mon Mar  1 09:57:00 2021

@author: klimi
"""


with open('data.txt', 'r') as file: 
    lines = file.readlines()
    numbers = lines[0]
    weight = [int(item) for item in lines[1].split()]
    start_position = [int(item) for item in lines[2].split()]
    end_position = [int(item) for item in lines[3].split()]
  
def elephants(weight, start_position, end_position):
    # creating 'scheme' dict {key : val} - 'value' represents the element 
    # that should replace the'key' element  
    scheme = {}
    for idx, item in enumerate(start_position):
        scheme[item] = end_position[idx]

    # creating unique cycles of elements that should be replaced 
    result = [] 
    for key, val in scheme.items():
        if key != val:    # if key is equal to val no modyfication is needed
            cycle = []
            while key not in cycle:
                cycle.append(key)
                key = scheme[key]
            cycle = set(cycle)
            if cycle not in result:
                result.append(cycle)
                                
    # changing cycle sets for lists
    new_result = [list(item) for item in result]
        
    # calculating parameters of the particular cycles
    lowest_all = min(weight) 
    all_cycles = []

    for item in new_result:
        total_weight_cycle = 0
        weight_cycle = []
        for element in item:
            total_weight_cycle += weight[element-1]
            weight_cycle.append(weight[element-1])
        lowest_cycle = min(weight_cycle)   
        lenght_cycle = len(weight_cycle)
        all_cycles.append([total_weight_cycle, lowest_cycle, lenght_cycle])
        
    # counting the final result using the methods described 
    final_result = 0
    for cycle in all_cycles:
        first_method = cycle[0] + (cycle[2] - 2) * cycle[1]
        second_method = cycle[0] + cycle[1] + (cycle[2] + 1) * lowest_all
        final_result += min(first_method, second_method)
    print(final_result)   


if __name__ == "__main__":
    elephants(weight, start_position, end_position)