class Solution:
    def removeInvalidParentheses(self, s: str) -> list[str]:
        longest_string = -1
        res = set()

        def backtrack(idx, curr_res, o_count, c_count):
            nonlocal longest_string, res

            if idx == len(s):
                if o_count == c_count:
                    if len(curr_res) > longest_string:
                        longest_string = len(curr_res)
                        res = {"".join(curr_res)}
                    elif len(curr_res) == longest_string:
                        res.add("".join(curr_res))

                return

            ch = s[idx]

            if ch == "(":
                curr_res.append(ch)
                backtrack(idx + 1, curr_res, o_count + 1, c_count)
                curr_res.pop()
                backtrack(idx + 1, curr_res, o_count, c_count)

            elif ch == ")":

                backtrack(idx + 1, curr_res, o_count, c_count)
                if o_count > c_count:
                    curr_res.append(ch)
                    backtrack(idx + 1, curr_res, o_count, c_count + 1)
                    curr_res.pop()

            else:
                curr_res.append(ch)
                backtrack(idx + 1, curr_res, o_count, c_count)
                curr_res.pop()

        backtrack(0, [], 0, 0)
        return list(res)