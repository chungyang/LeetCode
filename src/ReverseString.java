//Write a function that takes a string as input and returns the string reversed.


class ReverseString{
    public String reverseString(String s) {
        
        char[] c = s.toCharArray();
        int l = c.length-1;
        int mid = (l+1)/2;
        char t;
        for(int i=0; i<mid; i++){
            t = c[i];
            c[i] = c[l-i];
            c[l-i] = t;
        }
        return String.valueOf(c);
    }
}