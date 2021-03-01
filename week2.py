# 第一題 - 函式與流程控制
def calculate(min, max):
    total = 0
    for i in range(min, max+1):
        total += i
    print(total)

calculate(1, 3)
calculate(4, 8)

# 第二題 - python字典與列表
def avg(data):
    add = 0
    for i in range(data["count"]):
        add += data["employees"][i]["salary"]
    print(add/data["count"])

avg({
    "count":3,
    "employees":[
        {
            "name":"John",
            "salary":30000
        }, 
        {
            "name":"Bob",
            "salary":60000
        },
        {
            "name":"Jenny",
            "salary":50000
        }

    ]
})

# 第三題 - 演算法
def maxProduct(nums):
    max_value = 0
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            result = nums[i]*nums[j]
            if result > max_value:
                max_value = result
    print(max_value)
maxProduct([5, 20, 2, 6])
maxProduct([10, -20, 0, 3])

# 第四題 - 演算法
def twoSum(nums, target):
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            result = nums[i]+nums[j]
            if result == target:
                return f"[{i}, {j}]"

result = twoSum([2, 11, 7, 15], 9)
print(result)

# 第五題optional - 演算法
def maxZeros(nums):
    max_zero = 0
    for i in range(len(nums)):
        if nums[i] == 0:
            count_zero = 1
            for j in range(i+1, len(nums)):
                if nums[j] == 0:
                    count_zero += 1
                    if j+1 == len(nums):
                        if max_zero < count_zero:
                            max_zero = count_zero
                else:
                    if max_zero < count_zero:
                        max_zero = count_zero
                    break
    print(max_zero)

maxZeros([0, 1, 0, 0])
maxZeros([1, 0, 0, 0, 0, 1, 0, 1, 0, 0])
maxZeros([1, 1, 1, 1, 1])