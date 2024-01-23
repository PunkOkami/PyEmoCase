import argparse
parser, x = argparse.ArgumentParser(prog='PyEmoCase', description='Python tool to change any case to Emo Case'), -1
parser.add_argument('text', help='text to be converted')
text = parser.parse_args().text
print(''.join([[el.upper() if i % 2 == 0 else el.lower() for i, el in enumerate([el for el in text if el.isalpha()]) if el.isalpha()][x := x + 1] if text[i].isalpha() else text[i] for i in range(len(text))]))