import pandas as pd
import random
import matplotlib.pyplot as plt

first_names = ["Danielle", "Noah", "Roman", "Ben" , "Van", "Alexis", "Katerina", "Andrew" ,"Kyan"]
last_names = ["Esguerra", "Bradberry", "Williams", "Martin", "Latson", "Luebke", "Wedrychowicz", "Teddy", "Fogarty"]

bed_times = ["8-10pm", "10-11pm", "11pm-12am","12am-1am", "1am-3am"]
phone_use = ["Never", "Sometimes", "Often", "Always"]

names = []

for i in range(9):
    names.append(f"{random.choice(first_names)} {random.choice(first_names)}")

data = {
    "Name": names,
    "Age": [random.randint(14, 19) for _ in names ],
    "Bed Time": [random.choice([bed_times]) for _ in names],
    "Sleep Hours": [random.randint(0, 60) for _ in names],
    "Nap Before Bed": [random.randint(0, 5) for _ in names],
    "Phone Before Bed": [random.choice([phone_use]) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.0),2) for _ in names]
}


df = pd.DataFrame(data)


print(df.groupby('Year')['GPA'].mean())
df.groupby('Bed Time')['GPA'].mean().plot(kind='bar')
plt.title('Average GPA by Bed Time')
plt.show()
