class Solution {
    public int reverse(int x) {
        
        char[]arr =  String.valueOf(x).toCharArray();
        String temp = "";
        for (int i=arr.length-1;i>=0;i--){    // [-], [2], [3]
            if (arr[i] == '-'){   // arr.lenght = 3, 
                break;
            }
           temp += arr[i]; // temp = 3 2 
        }
        String s =  String.valueOf(Integer.MAX_VALUE);

        if (temp.length() > s.length()){
            return 0;
        }else if ( temp.length() == s.length()){
                if (Integer.MAX_VALUE <= Long.valueOf(temp)){
                   return 0; 
                }
            }
        
        Integer test = Integer.parseInt(temp);
        if (x<0){
            test = test* -1;
        }
        return test;
    }
}