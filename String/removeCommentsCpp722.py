'''
The main idea is simple - Go through each character, if we meet a special character, check whether the next character is one that is of interest to us (comment tokens) and then toggle some states that will determine whether we append the character to the final source.

Some insights:

There are three important tokens we want to identify within the source code //, /* and */.
We use a variable called buffer that acts as a buffer to store the characters that will definitely go into the final source code. This buffer can contain characters from multiple lines because of block comments.
We use another variable block_comments_open to keep track of whether we are inside a block comment or not.
At the end of each source line, we simply have to check whether we are inside of a block comment or not (i.e. block_comments_open is True) to decide whether we want to flush the buffer and append it to the results.
In each loop, we have to check that:

// - If it is a line comment and not part of a block comment, skip the rest of the line by shifting the pointer to the end of the line.
/* - If it is an opening block comment token and not part of a block comment, set block_comments_open to True.
*/ - If it is a closing block comment token and part of a block comment, set block_comments_open to False.
Else append to buffer if not part of a block comment.

'''
class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        res = []
        buffer, block_open = '', False
        for line in source:
            i, n = 0, len(line)
            while i < n:
                char = line[i]
                # case 1, '//', if the string "//" occurs in a block comment, it is ignored
                if char == '/' and (i + 1 < n and line[i + 1] == '/') and not block_open:
                    i = n # # Advance pointer to end of current line.
                # case 2, '/*', if the string "/*" occurs in a line or block comment, it is ignored
                elif char == '/' and (i + 1 < n and line[i + 1] == '*') and not block_open:
                    block_open = True
                    i += 1
                elif char == '*' and (i + 1 < n and line[i + 1] == '/') and block_open:
                    block_open = False
                    i += 1
                # Normal character. Append to buffer if not in block comment.
                elif not block_open:
                    buffer += char
                i += 1
            if buffer and not block_open: # has buffer and block comment is closed
                res.append(buffer)
                buffer = '' # reset
        return res