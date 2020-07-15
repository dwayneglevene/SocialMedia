from Users import Users


user1=Users("BillyBob","Billybob@yeehaw.com",27,"lala35")
user2=Users("Jorge","Jeorgyybob@yeehaw.com",27,"lala35")
user3=Users("James","Billybob@yeehaw.com",27,"lala35")


user1.add_post("3/3/3","8:88","This is my first social media post")
user1.add_post("3/3/3","8:88","Hi Friend")

user2.add_post("8/2/3","4:44","Happy James days")


print(user1.list_post())
print(user2.list_post())
