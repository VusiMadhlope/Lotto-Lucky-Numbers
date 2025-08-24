# Lottery-Predictor-Project

Lotto Lucky Numbers is a project created from the one dream we all hope to achieve. the lotto. Its is a full stack lottery predictor project that utilizes

## ⚠️ Disclaimer
This project is for **educational purposes only**.  
Lottery outcomes are based on **random chance** — no prediction is guaranteed. 



## Features of project: 
1. Retrieve past/historical data:
    - Gathered histocrical lotto results from Kaggle or valid sources.

2. Data processing:
    - Once retrieved we load and clean the dataset using Python's built in 'csv' module or Pandas library. 
	- Store the drawn numbers in a structured format for analysis.
			
3. Pattern Analysis:
    - Establish how often each number appears, frequency analysis.
    - Determine the "hot" (most frequent), "mild" (occasional/periodically) ( and "cold" (least frequent)).
    - Track pair/triples that appear together often.

4. Generate the predictions:
    - From the numbers based on hot, mild & cold frequency, program draws the most "hot" or predicted numbers.

5. Results Output:
    - From the backend, the Python logic sends the results to the Frontend handled by HTML/CSS/JS.
    - Program also prints reults directly into the console.

6. Historical Results:
    - Users are able to check their historical draws.



## Flow of project:
1. User is presented with the UI (Frontend) and has the choice between three buttons, "Upload CSV", "Generate Quick Picks" and "Historical Predictions"
2. If user chooses to upload a csv document:
-   Python will process and clean the data.
-   Will analyse and identify patterns and generate predictions.
-   Then return the predictions to the frontend for display.

-   If user chooses to quick pick option it will draw and choose numbers for you and display as well.
-   Once drawn from either option user can also have the chance to see their past draen numbers under "Historical Predictions" which will take you to the "Historical Page".


 
## Tech Stack:
-   Frontend: HTML, CSS and JavaScript
-   Backend: Python and Flask
-   Data Analysis: Python Pandas Library and CVS handling
-   Data Source: Kaggle datasets, manually uploaded cvs.
