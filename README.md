# tsp-ai-project
Group number 8

Project Overview

Goal:

Build a Python program that calculates the optimal marketing route across the following towns:

Nairobi

Meru

Nyeri

Nandi

Kericho

Nakuru


Features:

Each town is visited once before returning to Nairobi (Round trip).

Travel distances are fetched using real-world data from the Google Maps API.

The optimal route is calculated using TSP (Travelling Salesperson Problem) algorithms.

The route is visualized on a map.

Project is hosted and collaborated on GitHub.




 How to Run the Project

Prerequisites

Python 3.7+

pip (Python package manager)

Google Maps API Key (Get from: https://developers.google.com/maps)


 Installation

1. Clone the repository:

git clone https://github.com/your-repo/tsp-marketing-routes.git
cd tsp-marketing-routes


2. Install dependencies:

pip install -r requirements.txt


3. Set your Google Maps API Key:
Create a .env file and add:

GOOGLE_MAPS_API_KEY=your_api_key_here


4. Run the application:

python main.py





 Team Members
Team leader:plan, coordinate,check progress ,ensure GitHub is active and everyone contributes.

Member A. Set up API ,generate distance matrix between towns 
Member B. Help member A get travel times/ distance and clean data
C.Implement the tsp using brute force 
D improve the algorithm using heuristics.
E.Define and implement appropriate data structures.
F . Plot the final route using na visualization tool ; folium.
G.Ensure everyone commits their work ,help others with git commands , manage branches.
H.write the README file(documentation).
I.Test the full code ,find bugs , suggest improvements and help others debug.

 Tools & Technologies Used

Python

Google Maps open route service 

Folium (for visualization)

Git + GitHub (for version control)

.env & dotenv (for managing secrets)




Sample Output

Example Optimal Route (Round Trip Starting & Ending in Nairobi):

Nairobi → Nakuru → Kericho → Nandi → Meru → Nyeri → Nairobi
Total Distance: 852.3 KM
Estimated Total Time: 12 hrs 35 mins

Sample Map Output:
 A map is generated displaying the route with clear directional arrows, city markers, and estimated distances between stops.
