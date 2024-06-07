import csv
import sys


def longest_match(sequence, subsequence):
    """Returns length of longest run of subsequence in sequence."""

    # Initialize variables
    longest_run = 0
    subsequence_length = len(subsequence)
    sequence_length = len(sequence)

    # Check each character in sequence for most consecutive runs of subsequence
    for i in range(sequence_length):

        # Initialize count of consecutive runs
        count = 0

        # Check for a subsequence match in a "substring" (a subset of characters) within sequence
        # If a match, move substring to next potential match in sequence
        # Continue moving substring and checking for matches until out of consecutive matches
        while True:

            # Adjust substring start and end
            start = i + count * subsequence_length
            end = start + subsequence_length

            # If there is a match in the substring
            if sequence[start:end] == subsequence:
                count += 1

            # If there is no match in the substring
            else:
                break

        # Update most consecutive matches found
        longest_run = max(longest_run, count)

    # After checking for runs at each character in seqeuence, return longest run found
    return longest_run


def main():

    if len(sys.argv) != 3:
        print("Please provide a DNA sample and a DNA database")
    data_list = []
    DNA = ""

    with open(sys.argv[1], mode='r') as DNA_source:
        csv_reader = csv.DictReader(DNA_source)
        for row in csv_reader:
            for key in row:
                if key != 'name':  # Skip the 'name' field
                    row[key] = int(row[key])
            data_list.append(row)

    with open(sys.argv[2], mode='r') as DNA_sequence:
        DNA = DNA_sequence.read().strip()

    STR_dict = {}
    for key in data_list[0]:
        if key != 'name':
            STR_dict[key] = 0
    for STR in STR_dict:
        longest = longest_match(DNA, STR)
        STR_dict[STR] = longest

    for profile in data_list:
        match = True
        for STR in STR_dict:
            if profile[STR] != STR_dict[STR]:
                match = False
                break
        if match:
            print(profile['name'])
            return

    print("No match")

    return


main()
