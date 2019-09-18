class MaxHeapify:

    def __init__(self):
        pass
        
    def parent(self,i):
        return (i-1)//2

    def left(self,i):
        return 2*(i+1)-1

    def right(self,i):
        return 2*(i+1)

    #在堆排序时，会把最大值与堆的最后一个结点交换，即将根结点移除，但其实根结点还在堆数组中，
    #所以得设置堆大小，避免重建堆时，又将其加入到堆中
    def max_adus_heapify(self,arr,i,heap_size):
        left = self.left(i)
        right = self.right(i)
        if left < heap_size and arr[left]>arr[i]:
            largest = left
        else:
            largest = i 
        if right < heap_size and arr[right] > arr[largest]:
            largest = right
        if largest != i:
            temp = arr[i]
            arr[i] = arr[largest]
            arr[largest] = temp
            self.max_adus_heapify(arr,largest,heap_size)

    '''
    至底向上构建最大堆，因为i>arr.length/2下标出的结点都为叶结点，所以可以从arr.length/2开始
    '''
    def build_max_heapify(self,arr):
        for i in range(len(arr)-1,-1,-1):
            self.max_adus_heapify(arr,i,len(arr))

    '''
    首先构建最大堆，使用最大堆进行堆排序
    将最大堆中根结点（最大值）与堆末尾结点交换,因为交换后的堆可能不是最大堆了，所以得重建堆，但是堆的大小将减少1
    '''
    def heap_sort(self,arr):
        heap_size = len(arr)
        #构建最大堆
        self.build_max_heapify(arr)
        for i in range(len(arr)-1,0,-1):
            temp = arr[i]
            arr[i] = arr[0]
            arr[0] = temp
            heap_size -= 1
            self.max_adus_heapify(arr,0,heap_size)

if __name__ == '__main__':
    arr = [30,45,22,72,9,12,26,80,22,43,1]
    max_heapify = MaxHeapify()
    max_heapify.heap_sort(arr)
    print(arr)
