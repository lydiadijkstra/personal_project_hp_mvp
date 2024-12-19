from apscheduler.schedulers.background import BackgroundScheduler
from app.core.database import SessionLocal
from app.models.children import Child
from app.models.tips import Tip
from app.core.gemini_api_datafetcher import get_ai_tip


def generate_daily_tips():
    db = SessionLocal()
    children = db.query(Child).all()
    for child in children:
        try:
            tip_content = get_ai_tip(problem=child.problem)
            new_tip = Tip(
                user_id=child.user_id,
                child_id=child.id,
                problem=child.problem,
                tip_content=tip_content
            )
            db.add(new_tip)
        except Exception as e:
            print(f"Error generating tip for child {child.id}: {e}")
    db.commit()
    db.close()

# Start the scheduler
scheduler = BackgroundScheduler()
scheduler.add_job(generate_daily_tips, "interval", days=1)
scheduler.start()
