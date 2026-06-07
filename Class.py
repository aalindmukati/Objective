class User:
    def __init__(self, user_id , name , follower , following):
        self.id = user_id
        self.name = name
        self.follower = 0
        self.following

    def follow(self, user):
        user.follower += 1
        self.following += 1

user_1 = ('1',"aalind")
user_2 = ("2","Kratos")

user_2.follow(user_1)

print(user_1,user_2)
print(user_1.follower)
print(user_1.following)
print(user_2.follower)
print(user_2.following)