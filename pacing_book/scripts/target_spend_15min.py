import numpy as np
import matplotlib.pyplot as plt

# Generate random spend data for every 15 minutes
np.random.seed(42)  # For reproducibility
intervals = 96  # 96 intervals of 15 minutes in a day
random_spend = np.random.uniform(0.5, 1.5, intervals)
random_spend = random_spend / np.sum(random_spend) * 100  # Normalize to sum up to 100%

# Time intervals for every 15 minutes
time_intervals = np.arange(0, 24, 0.25)  # 15-minute intervals

# Plot the spend per 15 minutes
plt.figure(figsize=(15*1.3, 6*1.3))
plt.bar(time_intervals, random_spend, width=0.2, alpha=0.7, color='black')
# plt.plot(time_intervals, random_spend)
plt.xlabel('Time (hours)')
plt.ylabel('Target Spend($)')
plt.title('Target Spend Per 15 Minutes')
plt.grid(False)

plt.gca().spines['top'].set_visible(False)


plt.savefig('target_spend_15min.png')
plt.show()