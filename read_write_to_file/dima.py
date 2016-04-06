import re

def replace(file1, file2):
    matches_res = {}
    with open(file1) as f1:
        for line_in_f1 in f1:
            matches = re.match('(\w{1})=(\w{1})', line_in_f1)
            matches_res[matches.group(1)] = matches.group(2)
        with open(file2, 'r+') as f2:
            file_content = f2.read()
            replaced_content = None
            for replacement in matches_res:
                replaced_content = file_content.replace(replacement, matches_res[replacement])

        if replaced_content is not None:
            with open(file2, "w") as f2:
                f2.write(replaced_content)

replace("first_file", "second_file")

# replace(input('file1: '),input('file2: '))
