#! /bin/sh
udpipe --train --tokenizer=epochs=30 --tagger=iterations=20 --parser='embedding_form=10;embedding_lemma=0;embedding_upostag=10;embedding_xpostag=30;embedding_feats=0;embedding_deprel=20;iterations=20' ud-thai.udpipe th_pud-ud-orchid.conllu
mv spacy_thai/ud-thai.udpipe spacy_thai/ud-thai.udpipe.old
mv ud-thai.udpipe spacy_thai/ud-thai.udpipe
exit 0
