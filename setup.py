import setuptools

with open("README.md", "r", encoding="utf-8") as f:
    full_description = f.read()



__version__ = "0.0.0"


REPO_NAME = "Text_Summarizer_PyTorch"
AUTHOR_USER_NAME = "MrDote"
SRC_REPO = "textSummarizer"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    description="A small python package for NLP app",
    long_description=full_description,
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker": f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src")
)