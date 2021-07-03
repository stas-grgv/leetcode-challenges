nums = [2,7,11,15]
target = 9

def solution(array, target):
	i1 = 0
	i2 = 1
	sol = []
	found = False
	for i1 in range(0, len(array)):
		for i2 in range(i1+1, len(array)):
			print(str(array[i1])+ ", " + str(array[i2]))
			sum = array[i1]+array[i2]
			if sum == target:
				print("done")
				found = True
				sol = [i1,i2]
				break
			else:
				continue
		if found:
			break
					
	return sol


print(solution(nums, target))