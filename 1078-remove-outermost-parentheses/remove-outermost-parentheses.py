class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        depth_list = []
        depth = 0
        s_list = list(s)
        
        for char in s:
            if char == "(":
                depth += 1
                depth_list.append(depth)

            if char == ")":
                depth_list.append(depth)
                depth -= 1

        popped_count = 0
        for i, x in enumerate(depth_list):
            if x == 1:
                c_idx = i - popped_count
                s_list.pop(c_idx)
                popped_count += 1

        return "".join(s_list)