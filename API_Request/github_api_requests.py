import requests

response = requests.get("https://api.github.com/users/JAZALTRON10/projects")

#my_projects = response.json()


print(response.json())
print(type(response.json()))
#print(response.json()[0])



# for project in my_projects:
#     print(f"Project Name: {project['name']}\n Project Url: {project['web_url']}\n ")











