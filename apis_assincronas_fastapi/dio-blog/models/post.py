import sqlalchemy as sa

posts = sa.Table(
    "posts", 
    metadata, 
    sa.Column("id", sa.Integer, primary_key=True),
    sa.Column("title", sa.String(150), nullable=False, unique=True),
    sa.Column("published_at", sa.DateTime, nullable=True),
    sa.Column("published", sa.Boolean, default=False),
    sa.Column("content", sa.String, nullable=False),
    
)