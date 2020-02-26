
from timeit import default_timer as timer;

data_array = [9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20]

# 鸡尾酒排序
def cocktail_sort(data):
	size = len(data)
	sign = 1
	for i in range(int(size / 2)):
		if sign:
			sign = 0
			for j in range(i, size - 1 - i):
				if data[j] > data[j+1]:
					data[j], data[j+1] = data[j+1], data[j]
			for k in range(size - 2 - i, i, -1):
				if data[k] < data[k-1]:
					data[k], data[k-1] = data[k-1], data[k]
					sign = 1
		else:
			break
	return data

if __name__ == "__main__":

    # 鸡尾酒排序
    print("排序前:\n",data_array)
    start_time = timer()
    cocktailSortData = cocktail_sort(data_array)
    end_time = timer()
    run_time = end_time - start_time
    print("排序后:\n",cocktailSortData)
    print (">>> 鸡尾酒排序运算时间:%.5f秒"%run_time)
    print("=======================================================================")