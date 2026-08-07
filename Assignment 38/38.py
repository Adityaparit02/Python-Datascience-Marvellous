"""
Marvellous Infosystems - Machine Learning
Student Performance ML Dataset - Complete Solution (Q1 to Q10)
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# ============================================================
# Q1. Load the dataset and display basic info
# ============================================================
df = pd.read_csv("student_performance_ml.csv")

print("----- First 5 records -----")
print(df.head())

print("\n----- Last 5 records -----")
print(df.tail())

print("\n----- Shape (rows, columns) -----")
print(df.shape)

print("\n----- Column Names -----")
print(df.columns.tolist())

print("\n----- Data types of each column -----")
print(df.dtypes)


# ============================================================
# Q2. Total students, Pass count, Fail count
# ============================================================
print("\n----- Total number of students -----")
print(len(df))

print("\n----- Students Passed (FinalResult = 1) -----")
print((df['FinalResult'] == 1).sum())

print("\n----- Students Failed (FinalResult = 0) -----")
print((df['FinalResult'] == 0).sum())


# ============================================================
# Q3. Average StudyHours, Attendance, Max PreviousScore, Min SleepHours
# ============================================================
print("\n----- Average StudyHours -----")
print(df['StudyHours'].mean())

print("\n----- Average Attendance -----")
print(df['Attendance'].mean())

print("\n----- Maximum PreviousScore -----")
print(df['PreviousScore'].max())

print("\n----- Minimum SleepHours -----")
print(df['SleepHours'].min())


# ============================================================
# Q4. value_counts() on FinalResult + Pass/Fail percentage + balance check
# ============================================================
print("\n----- FinalResult value counts -----")
counts = df['FinalResult'].value_counts()
print(counts)

print("\n----- Percentage distribution -----")
percentages = df['FinalResult'].value_counts(normalize=True) * 100
print(percentages)

pass_pct = percentages.get(1, 0)
fail_pct = percentages.get(0, 0)

print(f"\nPass %: {pass_pct:.2f}%")
print(f"Fail %: {fail_pct:.2f}%")

if abs(pass_pct - fail_pct) <= 10:
    print("Observation: The dataset is fairly BALANCED "
          "(Pass and Fail percentages are close to each other).")
else:
    print("Observation: The dataset is IMBALANCED "
          "(one class dominates the other significantly).")


# ============================================================
# Q5. Analyze relationship of StudyHours & Attendance with FinalResult
# ============================================================
print("\n----- Average StudyHours grouped by FinalResult -----")
print(df.groupby('FinalResult')['StudyHours'].mean())

print("\n----- Average Attendance grouped by FinalResult -----")
print(df.groupby('FinalResult')['Attendance'].mean())

print("""
Observations :
1. Students who passed generally show higher average StudyHours than
   students who failed, indicating study time positively influences results.
2. Passed students also tend to have higher average Attendance percentage
   compared to failed students.
3. This suggests both StudyHours and Attendance are positively correlated
   with academic performance.
4. However, these are not the only factors - other variables like
   PreviousScore and AssignmentsCompleted may also play a role.
5. Correlation does not imply strict causation; some students may pass
   despite lower values due to other strengths.
""")


# ============================================================
# Q6. Histogram of StudyHours
# ============================================================
plt.figure(figsize=(8, 5))
plt.hist(df['StudyHours'], bins=10, color='skyblue', edgecolor='black')
plt.title("Distribution of StudyHours")
plt.xlabel("StudyHours")
plt.ylabel("Frequency")
plt.tight_layout()
plt.savefig("histogram_studyhours.png")
plt.show()

# Explanation:
# The histogram shows how study hours are spread across students.
# If it is roughly bell-shaped, most students study a moderate number
# of hours, with fewer students studying very little or very much
# (a normal-like distribution). If skewed, it indicates most students
# cluster around low or high study hours.


# ============================================================
# Q7. Scatter plot: StudyHours vs PreviousScore (colored by Pass/Fail)
# ============================================================
colors = df['FinalResult'].map({1: 'green', 0: 'red'})

plt.figure(figsize=(8, 5))
plt.scatter(df['StudyHours'], df['PreviousScore'], c=colors, alpha=0.7)
plt.title("StudyHours vs PreviousScore (Green=Pass, Red=Fail)")
plt.xlabel("StudyHours")
plt.ylabel("PreviousScore")
plt.tight_layout()
plt.savefig("scatter_studyhours_previousscore.png")
plt.show()


# ============================================================
# Q8. Boxplot for Attendance + Outlier check
# ============================================================
plt.figure(figsize=(6, 5))
sns.boxplot(y=df['Attendance'], color='lightblue')
plt.title("Boxplot of Attendance")
plt.tight_layout()
plt.savefig("boxplot_attendance.png")
plt.show()

# Outlier detection using IQR method
Q1 = df['Attendance'].quantile(0.25)
Q3 = df['Attendance'].quantile(0.75)
IQR = Q3 - Q1
lower_bound = Q1 - 1.5 * IQR
upper_bound = Q3 + 1.5 * IQR

outliers = df[(df['Attendance'] < lower_bound) | (df['Attendance'] > upper_bound)]
print("\n----- Attendance Outliers -----")
print(outliers)
print(f"\nNumber of outliers detected: {len(outliers)}")


# ============================================================
# Q9. AssignmentsCompleted vs FinalResult
# ============================================================
plt.figure(figsize=(8, 5))
sns.boxplot(x='FinalResult', y='AssignmentsCompleted', data=df, palette='Set2')
plt.title("AssignmentsCompleted vs FinalResult")
plt.xlabel("FinalResult (0=Fail, 1=Pass)")
plt.ylabel("AssignmentsCompleted")
plt.tight_layout()
plt.savefig("assignments_vs_result.png")
plt.show()

print("\n----- Average AssignmentsCompleted by FinalResult -----")
print(df.groupby('FinalResult')['AssignmentsCompleted'].mean())

# Observation:
# Students who completed more assignments tend to have a higher chance
# of passing, showing a positive relationship between assignment
# completion and academic outcome.


# ============================================================
# Q10. SleepHours vs FinalResult
# ============================================================
plt.figure(figsize=(8, 5))
sns.boxplot(x='FinalResult', y='SleepHours', data=df, palette='Set3')
plt.title("SleepHours vs FinalResult")
plt.xlabel("FinalResult (0=Fail, 1=Pass)")
plt.ylabel("SleepHours")
plt.tight_layout()
plt.savefig("sleephours_vs_result.png")
plt.show()

print("\n----- Average SleepHours by FinalResult -----")
print(df.groupby('FinalResult')['SleepHours'].mean())

# Explanation:
# Sleeping more does NOT guarantee success. While adequate sleep supports
# concentration and health, the plot usually shows overlapping ranges of
# SleepHours for both Pass and Fail students. This means sleep alone is
# not a decisive factor - it must be combined with sufficient StudyHours,
# Attendance, and Assignment completion to influence FinalResult.