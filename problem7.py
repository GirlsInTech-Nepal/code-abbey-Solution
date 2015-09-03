class degrees:
        def __init__(self):
           self.temp1=4
           self.temp2=15       
           self.temp3=34


        def __next__(self):
            res=[]
            for _t in [self.temp1,self.temp2,self.temp3]:
                _t = _t*(5/9)+32
                yield _t
            
        
        next= __next__
        def  __iter__(self):
            return self
t=degrees()
for _t in next(t):
    print(_t)

           
          
      #def to_fahrenheit(self): 
           #return self.temperature*self.factor
           #length=len(self.temperature)
           #print(length)
           #print(self.temperature)
           #res=[]
           #while i<length:
                  #b[i]=self.temperature[i] * (5/9) + 32
                  #res.append(b)
                  #i+=1
           #return res
     
  #print(self)

       #return (self.temperature * 1.8) + 32
     




