class time:
    def __init__(obj,h,m,s):
            obj.hour = h
            obj.minute = m
            obj.second = s

            
    def show(obj):
        return str(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)

    
    def sanie(obj):
        return str(obj.hour*3600+obj.minute*60+obj.second)

    
    def ezafe_kardan(obj,hh,mm,ss):
        obj.hour += hh
        obj.minute += mm
        obj.second += ss
        return(obj)

    
    def kam_kardan(obj,hh,mm,ss):
        obj.hour -= hh
        obj.minute -= mm
        obj.second -= ss
        return(obj)

    
    def __add__(obj,obj2):
        obj.hour += obj2.hour
        obj.minute += obj2.minute
        obj.second += obj2.second
        if obj.minute >= 60:
            obj.minute -= 60
            obj.hour += 1
        if obj.second >= 60:
            obj.second -= 60
            obj.minute += 1
        return (obj)

    
    def __sub__(obj,obj2):
        obj.hour -= obj2.hour
        obj.minute -= obj2.minute
        obj.second -= obj2.second
        if obj.second < 0:
            obj.second += 60
            obj.minute -= 1
        if obj.minute < 0:
            obj.minute += 60
            obj.hour -= 1
        return(obj)

    
    def __lt__(obj,obj2):
        if (obj.hour*3600+obj.minute*60+obj.second < obj2.hour*3600+obj2.minute*60+obj2.second):
            return True
        return False

    
    def __le__(obj,obj2):
        if (obj.hour*3600+obj.minute*60+obj.second <= obj2.hour*3600+obj2.minute*60+obj2.second):
            return True
        return False

    
    def __gt__(obj,obj2):
        if (obj.hour*3600+obj.minute*60+obj.second > obj2.hour*3600+obj2.minute*60+obj2.second):
            return True
        return False

    
    def __ge__(obj,obj2):
        if (obj.hour*3600+obj.minute*60+obj.second >= obj2.hour*3600+obj2.minute*60+obj2.second):
            return True
        return False

    
    def __eq__(obj,obj2):
        if (obj.hour*3600+obj.minute*60+obj.second == obj2.hour*3600+obj2.minute*60+obj2.second):
            return True
        return False

    
    def __ne__(obj,obj2):
        if (obj.hour*3600+obj.minute*60+obj.second != obj2.hour*3600+obj2.minute*60+obj2.second):
            return True
        return False
    

    def __repr__(obj):
        return str(obj.hour)+':'+str(obj.minute)+':'+str(obj.second)

    
            
        
            
        
         
