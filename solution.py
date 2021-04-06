class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        
        max_val = max(satisfaction)
        min_val = min(satisfaction)
        
        if max_val<=0:                  
            return 0                            #All negative, so return 0
        
        else:
            satisfaction.sort()
            if min_val>=0:
                sat = satisfaction
                summ=0
                for i in range(0,len(sat)):
                    summ+=(i+1)*sat[i]      #All positive, return sorted array's total like-time coefficient
                    
                return summ
             
            else:
                sat = satisfaction[::-1]    #Sort the list in reverse order
                
                i=1
                good_val_sum=sat[0]
                for i in range(1,len(sat)):
                    good_val_sum+=sat[i]    
                    if good_val_sum<=0:     #Take the satisfaction levels that gives more than zero sum
                        break
                        
                if good_val_sum>0:          #The whole list gives positive sum of satisfaction levels
                    sat = sat[0:i+1][::-1]  #So take the levels upto sat[i] including sat[i] and reverse sort it
                else:
                    sat = sat[0:i][::-1]    #Else, take the levels upto sat[i] excluding sat[i] and reverse sort it
                
                summ=0
                for i in range(0,len(sat)):
                    summ+=(i+1)*sat[i]      #Take the sum of time*satisfaction_level
                    
                return summ
                
                
        
