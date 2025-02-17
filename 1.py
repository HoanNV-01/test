nums = [1, 2, 3, 4]
output = []
for i in range(len(nums)):
   equa = 1
   for j in range(len(nums)): 
      if i != j: equa *= nums[j]
   output.append(equa)
print(output)