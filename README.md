# Python Password Generator

A Python-based password generator that creates secure, customizable passwords and stores them with associated platform names using a JSON-based storage system.

## Features

* Generate strong passwords with letters, numbers, and symbols
* Customize password length and composition
* Store generated passwords with platform names
* Retrieve saved passwords by platform
* Persistent storage using JSON

## How It Works

* The user selects how many letters, symbols, and numbers to include
* A random password is generated and shuffled
* The password is stored along with the platform name in `PyPasswordG.json`
* Users can retrieve previously saved passwords by entering the platform name

## Installation & Usage

1. Clone the repository:

```id="cln123"
git clone https://github.com/rcodes-ix/python-password-generator.git
```

2. Navigate to the folder:

```id="cd456"
cd python-password-generator
```

3. Run the program:

```id="run789"
python PyPasswordG.py
```

## Project Structure

* `PyPasswordG.py` → Main password generator logic
* `PyPasswordG.json` → Stores generated passwords

## Limitations

* Passwords are stored in plain text (not secure for real-world use)
* No encryption or hashing implemented
* Limited input validation

## Future Improvements

* Add password encryption or hashing
* Improve input validation
* Build a graphical user interface (GUI)
* Add password strength evaluation

## Author

Created by Rekik Samson

