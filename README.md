# dio_azure
Conceitos, anotações e insights adquiridos sobre Azure

Repositório criado para entrega de projetos relacionados aos cursos e bootcamps ministrados pela DIO.

## AI-900

Captura de tela de objetos e recuros criados em AZ-900/images

### Azure Bot

Neste repositório, contém em AI-900/images as capturas de telas sobre a criação de um serviço Azure Bot Azure Cloud soguindo o passo a passo gerado pelo Chat Bot.

Foi criada a aplicação em python no Google Colab com a configuração da chamada por Direct Line e teste do serviço BOT. Neste respositório pode ser encontrado o documento do próprio Google Colab "AI-900/Dio_Azure_Bot.ipynb", e em AI-900/images as capturas de telas referente às execuções de testes e métricas geradas no Azure.

### Language Studio e Speech Studio

Neste repositório, contém em AI-900/images as capturas de telas sobre a criação de um serviço Language Service na Azure Cloud 

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
foi criado no Google Colab o programa 'AI-900/Dio_Language_Service.ipynb' também disponível neste repositório.

As imagens com o resultado da execução destes testes estão em AI-900/images.

Obs.: Foi escolhido o "Google Colab" pela facilidade de tratamento e acesso das Secrets Keys.

### Bot Simples - Google Gemini

Neste repositório consta ainda o código  'AI-900/app.py' com chatbot simples chamando o modelo LLM do Google Gemini. Dependência de biblioteca informada em "AI-900/requirements.txt".



## AZ-900

Captura de tela de objetos e recuros criados em AZ-900/images


### Criando Grupo de Recursos

Explorando os sites a seguir para melhor entendimento e criação de recursos Azure:
https://azure.microsoft.com/pt-br/explore/
https://learn.microsoft.com/pt-br/training/modules/describe-core-architectural-components-of-azure/



### Criando VNet e Gateway

https://learn.microsoft.com/pt-br/azure/networking/foundations/network-foundations-overview
https://learn.microsoft.com/pt-br/azure/application-gateway/configuration-infrastructure
https://learn.microsoft.com/pt-br/training/paths/design-implement-microsoft-azure-networking-solutions-az-700/


Entendimento:
A diferença fundamental é que a Rede Virtual é a base da sua rede na nuvem, enquanto o Gateway de Rede Virtual é o componente que permite a conexão dessa rede virtual com redes externas. 

| Característica | Rede Virtual (Virtual Network - VNet) | Gateway de Rede Virtual (Virtual Network Gateway) |
| :--- | :--- | :--- |
| **Função** | É uma rede isolada na nuvem. Ela define o espaço de endereçamento IP e a segmentação de sub-redes para os recursos (como máquinas virtuais) que você cria. | É o ponto de entrada e saída para a VNet, permitindo a comunicação com redes externas. Ele traduz dados e protocolos de rede entre a VNet e outras redes. |
| **Escopo** | Abrange um ambiente de rede inteiro na nuvem. Todos os recursos dentro da mesma VNet podem se comunicar entre si por padrão. | É um componente específico, geralmente localizado em uma sub-rede dedicada dentro da VNet. Você pode ter, no máximo, um gateway de VPN por VNet. |
| **Propósito** | Fornecer uma infraestrutura de rede segura e isolada para seus recursos na nuvem. | Permitir a conectividade híbrida, conectando a VNet a outras redes, como redes locais, outras VNets ou a internet pública (usando VPNs). |
| **Tecnologia**| Funciona com o conceito de redes definidas por software (SDN), criando uma abstração da rede física. Não requer hardware físico gerenciado pelo usuário. | Baseia-se em protocolos de conexão (como VPN ou ExpressRoute) e requer um dispositivo de software gerenciado pelo provedor de nuvem para funcionar. |
| **Exemplo de uso** | Criar um ambiente de rede isolado para hospedar servidores web e bancos de dados. | Conectar a rede local da sua empresa à VNet na nuvem para que os servidores on-premise possam se comunicar com os servidores na nuvem. |

Em resumo, a Rede Virtual é o contêiner onde seus recursos vivem, enquanto o Gateway de Rede Virtual é a "porta" ou "ponte" que permite que esse contêiner se comunique com o mundo exterior.