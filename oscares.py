import json

with open('newNominees.txt') as f:
    input_str = f.read()

def parse_data(input_str):
    output = []
    categories = []
    current_category = ""
    current_nominees = []
    current_nominee = "";
    ended = True

    # Split the input string by line breaks
    lines = input_str.split('\n')

    # Loop through each line
    for line in lines:
        if ended:
            current_category = line
            current_nominees = []
            ended = False
        # If the line is empty, skip it
        elif not line:
            categories.append({"title": current_category, "nominees": current_nominees})
            ended = True
            continue
        # Otherwise, the line is a nominee
        elif current_nominee == "":
            current_nominee = line
        else:
            current_nominee += ", " + line
            current_nominees.append(current_nominee)
            current_nominee = ""

    # Add the last category to the output
    categories.append({"title": current_category, "nominees": current_nominees})

    return categories



res = parse_data(input_str)
res_string = json.dumps(res, ensure_ascii=False).encode('utf8')
text_file = open("nominations.json", "w", encoding='utf-8')
n = text_file.write(json.dumps(res, ensure_ascii=False))
text_file.close()

