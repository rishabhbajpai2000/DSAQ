class Solution {
    public int[][] flipAndInvertImage(int[][] image) {
        for (int i = 0; i < image.length; i++){
            int start = 0; 
            int end = image[i].length-1;
            while (start <= end){
                int temp = image[i][start];
                image[i][start] = image[i][end];
                image[i][end] = temp;
                
                if (image[i][start] == 1){
                    image[i][start] = 0;
                }
                else{
                    image[i][start] = 1;
                }
                
                if (image[i][end] == 1){
                    image[i][end] = 0;
                }
                else{
                    image[i][end] = 1;
                }
                start++;
                end--;
            }
            
            
            if ((image[i].length)%2 != 0){
                int mid = (image[i].length + 1)/2 - 1;
                 if (image[i][mid] == 1){
                    image[i][mid] = 0;
                }
                else{
                    image[i][mid] = 1;
                }   
            }
            }
        return image;
        }
    
    }
