import matplotlib.pyplot as plt
import numpy as np

# Create time data
time = np.linspace(0, 23, 96)

# Expected cost and actual cost data
np.random.seed(42)  # For reproducibility
intervals = 96  # 96 intervals of 15 minutes in a day
random_spend = np.random.uniform(0.5, 1.5, intervals)
expected_cost = np.cumsum(random_spend)


# expected_cost = np.log1p(time) / np.log1p(24) * 100
# print(expected_cost)
actual_cost = expected_cost + (np.sin(time / 2) * 5)

plt.figure(figsize=(10*1.3, 6*1.3))

# Plot expected cost
plt.plot(time, expected_cost, label='target spend', color='black')

# Plot actual cost
plt.plot(time, actual_cost, label='actual spend', color='red')

# Add vertical lines and annotations
points_of_interest = [2, 8, 15, 20.5]
annotations = ['ahead', 'behind', 'ahead', 'behind']
actions = ['lower bid', 'increase bid', 'lower bid', 'increase bid']
vertical_adjustments = [30, -5, -10, -7]

for poi, annotation, action, va in zip(points_of_interest, annotations, actions, vertical_adjustments):
    # plt.axvline(x=poi, color='k', linestyle='--')
    # Find the closest index
    closest_index = np.abs(time - poi).argmin()
    plt.text(poi, actual_cost[closest_index] + va, annotation, fontsize=12, verticalalignment='bottom')
    plt.text(poi, actual_cost[closest_index] - 5 + va, action, fontsize=12, verticalalignment='top')

vertical_line_x = [6.2, 12.5, 19]
for vlx in vertical_line_x:
    plt.axvline(x=vlx, color='k', linestyle='--')


# Labels and title
plt.xlabel('Time')
plt.ylabel('Spend')
plt.title('Target Spend vs Actual Spend Over Time')
plt.legend()
plt.grid(False)


# Remove upper and right box lines
plt.gca().spines['top'].set_visible(False)
plt.gca().spines['right'].set_visible(False)

# Save the plot
plt.savefig('flow_ratio_map.png')
plt.show()
