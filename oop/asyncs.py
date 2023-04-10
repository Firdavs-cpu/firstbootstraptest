# import asyncio
# import time

# async def test1():
#     print('Начало первой функции')
#     await asyncio.sleep(4)
#     print('Конец первой функции')

# async def test2():
#     print('Начало второй функции')
#     await asyncio.sleep(1)
#     print('Конец второй функции')

# async def runFunc():
#     task1 = asyncio.create_task(test1())
#     task2 = asyncio.create_task(test2())

#     await task1
#     await task2
    

# asyncio.run(runFunc())



# import asyncio
# import time


# async def nums1():
#     for i in range(0,100,2):
#         print(i)
#     await asyncio.sleep(1)
#     print('end')

# async def nums2():
#     for x in range(0,200,2):
#         print(x)
#     await asyncio.sleep(1)
#     print('Еще раз "end"')

# async def runFuncs():
#     task1 = asyncio.create_task(nums1())
#     task2 = asyncio.create_task(nums2())

#     await task1
#     await task2

# asyncio.run(runFuncs())










class Constructor:
    def __init__(self, floors):
        self.floors = floors
        self.current_floor = 0
        self.is_built = False
        
    def build(self):
        while self.current_floor < self.floors:
            self.current_floor += 1
            print(f"Строительство {self.current_floor}...")
        
        self.is_built = True
        print("Дом готов!")
        
    def __str__(self):
        if self.is_built:
            return f"В доме {self.floors} этажей."
        else:
            return f"В доме {self.floors} этажей."
        

my_house = Constructor(3)
my_house.build()
print(my_house)


        
