import random
import plotly.express as px
result=[]
count=[]
for i in range(0,100):
    dice1=random.randint(1,6)
    dice2=random.randint(1,6)
    result.append(dice1+dice2)
    count.append(i)
fig=px.bar(x=result, y=count)
fig.show()
