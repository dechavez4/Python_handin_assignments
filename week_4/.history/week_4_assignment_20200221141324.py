import numpy as np

filename = 'befkbhalderstatkode.csv'
bef_stats_df = np.genfromtxt(filename, delimiter=',', dtype=np.uint, skip_header=1)
dd = bef_stats_df
#exercise 3 people lived
neighb = {1: 'Indre By', 2: 'Østerbro', 3: 'Nørrebro', 4: 'Vesterbro/Kgs. Enghave', 
       5: 'Valby', 6: 'Vanløse', 7: 'Brønshøj-Husum', 8: 'Bispebjerg', 9: 'Amager Øst', 
       10: 'Amager Vest', 99: 'Udenfor'}
pp = neighb
def sumOfAllPeople():
    mask = (dd[:,0] == 2015) & (dd[:,1] == pp)
    return np.sum(dd[mask][:,4])
print(sumOfAllPeople())

#exercise 4 smallest and largest

#exercise 5 boolean:
def getPeopleOverSixtyFive():
    mask = (dd[:,0] == 2015) & (dd[:,2] <= 65)
    return np.sum(dd[mask][:,4])
#print(getPeopleOverSixtyFive())

#exercise 6 not DK
nordicCountryCodes = {5104: 'Finland', 5106: 'Island', 5110: 'Norge', 5120: 'Sverige'}
def sumNordicCountryCodesList():
    lst={}
    for key, value in nordicCountryCodes.items():
        lst.update({value: allNordicNotDK(key)})
    return lst

def allNordicNotDK(countryCode):
    mask = (dd[:,0] == 2015) & (dd[:,2] <=65) & (dd[:,3] == countryCode)
    return np.sum(dd[mask][:,4])
#print(sumNordicCountryCodesList())


#exercise 7 plotting