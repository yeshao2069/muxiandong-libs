
from timeit import default_timer as timer;

data_array = [9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20, 9, 99, 1,  103, 4, 8, 8, 6, 7, 990, 12, 4, 44, 55, 77, 88, 11, 9, 53, 20]

# 计数排序
def counting_sort(data):
     n=len(data)
     result=[None]*n
     for i in range(n):
          p=0
          q=0
          for j in range(n):
               if data[j]<data[i]:
                    p+=1
               elif data[j]==data[i]:
                    q+=1
          for k in range(p,p+q):
               result[k]=data[i]
     return result

if __name__ == "__main__":

    # 计数排序
    print("排序前:\n",data_array)
    start_time = timer()
    countingSortData = counting_sort(data_array)
    end_time = timer()
    run_time = end_time - start_time
    print("排序后:\n",countingSortData)
    print (">>> 计数排序运算时间:%.5f秒"%run_time)
    print("=======================================================================")