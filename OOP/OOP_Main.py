from OOP.user import User
from OOP.post import Post



# creating an object
app_user_one = User("johndoe@gmail.com", "John Doe", "123456969", "DevOps Engineer")
app_user_one.get_user_info()

app_user_one.change_job_title("DevOps Trainer")
app_user_one.get_user_info()

# Creating a new user
app_user_two =User("jamesbond@secretspy.com", "James Bond", "classifiedtins", "Super Agent")
app_user_two.get_user_info()

# creating new post
new_post = Post("I just have No Time To Die", app_user_two.name )
new_post.get_post_info()


