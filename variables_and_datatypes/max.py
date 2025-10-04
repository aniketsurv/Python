arr = [1,2,3,6,9]

ar = max(arr)
for x in range(ar):
    if x>0:
        if x not in arr:    
            print(x)
    
     


# str= "AAniket"

# # tr = str.count()
# # print(tr)

# arr = list(str)
# # print(arr)

# for el in arr:
#     strmm = str.count(el)
#     print(el , strmm)


# try:
#   a = [2,4,6]
#   print(a[5])
# except Exception as e:
#   print(e)
  


# dicttt = {
#     "abc":[{'a':'amol'},{'n':'nhavi'}],
#     "pqr":[3,9,8]   
# }
# a = dicttt['abc'][1]['n']
# print(a)

# for di in dicttt: 
#     if di != "pqr":
#         for s in dicttt[di]:
#             for ele in s:
#                 if s[ele] == 'nhavi': 
#                     print(s[ele])           