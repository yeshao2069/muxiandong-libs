
from timeit import default_timer as timer;

data_array = [9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20]

# 选择排序 
def selection_sort(data):
	for i in range(len(data) - 1):
		# 记录最小数的索引
		minIndex = i
		for j in range(i + 1, len(data)):
			if data[j] < data[minIndex]:
				minIndex = j
		# i 不是最小数时，将 i 和最小数进行交换
		if i != minIndex:
			data[i], data[minIndex] = data[minIndex], data[i]
	return data

if __name__ == "__main__":

    # 选择排序
    print("排序前:\n",data_array)
    start_time = timer()
    selectionSortData = selection_sort(data_array)
    end_time = timer()
    run_time = end_time - start_time
    print("排序后:\n",selectionSortData)
    print (">>> 选择排序运算时间:%.5f秒"%run_time)
    print("=======================================================================")