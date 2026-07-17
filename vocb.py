import csv

vocab_list = []
with open('vocab.csv', newline='', encoding='utf-8') as f:
    #tell the parser to use tab as the delimiter and two spaces as the quote character instead of regex re.split(r'\t|\s{2,}', line)

    reader = csv.reader(f, delimiter='\t') 
    
    for row in reader:
        if len(row) >= 2:
            card = {
                "format": row[0].strip(),
                "translation": row[1].strip()
            }
            vocab_list.append(card)
    print(vocab_list)

