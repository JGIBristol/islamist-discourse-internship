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
| `data/original` | All original data should be stored in this directory (and the files should be [made read-only](#protect-original-data).
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
4. Go to [this Sharepoint directory]() and download the data into the `data/orginal` directory you just created. 
5. After downloading, make these files read only, so you don't accidentally overwrite anything in them.
