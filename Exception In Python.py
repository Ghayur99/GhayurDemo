ItemInCart = 0

# 2 items are added in the cart

#if ItemInCart != 2:
    #raise Exception("Product item dose not matched")

#assert (ItemInCart != 0)  # if assert condition is false then it will give assertionerror

# try and except is used when user do not want to fail the test event it is failed it will run the code written in except part

try:
    with open('tet.txt', 'r') as reader:

        print(reader.read())
except:
    print("As try condition is failed except code is runing")
# to get the error message that was given by the pycharm
try:
    with open('tet.txt', 'r') as reader:
     print(reader.read())
except Exception as e:
        print(e)
