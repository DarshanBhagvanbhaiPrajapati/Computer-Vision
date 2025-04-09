#WAP to generate a csv file comprised of two columns named “alphabet” and “count”.
#Create a function to randomly generate a count for a given alphabet. Later, plot a
#histogram of alphabets that shows corresponding count.
import csv
import random
import string
import matplotlib.pyplot as plt

def generate_count():
    return random.randint(1, 20)

def generate_csv(filename, num_rows):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(["alphabet", "count"])
        for _ in range(num_rows):
            alphabet = random.choice(string.ascii_lowercase)
            count = generate_count()
            writer.writerow([alphabet, count])

def plot_histogram(filename):
    alphabets = []
    counts = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        next(reader)  
        for row in reader:
            alphabets.append(row[0])
            counts.append(int(row[1]))
    plt.bar(alphabets, counts)
    plt.xlabel('Alphabet')
    plt.ylabel('Count')
    plt.title('Histogram of Alphabets and Counts')
    plt.show()

generate_csv("data.csv", 50)
plot_histogram("data.csv")

