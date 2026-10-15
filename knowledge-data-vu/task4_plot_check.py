import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

# Bar chart check
df = pd.DataFrame({"teacher": ["Alice", "Bob", "Carol"], "courses": [4, 7, 9]})
df_plot = df.sort_values("courses", ascending=True).copy()
ax = df_plot.plot.barh(x="teacher", y="courses", figsize=(10, 6), color="steelblue", edgecolor="black")
ax.set_title("Course load per teacher")
ax.set_xlabel("Number of courses")
ax.set_ylabel("Teacher")
ax.invert_yaxis()
plt.tight_layout()
plt.savefig("task4_bar_test.png")
print("bar_ok")

# DBpedia-style bar chart check
pop = pd.DataFrame({"countryLabel": ["A", "B", "C"], "population": [1000000, 2000000, 3000000]})
ax2 = pop.plot.bar(x="countryLabel", y="population", figsize=(12, 6), color="darkgreen", edgecolor="black")
ax2.set_title("Top 10 countries by population (DBpedia)")
ax2.set_xlabel("Country")
ax2.set_ylabel("Population")
plt.xticks(rotation=45, ha="right")
plt.tight_layout()
plt.savefig("task4_dbpedia_test.png")
print("dbpedia_ok")
