import pandas as pd
import random
import matplotlib.pyplot as plt

first_names = ["Danielle", "Noah", "Roman", "Ben" , "Van", "Alexis", "Katerina", "Andrew" ,"Kyan"]
last_names = ["Esguerra", "Bradberry", "Williams", "Martin", "Latson", "Luebke", "Wedrychowicz", "Teddy", "Fogarty"]

bed_times = ["8-10pm", "10-11pm", "11pm-12am","12am-1am", "1am-3am"]
phone_use = ["Never", "Sometimes", "Often", "Always"]
grades = [9, 10, 11, 12]

names = []

for i in range(9):
    names.append(f"{random.choice(first_names)} {random.choice(first_names)}")

data = {
    "Name": names,
    "Age": [random.randint(14, 19) for _ in names ],
    "Bed Time": [random.choice(bed_times) for _ in names],
    "Sleep Hours": [random.randint(0, 10) for _ in names],
    "Nap Before Bed": [random.randint(0, 5) for _ in names],
    "Phone Before Bed": [random.choice(phone_use) for _ in names],
    "GPA": [round(random.uniform(0.3, 4.0),2) for _ in names]
}


df = pd.DataFrame(data)

df.groupby('Bed Time')['GPA'].mean().plot(kind='bar')
plt.title('Average GPA by Bed Time')
plt.xlabel("Bed Time")
plt.ylabel("GPA")
plt.tight_layout()
plt.show()

plt.hist(df["Sleep Hours"])
plt.title("Different Sleep Hours")
plt.xlabel("Hours Slept")
plt.ylabel("Number of Students")
plt.tight_layout()
plt.show()

plt.scatter(df["Sleep Hours"], df["GPA"])
plt.title("Sleep Hours vs GPA")
plt.xlabel("Sleep Hours per Night")
plt.ylabel("GPA")
plt.tight_layout()
plt.show()