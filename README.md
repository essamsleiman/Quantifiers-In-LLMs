# CocoSciFinal


Code for CocoSci Final Proj


### Abstract

This study delves into the significant role of quantifiers such as
”few,” ”some,” and ”many” in human cognition and language,
drawing upon Gricean reasoning and the Rational Speech Act
(RSA) framework. We explore how these quantifiers facili-
tate effective information conveyance by framing communica-
tion as a cooperative process between speakers and listeners.
Leveraging probabilistic models (RSA) framework, we study
how quantifiers are semantically understood. Furthermore, we
extend our analysis to compare quantifier usage between hu-
mans and Large Language Models (LLMs) and investigate the
influence of contextual cues on quantifier selection by both
groups. Our findings suggest that LLMs closely align with
human cognition, particularly when less context is provided,
emphasizing the role of context in quantifier usage.


### Experiment Code


1. Use the survey_question_distributions.py file to convert Human and LLM quantifier predictions into Probability Distributions.

2. q1_gpt.js, q1_human.js, q2_gpt.js, and q2_human.js are the problang files used to model each experiment with the RSA framework

3. divergence.py is used for calculating the kl divergence between the different distributions.
