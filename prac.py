# capitals={
#     "India":"Delhi",
#     "France":"Paris",
#     "USA":"Washignton DC",
#     "Japan":"Tokyo",
# }
#
# travel_logs={
#     "USA":"Washignton DC",
#     "Japan":"Tokyo",
#     "countries_visited":{
#         "Cities_visited":8,
#         "India":["pune","mumbai","manali",],
#     },
# }
#
# print(travel_logs["countries_visited"]["Cities_visited"])
#
# # print(travel_logs["France"][1])
#
# # nested_list=["A","B",["C","D"]]
# # print(nested_list[2][1])
from operator import indexOf

from pkginfo import index

# order = {
#     "starter": {1: "Salad", 2: "Soup"},
#     "main": {
#         1: ["Burger", "Fries"],
#         2: ["Steak"]
#     },
#     "dessert": {1: ["Ice Cream"], 2: []},
# }
#
# print(order["main"][1][0])

# print(3/2) #float
# print(3//2) #integer

# list1=[1,2,3]
# list2=[5,4,6]
#
# list3=list1 + list2
# print(list3)
class Solution:
    def longestSubarray(self,List):
        List2 = []
        for num in range(len(List)):
            if List[num] == 0:
                List2.append(num)

        if len(List2) == 0 or len(List2) == 1:
            return len(List - 1)

        large = 0
        for ele in range(len(List2) - 1):
            current = List2[ele + 1] - List2[ele]
            large = max(current, large)

        return large + 1


    longestSubarray(List=[1,1,1,0,1,0,1])

