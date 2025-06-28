import csv

def load_data(filename):
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        all_rows = list(reader)
        header = all_rows[0]
        data = all_rows[1:]
    return header, data

def find_s_algorithm(data):
    for row in data:
        if row[-1].lower() == 'yes':
            hypothesis = row[:-1]
            break
    for row in data:
        if row[-1].lower() == 'yes':
            for i in range(len(hypothesis)):
                if row[i] != hypothesis[i]:
                    hypothesis[i] = '?'
    return hypothesis

def main():
    header, data = load_data('training_data.csv')
    print("Training Data:")
    for row in data:
        print(row)
    final_hypothesis = find_s_algorithm(data)
    print("\nFinal Hypothesis:")
    print(final_hypothesis)

if __name__ == "__main__":
    main()
