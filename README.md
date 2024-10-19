# Japanese Practice Tool

A terminal-based tool for practicing Japanese kana and other characters. This project serves as a fun and educational way to learn and memorize Japanese characters by testing your knowledge through romaji input. The project also allows for expansion, enabling you to add more characters like kanji or full words.

## Features

- Practice different sets of Japanese characters (e.g., Hiragana, Katakana, Kanji).
- Add your own character sets by modifying JSON files.
- Randomized character order to keep the practice engaging.
- Performance statistics after each session, with motivational feedback based on results.
- Option to replay or quit after completing a session.

## How It Works

1. Choose one or more character sets to practice from a list of available sets in the `data` folder.
2. For each character in the set, enter the correct romaji translation.
3. Get feedback on your correct and incorrect answers.
4. Receive a performance summary with percentages of correct and incorrect answers.
5. Optionally, replay or quit after reviewing your results.

## Installation

1. Clone the repository:

   ```
   git clone https://github.com/YourUsername/japanese-practice.git
   cd japanese-practice
   ```

2. Install required Python dependencies:

   ```
   pip install inquirer
   ```

3. Add character sets (if needed) in the `data` folder as `.json` files. Follow the template shown below.

## Running the Game

To start practicing, simply run the `game.py` script:

```
python game.py
```

You'll be prompted to choose the character sets you want to practice. Enter the correct romaji for each character shown.

## Adding New Character Sets

You can expand the character sets by adding `.json` files to the `data` folder. Each JSON file should follow this format:

```
{
  "name": "Set Name",
  "description": "Brief description of the set.",
  "characters": {
    "character": ["romaji", "additional romaji if applicable"]
  }
}
```

Example (`hiragana.json`):

```
{
  "name": "Hiragana",
  "description": "The most basic component of the Japanese writing system.",
  "characters": {
    "あ": ["a"],
    "い": ["i"],
    "う": ["u"],
    "え": ["e"],
    "お": ["o"]
  }
}
```

## Contributing

Feel free to fork the project and submit pull requests for new features or bug fixes. Contributions for additional character sets (e.g., Katakana, Kanji) are highly appreciated.

## License

This project is licensed under the MIT License.
