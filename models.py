from config import db, ma

class Task(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100), nullable=False)
    description = db.Column(db.Text)
    due_date = db.Column(db.Date)
    priority = db.Column(db.Integer, default=0)
    is_completed = db.Column(db.Boolean, default=False)

    def __str__(self):
        return self.title + " " + self.description

class TaskSchema(ma.Schema):
    class Meta:
        fields = ('id', 'title', 'description', 'due_date', 'priority', 'is_completed')
        model = Task


task_schema = TaskSchema()
tasks_schema = TaskSchema(many=True)

