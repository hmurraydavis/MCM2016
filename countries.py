def countries(): 

    countries = {'Syria': 0,
        'Turkey': 1,
        'Greece': 2,
        'Bulgaria': 3,
        'Romania': 4,
        'Serbia': 5,
        'Macedonia': 6,
        'Albania': 7,
        'Montenegro': 8,
        'Bosnia': 9,
        'Hungary': 10,
        'Croatia': 11,
        'Slovenia': 12,
        'Italy': 13,
        'Switzerland': 14,
        'Austria': 15,
        'Germany': 16,
        'Czech Republic': 17,
        'Slovakia': 18,
        'Poland': 19,
        'Finland': 20,
        'Sweden': 21,
        'Norway': 22,
        'Denmark': 23,
        'Netherlands': 24,
        'Belgium': 25,
        'France': 26,
        'UK': 27,
        'Spain': 28,
        'Portugal': 29,
        'Malta': 30,
        'Morocco': 31,
        'Algeria': 32,
        'Tunisia': 33,
        'Libya': 34,
        'Egypt': 35,
        'Israel': 36,
        'Jordan': 37,
        'Lebanon': 38}
    return countries

def contiguousBorders(countries):
    edges = [ (countries['Syria'], countries['Turkey']),
        (countries['Syria'], countries['Lebanon']),
        (countries['Turkey'], countries['Bulgaria']),
        #(countries['Turkey'], countries['Greece']), 
        (countries['Bulgaria'], countries['Greece']), 
        (countries['Bulgaria'], countries['Romania']), 
        (countries['Bulgaria'], countries['Macedonia']), 
        (countries['Romania'], countries['Serbia']), 
        (countries['Romania'], countries['Hungary']), 
        (countries['Greece'], countries['Macedonia']), 
        (countries['Greece'], countries['Albania']), 
        (countries['Albania'], countries['Macedonia']), 
        (countries['Albania'], countries['Montenegro']), 
        (countries['Montenegro'], countries['Serbia']), 
        (countries['Montenegro'], countries['Bosnia']) ,
        (countries['Bosnia'], countries['Croatia']),
        (countries['Serbia'], countries['Hungary']),
        (countries['Hungary'], countries['Slovakia']),
        (countries['Hungary'], countries['Austria']),
        (countries['Croatia'], countries['Hungary']),
        (countries['Croatia'], countries['Slovenia']),
        (countries['Slovenia'], countries['Austria']),
        (countries['Slovenia'], countries['Italy']),
        (countries['Italy'], countries['Austria']),
        (countries['Italy'], countries['Switzerland']),
        (countries['Italy'], countries['France']),
        (countries['Switzerland'], countries['Austria']),
        (countries['Switzerland'], countries['Germany']),
        (countries['Switzerland'], countries['France']),
        (countries['Germany'], countries['Austria']),
        (countries['Germany'], countries['Denmark']),
        (countries['Germany'], countries['Netherlands']),
        (countries['Germany'], countries['Belgium']),
        (countries['Germany'], countries['Switzerland']),
        (countries['Austria'], countries['Germany']),
        (countries['Austria'], countries['Switzerland']),
        (countries['Czech Republic'], countries['Poland']), ## ??
        (countries['Czech Republic'], countries['Germany']),
        (countries['Czech Republic'], countries['Austria']),
        (countries['Poland'], countries['Czech Republic']),
        (countries['Poland'], countries['Germany']),
        (countries['Denmark'], countries['Sweden']),
        (countries['Norway'], countries['Sweden']),
        (countries['Norway'], countries['Finland']),
        (countries['Sweden'], countries['Finland']),
        (countries['Sweden'], countries['Norway']),
        (countries['Finland'], countries['Sweden']),
        (countries['Finland'], countries['Norway']),
        (countries['Netherlands'], countries['Germany']),
        (countries['Netherlands'], countries['Belgium']),
        (countries['Belgium'], countries['Netherlands']),
        (countries['Belgium'], countries['Germany']),
        (countries['Belgium'], countries['France']),
        (countries['France'], countries['Belgium']),
        (countries['France'], countries['Switzerland']),
        (countries['Spain'], countries['Portugal']),
        (countries['Spain'], countries['France']),
        (countries['Morocco'], countries['Algeria']),
        (countries['Tunisia'], countries['Algeria']),
        (countries['Libya'], countries['Tunisia']),
        (countries['Libya'], countries['Algeria']),
        (countries['Egypt'], countries['Libya']),
        (countries['Israel'], countries['Egypt']),
        (countries['Israel'], countries['Jordan']),
        (countries['Jordan'], countries['Egypt']),
        (countries['Slovakia'], countries['Poland']),
        (countries['Slovakia'], countries['Czech Republic']),
        (countries['Slovakia'], countries['Austria']),
        (countries['Lebanon'], countries['Israel'])  ] ##,
        #(countries[''], countries['']),
        #(countries[''], countries['']),
        #(countries[''], countries['']),
        # ]
    return edges
    
def waterRoutes(countries):
    waterRoutes = [ (countries['Egypt'], countries['Greece']),
        (countries['Turkey'], countries['Greece']),
        (countries['Greece'], countries['Italy']),
        (countries['Libya'], countries['Italy']),
        (countries['Libya'], countries['Malta']),
        (countries['Tunisia'], countries['Malta']),
        (countries['Algeria'], countries['France']),
        (countries['Algeria'], countries['Spain']),
        (countries['Morocco'], countries['Spain']),
        (countries['Malta'], countries['Italy']),
        (countries['France'], countries['UK']),
        (countries['Poland'], countries['Sweden']),
        (countries['Poland'], countries['Finland']),
        (countries['Poland'], countries['Norway']),
        (countries['Germany'], countries['Finland']),
        (countries['Germany'], countries['Sweden']),
        (countries['Germany'], countries['Norway']),
        (countries['Denmark'], countries['Norway']),
        (countries['Denmark'], countries['Finland']),
        (countries['Finland'], countries['Denmark']),
        (countries['Norway'], countries['Denmark'])  ]  ##,
        #(countries[''], countries['']),
    return waterRoutes
    
def africaCountries():
    return [ 'Morocco',
        'Algeria',
        'Tunisia', 
        'Libya',
        'Egypt'
    ]
    
def middleEastCountries():
    return [ 'Israel',
        'Jordan',
        'Lebanon',
        'Syria'
    ]
    
    
def nordicCountries():
    return ['Denmark',
        'Norway',
        'Sweden',
        'Finland'
    ]
    
def westernEuropeCountries():
    return ['France',
        'Belgium',
        'Netherlands',
        'Germany',
        'Switzerland',
        'Austria',
        'UK'
    ]
    
def centralEuropeCountries():
    return ['Slovenia',
        'Czech Republic',
        'Poland',
        'Bulgaria',
        'Romania',
        'Hungary',
        'Slovakia'
    ]
    
def southernEuropeCountries():
    return ['Portugal',
        'Spain',
        'Italy',
        'Slovenia',
        'Croatia',
        'Bosnia',
        'Montenegro',
        'Albania',
        'Greece',
        'Serbia',
        'Turkey',
        'Malta',
        'Macedonia'
    ]



    

if __name__ == '__main__':
    countries = countries()
    print contiguousBorders(countries)
