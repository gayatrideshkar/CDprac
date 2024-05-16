import matplotlib.pyplot as plt
import numpy as np

# Generate some sample data
np.random.seed(0)
# Sample data for demonstration
data = np.random.normal(loc=0, scale=1, size=100)  # Normal distribution

# Create a box plot
plt.figure(figsize=(16, 12))

# Box plot
plt.subplot(3, 2, 1)
plt.boxplot(data)
plt.title('Box Plot')
plt.xlabel('Data')
plt.ylabel('Values')

# Histogram
plt.subplot(3, 2, 2)
plt.hist(data, bins=20, color='skyblue', edgecolor='black')
plt.title('Histogram')
plt.xlabel('Data')
plt.ylabel('Frequency')

# Create sample data for scatter plot
x = np.random.normal(loc=0, scale=1, size=100)
y = 2 * x + np.random.normal(loc=0, scale=0.5, size=100)  # Adding noise

# Scatter plot
plt.subplot(3, 2, 3)
plt.scatter(x, y)
plt.title('Scatter Plot')
plt.xlabel('X')
plt.ylabel('Y')

# Bar chart
plt.subplot(3, 2, 4)
labels = ['A', 'B', 'C', 'D', 'E']
values = np.random.randint(1, 10, size=len(labels))
plt.bar(labels, values, color='orange')
plt.title('Bar Chart')
plt.xlabel('Categories')
plt.ylabel('Values')

# Pie chart
plt.subplot(3, 2, 5)
sizes = np.random.randint(1, 10, size=len(labels))
plt.pie(sizes, labels=labels, autopct='%1.1f%%', colors=plt.cm.tab20.colors)
plt.title('Pie Chart')

plt.tight_layout()
plt.show()
