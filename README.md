# Setup and Execution Instructions

_Each section has its own dependencies (requirements.txt)_.

## Customer Behavior Analysis

```
python3 -m venv .customer_behavior_analysis_venv

source .customer_behavior_analysis_venv/bin/activate

pip3 install -r requirements.txt
```

- Executing each cell in Jupyter Notebook sequentially.

## Recommendation Model

```
python3 -m venv .recommendation_model_venv

source .recommendation_model_venv/bin/activate

pip3 install -r requirements.txt
```

- Executing each cell in Jupyter Notebook sequentially.

## Chatbot

```
python3 -m venv .chatbot_venv

source .chatbot_venv/bin/activate

pip3 install -r requirements.txt
```

- Create a .env.local file with fields present in .env.example file.
- Executing each cell in Jupyter Notebook sequentially.

## RestAPI

```
docker build -t fastapi-ai .

docker run -p 8000:8000 --env-file .env.local fastapi-ai
```

- Create a .env.local file with fields present in .env.example file.
- Executing each cell in Jupyter Notebook sequentially.