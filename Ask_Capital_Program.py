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