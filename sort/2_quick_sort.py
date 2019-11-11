from timeit import default_timer as timer;

data_array = [9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20]


# 快速排序 分治+递归
def quick_sort(data):
	if len(data) >= 2:
		# 选取基准值，也可以选取第一个或最后一个元素
		mid = data[len(data)//2]
		# 定义基准值左右两侧的列表
		left, right = [], []
		# 从原始数组中移除基准值
		data.remove(mid)
		for num in data:
			if num >= mid:
				right.append(num)
			else:
				left.append(num)
		return quick_sort(left) + [mid] + quick_sort(right)
	else:
		return data


if __name__ == "__main__":

    # 快速排序
    print("排序前:\n",data_array)
    start_time = timer()
    quickSortData = quick_sort(data_array)
    end_time = timer()
    run_time = end_time - start_time
    print("排序后:\n",quickSortData)
    print (">>> 快速排序运算时间:%.5f秒"%run_time)
    print("=======================================================================")