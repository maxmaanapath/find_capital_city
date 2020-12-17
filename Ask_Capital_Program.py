import sys
from tkinter import Tk, simpledialog, messagebox

def read_from_file():
    with open('worldcapital.txt', 'r') as file:
        for line in file:
            line = line.rstrip('\n')
            country, capital = line.split('/')
            country = country.capitalize()
            capital = capital.capitalize()
            world_capital[country] = capital

def write_to_file(country_name, capital_name):
    with open('worldcapital.txt', 'a') as file:
        file.write('\n')
        file.write(country_name + '/' + capital_name)
        file.close()
root = Tk()
root.withdraw()
world_capital = {}