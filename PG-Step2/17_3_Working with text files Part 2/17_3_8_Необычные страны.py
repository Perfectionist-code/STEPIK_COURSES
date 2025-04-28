with open('population.txt') as file:
    for line in file:
        country, population = line.split('\t')
        if country.startswith('G') and int(population) > 500_000:
            print(country)


