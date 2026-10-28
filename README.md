# Test Gaming Experiment

Reward hacking is when an AI finds an unintentional shortcut to pass a score without doing the job you assigned it to do.

Take for instance, a technical drawing student sitting tasked to draw and be evaluated on a scale of 100 points, only to steal the marking scheme and copy the drawing to get the 100 points. 
Quite alright, the student scores the 100 points, but the aim, then, is defeated because, the examination was supposed to judge the students
ability and memory and not just to assign a perfect score. Or an essayist who writes long ambiguous grammar to bamboozle the
examiner without sticking to the topic. It hacked the rewards.

AI systems are guilty of the same flaw. They are evaluated or trained against a certain score, but they sometimes, find a way to go around
the rule and pass the evaluation without doing the assigned task.

Test-gaming, on the other hand is a category or type of reward hacking. It is reward hacking but done with tests. The tasks are tests.

Take for instance,
Real goal: An AI is given a task to write a function that subtracts the second number from the first one, for any two numbers.
Weak test: `subtract(8,0);` should return 8
The hack: The Ai writes, `return 8;` or "if the input is (8,0) retrun 8"
Result: The test passes, but `subtract(10,8);` will give a wrong answer and return `8` instead of `2`


`subtract(8,0);` is also a weak test in the sense that even if it doesn't hardcode it by checking one input `subtract(8,0);`, it could also be flawed in teh sense
that `subtract(8,0);` has a special property: subtracting `0` won't change anything because the ansser will always be the first number. 
Test-gaming is when an AI cheats to get a green check (for example: "all tests passed") without running the tests
it was meant to run. It gamed the tests.


