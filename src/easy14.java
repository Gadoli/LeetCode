/*
LeetCode - Easy 14. Longest Common Prefix
*/
class Solution {
    public String longestCommonPrefix(String[] strs) {
        if (strs.length==0) return "";
        if (strs.length==1) return strs[0];
        StringBuilder res = new StringBuilder();
        int max_tmp = Math.min(strs[0].length(), strs[1].length());

        for (int i = 0; i<max_tmp; i++){
            if (((strs[0]).charAt(i))==((strs[1]).charAt(i))){
                res.append(strs[0].charAt(i));
            }else{
                i=max_tmp;
            }
        }

        for (int i = 2; i<strs.length; i++){
            int length = res.length();
            int length_str = strs[i].length();
            if (length==0) return "";
            if (length_str==0) return "";
            for (int j=0; j<Math.min(length, length_str); j++){
                if (!((res.charAt(j))==(strs[i].charAt(j)))) {
                    res.delete(j,length);
                    j=length;
                }else{
                    if (j==(length_str-1) & j!=length){
                        res.delete(j+1, length);
                        j=length+length_str;
                    }
                }
            }
        }

        return res.toString();
    }
}
