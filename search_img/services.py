import asyncio
import httpx

from config import settings


async def get_link(image_type: str):
    headers = {'x-api-key': settings.API_KEY}
    params = {'mime_types': image_type, 'format': 'json', 'limit': 1}
    url = "https://api.thecatapi.com/v1/images/search"

    async with httpx.AsyncClient(verify=False) as client:
        res = await client.get(url, headers=headers, params=params)
        if res.status_code == 200:
            response = res.json()
            return response[0].get('url')


async def search_image(image_type: str, count: int):
    current_page = 0
    images = await asyncio.gather(
        *(get_link(image_type) for _ in range(current_page, count)),
        return_exceptions=True
    )
    return images
