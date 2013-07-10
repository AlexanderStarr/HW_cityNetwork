'''
>>> [cityList, distances] = createDistanceMatrix()
>>> cityNetwork = createCityNetwork(cityList, distances, 400)
>>> sorted(cityNetwork["Wilmington NC"])
['Richmond VA', 'Roanoke VA', 'Rocky Mount NC', 'Salisbury MD', 'Savannah GA', 'Staunton VA', 'Sumter SC', 'Swainsboro GA', 'Washington DC', 'Waycross GA', 'Wilmington NC', 'Winchester VA', 'Winston-Salem NC']
>>> distances[7][6]
1510
>>> distances[6][7]
1510
>>> distances[6][6]
0
>>> distances[127][0]
34
>>> sorted(cityNetwork["Ravenna OH"])
['Ravenna OH', 'Reading PA', 'Richmond IN', 'Rochester NY', 'Saginaw MI', 'Saint Joseph MI', 'Sandusky OH', 'Scranton PA', 'South Bend IN', 'Springfield OH', 'Staunton VA', 'Steubenville OH', 'Stroudsburg PA', 'Syracuse NY', 'Terre Haute IN', 'Toledo OH', 'Toronto ON', 'Uniontown PA', 'Warren PA', 'Washington DC', 'Wheeling WV', 'Williamson WV', 'Williamsport PA', 'Wilmington DE', 'Winchester VA', 'Youngstown OH']
>>> "Uniontown PA" in cityNetwork["Roanoke VA"]
True
>>> "Roanoke VA" in cityNetwork["Uniontown PA"]
True
>>> cityNetwork = createCityNetwork(cityList, distances, 100000)
>>> len(cityNetwork["Yakima WA"])
128
>>> cityNetwork = createCityNetwork(cityList, distances, 10)
>>> len(cityNetwork["Yakima WA"])
1
>>> cityNetwork = createCityNetwork(cityList, distances, 30)
>>> sorted([x for x in cityNetwork.items() if len(x[1]) > 1])
[('Seattle WA', ['Tacoma WA', 'Seattle WA']), ('Steubenville OH', ['Wheeling WV', 'Steubenville OH']), ('Tacoma WA', ['Tacoma WA', 'Seattle WA']), ('Wheeling WV', ['Wheeling WV', 'Steubenville OH'])]
>>> distances[cityList.index("Seattle WA")][cityList.index("Selma AL")]
2739
>>> "Scranton" in cityList
False
>>> cityList.index("Winston-Salem NC")
5
>>> cityNetwork = createCityNetwork(cityList, distances, 400)
>>> sorted(cityNetwork.keys()[:10])
['Regina SK', 'San Antonio TX', 'Scottsbluff NE', 'Stockton CA', 'Tallahassee FL', 'Tuscaloosa AL', 'Twin Falls ID', 'Victoria TX', 'Waycross GA', 'Williamson WV']
>>> sorted(cityNetwork.values()[:3])
[['Twin Falls ID', 'Salt Lake City UT', 'Rock Springs WY', 'Richfield UT'], ['Vicksburg MS', 'Valdosta GA', 'Tuscaloosa AL', 'Tupelo MS', 'Tallahassee FL', 'Swainsboro GA', 'Selma AL'], ['Waycross GA', 'Valdosta GA', 'Tuscaloosa AL', 'Tampa FL', 'Tallahassee FL', 'Swainsboro GA', 'Selma AL', 'Savannah GA', 'Sarasota FL', 'Saint Augustine FL']]
>>> cN1 = createCityNetwork(cityList, distances, 300)
>>> cN2 = createCityNetwork(cityList, distances, 309)
>>> "Wichita KS" in cN2["Wichita Falls TX"] and "Wichita KS" not in cN1["Wichita Falls TX"]
True
>>> cN2["Wichita Falls TX"] >= cN1["Wichita Falls TX"]
True
'''
#-------------------------------------------------------
from hw5Solution import *
#-------------------------------------------------------
if __name__ == "__main__":
    import doctest
    doctest.testmod()
