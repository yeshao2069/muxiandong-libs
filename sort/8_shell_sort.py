from timeit import default_timer as timer;

data_array = [9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20]

# 希尔排序
def shell_sort(data):
	import math
	gap = 1
	while(gap < len(data)/3):
		gap = gap*3+1
	while gap > 0:
		for i in range(gap, len(data)):
			temp = data[i]
			j = i - gap
			while j >=0 and data[j] > temp:
				data[j+gap] = data[j]
				j -= gap
			data[j+gap] = temp
		gap = math.floor(gap/3)
	return data

if __name__ == "__main__":

    # 希尔排序
    print("排序前:\n",data_array)
    start_time = timer()
    shellSortData = shell_sort(data_array)
    end_time = timer()
    run_time = end_time - start_time
    print("排序后:\n",shellSortData)
    print (">>> 希尔排序运算时间:%.5f秒"%run_time)
    print("=======================================================================")