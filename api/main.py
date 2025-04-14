import joblib
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

from chatbot import process_customer_query

app = FastAPI()

class RecommendationRequest(BaseModel):
    user_id: str

class ChatRequest(BaseModel):
    query: str

@app.post("/recommend")
def recommend_services(request: RecommendationRequest):
    user_id = int(request.user_id)

    try:
        model_package = joblib.load("recommendation_model.pkl")
        predicted_matrix = model_package['predicted_matrix']
        user_item_matrix = model_package['user_item_matrix']
    except Exception as e:
        raise RuntimeError(f"Failed to load model package: {e}")

    try:
        if user_id not in predicted_matrix.index:
            raise HTTPException(status_code=404, detail=f"User ID not found in prediction matrix: {e}")

        user_scores = predicted_matrix.loc[user_id]

        seen_items = user_item_matrix.loc[user_id]
        unseen_items = user_scores[seen_items == 0]

        top_items = unseen_items.sort_values(ascending=False).head(5)
        return {"recommended_services": top_items.index.tolist()}
    
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Prediction failed: {e}")

@app.post("/chatbot")
def chatbot_response(request: ChatRequest):
    query = request.query

    try:
        ai_response = process_customer_query(query)
        return {"response": ai_response["response"]}
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"Error generating response: {e}")