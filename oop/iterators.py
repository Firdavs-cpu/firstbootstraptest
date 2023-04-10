# class Test:
#     def __iter__(self):
#         return self
    
#     def __init__(self, number):
#         self.number = number
#         self.counter = 0
    
#     def __next__(self):
#         if self.counter < self.number:
#             self.counter+=1
#             return self.counter
#         else:
#             raise StopIteration

# test1 = Test(5)
# for i in test1:
#     print(i)



# class Test:
#     def __iter__(self):
#         return self
    
#     def __init__(self, word):
#         self.word = word
#         self.count = 0

#     def __next__(self):
#         if self.count < len(self.word):
#             t = self.count
#             self.count += 1
#             return self.word[t]
#         else:
#             raise StopIteration


# test1 = Test('Hello')

# for i in test1:
#     print(i)



# my_text = 'hello'
# for char in my_text:
#     print(char)



# def printText(arg):
#     n = 0
#     while arg > 1:
#         n+=1
#         arg -=1
#         yield '*' * n

# starts = printText(10)
# for i in starts:
#     print(i)


# def my_range(start, stop=None, step=1):
#     if stop is None:
#         stop = start
#         start = 0

#     i = start

#     while i < stop:
#         yield i
#         i += step
# for i in my_range(0,10,2):
#     print(i)


