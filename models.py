from extensions import db

class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    description = db.Column(db.Text)
    priority = db.Column(db.String(50), nullable=False)
    due_date = db.Column(db.String(50), nullable=False)
    status = db.Column(db.String(50), nullable=False)

    def __getitem__(self, item):
        return getattr(self, item)

def get_all_tasks():
    return Task.query.all()

def get_task_by_id(task_id):
    return Task.query.get(task_id)

def create_task(title, description, priority, due_date):
    new_task = Task(title=title, description=description, priority=priority, due_date=due_date, status="Pending")
    db.session.add(new_task)
    db.session.commit()

def update_task(task_id, title, description, priority, due_date, status):
    task = Task.query.get(task_id)
    if task:
        task.title = title
        task.description = description
        task.priority = priority
        task.due_date = due_date
        task.status = status
        db.session.commit()

def delete_task(task_id):
    task = Task.query.get(task_id)
    if task:
        db.session.delete(task)
        db.session.commit()
