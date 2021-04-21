import random
import statistics
import plotly.figure_factory as ff
result=[]
count=[]
for i in range(0,1000):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    result.append(dice1+dice2)
    count.append(i)
mean=sum(result)/len(result)
sd=statistics.stdev(result)
print("mean:= "+str(mean))
print("standard deviation:= "+str(sd))
median=statistics.median(result)
mode=statistics.mode(result)
print("median:= "+str(median))
print("mode:= "+str(mode))
first_sd_start,first_sd_end=mean-sd,mean+sd
second_sd_start,second_sd_end=mean-(sd*2),mean+(sd*2)
third_sd_start,third_sd_end=mean-(sd*3),mean+(sd*3)
listWithin_1sd=[data for data in result if data>first_sd_start and data<first_sd_end]
listWithin_2sd=[data for data in result if data>second_sd_start and data<second_sd_end]
listWithin_3sd=[data for data in result if data>third_sd_start and data<third_sd_end]
print("Standard deviation of this data is {}".format(sd))
print("{}% of data lies within 1 standard deviation".format(len(listWithin_1sd)*100.0/len(result)))
print("{}% of data lies within 2 standard deviation".format(len(listWithin_2sd)*100.0/len(result)))
print("{}% of data lies within 3 standard deviation".format(len(listWithin_3sd)*100.0/len(result)))
