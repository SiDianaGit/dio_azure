# dio_azure
Conceitos, anotações e insights adquiridos sobre Azure

Repositório criado para entrega de projetos relacionados aos cursos e bootcamps ministrados pela DIO.

## AI-900

Captura de tela de objetos e recuros criados em AI-900/images

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


### Entendendo Grupo de Recursos

Explorando os sites a seguir para melhor entendimento e criação de recursos Azure:
https://azure.microsoft.com/pt-br/explore/
https://learn.microsoft.com/pt-br/training/modules/describe-core-architectural-components-of-azure/




### Entendendo Serviços de Computação e Rede do Azure
https://learn.microsoft.com/pt-br/training/modules/describe-azure-compute-networking-services/1-introduction
https://learn.microsoft.com/pt-br/training/paths/design-implement-microsoft-azure-networking-solutions-az-700/
https://learn.microsoft.com/pt-br/azure/networking/foundations/network-foundations-overview
https://learn.microsoft.com/pt-br/azure/application-gateway/configuration-infrastructure

#### Rede Virtual (VNet)
https://learn.microsoft.com/pt-br/training/modules/describe-azure-compute-networking-services/8-virtual-network
https://learn.microsoft.com/pt-br/training/modules/describe-azure-compute-networking-services/9-exercise-configure-network-access

  As redes virtuais e as sub-redes virtuais do Azure permitem que recursos do Azure, como VMs, aplicativos Web e bancos de dados, comuniquem-se uns com os outros, com usuários na Internet e com computadores cliente locais. 
  A rede virtual do Azure permite criar várias redes virtuais isoladas. 
  Para resolução de nomes, você pode usar o serviço de resolução de nomes integrado ao Azure. Você também pode configurar a rede virtual para usar um servidor *DNS* interno ou externo.
  É possível habilitar conexões de entrada da Internet atribuindo um endereço IP público a um recurso do Azure ou colocar o recurso atrás de um balanceador de carga público.
  Convém habilitar recursos do Azure para que se comuniquem entre si com segurança.
  As redes virtuais do Azure permitem vincular recursos em seu ambiente local e na assinatura do Azure. 
  Por padrão, o Azure faz o *roteamento de tráfego* entre sub-redes em redes virtuais conectadas, em redes locais e na Internet.
  As redes virtuais do Azure permitem *filtrar o tráfego* entre sub-redes usando as seguintes abordagens:
  -   Grupos de segurança de rede são recursos do Azure que podem conter várias regras de segurança de entrada e saída. Você pode definir essas regras para permitir ou bloquear tráfego com base em fatores como endereço IP de origem e de destino, porta e protocolo.
  -   Soluções de virtualização de rede são VMs especializadas que podem ser comparadas a um dispositivo de rede protegida. Uma solução de virtualização de rede realiza uma função de rede específica, como execução de um firewall ou otimização de WAN (rede de longa distância).
  Você pode *vincular redes virtuais* usando o *emparelhamento* dessas redes. O emparelhamento permite que duas redes virtuais se conectem diretamente entre si. O tráfego de rede entre redes emparelhadas é privado e viaja na rede de backbone da Microsoft, nunca entrando na Internet pública.

#### VPN  e Gateway de VPN
https://learn.microsoft.com/pt-br/training/modules/describe-azure-compute-networking-services/10-virtual-private-networks
  Uma VPN (rede virtual privada) usa um túnel criptografado dentro de outra rede. As VPNs costumam ser implantadas para conectar duas ou mais redes privadas confiáveis entre si em uma rede não confiável (normalmente a Internet pública). 
  Um gateway de VPN é um tipo de gateway de rede virtual. As instâncias do Gateway de VPN do Azure são implantadas em uma subrede dedicada da rede virtual e permitem a seguinte conectividade:
  -   Conecte datacenters locais a redes virtuais por meio de uma conexão site a site.
  -   Conecte dispositivos individuais a redes virtuais por meio de uma conexão ponto a site.
  -   Conecte redes virtuais a outras redes virtuais por meio de uma conexão rede a rede.
  Cenários de alta disponibilidade
  -   Ativo/em espera: Por padrão, gateways de VPN são implantados como duas instâncias em uma configuração ativa/em espera, mesmo se você vê apenas um recurso de gateway de VPN no Azure.
  -   Ativo/ativo: Com a introdução da compatibilidade com o protocolo de roteamento BGP, você também pode implantar os gateways de VPN em uma configuração ativo/ativo.
  -   Failover do ExpressRoute: Outra opção de alta disponibilidade é configurar um gateway de VPN como um caminho de failover seguro para conexões ExpressRoute.
  -   Gateways com redundância de zona: Nas regiões que dão suporte a zonas de disponibilidade, os gateways de VPN e os gateways de ExpressRoute podem ser implantados em uma configuração com redundância de zona. 

##### Gateway x VNet:
A diferença fundamental é que a Rede Virtual é a base da sua rede na nuvem, enquanto o Gateway de Rede Virtual é o componente que permite a conexão dessa rede virtual com redes externas. 

| Característica | Rede Virtual (Virtual Network - VNet) | Gateway de Rede Virtual (Virtual Network Gateway) |
| :--- | :--- | :--- |
| **Função** | É uma rede isolada na nuvem. Ela define o espaço de endereçamento IP e a segmentação de sub-redes para os recursos (como máquinas virtuais) que você cria. | É o ponto de entrada e saída para a VNet, permitindo a comunicação com redes externas. Ele traduz dados e protocolos de rede entre a VNet e outras redes. |
| **Escopo** | Abrange um ambiente de rede inteiro na nuvem. Todos os recursos dentro da mesma VNet podem se comunicar entre si por padrão. | É um componente específico, geralmente localizado em uma sub-rede dedicada dentro da VNet. Você pode ter, no máximo, um gateway de VPN por VNet. |
| **Propósito** | Fornecer uma infraestrutura de rede segura e isolada para seus recursos na nuvem. | Permitir a conectividade híbrida, conectando a VNet a outras redes, como redes locais, outras VNets ou a internet pública (usando VPNs). |
| **Tecnologia**| Funciona com o conceito de redes definidas por software (SDN), criando uma abstração da rede física. Não requer hardware físico gerenciado pelo usuário. | Baseia-se em protocolos de conexão (como VPN ou ExpressRoute) e requer um dispositivo de software gerenciado pelo provedor de nuvem para funcionar. |
| **Exemplo de uso** | Criar um ambiente de rede isolado para hospedar servidores web e bancos de dados. | Conectar a rede local da sua empresa à VNet na nuvem para que os servidores on-premise possam se comunicar com os servidores na nuvem. |

Em resumo, a Rede Virtual é o contêiner onde seus recursos vivem, enquanto o Gateway de Rede Virtual é a "porta" ou "ponte" que permite que esse contêiner se comunique com o mundo exterior.


#### ExpressRoute
https://learn.microsoft.com/pt-br/training/modules/describe-azure-compute-networking-services/11-expressroute
  O Azure ExpressRoute permite que você estenda suas redes locais para a nuvem da Microsoft em uma conexão privada com a ajuda de um provedor de conectividade.

#### DNS
https://learn.microsoft.com/pt-br/training/modules/describe-azure-compute-networking-services/12-domain-name-system
  O DNS do Azure é um serviço de hospedagem para domínios DNS que fornece a resolução de nomes usando a infraestrutura do Microsoft Azure. Ao hospedar seus domínios no Azure, você pode gerenciar seus registros DNS usando as mesmas credenciais, APIs, ferramentas e cobrança que seus outros serviços do Azure.

#### Serviço de Máquinas Virtuais (VM)
https://learn.microsoft.com/pt-br/training/modules/describe-azure-compute-networking-services/2-virtual-machines
  Com as VMs (Máquinas Virtuais) do Azure, você pode criar e usar VMs na nuvem. As VMs fornecem IaaS (infraestrutura como serviço) na forma de um servidor virtualizado e podem ser usadas de várias maneiras.
  
#### Serviço de Área de trabalho virtual
https://learn.microsoft.com/pt-br/training/modules/describe-azure-compute-networking-services/4-virtual-desktop
  Outro tipo de máquina virtual é a Área de Trabalho Virtual do Azure. A Área de Trabalho Virtual do Azure é um serviço de virtualização de aplicativos e área de trabalho que é executado na nuvem. Ele permite que você use uma versão hospedada na nuvem do Windows de qualquer local.
  
#### Serviço de Contêineres
https://learn.microsoft.com/pt-br/training/modules/describe-azure-compute-networking-services/5-containers
  Contêineres são um ambiente de virtualização. Assim como a execução de várias máquinas virtuais em um só host físico, você pode executar vários contêineres em apenas um host físico ou virtual.
  
    -   Instâncias de Contêiner (Ex.: Docker. Permitem que você carregue seus contêineres e, a seguir, o serviço executa os contêineres para você. Oferta de PaaS (plataforma como serviço))
    -   Aplicativos de Contêiner (capacidade de incorporar balanceamento de carga e colocação em escala. Oferta de PaaS (plataforma como serviço))
    -   Serviço de Kubernetes ("AKS". É um serviço de orquestração de contêiner)
    
 Contêineres geralmente são usados para criar soluções que utilizam uma arquitetura de microsserviço. Essa arquitetura é onde você divide as soluções em partes menores e independentes. Por exemplo, você pode dividir um site em um contêiner que hospeda o front-end, outro que hospeda o back-end e um terceiro para o armazenamento. 
 
#### Serviço de Funções
https://learn.microsoft.com/pt-br/training/modules/describe-azure-compute-networking-services/6-functions
  O Azure Functions é uma opção de computação sem servidor controlada por eventos que não requer a manutenção de máquinas virtuais ou contêineres.
  
#### Serviço de Aplicativo
https://learn.microsoft.com/pt-br/training/modules/describe-azure-compute-networking-services/7-describe-application-hosting-options
  Tipos de serviços de aplicativos
  -   Aplicativos Web
  -   Aplicativos de API
  -   WebJobs
  -   Aplicativos móveis





### Entendendo Serviços de Armazenamento do Azure
https://learn.microsoft.com/pt-br/training/modules/describe-azure-storage-services/

#### Conta de Armazenamento do Azure

Uma conta de armazenamento do Azure é a base para todos os serviços de armazenamento na nuvem da Microsoft. É um contêiner que agrupa os diferentes tipos de dados que você quer guardar no Azure, como arquivos, objetos e mensagens. Pense nela como um "cofre" virtual que oferece um espaço de nome único e globalmente acessível para armazenar seus dados.

Aqui está um resumo sobre os principais pontos referentes às contas de armazenamento do Azure:

#### Tipos de Dados Suportados

Uma conta de armazenamento pode guardar quatro tipos principais de dados, cada um com um serviço correspondente:

-   **Blob Storage:** Ideal para armazenar grandes volumes de dados não estruturados, como imagens, vídeos, documentos, logs e arquivos de backup. É o serviço mais comum e versátil.
-   **Azure Files:** Permite criar compartilhamentos de arquivos totalmente gerenciados na nuvem. Eles podem ser acessados usando o protocolo SMB (Server Message Block), o que os torna perfeitos para migrar aplicativos que dependem de compartilhamentos de arquivos tradicionais.
-   **Azure Queues:** Um serviço de mensagens que armazena grandes quantidades de mensagens para serem processadas por componentes de aplicativos. É usado para criar uma fila de mensagens e desacoplar partes de um aplicativo distribuído.
-   **Azure Tables:** Um armazenamento NoSQL para grandes quantidades de dados estruturados e semi-estruturados. É um banco de dados de pares chave-valor que oferece um armazenamento flexível e de baixo custo.

#### Tipos de Contas de Armazenamento

Ao criar uma conta de armazenamento, você escolhe o tipo que melhor se adequa às suas necessidades de desempenho e custo. O tipo mais recomendado para a maioria dos cenários é o **General-purpose v2**.

-   **General-purpose v2 (GPv2):** O tipo mais comum e flexível. Ele suporta todos os serviços de armazenamento (Blobs, Files, Queues, Tables) e oferece diferentes camadas de acesso (Hot, Cool e Archive).
-   **Blob Storage Accounts:** Contas legadas, focadas apenas em blobs. É mais comum usar o GPv2.
-   **File Storage Accounts:** Focadas apenas em Azure Files. Oferecem desempenho premium e são ideais para cargas de trabalho que exigem alta performance de E/S.

#### Camadas de Acesso (para Blobs)

As contas de armazenamento oferecem diferentes camadas de acesso para otimizar os custos com base na frequência de uso dos dados:

-   **Hot (Quente):** Para dados acessados frequentemente. Tem o custo mais alto de armazenamento, mas o mais baixo de acesso.
-   **Cool (Fria):** Para dados acessados com pouca frequência (pelo menos uma vez a cada 30 dias). Tem um custo de armazenamento mais baixo que a camada Hot, mas um custo de acesso mais alto.
-   **Archive (Arquivo):** Para dados que raramente são acessados e podem tolerar longos tempos de recuperação (horas). Tem o custo de armazenamento mais baixo de todos, mas o custo de acesso é o mais alto. É ideal para backups e arquivamento de longo prazo.

#### Opções de Redundância

A Azure Storage oferece várias opções de redundância para garantir a durabilidade e a alta disponibilidade dos seus dados. A escolha da redundância depende do nível de proteção que você precisa:

-   **LRS (Locally-redundant storage):** Cria três cópias dos seus dados na mesma região. Oferece boa proteção contra falhas de hardware local.
-   **ZRS (Zone-redundant storage):** Cria três cópias dos seus dados em diferentes zonas de disponibilidade (data centers físicos) na mesma região. Protege contra falhas em data centers completos.
-   **GRS (Geo-redundant storage):** Cria três cópias na região primária (LRS) e mais três cópias em uma região secundária pareada. Protege contra desastres regionais.
-   **GZRS (Geo-zone-redundant storage):** Combina ZRS e GRS. Cria três cópias em zonas de disponibilidade na região primária e mais três cópias em uma região secundária. É a opção mais cara, mas oferece a maior durabilidade.

---

Em resumo, as contas de armazenamento do Azure são uma solução escalável, segura e altamente disponível para todas as necessidades de dados, desde arquivos simples até bancos de dados NoSQL e grandes volumes de dados não estruturados.




### Entendendo identidade, acesso e a segurança do Azure 
https://learn.microsoft.com/pt-br/training/modules/describe-azure-identity-access-security/1-introduction

#### Microsoft Entra ID: Identidade e Acesso no Azure

O **Microsoft Entra ID** é o serviço de identidade e acesso central do Azure, que unifica o acesso a recursos na nuvem, aplicativos e serviços externos. Anteriormente conhecido como Azure Active Directory (Azure AD), a mudança de nome reflete seu papel expandido como um pilar da estratégia de segurança da Microsoft.

##### Microsoft Entra ID e a Estratégia de Confiança Zero

O Microsoft Entra ID é o alicerce do modelo de segurança **Confiança Zero (Zero Trust)**, que se baseia na filosofia de "nunca confiar, sempre verificar". Ele garante que todas as solicitações de acesso sejam autenticadas e autorizadas, independentemente de onde se originam.

##### Camadas de Segurança e Defesa em Profundidade

A segurança no Azure é implementada em camadas, um modelo conhecido como **Defesa em Profundidade**. A identidade é a primeira e mais crucial dessas camadas:

- **Identidade e Acesso (Microsoft Entra ID):** Atua como a primeira barreira, verificando a identidade do usuário e o estado do dispositivo antes de conceder acesso.
- **Proteção de Endpoints (Microsoft Defender for Endpoint):** Protege dispositivos de ataques.
- **Segurança de Rede:** Controla o tráfego entre os recursos.
- **Segurança de Dados:** Classifica e protege informações sensíveis.

##### Principais Componentes de Acesso e Autenticação

O Microsoft Entra ID oferece um conjunto robusto de ferramentas para gerenciar o acesso de forma segura e flexível.

###### Métodos de Autenticação

O serviço suporta métodos de autenticação modernos para fortalecer a segurança:

- **Autenticação Multifator (MFA):** Adiciona uma camada extra de segurança, exigindo um segundo método de verificação, como um código no aplicativo Microsoft Authenticator.
- **Acesso sem Senha:** Permite que usuários se autentiquem usando métodos mais seguros e convenientes, como chaves de segurança FIDO2.

###### Acesso Condicional

É a ferramenta mais poderosa para implementar políticas de Confiança Zero. O Acesso Condicional permite criar regras granulares que controlam o acesso com base em fatores como:

- Identidade do usuário ou grupo.
- Localização da solicitação.
- Dispositivo que está sendo usado (por exemplo, exigindo um dispositivo gerenciado).
- Aplicativo ou serviço que o usuário está tentando acessar.

###### Identidades Externas

O Microsoft Entra ID simplifica a colaboração com parceiros e clientes, permitindo que eles acessem seus recursos de forma segura. O **Azure B2B (Business-to-Business)** e o **Azure B2C (Business-to-Consumer)** permitem gerenciar identidades de parceiros e consumidores, respectivamente, sem a necessidade de criar contas de usuário em seu próprio diretório.

###### Controle de Acesso Baseado em Função (RBAC)

Enquanto o Microsoft Entra ID gerencia a identidade (quem você é), o **RBAC (Role-Based Access Control)** controla o acesso (o que você pode fazer). Ele atribui permissões específicas, como "Leitor" ou "Colaborador", a usuários, grupos ou identidades em um determinado escopo, garantindo que as pessoas tenham apenas o acesso necessário para realizar suas tarefas.

##### Sinergia com o Microsoft Defender

O Microsoft Entra ID integra-se perfeitamente com a família de produtos Microsoft Defender para fornecer proteção completa:

- **Microsoft Defender for Identity:** Monitora o ambiente híbrido para detectar ataques baseados em identidade, como escalonamento de privilégios.
- **Microsoft Defender for Cloud:** Oferece visibilidade sobre a postura de segurança e as vulnerabilidades em suas cargas de trabalho na nuvem.

Em suma, a segurança de identidade e acesso no Azure, centrada no Microsoft Entra ID, é a base para a proteção de seus ambientes. Ao combinar métodos de autenticação robustos, acesso condicional, RBAC e a inteligência do Microsoft Defender, a plataforma permite que as organizações implementem uma estratégia de Confiança Zero e Defesa em Profundidade eficaz.


### Entendendo a Calculadora de Custos do Azure, Gestão e Otimização de Custos
https://azure.microsoft.com/pt-br/pricing/calculator/

A **Calculadora de Preços do Azure** é uma ferramenta essencial para planejar e estimar os gastos com a nuvem, permitindo que você configure e visualize os custos de diferentes serviços e produtos do Azure antes de implementá-los. Ela funciona como um simulador, onde você seleciona os recursos (como máquinas virtuais, armazenamento, bancos de dados, etc.) e a ferramenta calcula uma estimativa mensal ou anual com base nas suas escolhas.

#### Calculadora TCO (Custo Total de Propriedade)

Além da Calculadora de Preços, a **Calculadora de Custo Total de Propriedade (TCO)** do Azure é fundamental para comparar os custos de manter sua infraestrutura no local (on-premises) com a migração para o Azure. Essa ferramenta ajuda a entender os benefícios econômicos de mover para a nuvem. Ela leva em consideração não apenas os custos de hardware e software, mas também despesas como energia, refrigeração, manutenção e mão de obra. O resultado é um relatório detalhado que mostra a economia potencial ao migrar para a nuvem.

#### Estratégias de Gestão e Otimização de Custos no Azure

Para gerenciar e otimizar seus gastos na nuvem de forma eficaz, o Azure oferece diversas estratégias e ferramentas:

##### Monitoramento e Análise de Custos
Utilize o **Gerenciamento de Custos + Faturamento do Azure**. Essa ferramenta fornece dashboards e relatórios detalhados sobre como os custos estão sendo distribuídos. Você pode criar orçamentos, definir alertas e analisar o histórico de gastos para identificar onde os recursos estão sendo mais consumidos.

##### Otimização de Recursos
* **Dimensionamento Correto (Right-sizing):** Garanta que os recursos (como VMs) tenham o tamanho ideal para a carga de trabalho. Muitas vezes, recursos superdimensionados são criados, gerando custos desnecessários.
* **Exclusão de Recursos Inativos:** Identifique e delete recursos que não estão mais em uso. Servidores de desenvolvimento ou testes que ficam ligados fora do horário de trabalho são um exemplo comum.
* **Agendamento de Ativação/Desativação:** Para ambientes de desenvolvimento e teste, agende o desligamento automático dos recursos fora do horário comercial para economizar.

##### Modelos de Preços Flexíveis
* **Instâncias Reservadas (Reserved Instances - RIs):** Comprometa-se a utilizar um recurso (como uma VM) por um período de um ou três anos. Isso pode gerar uma economia de até 72% em comparação com o pagamento por uso (pay-as-you-go).
* **Plano de Economia do Azure (Azure Savings Plan):** Comprometa-se com um gasto por hora em serviços de computação (como VMs, App Service, Functions) por um ou três anos para obter descontos significativos.
* **Azure Hybrid Benefit:** Use suas licenças locais do Windows Server e SQL Server com Software Assurance para obter grandes descontos em VMs no Azure.

##### Recomendações e Automação
* **Azure Advisor:** Use essa ferramenta para obter recomendações personalizadas para otimizar seus custos. Ela analisa seu uso de recursos e sugere formas de economizar, como a compra de instâncias reservadas ou a exclusão de recursos subutilizados.
* **Automação:** Implemente automações para desligar recursos em horários de pico ou escalar a infraestrutura para cima ou para baixo com base na demanda, garantindo que você pague apenas pelo que realmente precisa.
