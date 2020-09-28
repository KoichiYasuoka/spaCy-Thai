[![Current PyPI packages](https://badge.fury.io/py/spacy-thai.svg)](https://pypi.org/project/spacy-thai/)

# spaCy-Thai

Tokenizer, POS-tagger, and dependency-parser for Thai language, working on [Universal Dependencies](https://github.com/UniversalDependencies/UD_Thai-PUD).

## Basic Usage

```py
>>> import spacy_thai
>>> nlp=spacy_thai.load()
>>> doc=nlp("แผนกนี้กำลังเผชิญกับความท้าทายใหม่")
>>> for t in doc:
...   print("\t".join([str(t.i+1),t.orth_,t.lemma_,t.pos_,t.tag_,"_",str(0 if t.head==t else t.head.i+1),t.dep_,"_","_" if t.whitespace_ else "SpaceAfter=No"]))
...
1	แผนก	แผนก	NOUN	NCMN	_	4	nsubj	_	SpaceAfter=No
2	นี้	นี้	DET	DDAC	_	1	det	_	SpaceAfter=No
3	กำลัง	กำลัง	AUX	XVBM	_	4	aux	_	SpaceAfter=No
4	เผชิญ	เผชิญ	VERB	VSTA	_	0	ROOT	_	SpaceAfter=No
5	กับ	กับ	ADP	RPRE	_	6	case	_	SpaceAfter=No
6	ความ	ความ	PART	FIXN	_	4	obl	_	SpaceAfter=No
7	ท้าทาย	ท้าทาย	VERB	VACT	_	6	acl	_	SpaceAfter=No
8	ใหม่	ใหม่	ADV	ADVN	_	7	advmod	_	SpaceAfter=No
>>> import deplacy
>>> deplacy.render(doc,WordRight=True)
 nsubj ╔════════>╔═ NOUN แผนก
   det ║         ╚> DET  นี้
   aux ║ ╔════════> AUX  กำลัง
  ROOT ╚═╚═╔═══════ VERB เผชิญ
  case     ║ ╔════> ADP  กับ
   obl     ╚>╚═╔═══ PART ความ
   acl         ╚>╔═ VERB ท้าทาย
advmod           ╚> ADV  ใหม่
```

## Installation for Linux

```sh
pip3 install spacy_thai --user
```

## Installation for Cygwin

Make sure to get `python37-devel` `python37-pip` `python37-numpy` `python37-cython` `gcc-g++`, and then:

```sh
pip3.7 install spacy_thai --no-build-isolation
```

## Installation for Google Colaboratory

```py
!pip install spacy_thai
```

Try [notebook](https://colab.research.google.com/github/KoichiYasuoka/spaCy-Thai/blob/master/spacy_thai.ipynb).

