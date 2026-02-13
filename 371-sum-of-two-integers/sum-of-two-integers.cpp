class Solution {
public:
    int getSum(int a, int b) {
        int nsum= a^b;
        int carry=a&b; 
       int new_carry=carry<<1;

     while(carry!=0)
         {
            carry=(nsum&new_carry);
         nsum=(nsum^new_carry);
         
         new_carry=(carry<<1);

         }
        
        return nsum;
    }
};