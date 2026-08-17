class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        st = []  # (pos, val)

        order = sorted(range(len(position)), key=lambda i: position[i], reverse = True)

        for i in order:
            pos = position[i]
            val = (target - pos) / speed[i]

            if not st:
                st.append((pos, val))
                continue

            if val > st[-1][1]:
                st.append((pos, val))

        return len(st)