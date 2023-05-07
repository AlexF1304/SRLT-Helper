from tortoise import Tortoise


async def init():
    await Tortoise.init(
        db_url='sqlite://database/db.sqlite3',
        modules={'models': ['orm.models.models']}
    )
    await Tortoise.generate_schemas()
