#User function Template for python3

class Solution:
    def segregateElements(self, arr, n):
        # Your code goes here
        negatives = []
        positives = []
        for i in arr:
            if i>= 0:
                positives.append(i)
            else: negatives.append(i)
        
        index = 0
        for i in positives:
            arr[index] = i
            index+= 1
        
        for i in negatives:
            arr[index] = i
            index+= 1


#{ 
 # Driver Code Starts
#Initial Template for Python 3


def main():

    T = int(input())

    while(T > 0):
        n = int(input())
        a = [int(x) for x in input().strip().split()]
        ob=Solution()
        ob.segregateElements(a, n)
        print(*a)

        T -= 1


if __name__ == "__main__":
    main()





    
# } Driver Code Ends