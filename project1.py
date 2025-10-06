# SI 201 Project 1
# Your name: Norah Harper
# Your student id: 46495145
# Your email: norahha@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT):
# If you worked with generative AI also add a statement for how you used it.  
# 

def load_data(csv_file):
    with open(csv_file) as inFile:
        lines = inFile.readlines()
        peng_species_d = {}
        peng_island_d = {}
        peng_sex_d = {}
        peng_mass_d = {}
        for line in lines:
            values = line.rstrip('"\n').split(',')
            peng_num = values[0]
            peng_species = values[1]
            peng_island = values [2]
            peng_sex = values[7]
            peng_mass = values[6]
            peng_species_d[peng_num] = peng_species
            peng_island_d[peng_num] = peng_island
            peng_sex_d[peng_num] = peng_sex
            peng_mass_d[peng_num] = peng_mass
        peng_data = [peng_species_d, peng_island_d, peng_sex_d, peng_mass_d]
    return peng_data

def get_gentoos(peng_data):
    peng_species_d = peng_data[0]
    peng_island_d = peng_data[1]
    gentoo_islands = []
    for key, value in peng_species_d.items():
        if value == '"Gentoo"':
            gentoo_islands.append(peng_island_d[key])
    print(gentoo_islands)
    return gentoo_islands

def get_males(peng_data):
    peng_sex_d = peng_data[2]
    peng_mass_d = peng_data[3]
    male_masses = []
    for key, value in peng_sex_d.items():
        if value == '"Gentoo"':
            male_masses.append(peng_mass_d[key])
    return male_masses

def calc_percent(gentoo_islands):
    pass

def calc_average(male_masses):
    pass

def generate_report(percent_dream, average_mass):
    pass

def main():
    peng_data = load_data("penguins.csv")
    print(get_gentoos(peng_data))
    pass

if __name__ == '__main__':
    main()