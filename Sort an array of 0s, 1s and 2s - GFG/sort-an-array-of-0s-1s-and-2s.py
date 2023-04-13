#User function Template for python3

class Solution:
    def sort012(self,arr,n):
        # code here
        count = [0,0,0]
        for i in arr:
            count[i] += 1

        index = 0
        # for i in enumerate(count): print(i)
        for elem,freq in enumerate(count):
            # print(elem, freq)
            for j in range(freq):
                arr[index] = elem
                index+= 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    t=int(input())
    for _ in range(t):
        n=int(input())
        arr=[int(x) for x in input().strip().split()]
        ob=Solution()
        ob.sort012(arr,n)
        for i in arr:
            print(i, end=' ')
        print()

# } Driver Code Ends