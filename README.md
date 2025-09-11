# dio_azure
Conceitos, anotações e insights adquiridos sobre Azure

## Azure Bot

Neste repositório, contém em /images as capturas de telas sobre a criação de um serviço Azure Bot Azure Cloud soguindo o passo a passo gerado pelo Chat Bot.

Foi criada a aplicação em python no Google Colab com a configuração para chamada por Direct Line e teste do serviço BOT. Neste respositório pode ser encontrado o documento do próprio Google Colab "Dio_Azure_Bot.ipynb", e em /images as capturas de telas referente às execuções de testes e métricas geradas no Azure.

## Language Studio e Speech Studio

Neste repositório, contém em /images as capturas de telas sobre a criação de um serviço Language Service na Azure Cloud 

Acesso aos links abaixo para experimentar e aprender sobre os serviços Language Studio, Speech Studio em Azure AI Foundry:

https://language.cognitive.azure.com/home
https://speech.microsoft.com/portal
https://ai.azure.com/?tid=986cdeda-9de9-4521-b612-ebe3bcf7b854&doNotRedirectLastResource=true


Neste link abaixo é possível acessar o Playgound de idiomas, onde é possível testar os modelos de IA com suas próprias informações.
https://ai.azure.com/explore/language?tid=986cdeda-9de9-4521-b612-ebe3bcf7b854


A criação evetiva dos serviços na Azure Cloud, possibilita a utilização/execução das APIs de serviço por código SDK, e CURL requests. 

https://diospeech.cognitiveservices.azure.com/


Once you have created a Language resource, next set up the environment, install the Language SDK, and run sample code by following the steps in the quick start guide.

https://learn.microsoft.com/pt-br/azure/ai-services/language-service/sentiment-opinion-mining/quickstart?tabs=windows&pivots=ai-foundry-portal

ou

https://learn.microsoft.com/pt-br/azure/ai-services/language-service/sentiment-opinion-mining/quickstart?tabs=windows&pivots=programming-language-python


Para teste do serviço dioSpeech criado pelo PlayGround de idiomas, e com base no código template 'https://github.com/Azure/azure-sdk-for-python/blob/main/sdk/textanalytics/azure-ai-textanalytics/samples/sample_analyze_sentiment.py'
foi criado no Google Colab o programa 'Dio_Language_Service.ipynb' também disponível neste repositório.

As imagens com o resultado da execução destes testes estão em /images.


Obs.: Foi escolhido o "Google Colab" pela facilidade de tratamento e acesso das Secrets Keys.


## Bot Simples - Google Gemini

Neste repositório consta ainda o código  'app.py' com chatbot simples chamando o modelo LLM do Google Gemini. Dependência de biblioteca informada em "requirements.txt".

