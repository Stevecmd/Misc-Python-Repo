import requests
import pandas as pd
from bs4 import BeautifulSoup

def get_clinic_name(clinic_id):
    url = f'https://{clinic_id}.portal.athenahealth.com/' # website link to be parsed according to the format of the url which has the clinic number in it
    response = requests.get(url)
    html = response.text # Converting the html page to text
    soup = BeautifulSoup(html, 'html-parser') # Activating Beautiful soup to parse the page into a html format
    clinic_name = soup.find_all('h1')[-1].text.strip() # finding all the H1 heading tags and stripping them
    return clinic_name # Returning the H1 heading tags (clinic names) without their html tags

start  = 12690 # Number from which to start the program
end = 12710 # Number from which to end the program

master_list = [] # Initializing an empty array to store the names that meet our criteria

for clinic_id in range(start, end+1): # We do end+1 so as to include the actual end number ie 12710
    data_dict = {}  # Initializing an empty dictionary
    data_dict['clinic_id'] = clinic_id # Populating the dictionary
    data_dict['clinic_name'] = get_clinic_name
    if data_dict['clinic_name'] != 'Payment Confirmation' and data_dict['clinic_name'] != "Sorry we cant find that practice. Make sure you typed the right address.":
        master_list.append(data_dict) # Setting parameters for exceptions to the results ie excluding unwanted items
    print(clinic_id)


df = pd.DataFrame(master_list) # Creating a data frame to output the info received above, this is done through the import pandas as pd import
df.to_csv('clinic_data.csv', index=False) # Creating an excel sheet with the dataframe info and removing the first column that contained index which was unnecessary