import sys

if len(sys.argv) < 2:
    print("usage: python listify.py <path>")
else:
    with open(sys.argv[1], 'r') as f:
        lines = f.readlines()

    new_lines = lines
    print(new_lines)
    for i, line in enumerate(lines):
        if line.strip() != "":
            if line.strip()[0] in ('(', '['):
                if line.strip()[:3] == "- [ ]" or line.strip()[0] not in ("(", "["):
                    continue

                new_line = line
                open_found_idx = -1
                for j, char in enumerate(line):
                    if char in ('(', '[') and open_found_idx == -1:
                        new_line = new_line[:j] + "- [ ]" + new_line[j+1:]
                        open_found_idx = j
                        new_lines[i] = new_line
                    elif char in (')', ']') and open_found_idx != -1:
                        new_line = new_line[:open_found_idx+5] + line[j+1:]
                        new_lines[i] = new_line
                        break

    print(new_lines)

    with open(sys.argv[1], 'w') as f:
        f.writelines(new_lines)
