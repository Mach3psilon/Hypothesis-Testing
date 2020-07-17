# -*- coding: utf-8 -*-
"""
Created on Fri Jun 26 09:18:40 2020

@author: atebu
"""
import numpy as np

file1 = open("titanic_data.txt","r")
class_0 = 0
class_1 = 0
class_2 = 0
class_3 = 0
surv_0 = 0
surv_1 = 0
surv_2 = 0
surv_3 = 0
returning = []
text_data = file1.readlines()
for i in text_data:
    a=i.split('\t')
    
    if a[0] == "0":
        class_0 += 1
        if a[1] == "1\n":
            surv_0 += 1
    elif a[0] == "1":
        class_1 += 1
        if a[1] == "1\n":
            surv_1 += 1
    elif a[0] == "2":
        class_2 += 1
        if a[1] == "1\n":
            surv_2 += 1
    elif a[0] == "3":
        class_3 += 1
        if a[1] == "1\n":
            surv_3 += 1
sample_mean_0 = surv_0/class_0
returning.append(sample_mean_0)
sample_mean_1 = surv_1/class_1
returning.append(sample_mean_1)
sample_mean_2 = surv_2/class_2
returning.append(sample_mean_2)
sample_mean_3 = surv_3/class_3
returning.append(sample_mean_3)
sample_mean_all = (surv_0+surv_1+surv_2+surv_3)/(class_0+class_1+class_2+class_3)
all_except_first = (surv_0+surv_2+surv_3)/(class_0+class_2+class_3)
returning.append(sample_mean_all)
returning.append(class_0)
returning.append(class_1)
returning.append(class_2)
returning.append(class_3)
returning.append(all_except_first)
returning.append(class_0+class_2+class_3)
returning.append(class_0+class_1+class_2+class_3)


file1.close()
    

    
def distribute_binomialy(number_of_trials,probability,sample_size):
    N = number_of_trials
    p = probability
    Y = []
    for j in range(sample_size):
        X = []
        for i in range(N):
            u = np.random.rand()
            x = u<p
            X.append(x)
        y = sum(X)
        
        Y.append(y)
    return Y
def calculate_mean(numbers):
    sumof = 0 
    for i in numbers:
        sumof += i
    return sumof/len(numbers)

def return_a_mean_list(number_of_trials,probability,sample_size,list_size):
    returning_list = []
    for i in range(list_size):
        dist = distribute_binomialy(number_of_trials,probability,sample_size)
        mean = calculate_mean(dist)
        returning_list.append(mean)
    return returning_list
def print_means(numbers):
    print("The averages for the whole data, crew data, first class, second class and third class data are",round(numbers[4], 2)+",",round(numbers[0], 2)+",",round(numbers[1], 2)+",", round(numbers[4], 2),"and", round(numbers[3], 2),"respectively.")

def differ(first_mean,second_mean,first_length,second_length,deviation):
    total_length = first_length + second_length
    difference_between_means = first_mean-second_mean
    list_size = 100
    data_1 = return_a_mean_list(first_length,total_length,list_size)
    data_2 = return_a_mean_list(second_length,total_length,list_size)
    data_diff = []
    for i in range(len(data_1)):
        data_diff.append(data_1[i] - data_2[i])
    p_before_divide = 0
    p_crew_third_list = []
    for i in data_diff:
        if i < -difference_between_means or i > difference_between_means:
            p_before_divide+=1
            p_crew_third_list.append(i)
    p = p_before_divide/list_size
    print(p)
differ(sample_mean_0,sample_mean_3,class_0,class_3,0.1)





















            
        
        
