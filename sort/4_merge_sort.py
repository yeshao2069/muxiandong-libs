
from timeit import default_timer as timer;

data_array = [9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20]

# 归并排序
def merge_sort(data):
	if len(data) <= 1:
		return data
	num = int( len(data) / 2 )
	left = merge_sort(data[:num])
	right = merge_sort(data[num:])
	return merge(left, right)

def merge(left,right):
	r, l=0, 0
	result=[]
	while l<len(left) and r<len(right):
		if left[l] <= right[r]:
			result.append(left[l])
			l += 1
		else:
			result.append(right[r])
			r += 1
	result += list(left[l:])
	result += list(right[r:])
	return result

if __name__ == "__main__":

    # 归并排序
    print("排序前:\n",data_array)
    start_time = timer()
    mergeSortData = merge_sort(data_array)
    end_time = timer()
    run_time = end_time - start_time
    print("排序后:\n",mergeSortData)
    print (">>> 归并排序运算时间:%.5f秒"%run_time)
    print("=======================================================================")