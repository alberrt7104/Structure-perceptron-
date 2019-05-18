import os
a=[]
b=[]
c=[]
dataxy=[]
temp=[]
temp1=[]
tablexy={}
tableyy1={}
tableyy2={}
tableyy3={}
flag=0
flag2=0
value=0
countnumber=0
count=0
statistic={}
seq=[]
count5=0
with open("nettalk_stress_train.txt","r") as f:
    lines=f.readlines()
    for line in lines:
    	if len(line)==1:
    		countnumber=countnumber+1
    	else:
    		c=line.split()    		
    		if c[0]=="1":
    			if flag2==0:
    				seq.clear()		
    			else:
    				for i in range(len(seq)-1):
    					temp1=[seq[i]+seq[i+1]]
    					temp1=str(temp1)
    					if not (tableyy1.__contains__(temp1)):
    						#print(temp1)
    						tableyy1[temp1]=1
    					else:
    						tableyy1[temp1]=tableyy1[temp1]+1
    				for i in range(len(seq)-2):
    					temp1=[seq[i]+seq[i+1]+seq[i+2]]
    					temp1=str(temp1)
    					if not (tableyy2.__contains__(temp1)):
    						tableyy2[temp1]=1
    					else:
    						tableyy2[temp1]=tableyy2[temp1]+1   				
    				for i in range(len(seq)-3):    					
    					temp1=[seq[i]+seq[i+1]+seq[i+2]+seq[i+3]]
    					#print(temp1)
    					temp1=str(temp1)
    					if not (tableyy3.__contains__(temp1)):
    						tableyy3[temp1]=1
    					else:
    						tableyy3[temp1]=tableyy3[temp1]+1    					
    				
    			flag2=1
    			seq.clear()
    		seq.append(c[2])
    		if not (statistic.__contains__(c[2])):
    			statistic[c[2]]=1
    		if not (tablexy.__contains__(c[2])):
    			tablexy[c[2]]=list(c[1])
    		else:
    			temp=list(c[1])
    			statistic[c[2]]=int(statistic[c[2]])+1
    			for i in range(2,len(tablexy[c[2]])):    				
    				tablexy[c[2]][i]=int(temp[i])+int(tablexy[c[2]][i])
    		

    		b.append(c[2])
    		dataxy.append(list(c[1]))
    		if c[0]=="1":    			
    			a.append(c[2])	
    		#seqdata1[c[0]]=list(c[1])
    		#seqdata1[c[0]].append(c[2])


for key1 in tablexy:
	for key2 in statistic:
		if key2==key1:
			for i in range(2,len(tablexy[key1])):
				tablexy[key1][i]=int(tablexy[key1][i])/int(statistic[key2])

#print(seqdata1)
b=list(set(b))    
a=list(set(a))
#print(a)  
#print(len(a))
#print(b)
#print(len(b))
#print(countnumber)
print("Phi xy : ",tablexy)
print("Phi first order : ",tableyy1)
print("Phi second order : ",tableyy2)
print("Phi third order : ",tableyy3)

search={'00':1,'01':2,'02':3,'03':4,'04':5}
w=[1]*5
#print(w)
datatrain=[]
seqtrain={}
seqdata={}
flag3=0
countsqe=0
sumxy={}
tempc=0
minxy=10000
prexy=[]
correct=1
alldata=1
iteration=10
with open("nettalk_stress_test.txt","r") as f:
    lines=f.readlines()
    for line in lines:
    	if len(line)==1:
    		pass
    	else:
    		for r in range(1):
	    		c=line.split()	    		    		
	    		if c[0]=='1':
	    			if flag3==0:    				
	    				countsqe=countsqe+1
	    			else:    				
	    				#print(seqdata)
	    				#print(seqdata.keys())
	    				for k in seqdata:
	    					for i in range (2,len(seqdata[k])-1):
	    						for key in tablexy:	    							
	    							tempc=int(seqdata[k][i])-tablexy[key][i]
	    							
	    							tempc=tempc*tempc
	    							#print(tempc)
	    							if sumxy.__contains__(key):
	    								sumxy[key]=sumxy[key]+tempc*w[search[key]-1]
	    							else:
	    								#print(tempc)
	    								#sumxy[key]=tempc
	    								#print(search[key]-1)
	    								#print(sumxy[key])
	    								sumxy[key]=tempc*w[search[key]-1]
	    								#print(w[search[key]-1])
	    								#print(sumxy[key])
	    							#print(sumxy)


	    					for alpha in sumxy:  
	    						#print(minxy)  							
	    						if (minxy>sumxy[alpha]):
	    							#print(sumxy[alpha])
	    							minxy=sumxy[alpha]
	    							#print(minxy)
	    							prexy=alpha
	    							#print(alpha)
	    					minxy=10000
	    							
	    							#print(prexy)
	    					if prexy==seqdata[k][-1]:
	    						correct=correct+1
	    						alldata=alldata+1
	    					else:
	    						w[search[prexy]-1]=w[search[prexy]-1]+0.01
	    						w[search[seqdata[k][-1]]-1]=w[search[seqdata[k][-1]]-1]-0.01
	    						alldata=alldata+1
	    					#print(correct/alldata)

	    					#print(prexy+" "+seqdata[k][-1])
	    					#print(sumxy)
	    					sumxy.clear()
	    							#print(seqdata[k][i])
	    				#print(w)	
	    				#print(correct/alldata)	
	    				countsqe=countsqe+1    
	    				seqdata.clear()

	    		flag3=1	
	    		
    		seqdata[c[0]]=list(c[1])
    		seqdata[c[0]].append(c[2])
    print("train accuracy : ", correct/alldata)
correct=0
alldata=0
with open("nettalk_stress_test.txt","r") as f:
    lines=f.readlines()
    for line in lines:
    	if len(line)==1:
    		pass
    	else:
    		c=line.split() 
    		#print(c)   		
    		if c[0]=='1':
    			if flag3==0:    				
    				countsqe=countsqe+1
    			else:    				
    				#print(seqdata)
    				#print(seqdata.keys())
    				for k in seqdata:
    					for i in range (2,len(seqdata[k])-1):
    						for key in tablexy:	    							
    							tempc=int(seqdata[k][i])-tablexy[key][i]
    							
    							tempc=tempc*tempc
    							#print(tempc)
    							if sumxy.__contains__(key):
    								sumxy[key]=sumxy[key]+tempc*w[search[key]-1]
    							else:
    								#print(tempc)
    								sumxy[key]=tempc*w[search[key]-1]
    								#print(w[search[key]-1])
    								#print(sumxy[key])
    							#print(sumxy)


    					for alpha in sumxy:  
    						#print(minxy)  							
    						if (minxy>sumxy[alpha]):
    							#print(sumxy[alpha])
    							minxy=sumxy[alpha]
    							#print(minxy)
    							prexy=alpha
    							#print(alpha)
    					minxy=10000
    							
    							#print(prexy)
    					if prexy==seqdata[k][-1]:
    						correct=correct+1
    						alldata=alldata+1
    					else:    						
    						alldata=alldata+1
    					#print(correct/alldata)

    					#print(prexy+" "+seqdata[k][-1])
    					#print(sumxy)
    					sumxy.clear()
    							#print(seqdata[k][i])
    				#print(w)	
    				#print(correct/alldata)	
    				countsqe=countsqe+1    
    				seqdata.clear()

    		flag3=1	
    		
    		seqdata[c[0]]=list(c[1])
    		seqdata[c[0]].append(c[2])
print("test accuracy : ",correct/alldata)





