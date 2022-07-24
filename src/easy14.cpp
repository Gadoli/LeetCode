/*
LeetCode - Easy 14. Longest Common Prefix
*/
class Solution {
public:
    string longestCommonPrefix(vector<string>& strs) {
        if (strs.size()==0) return "";
        if (strs.size()==1) return strs[0];
        string res = "";
        int max_tmp = min(strs[0].size(), strs[1].size());

        for (int i = 0; i<max_tmp; i++){
            if (((strs[0])[i])==((strs[1])[i])){
                res += strs[0][i];
            }else{
                i=max_tmp;
            }
        }

        for (int i = 2; i<strs.size(); i++){
            int length = res.size();
            int length_str = strs[i].size();
            if (length==0) return "";
            if (length_str==0) return "";
            for (int j=0; j<min(length, length_str); j++){
                if (!((res[j])==(strs[i][j]))) {
                    res.erase(j,length-j);
                    j=length;
                }else{
                    if (j==(length_str-1) & j!=length){
                        res.erase(j+1, length-(j+1));
                        j=length+length_str;
                    }
                }
            }
        }

        return res;
    }
};
