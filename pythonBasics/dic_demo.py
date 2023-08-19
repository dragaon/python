# Sample code which contains usage of
# Dictionary example, importing functions and built-in functions
import helper as validator
import math
import os
import logging

from datetime import datetime, timezone

date_of_join_name = "DOJ"
designation_list = ["VP" ,"SVP" , "AVP" ,"Manager", "Officer"]
employee_dic = {"name" : "Python Programmer" , date_of_join_name : "30-02-2004" ,
                "Designation" : designation_list[1]}
print (f"Employee details using dictionary : {employee_dic}")
print(f"Employee Date of Joining: {employee_dic[date_of_join_name]}")

#Navigate Dictionary
for key in employee_dic.keys():
    print(f"Key and value in dictionary is {key}, {employee_dic[key]}")

#Built in functions
print(datetime.now())
print (os.name)

#Looger
logger = logging.getLogger("dic_demo")
logger.info("Info")
logger.error("Error")