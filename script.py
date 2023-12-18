from collections import Counter
import itertools


vs2 = ["a couple", "a few", "some", "several", "most", "a majority", "almost all", "all"]

strat1LLM = ["some", "several", "some", "several", "several", "a few", "a few", "a few", "a few", "a few"]
strat1Human =  ["a couple", "several", "a few", "several", "a couple", "a few", "a few", "a couple", "several", "a few"]


counter_llm = Counter(strat1LLM)
counter_human = Counter(strat1Human)

# Calculating the probability distribution
prob_dist_llm1 = {option: counter_llm.get(option, 0) / len(strat1LLM) for option in vs2}
prob_dist_human1 = {option: counter_human.get(option, 0) / len(strat1Human) for option in vs2}



# returnDist = getDist(strat2LLM)
print("prob_dist_llm1: ", prob_dist_llm1)
print("prob_dist_human1: ", prob_dist_human1)




strat2LLM = ["several", "a few", "several", "a few", "a few",  "a few", "some", "several", "some", "some"]
strat2Human = ["a few", "a couple", "some", "several", "a couple", "a few", "a few", "several", "several", "a couple"]



counter_llm = Counter(strat2LLM)
counter_human = Counter(strat2Human)

# Calculating the probability distribution
prob_dist_llm2 = {option: counter_llm.get(option, 0) / len(strat2LLM) for option in vs2}
prob_dist_human2 = {option: counter_human.get(option, 0) / len(strat2Human) for option in vs2}


print("exp 2========")
# returnDist = getDist(strat2LLM)
print("prob_dist_llm2: ", prob_dist_llm2)
print("prob_dist_human2: ", prob_dist_human2)

