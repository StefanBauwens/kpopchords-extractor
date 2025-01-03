import requests
from bs4 import BeautifulSoup
import sys

def fetch_html_from_url(url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    response = requests.get(url, headers=headers)
    response.raise_for_status()  # Raise for 403 or 404 errors
    return response.text

def parse_html_to_chords_and_lyrics(input_html):
    soup = BeautifulSoup(input_html, 'html.parser')
    lines = soup.find_all('div', class_='cpress_line')
    output = []

    for line in lines:           
        comment = line.find('span', class_='cpress_comment')
        if comment:
            output.append(f"\n[{comment.get_text(strip=True)}]\n\n")

        chords = line.find_all('div', class_='chord')
        lyrics = line.find_all('div', class_='lyric')

        chords_text = [chord.get_text(strip=True) for chord in chords if chord.get('style') is None]
        lyrics_text = [lyric.get_text(strip=True) for lyric in lyrics]

        for i in range(len(chords_text)):
            chord_length = len(chords_text[i])
            lyric_length = len(lyrics_text[i])
            if chord_length < lyric_length:
                chords_text[i] += ' ' * (lyric_length - chord_length)
        
        if chords_text or lyrics_text:
            output.append((chords_text, lyrics_text))

    return output

def convert_to_chordpress_format(output):
    formatted_output = []

    for item in output:
        if isinstance(item, str):
            formatted_output.append(item)
        else:
            chords, lyrics = item
            chords_line = " ".join(chords)
            lyrics_line = " ".join(lyrics)
            formatted_output.append(f"{chords_line}\n{lyrics_line}\n")

    return "".join(formatted_output)

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python script.py <url>")
        sys.exit(1)

    url = sys.argv[1]

    try:
        input_html = fetch_html_from_url(url)
        output = parse_html_to_chords_and_lyrics(input_html)
        formatted_output = convert_to_chordpress_format(output)

        output_file_path = 'output.txt'
        with open(output_file_path, 'w', encoding='utf-8') as output_file:
            output_file.write(formatted_output)

        print(f"Output saved to {output_file_path}")
    except requests.exceptions.RequestException as e:
        print(f"Error fetching URL: {e}")
