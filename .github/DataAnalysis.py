import pandas as pd
import random
import matplotlib.pyplot as plt

fNames = ["Danielle", "Noah", "Roman", "Ben" , "Van", "Alexis", "Katerina", "Andrew" ,"Kyan"]
lNames = ["Esguerra", "Bradberry", "Williams", "Martin", "Latson", "Luebke", "Wedrychowicz", "Teddy", "Fogarty"]
timetobed = ["8 - 10pm", "11 - 12am", "1am - 2am","3am - 4am"]
howmuchsleep = ["1 - 4", "5 - 7", "8 - 10", "10+"]
names = []

for i in range(9):
    names.append(f"{random.choice(fNames)} {random.choice(lNames)}")

data = {
    "Name": names,
    "Age": [random.randint(14, 19) for _ in names ],
    "GPA": [round(random.uniform(0.3, 4.0),2) for _ in names],
    "Credits Completed": [random.randint(0, 60) for _ in names],
    "Year": [random.choice(timetobed) for _ in names],
    "Pathway": [random.choice(howmuchsleep) for _ in names]
}

pennData = pd.DataFrame(data)

print(pennData)

df = pd.DataFrame(pennData)
print(df.describe())
print(df.info())
print(df.groupby('Year')['GPA'].mean())
df.groupby('Year')['GPA'].mean().plot(kind='bar')
plt.title('Average Time to Bed')
plt.xlabel('Times')
plt.ylabel('GPA')


plt.show()