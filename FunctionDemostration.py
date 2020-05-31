# def additional(*nums):
#     total = 0
#     for i in nums:
#         total = total+i
#
#     return total

#Ham lamda
#nhanDoi = lambda a:a*2

#Su dung ham filter va bieu thuc lamda de tim kiem phan tu chan

listSN = [1,2,3,4,5,6,7,8,9,10]
listSC = list(filter(lambda a: a%2 == 0,listSN))
print(listSC)

#Upgrading the new version
