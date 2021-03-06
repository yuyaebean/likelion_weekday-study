import sys


def main(in_file_name: str, out_file_name: str = 'zipped.txt') -> None:
    in_file_stream = open(in_file_name, 'r')
    out_file_stream = open(out_file_name, 'w')

    while True:
        line = in_file_stream.readline()
        if not line:
            break

        temp: str = ''
        count: int = 1
        current_line: str = ''
        for c in line:                      # c stands for character
            if temp == '':                  # initial condition
                temp = c
                count = 1
            elif temp != c:                 # if character changed
                current_line += temp
                current_line += str(count)
                temp = c
                count = 1
            else:                           # if character not changed
                count += 1
        if temp != '':
            current_line += temp
            current_line += str(count)
        out_file_stream.write(current_line)

    in_file_stream.close()
    out_file_stream.close()


if __name__ == '__main__':
    if len(sys.argv) < 2 or len(sys.argv) >= 4:
        print(
            f'Usage: {sys.argv[0]} <input_filename> <output_filename(optional)>')
    elif len(sys.argv) is 2:
        main(sys.argv[1])
    else:
        main(sys.argv[1], sys.argv[2])
