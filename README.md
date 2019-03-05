# NTU CSIE Seminar Poster Generator

## Installation

1. Install miniconda/anaconda, a package for  package/environment management
```
wget repo.continuum.io/miniconda/Miniconda3-latest-Linux-x86_64.sh
bash Miniconda3-latest-Linux-x86_64.sh
```

2. Build conda environment from file
```
conda env create -f environment.yaml
```

3. Activate the environment
```
source activate <environemnt name>
```


## Usage

The seminar announcement is a public Google Calendar, which could be fetched by the API.

This could be done by an script but here I just do it manually.

1. Go to Google Calendar API page:
https://developers.google.com/calendar/v3/reference/events/list?apix_params=%7B%22calendarId%22%3A%229so7940oqmaih91f869plrtsd8%40group.calendar.google.com%22%2C%22alwaysIncludeEmail%22%3Atrue%2C%22timeMin%22%3A%222019-03-01T10%3A30%3A00%2B08%3A00%22%7D

2. The NTU CSIE seminar annoucement calenderID is `9so7940oqmaih91f869plrtsd8@group.calendar.google.com`

3. Set `timeMin` or `updateMin` to cuurent time (e.g., `2019-03-01T10:30:00+08:00`)

4. Press `Execute`

5. Copy paste the API result

6. Run
```
python src/read_json.py -f 20190304.json
```

7. The result .docx will be in `outputs/`

## Repository Structure
```
├── .flake8                 Syntax and style settings for Flake8
├── .gitignore              Filenames in this file would be ignored by Git
├── .travis.yml             For Travis CI configuration
├── environment.yaml        For Conda environment
├── README.md
├── LICENSE                 LICENSE file (MIT license here)
├── .github/                For the PR template
├── tests/                  For tests
├── lib/                    For third-party libraries
└── src/                    For source code

```
## License

MIT 

## Authors

Ya-Liang Chang (Allen) [amjltc295](https://github.com/amjltc295/)


