num_of_countries = int(input())

countries = set()
for i in range(num_of_countries):
    country = input()
    countries.add(country)
    
print(len(countries))