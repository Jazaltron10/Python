class User:
    def __init__(self, user_email, name, password, current_job_title):
        self.email = user_email
        self.name = name
        self.password = password
        self.title = current_job_title

    def change_password(self, new_password):
        self.password = new_password
    def change_job_title(self,new_current_job_title):
        self.title = new_current_job_title
    def get_user_info(self):
        print(f"User {self.name} currently works as a {self.title}. You can contact them at {self.email}\n")

