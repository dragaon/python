# Dictionary example, importing functions and other modules
import helper as validator
import math
import os
import logging

from datetime import datetime, timezone

designation_list = ["VP" ,"SVP" , "AVP" ,"Manager", "Officer"]
employee_dic = {"name" : "Prakasa rao" , "DOJ" : "30-02-2004" ,
                "Designation" : designation_list[1]}
print (employee_dic)
print(employee_dic["DOJ"])
for designation in designation_list :
    print(validator.validateInput(designation))

print(datetime.now())
print (os.name)

logger = logging.getLogger("dic_demo");
logger.info("Info")
logger.error("Error")