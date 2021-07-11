# conversational_bot

The aim of this project was to make a Talking bot, one which can pay attention to the user's voice and generate meaningful and contextual responses according to their intent, much like human conversations.

Speech recognition:
A Deep Speech 2 like architecture had been made for this purpose. Eventually we used google-speech-to-text (gstt) API for the conversion of speech to text transcripts with a WER(Word Error Rate) of 4.7%.

Response Generation
The second step in our pipeline is generating conversational responses after we have recognised input speech content. We tried two distinct response generation models trained on a subset of OpenSubtitles Dataset.
Seq2Seq with Message Attention
Topic Aware Seq2Seq with Message Attention


Video:
Here's a video demonstrating the functioning of the bot as well as the use of a GUI in tkinter.

Documentation:
Here's a documentation of the project.


References
Deep Speech 2: End-to-End Speech Recognition in English and Mandarin

Link : [https://arxiv.org/abs/1512.02595]
Author(s)/Organization : Baidu Research – Silicon Valley AI Lab
Tags : Speech Recognition
Published : 8 Dec, 2015
Topic Aware Neural Response Generation

Link : [https://arxiv.org/abs/1606.08340]
Authors : Chen Xing, Wei Wu, Yu Wu, Jie Liu, Yalou Huang, Ming Zhou, Wei-Ying Ma
Tags : Neural response generation; Sequence to sequence model; Topic aware conversation model; Joint attention; Biased response generation
Published : 21 Jun 2016 (v1), 19 Sep 2016 (v2)
Topic Modelling and Event Identification from Twitter Textual Data

Link : [https://arxiv.org/abs/1608.02519]
Authors : Marina Sokolova, Kanyi Huang, Stan Matwin, Joshua Ramisch, Vera Sazonova, Renee Black, Chris Orwa, Sidney Ochieng, Nanjira Sambuli
Tags : Latent Dirichlet Allocation; Topic Models; Statistical machine translation
Published : 8 Aug 2016
OpenSubtitles (Dataset)

Link : [http://opus.nlpl.eu/OpenSubtitles-v2018.php]
