# def countdown(n):
#     print("Counting down from", n)
#     while n > 0:
#         yield n # 2
#         n -= 1
#         print("Next call")
#
# x = countdown(3)

def summer(n):
    temp,i = 0,1
    while i <= n:
        temp += i
        yield temp
        i += 1
z = summer(5)
print(z) # Lazy Evaluation
print(list(z))

# for each in x:
#     print(each)


# def check(n):
#     print("step1")
#     yield n
#     print("step2")
#     n -= 1
#     yield n
#     print("step3")
#
#
# x = check(2)
# print(next(x))
# print(next(x))
# print(next(x))


