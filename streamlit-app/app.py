from gettext import translation
import streamlit as st
import os

def main(audio_file):
  import os
  import librosa
  import torch
  from transformers import Wav2Vec2ForCTC, Wav2Vec2Tokenizer
  from transformers import AutoTokenizer, AutoModelForSeq2SeqLM
  from keybert import KeyBERT

  def convert_extension(audio_file):
    filename, file_extension = os.path.splitext(audio_file)
    if (str(file_extension)) != ".flac":
      print('another extension')
      audio_file = str(filename) + ".flac"
      print(audio_file)
      return audio_file

  def translate(tokenizer, model, transcript):
    batch = tokenizer([transcript], return_tensors='pt')
    generated_ids = model.generate(**batch)
    translated_text = tokenizer.batch_decode(generated_ids, skip_special_tokens=True)[0]
    return translated_text

  def transcript(tokenizer, model, audio_file):

    print('---File Converter---')
    convert_extension(audio_file)
    
    transcript = ""

    # Stream over 20 seconds chunks
    stream = librosa.stream(
        audio_file, block_length=20, frame_length=16000, hop_length=16000
    )

    for speech in stream:
        if len(speech.shape) > 1:
            speech = speech[:, 0] + speech[:, 1]

        input_values = tokenizer(speech, return_tensors="pt").input_values
        logits = model(input_values).logits

        predicted_ids = torch.argmax(logits, dim=-1)
        transcription = tokenizer.decode(predicted_ids[0])
        transcript += transcription.lower() + " "
        
    return transcript

  tokenizer_transcribe = Wav2Vec2Tokenizer.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
  model_transcribe = Wav2Vec2ForCTC.from_pretrained("facebook/wav2vec2-large-960h-lv60-self")
  tokenizer_translate = AutoTokenizer.from_pretrained("Helsinki-NLP/opus-mt-en-ur")
  model_translate = AutoModelForSeq2SeqLM.from_pretrained("Helsinki-NLP/opus-mt-en-ur")


  transcription = transcript(tokenizer_transcribe, model_transcribe, audio_file)
  print('---Transcription---')
  print(transcription)

  translation = translate(tokenizer_translate, model_translate, transcription)
  print('---Translation---')
  print(translation)

  kw_model = KeyBERT()
  keywords = kw_model.extract_keywords(transcription, highlight=True)
  print(keywords)
  return [transcription, translation , keywords]


st.title('The Speako')
st.write (""" Speech to text transcription app """)


audio = st.file_uploader("Choose a file", type=['wav','flac'])
if audio is not None:
    print(audio)
    st.audio(audio, format='audio/wav', start_time=0)
    with open(os.path.join("data",audio.name),"wb") as f: 
      f.write(audio.getbuffer())
    if st.button('Transcription'):
        transcription = main(os.path.join("data",audio.name))
        st.subheader('Transcrption')
        st.write(transcription[0])
        st.subheader('Translation')
        st.write(transcription[1])
        st.subheader('Keywords')
        st.write(transcription[2])
    