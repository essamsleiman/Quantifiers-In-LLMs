import numpy as np
from scipy.stats import entropy

# Define the two probability distributions as arrays
# Replace these with your own distributions


vs2 = ["a couple", "a few", "some", "several", "most", "a majority", "almost all", "all"]

distribution_P = np.array([0.2, 0.3, 0.5])
distribution_Q = np.array([0.25, 0.35, 0.4])


dist_gpt_1 =[
            [.01, .98, .01, 0.0, 0.0, 0.0, 0.0, 0.0],
            [.01, .43, .027, 0.29, 0.0, 0.0, 0.0, 0.0],
             ]

dist_human_1 =[
            [.33, .66, .01, 0.0, 0.0, 0.0, 0.0, 0.0],
            [.21, .43, .02, 0.34, 0.0, 0.0, 0.0, 0.0],
             ]



dist_gpt_2 =[
            [.36, .63, .01, 0.0, 0.0, 0.0, 0.0, 0.0],
            [.23, .40, .03, 0.34, 0.0, 0.0, 0.0, 0.0],
             ]


dist_human_2 =[
            [.42, .57, .01, 0.0, 0.0, 0.0, 0.0, 0.0],
            [.22, .30, .15, 0.33, 0.0, 0.0, 0.0, 0.0],
             ]

# Calculate KL Divergence
kl_divergence_total1 = []
for i in range(len(dist_gpt_1)):
    kl_divergence = entropy(dist_gpt_1[i], dist_human_1[i])
    kl_divergence_total1.append(kl_divergence)
print("avg divergence 1: ", sum(kl_divergence_total1) / len(kl_divergence_total1))

kl_divergence_total2 = []
for i in range(len(dist_gpt_2)):
    kl_divergence = entropy(dist_gpt_2[i], dist_human_2[i])
    kl_divergence_total2.append(kl_divergence)
print("avg divergence 2: ", sum(kl_divergence_total2) / len(kl_divergence_total2))


# print(f"KL Divergence: {kl_divergence}")