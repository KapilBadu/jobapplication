
#include<stdio.h>

 int main()                           // c program to get the n'th number of fibonacci series 
  {
      int n=9;                          // here we are trying to find 9th position fibonacci number 

      printf("F(n) =%d", findfibo(n));
      
      return 0;
  }


 int findfibo(int n)             // function to find the nth fibonacci number 
  {
     if (n<=1) {
         return n;
     }
      
     return findfibo(n-1) + findfibo(n-2);

   }
    
    

  