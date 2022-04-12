import sys

# sys.argv: ["listify.py", <filename>, [0/1]]
if len(sys.argv) < 2:
    print("usage: python listify.py <path> <opt: overwrite 1/0>")
else:
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    new_lines = lines
    print(new_lines)
    for i, line in enumerate(lines):
        if line.strip() != "":
            if line.strip()[0] in ('(', '[', "-"):
                if line.strip()[:5] == "- [ ]" or line.strip()[0] not in ("(", "[", "-"):
                    continue

                new_line = line
                open_found_idx = -1
                for j, char in enumerate(line):
                    if char in ('(', '[', '-') and open_found_idx == -1:
                        # pre_str = line[:j]
                        new_line = line[:j] + "- [ ]" + line[j+1:]
                        open_found_idx = j
                        new_lines[i] = new_line
                    elif char in (')', ']') and open_found_idx != -1:
                        new_line = new_line[:open_found_idx+5] + line[j+1:]
                        new_lines[i] = new_line
                        break

    print(new_lines)

    if len(sys.argv) > 2:
        if sys.argv[2] == "1":
            with open(sys.argv[1], 'w') as f:
                f.writelines(new_lines)
        elif sys.argv[2] == "0":
            splitted_filename = sys.argv[1].split(".")
            with open(splitted_filename[0] + "_listified" + splitted_filename[1], 'w') as f:
                f.writelines(new_lines)
        else:
            print("usage: python listify.py <path> <opt: overwrite 1/0>")
    else:
        with open(sys.argv[1], 'w') as f:
            f.writelines(new_lines)
