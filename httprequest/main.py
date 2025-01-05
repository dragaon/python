#Program for demonstrating API call

import requests
import logging

logger = logging.getLogger("httprequest")

response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
#response = requests.get("https://gitlab.com/api/v4/users/dragaon/projects")
my_projects = response.json()



# print the whole objects list
print(f"Response from Gitlab is : {my_projects}\n")
print(f"Type of response object is : {type(my_projects)}\n")

# print just the names and urls
for project in my_projects:
    print(f"Project Name: {project['name']}\nProject Url: {project['http_url_to_repo']}\n")

try:
    response = requests.get("https://gitlab.com/api/v4/users/dragaon/projects")
    my_projects = response.json()
    # print the whole objects list
    print(f"Response from Gitlab is : {my_projects}\n")
    print(f"Type of response object is : {type(my_projects)}\n")
except  Exception as error:
    logger.error(f"Error while getting projects list from gitlab {error} and"
                 f"the type of error is {type(error).__name__} "
                 f"and the cause is {error.with_traceback()}")
