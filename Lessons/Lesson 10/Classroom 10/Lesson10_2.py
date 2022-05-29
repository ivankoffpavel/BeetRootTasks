# Write a program that checks that DNA sequence is valid (consists only of the characters 'A', 'C', 'G', ’T’).
# If not - raise an Exception.
DNA_valid = 'A','C','G','T'
current_DNA = 'F','C','K','D'
for i in current_DNA:
    if i not in DNA_valid:
        raise Exception('DNA is bad')