#! /usr/bin/python3 -i
# coding=utf-8

import os,numpy
from spacy.lang.th import Thai
from spacy.symbols import POS,TAG,DEP,HEAD,X
from spacy.tokens import Doc
from spacy.language import Language
PACKAGE_DIR=os.path.abspath(os.path.dirname(__file__))
SPACY_V3=hasattr(Language,"component")

class ThaiTagger(object):
  name="thai_tagger"
  def __init__(self,nlp):
    from pythainlp import pos_tag
    from pythainlp.tag.orchid import TO_UD
    self.pos_tag=pos_tag
    self.tag_map={p:{POS:nlp.vocab.strings.add(TO_UD[p])} for p in list(TO_UD)}
    self.vocab=nlp.vocab
  def __call__(self,doc):
    vs=self.vocab.strings
    words=[]
    pos=[]
    tags=[]
    spaces=[]
    for i,(form,xpos) in enumerate(self.pos_tag([t.orth_ for t in doc])):
      if form.strip()=="":
        if len(spaces)>0:
          spaces[-1]=True
      else:
        words.append(form)
        spaces.append(doc[i].whitespace_!="")
        tags.append(vs.add(xpos))
        pos.append(self.tag_map[xpos][POS] if xpos in self.tag_map else X)
    doc=Doc(self.vocab,words=words,spaces=spaces)
    a=numpy.array(list(zip(pos,tags)),dtype="uint64")
    doc.from_array([POS,TAG],a)
    if not SPACY_V3:
      doc.is_tagged=True
    return doc

class ThaiParser(object):
  name="thai_parser"
  def __init__(self,nlp):
    import ufal.udpipe
    self.model=ufal.udpipe.Model.load(os.path.join(PACKAGE_DIR,"ud-thai.udpipe"))
    self.udpipe=ufal.udpipe.Pipeline(self.model,"conllu","none","","").process
    self.vocab=nlp.vocab
  def __call__(self,doc):
    s="".join("\t".join([str(t.i+1),t.orth_,"_",t.pos_,t.tag_,"_","_","_","_","_" if t.whitespace_ else "SpaceAfter=No"])+"\n" for t in doc)+"\n"
    vs=self.vocab.strings
    r=vs.add("ROOT")
    heads=[]
    deps=[]
    for t in self.udpipe(s).split("\n"):
      if t=="" or t.startswith("#"):
        continue
      s=t.split("\t")
      if len(s)!=10:
        continue
      id,form,dummy_lemma,upos,xpos,dummy_feats,head,deprel,dummy_deps,misc=s
      if deprel=="root":
        heads.append(0)
        deps.append(r)
      else:
        heads.append(int(head)-int(id))
        deps.append(vs.add(deprel))
    a=numpy.array(list(zip(deps,heads)),dtype="uint64")
    doc.from_array([DEP,HEAD],a)
    if not SPACY_V3:
      doc.is_parsed=True
    return doc

def load():
  nlp=Thai()
  if SPACY_V3:
    Language.component("thai_tagger",func=ThaiTagger(nlp))
    nlp.add_pipe("thai_tagger")
    Language.component("thai_parser",func=ThaiParser(nlp))
    nlp.add_pipe("thai_parser")
  else:
    nlp.add_pipe(ThaiTagger(nlp))
    nlp.add_pipe(ThaiParser(nlp))
  return nlp

