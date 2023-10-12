import aiohttp


async def get_topics():
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://api-for-python-interview-preparation.onrender.com/topics") as response:
            topics = await response.json()
    return topics


async def get_questions():
    async with aiohttp.ClientSession() as session:
        async with session.get(url="https://api-for-python-interview-preparation.onrender.com/questions") as response:
            questions = await response.json()
    return questions
