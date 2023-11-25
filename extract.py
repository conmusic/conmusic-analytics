import re
import time

target_filename = 'K3241.K03200Y0.D31111.ESTABELE'
filename = 'estabelecimentos0_conmusic.csv'

selected_lines = []
regex = r";\"5611205|9001902\";"

print('Before open')

start_read_timer = time.time()

with open(target_filename, 'r', encoding='ansi') as file:
    print('Sucessfully opened')

    line = file.readline()

    while line:
        if re.search(regex, line):
            selected_lines.append(line)

        line = file.readline()

end_read_timer = time.time()

read_time = end_read_timer - start_read_timer

print(f"File was read after {read_time} seconds. {len(selected_lines)} lines matched")

start_write_timer = time.time()

with open(filename, 'w') as filtered_file:
    while selected_lines:
        line = selected_lines.pop()

        filtered_file.write(line)

end_write_timer = time.time()

write_time = end_write_timer - start_write_timer

print(f"File written sucessfully after {write_time} seconds.")