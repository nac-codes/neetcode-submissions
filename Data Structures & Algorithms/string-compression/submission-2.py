class Solution:
    def compress(self, chars: List[str]) -> int:
        base_cursor = 0
        explore_cursor = 0

        while base_cursor < len(chars)-1:

            while explore_cursor < len(chars) and chars[base_cursor] == chars[explore_cursor]:
                explore_cursor+=1

            # explore cursor - 1 is end of group
            # base_cursor is the start of the group

            if explore_cursor == base_cursor+1:
                base_cursor+=1
                continue
            else:
                # print(chars)
                group_size = explore_cursor - base_cursor
                i=0 
                while i < group_size-1:
                    del chars[base_cursor+1]
                    i+=1
                # print(group_size)
                group_size_charlist = list(str(group_size))
                # print(group_size_charlist)
                for c in reversed(group_size_charlist):
                    chars.insert(base_cursor+1,c)

                base_cursor+=len(group_size_charlist)+1
                explore_cursor=base_cursor
                # print(chars)
        
        return len(chars)
                    

                


        
        

        
          

        