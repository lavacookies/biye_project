# Voice Conversion
## Source
here is a pytorch implementation of the paper: StarGAN-VC: Non-parallel many-to-many voice conversion with star generative adversarial networks https://arxiv.org/abs/1806.02169 .

and source code is from https://github.com/liusongxiang/StarGAN-Voice-Conversion
## Usage
the step only need to do is run:
```
python convert.py
```
you will get converted result in "./converted/200000"

### Custum
the custum data should put in "./src_audio/"
src_spk in p0 folder
trg_spk in p1 folder

then run:
```
python preprocess.py
python convert.py --resume_iters 200000 --src_spk p0 --trg_spk p1
```