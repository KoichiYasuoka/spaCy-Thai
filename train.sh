#! /bin/sh
TMP=/tmp/tud$$.conllu
curl -L https://github.com/nlp-chula/TUD/raw/main/TUD/train.conllu |
python3 -c '
from pythainlp import pos_tag
w=[]
while True:
  try:
    s=input()
  except:
    quit()
  t=s.split("\t")
  if len(t)==10:
    if t[0].isdecimal():
      w.append(t)
  elif s=="":
    for t,(f,p) in zip(w,pos_tag([t[1] for t in w])):
      t[4]=p
      if t[3]=="ADJ":
        t[3]="VERB"
    print("\n".join("\t".join(t) for t in w)+"\n")
    w=[]
  else:
    print(s)
' > $TMP
udpipe --train --tokenizer=epochs=30 --tagger=iterations=20 --parser='embedding_form=10;embedding_lemma=0;embedding_upostag=10;embedding_xpostag=30;embedding_feats=0;embedding_deprel=20;iterations=20' ud-thai.udpipe UD_Thai-Corpora/th_pud-ud-orchid.conllu $TMP
if [ -s ud-thai.udpipe ]
then mv -f spacy_thai/ud-thai.udpipe spacy_thai/ud-thai.udpipe.old
     mv ud-thai.udpipe spacy_thai/ud-thai.udpipe
fi
rm $TMP
exit 0
