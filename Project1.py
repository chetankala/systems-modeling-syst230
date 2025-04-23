#Project 1
import csv
import json

#Task 1: Read & Write file
def output_tab():
    input_name = input("Enter name of .csv file: ")
    output_name = input("Enter name of .tab file: ")
  
    file = open(input_name)
    list1 = file.readlines()
    file.close()

    file2 = open(output_name, 'w')
    for i in list1:
        j = i.replace(',','\t')
        file2.write(j) 
    
    file2.close()

print(output_tab())


# Task 2: Read & Write File -- JSON 
def JSON_output():
    input_name = input("Enter name of .csv file: ")
    output_name = input("Enter name of .JSON file: ")

    from csv import DictReader
    with open(input_name, 'r') as line:
        dict1= DictReader(line)
        list1 = list(dict1)
    
    jf = open(output_name, "w")
    for dicts in list1:
        line = json.dumps(dicts)
        jf.write(line)
    jf.close()
    
print(JSON_output())


#Task 3: convert to list of tuples
def list_of_tuples():
    name = input("Enter name of .csv file: ")
    from csv import reader
    with open(name, 'r') as line:
        read = reader(line)
        list1 = list(map(tuple, read))
        return(list1)

print(list_of_tuples())


# Task 4: Convert the File to list of dictionaries
def list_of_dicts():
    input_name = input("Enter name of .csv file: ")
    from csv import DictReader
    with open(input_name, 'r') as line:
        dict1= DictReader(line)
        list1 = list(dict1)
        return(list1)
print(list_of_dicts())


#Task 5: Unique Groups
def unique_groups():
    
    input_name = input("Enter name of .csv file: ")
    from csv import DictReader
    with open(input_name, 'r') as line:
        dict1= DictReader(line)
        list1 = list(dict1)
        
        group_list = list()
        
        for i in list1:
            x = i["Group"]
            if x not in group_list:
                group_list.append(x)
            else:
                continue
        return group_list
print(unique_groups())


#Task 6: Unique Item Categories
def unique_categories():
    input_name = input("Enter name of .csv file: ")
    from csv import DictReader
    with open(input_name, 'r') as line:
        dict1= DictReader(line)
        list1 = list(dict1)
        
        Category_list = list()
        
        for i in list1:
            x = i["Item Category"]
            if x not in Category_list:
                Category_list.append(x)
            else:
                continue
        return Category_list

print(unique_categories())


#Task 7: Count of Record in a Group 
def count_record_group():
    name = input("Enter name of .csv file: ")

    file = open(name)
    list1 = file.readlines()
    file.close()

    list2=[]
    list3=[]

    for i in list1:
        list2=list(i.split(','))
        tuple1 = tuple(list2)
        list3.append(tuple1)
        list2=[]

    count = 0
    group = input("Enter group name: ")

    for i in (list3):
        if group in i:
            count+=1
    return count

print(count_record_group())


#Task 8: Total Cost for all Orders in Group
def totalcost_in_group():
    input_name = input("Enter name of .csv file: ")
    group_name = input("Enter group name: ")

    from csv import DictReader
    with open(input_name, 'r') as line:
        dict1= DictReader(line)
        list1 = list(dict1)

    total_cost = 0
    for dictionary in list1:
        if ('Group', group_name) in dictionary.items():
            cost = float(dictionary['Item Total'][1:]) #to remove $sign
            total_cost += cost

    return(round(total_cost,2))

print(totalcost_in_group())
  