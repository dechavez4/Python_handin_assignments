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