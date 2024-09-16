# System Design Interviews: A step by step guide

Generally, software engineers have difficult with system design interviews (SDIs) for three primary reasons:

- SDIs are unstructured and open-ended. They don't have a standard solution.
- Candidates lack experience reasoning about complex, large-scale systems.
- Insufficient time spent preparing.

SDIs are similar to coding interviews in that candidates who don't prepare well tend to do poorly, particularly at high-profile companies.
In these companies, candidates who do not perform above average have a limited chance to get an offer.
On the other hand, a good performance always results in a better offer (higher position and salary) since it proves the candidate's ability to handle a complex system.

## Schematic of a typical SDI

1. Requirements clarifications
2. Back-of-envelope estimation
3. System interface definition
4. Defining data model
5. High-level design
6. Detailed design
7. Identifying and resolving bottlenecks

### Step 1: Requirements clarifications

It is always a good idea to ask questions about the exact scope of the problem we are trying to solve.
Design questions are mostly open-ended, and they don't have ONE correct answer.
That's why clarifying ambiguities early in the interview becomes critical.
Candidates who spend enough time to define the end goals of the system always have a better chance to be successful in the interview.
Also, since we only have 35-40 minutes to design a (supposedly) large system, we should clarify what parts of the system we will be focusing on.
Being able to define a clean scoping boundary always helps.

Let's expand this with an actual example of designing a Twitter-like service.
Here are some questions for designing Twitter that should be answered before moving on to the next steps:

- Will users of our service be able to post tweets and follow other people?
- Should we also design to create and display the user's timeline?
- Will tweets contain photos and videos?
- Are we focusing on the back-end only, or are we developing the front-end too?
- Will users be able to search tweets?
- Do we need to display hot trending topics?
- will there be any push notification for new (or important tweets)?
- If we care about tweet "importance", will there be a customizable or user-dependent component to the ranking scoring?

Notice here that we are trying to explore, in a breadth-first fashion, the space of possible functionalities which the system needs to support.
Notice as well that the questions above are quite binary.
We don't want to ask how or why just yet.
We want to ask yes/no questions, just to feel out where the targets of our system design are.
So let your imagination run and be ready to take good notes about what you scope in or out.
The features that make it into the above bullet point list would inform your end design.
