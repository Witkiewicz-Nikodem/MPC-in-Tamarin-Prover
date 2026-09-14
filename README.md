# MPC_symbolic_model_in_tamarin


### attribute based models
We show here how to capture MPC attributes. Parties try to check whether their values are the same or not. The values are always fresh, so they are always different. Therefore, secure MPC should evaluate to false. However, if an adversary violates security attributes, they are able to force MPC to return true.

We created four similar models, three for a specific output delivery attribute with a malicious adversary and one for a semi-honest adversary. 

#### output delivery attributes
Fairness and GOD models differ only in how they approach the output delivery attribute; they capture privacy, correctness and independence of inputs in the same way. The security with abort model is different. This approach is used to obtain schemes which preserve attributes in the presence of a malicious adversary in a dishonest majority setting. Therefore, the adversary controls who gets the output; however, he can't achieve anything more.

#### semi-honest adversary
This model captures a semi-honest adversary. Meaning, he can only violate privacy and nothing more. 


### Complexity measures
In the file __complexity measures__ we focused on measuring the models' complexity. There we facilitate an abstract functionality — just a function f(x1, ..., xn). Then, the not-correct function is cf(x1, ..., xn), and the dependent input is captured by evaluating the dependent(x) function on honest input. We always assume that the adversary has to corrupt n-1 parties to violate the security attributes. The goal is to check how much time we need to prove that the model is built properly. We covered MPC with group sizes of {2,3,4}.

Please note that complexity in Tamarin is somewhat random and strongly depends on what the lemmas state, and on heuristics. The tests, rather than providing exact timings, provide their order of magnitude.


### tests
The tests.py file contains a script that runs models and provides CPU and RAM measurements. The script takes one argument which points to a specific benchmark.

__argument list:__
1. C2 - run complexity model test, the group contains 2 parties.
2. C3 - run complexity model test, the group contains 3 parties.
3. C4 - run complexity model test, the group contains 4 parties.
4. AllC - run all complexity model tests.
5. semi-honest - run model with semi-honest adversary
6. GOD - run setup model with guaranteed output delivery
7. Fairness - run setup model with fairness
8. Abort - run setup model with security with abort