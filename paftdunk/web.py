import uvicorn
from pydantic import BaseModel
from fastapi import FastAPI
from paftdunk.recommender import Recommender


def create_app(model_path):
    app = FastAPI()
    rec = Recommender.from_disk(model_path)

    class ItemItemQuery(BaseModel):
        item_id: int
        n: int

    @app.get("/")
    def root():
        return {"message": "hello world"}

    @app.post("/recommend_item_item")
    def recommend_item_item(query: ItemItemQuery):
        tbl = rec.rec_item_item(item=query.item_id, n=query.n)
        return {
            "input": query,
            "recommendations": tbl[["item_to", "rating"]].to_dict(orient="records"),
        }

    return app


if __name__ == "__main__":
    uvicorn.run(
        create_app("trained-model"), host="127.0.0.1", port=5000, log_level="info"
    )
