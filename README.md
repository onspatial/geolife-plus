We are currently generating, processing, and uploading data here: https://osf.io/96tvy/. OSF has a storage limit, and we are exploring alternative options to host the data and link it to OSF. The data generation process is ongoing. The genetic algorithm is still running to achieve a better score.

In the following table, recording GPS locations for larger datasets is time-consuming. We provide configurations with the dataset to enable regeneration if necessary.

![image](https://github.com/onspatial/geolife-star/assets/168866932/5c945ec7-2a18-461a-a4e4-58a9d984d859)


The following table provides information for the generated data. We run the data generation for the top 10 parameter sets, and the ones that have already been generated and calculated are provided here. As the data generation finishes, we will update the data statistics here

![image](https://github.com/onspatial/geolife-star/assets/168866932/49209ddb-21ee-47f0-8e5e-cb8175af757c)


The score can range from negative to 1, not only between 0 and 1. It varies from negative semi-infinity to 1, depending on the metrics. As the number of agents increases or the number of days decreases, the score will drop due to the vast number of places, or less days impacting the number of trips and distances traveled in the simulation. This is because, in the simulation parameters studied, certain parameters affect the number of preferred locations, and agents are more likely to visit the nearest places. As the map becomes denser, the travel duration decreases. Additionally, the duration of the simulation is important because the agents' behavior may change over time due to financial situations, workplace changes, etc., which alter the distances traveled each day. Consequently, the averages in a longer simulation, such as over five years, will differ.

We combined the results for the top approximately 300 simulations and provided a dataset spanning 59k agents for 5 years, among other datasets.
