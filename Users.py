class Users:

  def __init__(self,userName,email,age,password):
    self.userName = userName
    self.email = email
    self.age = age
    self.password = password
    self.posts=[]
    
  def add_post(self,date,time,text):
    status = Post(date,time,text)#creates post
    self.posts.append(status)
    #each user gets to add a post

  def list_post(self):
    display= self.userName + " posted the following: \n\n"
    count=1#keeps track of posts
    for post in self.posts:#for each user
      display += f"{count}. \t{post.display_post()}\n\n"
      count+=1

      #display +=  '{post.display()} \n\n'
    return display
    #this funstion creates a list of post for each user
   
class Post:

  def __init__(self,date,time,text):
    self.date=date
    self.time=time
    self.text=text

  def display_post(self):
    return f'on {self.date} at {self.time}  posted \n"{self.text}"'

    #You can only concacat a string not a set or a dictionry so you have to format your return like this inorder for it to work

    #\n just meants new line , \t just means new tab