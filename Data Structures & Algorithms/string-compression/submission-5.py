class Solution:
    def compress(self, chars: List[str]) -> int:
        write_cursor=1
        read_cursor=0                

        while read_cursor < len(chars): 
            base_read_cursor = read_cursor

            while read_cursor < len(chars) and chars[read_cursor] == chars[base_read_cursor]:
                read_cursor+=1
            
            group_size = read_cursor - base_read_cursor
            if group_size > 1:
                for digit in str(group_size):
                    chars[write_cursor] = digit
                    write_cursor += 1
                
            if read_cursor < len(chars):
                chars[write_cursor] = chars[read_cursor]
                write_cursor+=1
               
        del chars[write_cursor:]
        return write_cursor

            

