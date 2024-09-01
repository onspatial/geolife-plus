Please download the dataset from: https://osf.io/96tvy/

In the following table, recording GPS locations for larger datasets is time-consuming. We provide configurations with the dataset to enable regeneration if necessary.

![image](https://github.com/user-attachments/assets/bf36b648-13b4-470e-ad5a-52a8fa0ffc5c)



The following table provides information for the generated data. We run the data generation for the top 10 parameter sets, and the ones that have already been generated and calculated are provided here. As the data generation finishes, we will update the data statistics here

![image](https://github.com/user-attachments/assets/8d60e37e-dd0c-4a60-9394-2f2b2242ddc6)



The score can range from negative to 1, not only between 0 and 1. It varies from negative semi-infinity to 1, depending on the metrics. As the number of agents increases or the number of days decreases, the score will drop due to the vast number of places, or less days impacting the number of trips and distances traveled in the simulation. This is because, in the simulation parameters studied, certain parameters affect the number of preferred locations, and agents are more likely to visit the nearest places. As the map becomes denser, the travel duration decreases. Additionally, the duration of the simulation is important because the agents' behavior may change over time due to financial situations, workplace changes, etc., which alter the distances traveled each day. Consequently, the averages in a longer simulation, such as over five years, will differ.

We combined the results for the top approximately 300 simulations and provided a dataset spanning 59k agents for 5 years, among other datasets.
