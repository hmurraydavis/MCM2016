def coList():
    countries = ['Syria',
        'Turkey',
        'Greece',
        'Bulgaria',
        'Romania',
        'Serbia',
        'Macedonia',
        'Albania',
        'Montenegro',
        'Bosnia',
        'Hungary',
        'Croatia',
        'Slovenia',
        'Italy',
        'Switzerland',
        'Austria',
        'Germany',
        'Czech Republic',
        'Slovakia',
        'Poland',
        'Finland',
        'Sweden',
        'Norway',
        'Denmark',
        'Netherlands',
        'Belgium',
        'France',
        'UK',
        'Spain',
        'Portugal',
        'Malta',
        'Morocco',
        'Algeria',
        'Tunisia',
        'Libya',
        'Egypt',
        'Israel',
        'Jordan',
        'Lebanon']
    return countries

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
        (countries['Syria'], countries['Jordan']),
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
        (countries['Macedonia'], countries['Serbia']),  
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
    
def countryList():
    return countries()
    
    
def distanceBetweenCountries(): 
    countries = countryList()
        
    distances = {(countries['Albania'],countries['Macedonia']):.15 ,
            (countries['Albania'],countries['Montenegro']): .15,
            (countries['Algeria'],countries['France']):.9 ,
            (countries['Algeria'],countries['Spain']):.9 ,
            (countries['Austria'],countries['Germany']):.4 ,
            (countries['Austria'],countries['Switzerland']):.4 ,
            (countries['Belgium'],countries['Germany']):.4 ,
            (countries['Belgium'],countries['Netherlands']):.15 ,
            (countries['Belgium'],countries['France']):.4 ,
            (countries['Bosnia'],countries['Croatia']):.15 ,
            (countries['Bulgaria'],countries['Greece']):.4 ,
            (countries['Bulgaria'],countries['Macedonia']):.4 ,
            (countries['Bulgaria'],countries['Romania']):.4 ,
            (countries['Czech Republic'],countries['Austria']):.15 ,
            (countries['Czech Republic'],countries['Germany']):.4 ,
            (countries['Czech Republic'],countries['Poland']):.15 ,
            (countries['Croatia'],countries['Hungary']):.4 ,
            (countries['Croatia'],countries['Slovenia']):.15 ,
            (countries['Denmark'],countries['Finland']):.9 ,
            (countries['Denmark'],countries['Norway']):.4 ,
            (countries['Denmark'],countries['Sweden']):.65 ,
            (countries['Egypt'],countries['Greece']):.9 ,
            (countries['Egypt'],countries['Libya']):.9 ,
            (countries['France'],countries['Belgium']):.4 ,
            (countries['France'],countries['Switzerland']):.4 ,
            (countries['France'],countries['UK']):.9 ,
            (countries['Finland'],countries['Denmark']):.9 ,
            (countries['Finland'],countries['Sweden']):.4 ,
            (countries['Finland'],countries['Norway']):.65 ,
            (countries['Germany'],countries['Austria']):.4 ,
            (countries['Germany'],countries['Belgium']):.4 ,
            (countries['Germany'],countries['Denmark']):.4 ,
            (countries['Germany'],countries['Finland']):.9 ,
            (countries['Germany'],countries['Netherlands']):.4 ,
            (countries['Germany'],countries['Norway']):.9 ,
            (countries['Germany'],countries['Sweden']):.9 ,
            (countries['Germany'],countries['Switzerland']):.4 ,
            (countries['Greece'],countries['Albania']):.15 ,
            (countries['Greece'],countries['Italy']):.65 ,
            (countries['Greece'],countries['Macedonia']):.15 ,
            (countries['Hungary'],countries['Austria']):.4 ,
            (countries['Hungary'],countries['Slovakia']):.15 ,
            (countries['Israel'],countries['Egypt']):.65 ,
            (countries['Israel'],countries['Jordan']):.15 ,
            (countries['Italy'],countries['Austria']):.65 ,
            (countries['Italy'],countries['France']):.65 ,
            (countries['Italy'],countries['Switzerland']):.65 ,
            (countries['Jordan'],countries['Egypt']):.65 ,
            (countries['Lebanon'],countries['Israel']):.4 ,
            (countries['Libya'],countries['Algeria']):.9 ,
            (countries['Libya'],countries['Italy']):.9 ,
            (countries['Libya'],countries['Malta']):.9 ,
            (countries['Libya'],countries['Tunisia']):.9 ,
            (countries['Macedonia'],countries['Serbia']):.15 ,
            (countries['Malta'],countries['Italy']):.4 ,
            (countries['Montenegro'],countries['Bosnia']):.15 ,
            (countries['Montenegro'],countries['Serbia']):.15 ,
            (countries['Morocco'],countries['Algeria']):.65 ,
            (countries['Morocco'],countries['Spain']):.9 ,
            (countries['Netherlands'],countries['Germany']):.4 ,
            (countries['Netherlands'],countries['Belgium']):.15 ,
            (countries['Norway'],countries['Finland']):.65 ,
            (countries['Norway'],countries['Sweden']):.4 ,
            (countries['Norway'],countries['Denmark']):.4 ,
            (countries['Poland'],countries['Czech Republic']):.15 ,
            (countries['Poland'],countries['Finland']):.9 ,
            (countries['Poland'],countries['Germany']):.65 ,
            (countries['Poland'],countries['Norway']):.9 ,
            (countries['Poland'],countries['Sweden']):.65 ,
            (countries['Romania'],countries['Hungary']):.4 ,
            (countries['Romania'],countries['Serbia']):.4 ,
            (countries['Serbia'],countries['Hungary']):.4 ,
            (countries['Slovakia'],countries['Austria']):.15 ,
            (countries['Slovakia'],countries['Czech Republic']):.4 ,
            (countries['Slovakia'],countries['Poland']):.4 ,
            (countries['Slovenia'],countries['Austria']):.15 ,
            (countries['Slovenia'],countries['Italy']):.4 ,
            (countries['Spain'],countries['France']):.65 ,
            (countries['Spain'],countries['Portugal']):.4 ,
            (countries['Sweden'],countries['Finland']):.4 ,
            (countries['Sweden'],countries['Norway']):.4 ,
            (countries['Switzerland'],countries['Austria']):.4 ,
            (countries['Switzerland'],countries['France']):.4 ,
            (countries['Switzerland'],countries['Germany']):.4 ,
            (countries['Syria'],countries['Lebanon']):.4 ,
            (countries['Syria'],countries['Turkey']):.4 ,
            (countries['Syria'],countries['Jordan']):.4 ,
            (countries['Tunisia'],countries['Algeria']):.65 ,
            (countries['Tunisia'],countries['Malta']):.4 ,
            (countries['Turkey'],countries['Bulgaria']):.65 ,
            (countries['Turkey'],countries['Greece']):.9 
        }
#    print distances
    return distances

def nativePopulationCountries(): 
    countries = {'Syria': 22850000,
        'Turkey': 75932348.00,
        'Greece': 11030000.00,
        'Bulgaria': 6924716,
        'Romania': 21729871,
        'Serbia': 7209764,
        'Macedonia': 2091719,
        'Albania': 2894475,
        'Montenegro': 650036,
        'Bosnia': 3871000,
        'Hungary': 9919128,
        'Croatia': 4470534.00,
        'Slovenia': 2061000,
        'Italy': 61070224,
        'Switzerland': 8139600,
        'Austria': 8223062,
        'Germany': 82652256,
        'Czech Republic': 10538300,
        'Slovakia': 5417000,
        'Poland': 38020000.00,
        'Finland': 5268799,
        'Sweden': 9644864,
        'Norway': 5109059,
        'Denmark': 5617000,
        'Netherlands': 16860000.00,
        'Belgium': 11204000,
        'France': 64641279,
        'UK': 64597000,
        'Spain': 46439864,
        'Portugal': 10401000,
        'Malta': 412655,
        'Morocco': 32987206,
        'Algeria': 38700000,
        'Tunisia': 10937521,
        'Libya': 6244174,
        'Egypt': 83386739,
        'Israel': 8200000,
        'Jordan': 6607000,
        'Lebanon': 4500000}
    return countries

def safetyCountries(): 
    countries = {'Syria': 0.47,
        'Turkey': 0.73,
        'Greece': 0.82,
        'Bulgaria': 0.88,
        'Romania': 0.89,
        'Serbia': 0.85,
        'Macedonia': 0.81,
        'Albania': 0.84,
        'Montenegro': 0.83,
        'Bosnia': 0.83,
        'Hungary': 0.91,
        'Croatia': 0.89,
        'Slovenia': 0.92,
        'Italy': 0.87,
        'Switzerland': 0.95,
        'Austria': 0.96,
        'Germany': 0.92,
        'Czech Republic': 0.93,
        'Slovakia': 0.90,
        'Poland': 0.91,
        'Finland': 0.94,
        'Sweden': 0.93,
        'Norway': 0.92,
        'Denmark': 0.97,
        'Netherlands': 0.91,
        'Belgium': 0.93,
        'France': 0.85,
        'UK': 0.86,
        'Spain': 0.91,
        'Portugal': 0.93,
        'Malta': 0.87,
        'Morocco': 0.80,
        'Algeria': 0.77,
        'Tunisia': 0.81,
        'Libya': 0.64,
        'Egypt': 0.72,
        'Israel': 0.64,
        'Jordan': 0.81,
        'Lebanon': 0.68}
    return countries
    
def refugeeApplicationsCountries(): 
    countries = {'Syria': 1, 
        'Turkey': 145335, 
        'Greece': 4862,
        'Bulgaria': 16929,
        'Romania': 2449,
        'Serbia': 276211,
        'Macedonia': 2087,
        'Albania': 190,
        'Montenegro': 2975,
        'Bosnia': 103,
        'Hungary': 71999,
        'Croatia': 359,
        'Slovenia': 193,
        'Italy': 2417,
        'Switzerland': 11180,
        'Austria': 31160,
        'Germany': 184053,
        'Czech Republic': 357,
        'Slovakia': 62,
        'Poland': 746,
        'Finland': 1127,
        'Sweden': 102870,
        'Norway': 11246,
        'Denmark': 15978,
        'Netherlands': 29813,
        'Belgium': 13768,
        'France': 9431,
        'UK': 8060,
        'Spain': 7631,
        'Portugal': 190,
        'Malta': 1191,
        'Morocco': 2216, 
        'Algeria': 5892, 
        'Tunisia': 156, 
        'Libya': 8904, 
        'Egypt': 30019, 
        'Israel': 1,
        'Jordan': 20693,
        'Lebanon': 10851}
    return countries
    
def refugeeEstimateCountries(): 
    countries={'Germany': 500000,
    'Jordan': 1400000,
    'Ireland': 10250,
    'Albania': 8000,
    'SlovakRepublic': 2500,
    'CzechRepublic': 3000,
    'Bulgaria': 18000,
    'Tunisia': 1000,
    'France': 320000,
    'Malta': 1500,
    'Italy': 15000,
    'Poland': 25000,
    'Estonia': 86000,
    'Croatia': 5000,
    'Netherlands': 90000,
    'Sweden': 225000,
    'Macedonia': 3000,
    'Greece': 37000,
    'Morocco': 4000,
    'Bosnia': 150000,
    'Austria': 92000,
    'Hungary': 50000,
    'Luxembourg': 2000,
    'Norway': 50000,
    'Portugal': 1350,
    'UnitedKingdom': 155000,
    'Lebanon': 1200000,
    'Spain': 17000,
    'Denmark': 27000,
    'Slovenia': 400,
    'Switzerland': 80000,
    'Israel': 45000,
    'Algeria': 100000,
    'Turkey': 2200000,
    'Serbia': 250000,
    'Montenegro': 15000,
    'Romania': 2800,
    'Egypt': 180000,
    'Syria': 0,
    'Belgium': 45000, 
    'Libya': 40000,
    'Finland': 15000}
    
    return countries

def gniPerCapitaCountries(): 
    countries = {'Syria': 5090.00, ## <-- Suspect value
        'Turkey': 10830.00, 
        'Greece': 22680.00,
        'Bulgaria': 7620.00,
        'Romania': 9520.00,
        'Serbia': 5820.00,
        'Macedonia': 5150.00,
        'Albania': 4450.00,
        'Montenegro': 7320.00,
        'Bosnia': 4760.00,
        'Hungary': 13340.00,
        'Croatia': 12980.00,
        'Slovenia': 23580.00,
        'Italy': 34270.00,
        'Switzerland': 88120.00,
        'Austria': 49670.00,
        'Germany': 47640.00,
        'Czech Republic': 18370.00,
        'Slovakia': 17750.00,
        'Poland': 13690.00,
        'Finland': 48420.00,
        'Sweden': 61610.00,
        'Norway': 103630.00,
        'Denmark': 61310.00,
        'Netherlands': 51890.00,
        'Belgium': 47260.00,
        'France': 42960.00,
        'UK': 43430.00,
        'Spain': 29440.00,
        'Portugal': 21360.00,
        'Malta': 21000.00,
        'Morocco': 3070.00, 
        'Algeria': 5490.00, 
        'Tunisia': 4230.00, 
        'Libya': 7820.00, 
        'Egypt': 3050.00, 
        'Israel': 35320.00,
        'Jordan': 5160.00,
        'Lebanon': 10030.00}
    return countries

def unemploymentCountries(): 
    countries = {'Syria': .75, 
        'Turkey': 0.11, 
        'Greece': 0.24,
        'Bulgaria': 0.10,
        'Romania': 0.07,
        'Serbia': 0.17,
        'Macedonia': 0.25,
        'Albania': 0.18,
        'Montenegro': 0.17,
        'Bosnia': 0.43,
        'Hungary': 0.06,
        'Croatia': 0.18,
        'Slovenia': 0.12,
        'Italy': 0.11,
        'Switzerland': 0.04,
        'Austria': 0.11,
        'Germany': 0.05,
        'Czech Republic': 0.06,
        'Slovakia': 0.11,
        'Poland': 0.10,
        'Finland': 0.09,
        'Sweden': 0.07,
        'Norway': 0.05,
        'Denmark': 0.05,
        'Netherlands': 0.07,
        'Belgium': 0.08,
        'France': 0.11,
        'UK': 0.05,
        'Spain': 0.21,
        'Portugal': 0.12,
        'Malta': 0.05,
        'Morocco': 0.10, 
        'Algeria': 0.11, 
        'Tunisia': 0.15, 
        'Libya': 0.20, 
        'Egypt': 0.13, 
        'Israel': 0.05,
        'Jordan': 0.14,
        'Lebanon': 0.06}
    return countries

def educationCountries(): 
    countries= {"Germany": 0.044,
    'Jordan': 0.0496, 
    'Ireland': 0.057, 
    'Albania': 0.035,
    'Slovakia': 0.038,
    'Czech Republic': 0.044, 
    'Bulgaria': 0.036, 
    'Tunisia': 0.0622, 
    'France': 0.056, 
    'Malta': 0.0676,
    'Italy': 0.042,
    'Poland': 0.048, 
    'Estonia': 0.052, 
    'Croatia': 0.042, 
    'Netherlands': 0.05, 
    'Sweden': 0.062, 
    'Macedonia': 0.066, 
    'Greece': 0.04,
    'Morocco': 0.0538, 
    'Bosnia': 0.06, 
    'Austria': 0.055, 
    'Hungary': 0.044, 
    'Luxembourg': 0.043, 
    'Norway': 0.073, 
    'Portugal': 0.051, 
    'UK': 0.056, 
    'Lebanon': 0.0257, 
    'Spain': 0.053, 
    'Denmark': 0.079, 
    'Slovenia': 0.053, 
    'Switzerland': 0.056, 
    'Israel': 0.056, 
    'Algeria': 0.0434, 
    'Turkey': 0.034, 
    'Serbia': 0.044, 
    'Montenegro': 0.025,
    'Romania': 0.0299, 
    'Egypt': 0.0376, 
    'Syria': 0.0513, 
    'Belgium': 0.064, 
    'Libya': 0.0226,
    'Finland': 0.063}
    return countries
    
def lifeExpCountries(): 
    countries= {'Germany': 81.04,
    'Jordan': 73.9,
    'Ireland': 81.04,
    'Albania': 77.54,
    'Serbia': 75.14,
    'Bulgaria': 74.46,
    'Tunisia': 73.65,
    'France': 81.97,
    'Malta': 80.75,
    'Italy': 82.29,
    'Poland': 76.85,
    'Estonia': 76.42,
    'Croatia': 77.13,
    'Netherlands': 81.4,
    'Sweden': 82.0,
    'Macedonia': 75.18,
    'Greece': 80.63,
    'Morocco': 73.71,
    'Bosnia': 76.28,
    'Austria': 80.89,
    'Hungary': 75.27,
    'Luxembourg': 81.7,
    'Norway': 81.45,
    'Portugal': 80.37,
    'UK': 80.96,
    'Lebanon': 80.13,
    'Spain': 82.43,
    'Denmark': 80.3,
    'Slovenia': 80.28,
    'Switzerland': 82.75,
    'Israel': 82.06,
    'Algeria': 74.57,
    'Turkey': 75.18,
    'Czech Republic': 78.28,
    'Montenegro': 74.76,
    'Romania': 74.46,
    'Egypt': 70.92,
    'Syria': 74.71,
    'Slovakia': 76.26,
    'Belgium': 80.39,
    'Libya': 71.66,
    'Finland': 80.83}
    
    return countries
    
def healthCountries():
    countries={'Germany': 5006.0,
    'Jordan': 336.0,
    'Ireland': 4233.0,
    'Albania': 240.0,
    'Slovakia': 1454.0,
    'Czech Republic': 1367.0,
    'Bulgaria': 555.0,
    'Tunisia': 309.0,
    'France': 4864.0,
    'Malta': 2000.0, 
    'Italy': 3155.0,
    'Poland': 895.0,
    'Estonia': 1072.0,
    'Croatia': 982.0, 
    'Netherlands': 6145.0, 
    'Sweden': 5680.0, 
    'Macedonia': 312.0, 
    'Greece': 2146.0, 
    'Morocco': 314.0, 
    'Bosnia': 449.0, 
    'Austria': 5427.0, 
    'Hungary': 1056.0, 
    'Luxembourg': 7981.0, 
    'Norway': 9715.0, 
    'Portugal': 2037.0, 
    'UK': 3598.0, 
    'Lebanon': 631.0, 
    'Spain': 2581.0, 
    'Denmark': 6270.0, 
    'Slovenia': 2085.0,
    'Switzerland': 9276.0, 
    'Israel': 2599.0, 
    'Algeria': 314.0, 
    'Turkey': 608.0, 
    'Serbia': 475.0, 
    'Montenegro': 461.0, 
    'Romania': 504.0,
    'Egypt': 151.0, 
    'Syria': 43.0, 
    'Belgium': 5093.0, 
    'Libya': 433.0, 
    'Finland': 4449.0}
       
    return countries

def healthGDPCountries():
    countries={'Germany': 0.087, 
    'Jordan': 0.048, 
    'Ireland': 0.060, 
    'Albania': 0.028, 
    'Serbia': 0.064, 
    'Bulgaria': 0.045, 
    'Tunisia': 0.042, 
    'France': 0.090, 
    'Malta': 0.058, 
    'Italy': 0.071, 
    'Poland': 0.046,
    'Estonia': 0.045,
    'Croatia': 0.058,
    'Netherlands': 0.103,
    'Sweden': 0.779,
    'Macedonia': 0.044,
    'Greece': 0.068,
    'Morocco': 0.020,
    'Bosnia': 0.067, 
    'Austria': 0.084,
    'Hungary': 0.051,
    'Luxembourg': 0.059,
    'Norway': 0.082,
    'Portugal': 0.063, 
    'UK': 0.076,
    'Lebanon': 0.036, 
    'Spain': 0.063,
    'Denmark': 0.091, 
    'Slovenia': 0.066, 
    'Switzerland': 0.076, 
    'Israel': 0.043, 
    'Algeria': 0.049, 
    'Turkey': 0.043, 
    'Czech Republic': 0.060,
    'Montenegro': 0.037,
    'Romania': 0.043,
    'Egypt': 0.021,
    'Syria': 0.015, 
    'Slovakia': 0.058, 
    'Belgium': 0.085,
    'Libya': 0.030, 
    'Finland': 0.071}
    return countries
    
    
def transitionCoList (): 
    return ['Turkey', 'Greece', 'Bulgaria', 'Romania', 'Serbia', 'Albania', 
    'Macedonia', 'Montenegro', 'Bosnia', 'Croatia', 'Slovenia', 'Italy', 
    'Slovakia', 'Poland', 'Malta', 'Lebanon', 'Israel', 'Jordan', 'Egypt', 
    'Libya', 'Tunisia', 'Algeria']
    
def originCoList():
    return [ 'Syria', 'Morocco', 'Libya', 'Egypt', 'Jordan', 'Lebanon', 
    'Turkey' ]
    
def endCountryList():
    return [ 'UK', 'Sweden', 'Norway', 'Finland', 'Denmark', 'Germany', 
    'Austria', 'France', 'Belgium', 'Netherlands', 'Portugal', 'Spain', 
    'Switzerland', 'Hungary' ]
if __name__ == '__main__':
    #countries = countries()
    #print contiguousBorders(countries)
    #print coList()
    distances = distanceBetweenCountries()
    print lifeExpCountries()
    print educationCountries()
    print healthCountries()
    print healthGDPCountries()
