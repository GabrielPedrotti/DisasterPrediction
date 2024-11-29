<h1> CENTRO UNIVERSITÁRIO CATÓLICA DE SANTA CATARINA </h1>

Alex Henrique da Silva

Gabriel Pedrotti da Silva

Marco Antonio Feliponi

<h1>ANÁLISE PREDITIVA DE DESASTRES NATURAIS</h1> 

<b>Modelo de predição de dados para detecção de possíveis desastres naturais</b>

Jaraguá do Sul, Santa Catarina

2024

# Introdução

Os desastres naturais representam um dos maiores desafios enfrentados pelas sociedades modernas, com consequências devastadoras para vidas humanas, economias e ecossistemas. Fenômenos como terremotos, inundações, furacões e incêndios florestais, entre outros, têm se tornado mais frequentes e intensos devido às mudanças climáticas e à crescente urbanização. O impacto desses eventos é amplificado pela imprevisibilidade e pela falta de preparação adequada, resultando em enormes prejuízos materiais e na perda de inúmeras vidas.

A previsão precisa e antecipada desses desastres se tornou uma prioridade para cientistas e autoridades, na esperança de reduzir os danos causados por esses eventos. O avanço das tecnologias de análise de dados e inteligência artificial (IA) oferece novas possibilidades para compreender e prever esses fenômenos com maior precisão. Modelos preditivos baseados em algoritmos de aprendizado de máquina e redes neurais têm demonstrado potencial para detectar padrões complexos em grandes volumes de dados climáticos, sísmicos e geoespaciais, possibilitando a antecipação de eventos com maior acurácia do que métodos tradicionais.

Este artigo tem como objetivo explorar técnicas de previsão de desastres naturais, utilizando algoritmos avançados de aprendizado de máquina para prever a ocorrência e a intensidade desses eventos. Além de uma revisão das abordagens atuais, este estudo apresenta um modelo de predição aplicado a um conjunto de dados históricos, buscando identificar as técnicas mais eficazes e avaliar o desempenho em relação a critérios específicos de acurácia e confiabilidade. Assim, espera-se que este trabalho contribua para o desenvolvimento de métodos mais robustos e eficientes, capazes de apoiar tomadas de decisão e estratégias de mitigação em cenários de risco.

# Revisão da Literatura

A previsão de desastres naturais tem sido um campo de estudo em constante evolução, especialmente à medida que se ampliam as possibilidades de análise de dados climáticos, geológicos e meteorológicos. Os métodos tradicionais de previsão, que envolvem análises estatísticas e modelos baseados em séries temporais, permitiram avanços consideráveis, porém limitados em relação à complexidade e à variabilidade dos fenômenos naturais. Com o crescimento das capacidades computacionais e o desenvolvimento de algoritmos avançados, como aprendizado de máquina (ML) e redes neurais, novas abordagens surgiram para enfrentar as limitações dos modelos tradicionais, permitindo prever eventos extremos com maior precisão e antecedência.

## 2.1 Métodos Baseados em Séries Temporais e Estatística

Métodos de séries temporais, como ARIMA (AutoRegressive Integrated Moving Average), vêm sendo amplamente utilizados na previsão de desastres naturais, especialmente para eventos como inundações e temperaturas extremas. ARIMA e modelos derivados são eficazes para capturar padrões históricos e prever tendências futuras, mas apresentam limitações quanto à sua capacidade de modelar dados não-lineares e de alta complexidade, características comuns em fenômenos climáticos e sísmicos. Outros métodos estatísticos incluem o uso de regressão linear e análise de correlação para relacionar variáveis como temperatura, umidade e pressão atmosférica com a frequência e a intensidade de determinados eventos.

## 2.2 Aprendizado de Máquina e Redes Neurais

O uso de aprendizado de máquina na previsão de desastres naturais cresceu significativamente nos últimos anos, oferecendo técnicas mais robustas para lidar com dados não-lineares e de alta dimensão. Modelos como Florestas Aleatórias (Random Forest) e Máquinas de Vetores de Suporte (SVM) têm se mostrado eficazes na detecção de padrões complexos e na previsão de fenômenos como deslizamentos de terra e incêndios florestais. Florestas Aleatórias, por exemplo, são conhecidas por sua resistência ao sobreajuste e sua capacidade de interpretar variáveis importantes, tornando-se uma escolha comum para dados multivariados.

As redes neurais profundas, como Redes Neurais Convolucionais (CNNs) e Redes Neurais Recorrentes (RNNs), vêm ganhando destaque, especialmente para análise de séries temporais e dados espaciais. RNNs e suas variantes, como a Long Short-Term Memory (LSTM), são especialmente eficazes para prever desastres que apresentam padrões temporais, como terremotos e ciclones, devido à sua capacidade de aprender e lembrar de sequências de dados. CNNs, por outro lado, são comumente aplicadas na análise de imagens de satélite e mapas geoespaciais, úteis na detecção de áreas de risco e na previsão de desastres visuais, como enchentes e incêndios.

## 2.3 Integração de Big Data e Dados de Sensores

A integração de dados de sensores e dados geoespaciais em modelos de aprendizado de máquina oferece novas perspectivas para previsões de desastres naturais. Sensores ambientais, redes de satélites e sistemas de monitoramento em tempo real fornecem dados cruciais sobre variáveis como temperatura, umidade, movimento tectônico e padrões oceânicos. O uso de Big Data e análise em tempo real permite que algoritmos preditivos respondam rapidamente a mudanças nas condições, fornecendo alertas antecipados e informações acionáveis para a população e autoridades.

## 2.4 Desafios e Limitações dos Métodos Preditivos

Apesar dos avanços, os métodos de previsão de desastres naturais ainda enfrentam desafios significativos. A precisão das previsões é fortemente dependente da qualidade e da resolução dos dados disponíveis, além de fatores como incertezas climáticas e eventos extremos fora dos padrões históricos. A variabilidade dos fenômenos naturais e a imprevisibilidade dos sistemas climáticos representam obstáculos, exigindo aprimoramentos contínuos nos algoritmos e na integração de múltiplas fontes de dados. Modelos de aprendizado profundo, como redes neurais, também demandam grande poder computacional e uma quantidade massiva de dados para evitar problemas de sobre ajuste e melhorar a precisão.

# Metodologia

A metodologia utilizada para a predição de dados relacionados a desastres naturais consistiu em diversas etapas estruturadas, abrangendo desde a coleta de dados até o treinamento e avaliação do modelo preditivo.

## 3.1 Coleta e Pré-Processamento dos Dados

Os dados foram extraídos de um banco de dados MongoDB hospedado na nuvem, utilizando a biblioteca pymongo. Cada registro representava um desastre declarado, contendo informações como o estado, o tipo de declaração, a área designada, e características climáticas (precipitação, dias de aquecimento e resfriamento, entre outros).

Após a extração, os dados foram carregados em um DataFrame do pandas para análise e manipulação. Verificou-se a presença de valores nulos e foram definidas as colunas categóricas e numéricas para tratamentos específicos.

Colunas categóricas: state, declarationType e designatedArea foram codificadas usando OneHotEncoder, permitindo que o modelo lidasse com valores categóricos de forma eficiente.

Colunas numéricas: as variáveis numéricas, como fipsStateCode, year, Precipitation e AverageTemp, foram normalizadas utilizando StandardScaler para garantir que todas tivessem a mesma escala, minimizando o impacto de diferenças de magnitude.

## 3.2 Divisão de Dados e Seleção de Variáveis

A variável alvo escolhida foi incidentType, representando o tipo de desastre (por exemplo, incêndio). Os dados foram divididos em conjuntos de treino e teste na proporção 80-20, utilizando a função train_test_split da biblioteca scikit-learn.

As características (features) foram agrupadas em duas categorias principais:

Categóricas, que foram codificadas com OneHotEncoder.

Numéricas, que foram escaladas com StandardScaler.

Os conjuntos processados de treino e teste foram posteriormente combinados para formar as entradas finais do modelo.

## 3.3 Treinamento do Modelo

Para a tarefa de classificação, foi utilizado o algoritmo Random Forest Classifier, conhecido por sua robustez e capacidade de lidar com dados mistos (categóricos e numéricos). O modelo foi treinado no conjunto de treino e avaliado no conjunto de teste.

## 3.4 Avaliação do Modelo

As métricas de avaliação incluíram:

Acurácia: calculada manualmente e utilizando o método score do modelo.

Importância das variáveis: as features mais relevantes para a predição foram identificadas usando o atributo feature_importances_ do Random Forest.

## 3.5 Armazenamento do Modelo

O modelo treinado, juntamente com o codificador (OneHotEncoder) e o escalador (StandardScaler), foi salvo no disco utilizando a biblioteca joblib, permitindo sua reutilização sem a necessidade de retraining.

## 3.6 Implementação e Integração com API

Após o treinamento do modelo de machine learning, foi desenvolvida uma API para integrar as funcionalidades de predição e manipulação de dados. A API foi implementada usando o framework Flask, permitindo que o modelo fosse disponibilizado para uso em tempo real por sistemas externos.

A API foi estruturada com suporte a rotas dinâmicas e dois serviços principais:

disaster: responsável pelo gerenciamento e recuperação de dados relacionados a desastres.

model: destinado a interações com o modelo preditivo, como execução de inferências e recuperação de informações sobre o modelo.

Para garantir compatibilidade com os tipos de dados específicos utilizados, como objetos do MongoDB (ObjectId) e datas, foi implementada uma classe personalizada chamada MongoJsonEncoder. Essa classe estende o JSONEncoder do Flask, convertendo automaticamente esses tipos para representações compatíveis com JSON.

CORS (Cross-Origin Resource Sharing): configurado com flask_cors.CORS para permitir que diferentes domínios consumam a API sem restrições.

Serviço de Frontend: o backend foi configurado para servir o frontend da aplicação, indicando um fluxo de integração completo entre a interface de usuário e os serviços de backend.

Rotas Dinâmicas: o método serve foi implementado para lidar com todas as rotas desconhecidas, redirecionando-as para o arquivo index.html, possibilitando a navegação em um aplicativo SPA (Single Page Application).

Uma funcionalidade útil incluída foi a exibição de todas as rotas registradas, facilitando o desenvolvimento e a depuração, especialmente em um ambiente com múltiplos serviços.

# Resultados

O presente estudo avaliou a capacidade preditiva de um modelo Random Forest para a previsão de desastres naturais, utilizando um conjunto de dados climatológicos e socioeconômicos. Os resultados obtidos são detalhados a seguir:

## 4.1 Estrutura dos Dados

O conjunto de dados utilizado para o treinamento do modelo contém 19 variáveis explicativas, entre categóricas (state, declarationType, incidentType) e numéricas (Precipitation, Cooling_Days, Heating_Days, AverageTemp). Durante a análise inicial, verificou-se que o dataset estava completo, sem valores ausentes, o que favoreceu o pré-processamento e o treinamento do modelo.

## 4.2 Performance do Modelo

O modelo Random Forest apresentou uma acurácia de 93% no conjunto de testes, indicando boa capacidade preditiva. O score no conjunto de treinamento foi de 99,95%, enquanto o score no conjunto de teste alcançou 93,48%, o que demonstra uma boa generalização. Estes resultados sugerem que o modelo é robusto e eficaz para a tarefa de classificação.

## 4.3 Importância das Variáveis

A análise da importância das variáveis revelou que os fatores climáticos desempenham um papel significativo na previsão de desastres. Entre as variáveis mais relevantes destacam-se:

Cooling_Days (importância: 0.028);
Heating_Days (0.024);
Precipitation (0.008);

Esses resultados refletem a relação intrínseca entre padrões climáticos e a ocorrência de eventos adversos.

## 4.4 Avaliação Qualitativa das Predições

Uma análise qualitativa revelou que o modelo foi capaz de prever corretamente eventos como Hurricane, Flood e Severe Storm, demonstrando confiabilidade em cenários reais.

## 4.5 Armazenamento e Reutilização do Modelo

O modelo treinado foi salvo no formato pkl junto com os pré-processadores (encoder e scaler). Essa abordagem permite sua reutilização futura sem a necessidade de um novo treinamento, promovendo eficiência e escalabilidade para aplicações práticas.

Os resultados indicam que o modelo possui um potencial significativo para prever desastres naturais com base em dados históricos e climáticos, oferecendo suporte à tomada de decisão e à mitigação de impactos.

Para o funcionamento pleno do programa, o usuário necessita preencher as informações nos campos disponíveis, e o processamento desses dados é utilizado para gerar uma análise em tempo real e retornar para a aplicação.

# Discussão e Conclusão

O modelo desenvolvido para previsão de desastres naturais, utilizando o algoritmo Random Forest, apresentou resultados satisfatórios em termos de precisão e generalização. A escolha do algoritmo se mostrou apropriada, dada sua capacidade de lidar com variáveis categóricas e numéricas e sua robustez em relação a problemas de overfitting.

A análise das importâncias das variáveis revelou que fatores como Precipitação, Temperatura Média, e Código FIPS foram determinantes para a previsão dos tipos de incidentes. Esse resultado está alinhado com a literatura, que aponta condições climáticas como fatores críticos na ocorrência de desastres naturais.

Além disso, a utilização de técnicas de pré-processamento, como OneHotEncoding para variáveis categóricas e StandardScaler para variáveis numéricas, garantiu uma representação consistente dos dados, contribuindo para a performance do modelo. Apesar disso, a abordagem pode ser aprimorada em algumas áreas:

Exploração de Modelos Alternativos: Outras técnicas, como Gradient Boosting (e.g., XGBoost ou LightGBM), podem ser exploradas para melhorar a acurácia e identificar possíveis ganhos de performance.

Ampliação da Base de Dados: A inclusão de mais dados históricos e variáveis contextuais, como padrões climáticos em longo prazo e características socioeconômicas das regiões, pode enriquecer a análise.

Validação em Cenários Reais: Embora o modelo tenha apresentado bom desempenho nos dados de teste, sua aplicação em cenários reais exige validação contínua e ajustes dinâmicos para acompanhar mudanças climáticas e comportamentais.

O projeto demonstrou a viabilidade de utilizar aprendizado de máquina para prever desastres naturais, contribuindo para a mitigação de impactos e a tomada de decisões estratégicas.  Indicando seu potencial como ferramenta de apoio à gestão de desastres.

Ainda assim, melhorias contínuas são necessárias para garantir maior precisão e confiabilidade. A integração de previsões em sistemas de alerta precoce pode ser o próximo passo lógico, permitindo que autoridades e comunidades estejam mais bem preparadas para lidar com situações adversas.

Este trabalho reforça a importância de explorar a interseção entre ciência de dados e sustentabilidade, com o objetivo de criar soluções tecnológicas para problemas globais.

# Referências

XIA, Ren. Disaster Prediction. GitHub, 2023. Disponível em: . Acesso em: 11 nov. 2024.

FEDERAL EMERGENCY MANAGEMENT AGENCY – FEMA. Disaster Declarations Summaries – v2. 2024. Disponível em: . Acesso em: 11 nov. 2024.

MongoDB. "MongoDB Manual." Disponível em: . Acesso em: 11 nov. 2024

Breiman, L. "Random Forests." Machine Learning, 2001. Disponível em: https://doi.org/10.1023/A:1010933404324.

