import java.util.HashMap;
import java.util.LinkedList;

public class LongestSubString {
	
	 public static int lengthOfLongestSubstring(String s) {
	        
	        if(s.isEmpty()){
	            return 0;
	        }
	        
	        int longestCount = 1;
	        int stringHeadIndex = 0;
	        HashMap map = new HashMap();
	        
	        for(int stringTailIndex = 0; stringTailIndex < s.length(); stringTailIndex++){
	        	
	        	if(map.get(s.charAt(stringTailIndex)) == null){
	        		map.put(s.charAt(stringTailIndex),stringTailIndex);
	        		
	        	}
	        	else{
	        		
	        		if((int) map.get(s.charAt(stringTailIndex)) >= stringHeadIndex){
	        			stringHeadIndex = (int) map.remove(s.charAt(stringTailIndex)) + 1;
	        		}
	        		
	        		map.put(s.charAt(stringTailIndex), stringTailIndex);
	        	}
	        	
	        	int subStringLength = stringTailIndex - stringHeadIndex + 1;
        		
        		if(subStringLength > longestCount){
        			longestCount = subStringLength;
        		}
        		
	        }
	        
	        return longestCount;
	    }
	 
	 public static void main(String[] args){
		 
		 System.out.println(lengthOfLongestSubstring("cccc"));
	 }

}
