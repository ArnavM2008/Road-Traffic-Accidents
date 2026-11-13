# Road-Traffic-Accidents

## Business Problem
This project analyzes road traffic accident data to
identify dangerous driving conditions and help an
autonomous vehicle company prioritize data collection.

## Dataset
Addis Ababa Road Traffic Accident Dataset

## Business Questions
1. What is the distribution of accident severity across different days of the week?
2. What are the top 5 most common causes of accidents?
3. How does the driver's driving experience impact the count of serious or fatal accidents (where Accident_severity is 'Serious Injury' or 'Fatal injury')?
4. What types of vehicles are most commonly involved in accidents?
5. What is the distribution of accidents by driver's age band?

### Week 2 SQL Results

1. **Lighting conditions:** Darkness with no lighting had the highest share of serious or fatal crashes, at **28.1%** of 192 recorded crashes.
2. **Weather data gap:** Fog or mist (10 crashes), raining and windy conditions (40), and snow (61) had the fewest recorded crashes, so they would provide the fewest examples for a model trained on this dataset.
3. **Weather and severity:** Among named weather conditions, windy conditions had the highest share of serious or fatal crashes (**16.3%**), compared with **16.0%** in normal conditions.
4. **Junction types:** Crashes in the **Other** junction category had the highest share of serious or fatal injuries, at **19.1%** of 445 recorded crashes.
5. **Crash frequency by hour:** The **5:00–5:59 p.m.** hour had the most recorded crashes, with **1,228**.

## Model Results
On the held-out 20% of crashes, the model achieved 53.0% accuracy, compared with 84.6% for always predicting slight injury.
The model correctly identified 198 of 380 serious or fatal crashes (52.1%) but failed to identify the other 182.
