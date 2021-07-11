# conversational_bot

The aim of this project was to make a Talking bot, one which can pay attention to the user's voice and generate meaningful and contextual responses according to their intent, much like human conversations.

Speech recognition:
A Deep Speech 2 like architecture had been made for this purpose. Eventually we used google-speech-to-text (gstt) API for the conversion of speech to text transcripts with a WER(Word Error Rate) of 4.7%.

Response Generation
The second step in our pipeline is generating conversational responses after we have recognised input speech content. We tried two distinct response generation models trained on a subset of OpenSubtitles Dataset.
1) Seq2Seq with Message Attention
2) Topic Aware Seq2Seq with Message Attention


References
1) Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

2) Topic Aware Neural Response Generation

3)Topic Modelling and Event Identification from Twitter Textual Data

4) OpenSubtitles (Dataset)

