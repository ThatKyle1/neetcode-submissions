class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
    
        # sorted slow to fast car picture

        # example 2 target = 10

        # car0Mile=1mph  #car1Mile-2mph  #car4mile-2mph   #car7Mile-1mph
        
        # car1Mile=2mph # car2Mile-2mph # car6Mile-2mph # car8Mile-1mph   

        # car3Mile=2mph # car4mile-2mph #car8Mile-1mph #car9Mileph

        # after first run car0 catchscar1 one fleet
        # Second run nothing
        #third run car 8 catch car

        # nvm this is wrong ahead it only catches when after both runs same number or ahead of it 
        # important cant  go ahead so stack has to pop a certain way.

        #my idea, you have to pop from the furthest car first get that distance, if any
        # car after is further than one before or the same it caught up and it is now one
        # the same mile and same speed.

        # we don't need to actually keep track just number so maybe once you get one that passes
        #then you just get rid of that whole fleet -=1 a count seems easiest

        #sort both things with bubble sort
        stack = []
        for p, s in sorted(zip(position, speed), reverse=True):
            stack.append((target - p) / s) # how many runs till hit target
            if len(stack) >= 2 and stack[-1] <= stack[-2]: # if it hits target before remmove one
                stack.pop()
        return len(stack)



        


        

