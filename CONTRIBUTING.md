# Developer Guidelines

## Directory structure.

The structure of the directory is as follows, not all of this is available through GitHub as explained below.
```
.
├── _ data/
│   ├── created/
│   └── original/
├──  misc/
├──  scripts/
├──  venv/
├── README.md
├── .gitignore
└── requirements.txt

```

| File/directory | Notes|
|----------------|------|
| `data/` | We don't provide the data here, since it is of a sensitive nature. |
| `data/created` | All newly created/processed data is stored in this directory |
| `data/created/arabic_corpus.csv` | Arabic script speeches |
| `data/created/english_corpus.csv` | Speeches translated into English |
| `data/original` | All original data should be stored in this directory (and the files should be made read-only. |
| `figures/` | This is where we will store figures |
| `misc/` | Contains miscellaneous documents relating to the project that we don't want to upload to GitHub, like timesheets, CVs, etc. |
| `scripts/` | Contains Python scripts. Each script has a docstring explaining what it does at the top of the file. |
| `.gitignore` | Tells Git what we want to save copies of (and therefore what will be visible on GitHub) and what we do not. |
| `CONTRIBUTING.md` | Explains how to get things installed, and how to make changes to the repository |
| `README.md` | Acts as a front-page for the GitHub repository for anyone who comes across it. |
| `requirements.txt` | Lists the Python packages that are needed to run the code. |

<!--
| `venv/` | When working on Python projects, having a virtual environment is helpful to make sure that you keep the right version of each package where you are using it (see [setting up a virtual environment](#virtual-environments) |
-->

## How-to

### How to set up your computer

1. If you don't have one already, create a GitHub account](https://github.com/join) and make sure that you have Python installed (for example, through Anaconda).
1. Open a terminal on your computer.
2. Git clone this repository.
3. Go to the cloned repository and create new folders for `data`, `data/created`, `data/original`, etc.
4. Go to [this Sharepoint directory](https://uob-my.sharepoint.com/:f:/r/personal/fd17626_bristol_ac_uk/Documents/Text-Mining%20Project?csf=1&web=1&e=6vj49M) and download the data into the `data/orginal` directory you just created and rename the two csv files to `arabic_corpus.csv` and `english_corpus.csv`.
5. Make these files read only, so you don't accidentally overwrite anything in them.

### How to make changes

1. Find the GitHub issue, or make a new GitHub issue for the task that you're planning on working on, and assign it to yourself to let us know you're working on it. You can also comment on this issue (and tag me @nataliethurlby) to let me know if you need to ask any questions at any point.git
2. Fork the main branch of the repository to create your own copy. 
3. Create a new branch for the new feature that you're working on. 
3. Work on your local branch to make changes, commiting and pushing frequently.
3. When you have made some progress, e.g. got tokenisation working, make a Pull Request, and ask for a review. This will let us know about the change that you've made and we can "pull in" the work that you've done to the main repository. It's good to do this little and often.
4. I will approve the pull request, or ask for some small changes. If small changes, make the changes, then let me know when you're finished. 
5. Success!