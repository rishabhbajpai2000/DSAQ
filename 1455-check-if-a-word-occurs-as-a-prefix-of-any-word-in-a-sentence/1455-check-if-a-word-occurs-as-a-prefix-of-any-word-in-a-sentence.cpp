// class Solution {
// public:
//     int isPrefixOfWord(string sentence, string searchWord) {
        
//         int count=0;
        
//         for(int i=0 ; i<sentence.size() ; i++)
//         {
//             if(sentence[i]==' ')
//                 count++;
            
//             if(sentence[i]==searchWord[0] && i==0)
//             {
//                 string compare=sentence.substr(i,searchWord.size());
                
//                  if(compare==searchWord)
//                     return count+1;
            
//             }
//             if(sentence[i]==searchWord[0] && sentence[i-1]==' ')
//             {
//                 string compare=sentence.substr(i,searchWord.size());
                
//                  if(compare==searchWord)
//                     return count+1;
            
//             }

//         }
        
//         return -1;
//     }
// };

class Solution {
public:
    int isPrefixOfWord(string sentence, string searchWord) {
        
        int count=0;
        
        for(int i=0 ; i<sentence.size() ; i++)
        {
            if(sentence[i]==' ')
                count++;
            
            if(sentence[i]==searchWord[0] && i==0)
            {
                string compare=sentence.substr(i,searchWord.size());
                
                 if(compare==searchWord)
                  return count+1;
            
            }
            
           else if(sentence[i]==searchWord[0] && sentence[i-1]==' ')
            {
                string compare=sentence.substr(i,searchWord.size());
                
                 if(compare==searchWord)
                     return count+1;
            
            }
            
           
            
        }
        
        return -1;
    }
};