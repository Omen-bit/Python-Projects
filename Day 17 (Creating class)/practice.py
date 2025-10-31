class User:
    def __init__(self,id,username,followers):
        self.id=id
        self.username=username
        self.followers=followers
        self.following=0

    def follow(self,user):
        user.followers+=1
        self.following+=1

user1=User("001","darshan",0)
user2=User("002","rohit",0)

user1.follow(user2)
user2.follow(user1)

print(user1.followers,user1.following)
print(user2.followers,user2.following)