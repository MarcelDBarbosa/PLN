# PLN
Alguns códigos para demonstrar o Processamento de Linguagem Natural usando Python.

1) O arquivo txttowav.py transforma uma string num arquivo de áudio e depois o reproduz. Há uma verificação do sistema operacional para chamar adequadamente o reprodutor de som, tanto para Windows, como para Linux e para MacOS.

2) Já o arquivo ailexa.py é uma assistente de voz com algumas tarefas definidas e foi desenvolvida para o sistema MacOS. O assistente funciona na língua portuguesa. Quando o programa é executado ele fica em espera aguardando dois comandos LEXA para começar a assistência ou SAIR para terminar. Após dizer LEXA o sistema é capaz:
- de abrir o navegador na página inicial do Youtube, dizendo qualquer frase que contenha YOUTUBE;
- abrir a página do UOL, dizendo qualquer frase que contenha UOL;
- abrir o programa VLC no diretório que contenha músicas e executá-las, dizendo qualquer frase que contenha a palavra MÚSICA;
- fazer uma busca simples na Wikipedia, dizendo PROCURE ALGO NA WIKIPÉDIA;
- voltar para a condição de espera, dizendo DORMIR ou AGUARDAR

## OBSERVAÇÃO
- Os arquivos foram testados num MacBook Air com processador M2 e 8Gb de RAM, com MacOS 15.6;
- Necessário instalar a biblioteca portaudio usando o comando brew install portaudio e as demais bibliotecas usando pip install ... SpeechRecognition, gTTS, pyaudio e wikipedia.

