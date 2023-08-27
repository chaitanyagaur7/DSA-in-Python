#PYTHON PROGRAM TO FIND THE SMALLEST INTEGER IN AN ROTATED ARRAY
def binarysearch(nums):
        start = 1
        end = len(nums)-1
        while (start<end):
            mid = start+(end-start)//2
            if L[mid]<L[mid-1]:
                return L[mid]
            elif L[mid]>L[end]:
                start = mid+1
            else:
                end = mid-1

L=[1,1,0,1,1,1,1,1,1,1,1,1]
print(binarysearch(L))