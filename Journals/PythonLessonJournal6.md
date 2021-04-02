# The Jazaltron Learning Journal
## This is the Sixth LessonJournal in the Python series 


###### User Data
    email = "johndoe@email.com"
    name = "John Doe"
    password = "123456969"
    current_job_title = "DevOps engineer"

###### User behavior
    def change_password():
        # do smth
    def change_job_title():
        # do smth 
    def add_new_skill():
        # do smth   

###### Class 
This is a blueprint for all users in a related field that contains 
models for both user data as well as user behavior

###### Object
This is the specific implementation of the class(blueprint)
example each of the millions of peeps on facebook are all objects whose 
data and behavior are modelled after the class.  

####
+ class is like an object constructor 
+ all classes have a __init__() function
+ __init__() is executed automatically, whenever we create the objects from his class 
+ def __init__(self): this is what is called a constructor 
+ it'll help us to construct objects from the class(blueprint)
+ "self" Parameter is a reference to the current instance of the class 
+ Functions that belong to a class are actually called Methods 



#######OOP Syntax 
    
    
    class User:
        def __init__(self, user_email, name, password, current_job_title):
            self.email = user_email
            self.name = name
            self.password = password
            self.current_job_title = current_job_title

        def change_password(self, new_password):
            self.password = new_password
        def change_job_title(self,new_current_job_title):
            self.current_job_title = new_current_job_title
        def get_user_info(self):
            print(f"User {self.name} currently works as a {self.current_job_title}. You can contact them at {self.email }")

    # creating an object

    app_user_one = User("johndoe@gmail.com", "John Doe", "123456969", "DevOps Engineer")
    app_user_one.get_user_info()

    app_user_one.change_job_title("DevOps Trainer")
    app_user_one.get_user_info()
    
    # Creating a new user
    app_user_two =User("jamesbond@secretspy.com", "James Bond", "classifiedtins", "Super Agent")
    app_user_two.get_user_info()
    
    
    
    
#### Object Oriented Programming 
+ In python almost everything is an object
+ str(), int(), ... are the constructor functions

###### API REQUEST
    import requests

    response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
    print(response.text)
    print(type(response.text))


+ json is lightweight format for transporting data 
+ It is often used to send data over the web
+ The requests module basically gives us this json() function which converts 
+ The data from json into python data type 
  
> Basically   
    + Request in JSON => 
    + Response in JSON <=

######## Syntax 
    import requests

    response = requests.get("https://gitlab.com/api/v4/users/nanuchi/projects")
    print(response.json())
    print(type(response.json()))
    print(response.json()[0])



list repository projects 
/repos/{owner}/{repo}/projects



list user projects 
/users/{username}/projects






    