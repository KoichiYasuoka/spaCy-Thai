import setuptools,subprocess,platform

with open("README.md","r",encoding="utf-8") as r:
  long_description=r.read()
URL="https://github.com/KoichiYasuoka/spaCy-Thai"

setuptools.setup(
  name="spacy_thai",
  version="0.7.1",
  description="Dependency-parser for Thai language",
  long_description=long_description,
  long_description_content_type="text/markdown",
  url=URL,
  author="Koichi Yasuoka",
  author_email="yasuoka@kanji.zinbun.kyoto-u.ac.jp",
  license="MIT",
  keywords="spaCy udpipe nlp",
  packages=setuptools.find_packages(),
  install_requires=["spacy>=2.2.2","ufal.udpipe>=1.2.0","deplacy>=2.0.2","pythainlp>=2.3.2"],
  python_requires=">=3.6",
  package_data={"spacy_thai":["./*.udpipe"]},
  classifiers=[
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python :: 3",
    "Operating System :: POSIX :: Linux",
    "Topic :: Text Processing :: Linguistic",
    "Natural Language :: Thai",
  ],
  project_urls={
    "Source":URL,
    "Tracker":URL+"/issues",
  }
)
