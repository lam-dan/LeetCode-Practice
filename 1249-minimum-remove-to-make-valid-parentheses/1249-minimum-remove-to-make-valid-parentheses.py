class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        s_list = list(s)
        open_par_idx = [] # Stack to track number of "(" and store their indexes

        for i in range(len(s_list)):
            # Case 1 String is a "(" we store the index
            if s_list[i] == "(":
                open_par_idx.append(i)
            # Case 2 String is a ")" find matching parantheses "(" and remove
            # If there is no matching, we remove to make valid paratheses
            elif s_list[i] == ")":
                if open_par_idx:
                    open_par_idx.pop()
                else:
                    s_list[i] = "" # Remove from s_list to make it overall valid

        print("open_par_idx", open_par_idx)
        print("s_list", s_list)
        # Using list of open_par_idx, we're going to remove them from the list
        for i in range(len(open_par_idx)):
            s_list[open_par_idx[i]] = ""
        return "".join(s_list)

        # Time Complexity - O(n)
        # Space Complexity - O(n)
                