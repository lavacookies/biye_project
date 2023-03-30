import time
import torch
import scipy.io.wavfile
from espnet2.bin.tts_inference import Text2Speech
from espnet2.utils.types import str_or_none

lang = 'English'
tag = 'kan-bayashi/ljspeech_vits' 
vocoder_tag = "none" 

from espnet2.bin.tts_inference import Text2Speech
from espnet2.utils.types import str_or_none

text2speech = Text2Speech.from_pretrained(
    model_tag=str_or_none(tag),
    vocoder_tag=str_or_none(vocoder_tag),
    device="cuda",
    # Only for Tacotron 2 & Transformer
    threshold=0.5,
    # Only for Tacotron 2
    minlenratio=0.0,
    maxlenratio=10.0,
    use_att_constraint=False,
    backward_window=1,
    forward_window=3,
    # Only for FastSpeech & FastSpeech2 & VITS
    speed_control_alpha=1.0,
    # Only for VITS
    noise_scale=0.333,
    noise_scale_dur=0.333,
)

import time
import torch

# decide the input sentence by yourself
print(f"Input your favorite sentence in {lang}.")
x = input()

# synthesis
with torch.no_grad():
    start = time.time()
    wav = text2speech(x)["wav"]
rtf = (time.time() - start) / (len(wav) / text2speech.fs)
print(f"RTF = {rtf:5f}")

# let us listen to generated samples
from IPython.display import display, Audio
import soundfile as sf 

sf.write('output.wav', Audio(wav.view(-1).cpu().numpy(), rate=text2speech.fs), 16000) 
# display(Audio(wav.view(-1).cpu().numpy(), rate=text2speech.fs))