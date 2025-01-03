# Kpopchords.com Chords Extractor

## Description

This Python script takes a kpopchords.com HTML link, extracts the lyrics and chords, and formats it to an output.txt. 
I haven't extensively tested it. I created it to use for specific pages that don't allow me to copy and paste.

## Dependencies

Ensure you have the following Python packages installed:

- `requests` – To fetch the HTML content from the URL
- `beautifulsoup4` – To parse and extract data from the HTML

You can install these dependencies using pip:

```bash
pip install requests beautifulsoup4
```

## Installation

1. Clone or download this repository.
2. Install dependencies as mentioned above.
3. Ensure Python 3.x is installed on your system.

## Usage

Run the script by passing the URL as a parameter:

```bash
python converter.py <url>
```

Example:

```bash
python converter.py https://www.kpopchords.com/suzy-cape-chords-lyrics.html
```

### Output

- The parsed and formatted chord-lyric data is saved in `output.txt` in the same directory as the script.

