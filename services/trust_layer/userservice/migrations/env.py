from logging.config import fileConfig
from alembic import context
from app.db import engine
from app.models.user import Base

import asyncio
from sqlalchemy import pool
from sqlalchemy.engine import Connection

config = context.config
fileConfig(config.config_file_name)

# ✅ Use your actual model's metadata here
target_metadata = Base.metadata

# ✅ Offline mode (generates SQL string output)
def run_migrations_offline():
    context.configure(
        url=engine.url.render_as_string(hide_password=False),
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()

# ✅ Online mode (runs against live DB via async engine)
def do_run_migrations(connection: Connection):
    context.configure(connection=connection, target_metadata=target_metadata)
    with context.begin_transaction():
        context.run_migrations()

async def run_migrations_online():
    async with engine.begin() as conn:
        await conn.run_sync(do_run_migrations)

if context.is_offline_mode():
    run_migrations_offline()
else:
    asyncio.run(run_migrations_online())
