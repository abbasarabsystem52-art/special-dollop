from fastapi import FastAPI, Query
import datetime
import os

app = FastAPI()

# اگر فایل وجود نداشت بسازیم
if not os.path.exists("watering_log.txt"):
    with open("watering_log.txt", "w", encoding="utf-8") as f:
        f.write("plant_id,time\n")

@app.api_route("/water", methods=["GET", "POST"])
async def water(plant_id: int = Query(..., description="شماره گیاه")):
    # ثبت زمان
    now = datetime.datetime.now().isoformat()

    # ذخیره داخل فایل
    with open("watering_log.txt", "a", encoding="utf-8") as f:
        f.write(f"{plant_id},{now}\n")

    # پاسخ
    return {
        "status": "ok",
        "message": "زمان آبیاری ثبت شد",
        "plant_id": plant_id,
        "time": now
    }

@app.get("/")
async def home():
    return {"message": "Plant Watering API is running"}
