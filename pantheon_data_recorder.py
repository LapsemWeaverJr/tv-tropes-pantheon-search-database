# File began on February 3rd, 2024

# This bit is for showing how long it takes for the program to do its thing.
import time
start = time.time()

# This first line prepares the pantheon data .csv file to have information written into it.
pantheon_data = open('pantheon_data.csv', 'w', encoding='utf-8')

# This "list_of_files" array would correspond to the addresses of wherever the text data of each Pantheon page is
# stored. Currently, they're arranged as "<House>/<Hall>.txt", except for the House itself, where the <Hall> bit is a 0
# instead. I don't expect that this is how TV Tropes stores the Pantheon pages, and I plan on this being replaced with
# the real addresses of the text files that contain the Pantheon page data.
list_of_files = open('list_of_pantheon_pages.txt', 'r', encoding='utf-8').read().replace('\n', ', ').split(', ')

# This for loop then searches through every line of each page, looking for if each line begins with a certain phrase
# that tells the program, "Yes, this line is where the Pantheon Search Database Data is stored."
for x in list_of_files:
    # However, if the file doesn't exist, this try-except block keeps the program from halting when it tries to scan a
    # nonexistent file.
    try:
        # This is how it does it: for each text-file address, it takes the data therein (what you'd see while editing
        # the page) and converts it into a list, such that each line of the file sits on its own.
        current_file = open(x, 'r', encoding='utf-8').read().split('\n')
        for y in current_file:
            # The program then checks each line to see if it begins with the phrase that points out where the data is,
            # and if it is, it records the data into the data-file.
            if y.startswith('%% PANTHEON SEARCH DATABASE DATA: [='):
                pantheon_data.write(y.replace('%% PANTHEON SEARCH DATABASE DATA: [=', '').replace('=]', '\n'))
    except FileNotFoundError:
        print('File not found: \"' + x + '\"')
pantheon_data.close()
print(f'Total elapsed time: {(time.time() - start):.3f} seconds')
