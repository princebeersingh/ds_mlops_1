import setuptools
with open("README.md","r",encoding="utf-8") as f:
    long_description=f.read()




__version__="0.0.0"

REPO_NAME="ds_mlops_1"
AUTHER_USER_NAME="princebeersingh"
SRC_REPO="ml_projects"
AUTHER_EMAIL="princebeersingh@gmail.com"


setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHER_USER_NAME,
    description="First mlops project",
    long_description=long_description,
    long_description_content="text/markdown",
    url=f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}",
    project_urls={
        "Bug Tracker":f"https://github.com/{AUTHER_USER_NAME}/{REPO_NAME}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)