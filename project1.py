# SI 201 Project 1
# Your name: Norah Harper
# Your student id: 46495145
# Your email: norahha@umich.edu
# Who or what you worked with on this homework (including generative AI like ChatGPT): Used ChatGPT to help me understand errors I was getting with my test cases and stripping csv text
# 

import unittest

def load_data(csv_file):
    with open(csv_file) as inFile:
        next(inFile)  # skip header line
        peng_species_d = {}
        peng_island_d = {}
        peng_sex_d = {}
        peng_mass_d = {}
        for line in inFile:
            values = [v.strip().strip('"') for v in line.strip().split(",")]
            peng_num = values[0]
            peng_species = values[1]
            peng_island = values[2]
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
        if value == 'Gentoo':
            gentoo_islands.append(peng_island_d[key])
    return gentoo_islands

def get_males(peng_data):
    peng_sex_d = peng_data[2]
    peng_mass_d = peng_data[3]
    male_masses = []
    for key, value in peng_sex_d.items():
        if value == 'male':
            male_masses.append(peng_mass_d[key])
    return male_masses

def calc_percent(gentoo_islands):
    peng_count = 0
    island_count = 0
    for value in gentoo_islands:
        peng_count += 1
        if value == "Dream":
            island_count += 1
    if peng_count == 0:
        return 0
    return (island_count / peng_count) * 100

def calc_average(male_masses):
    peng_count = 0
    total_mass = 0
    for value in male_masses:
        if value != "NA":
            total_mass += float(value)
            peng_count += 1
    if peng_count == 0:
        return 0
    return total_mass / peng_count

def generate_report(percent_dream, average_mass):
    fout = open('output.txt', 'w')
    line1 = f"Percentage of Gentoos from Dream Island: {percent_dream}\n"
    fout.write(line1)
    line2 = f"Average body mass in grams of male penguins: {average_mass}\n"
    fout.write(line2)
    fout.close()
    return 'output.txt'

class myTests(unittest.TestCase):

    def setUp(self):
        self.peng_data = load_data("penguins.csv")
        self.gentoo_islands = get_gentoos(self.peng_data)
        self.percent_dream = calc_percent(self.gentoo_islands)
        self.male_masses = get_males(self.peng_data)
        self.average_mass = calc_average(self.male_masses)

    def test_percent_dream(self):
        self.assertAlmostEqual(self.percent_dream, 0.00, 2, "test percent_dream")

    def test_average_mass(self):
        self.assertAlmostEqual(self.average_mass, 4545.68, 2, "test average_mass")

    def test_case_3(self):
        self.assertEqual(self.peng_data[3]["4"], "NA", 'test reading "NA" for mass')
        pass

    def test_case_4(self):
        self.assertEqual(self.peng_data[0]["344"], 'Chinstrap', 'test end of file')
        pass

def main():
    peng_data = load_data("penguins.csv")
    gentoo_islands = get_gentoos(peng_data)
    percent_dream = calc_percent(gentoo_islands)
    male_masses = get_males(peng_data)
    average_mass = calc_average(male_masses)
    fout = open(generate_report(percent_dream, average_mass))
    print(fout.read())
    fout.close()
    pass

if __name__ == '__main__':
    main()
    unittest.main()