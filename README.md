# PLN BASICS - MVP de Satisfação do Cliente

_Projeto para fins acadêmicos estudando o básico dos conceitos de PLN com as bibliotecas streamlit e nltk._

## Dependências 

Para instalar as dependências do projeto, execute:

```bash
pip install -r requirements.txt
```

## Instalação 

1. Clone o repositório:

```bash
git clone https://github.com/marqsleal/pln-basics.git
```

2. Abra o arquivo `sentiment.py` dentro do ambiente python com as dependências instaladas utilizando streamlit:

```bash
streamlit run sentiment.py
```

## Conceito do Projeto
MVP que gere um modelo preditivo do sentimento do usuário baseado em feedback. Projeto possui 3 estágios: Criação do Sistema, Criação da Máquina Preditiva e Utilização.

## Criação do Sistema:

```python
st.write('Analise de Satisfação do Cliente')

usr_input = st.text_input('Como você avalia o nosso atendimento?')
```

## Criação da Máquina Preditiva:

```python
nl.download('vader_lexicon')
from nltk.sentiment.vader import SentimentIntensityAnalyzer

sia = SentimentIntensityAnalyzer()

score = sia.polarity_scores(usr_input)
```

### Refinamento:
```python
if score == 0:
    st.write('')
elif score['neg'] != 0:
    st.write('Analise Negativo')
elif score['pos'] != 0:
    st.write('Analise Positivo')
```

## Utilização:

```bash
streamlit run sentiment.py
```

