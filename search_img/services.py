import asyncio
import httpx
import aiofiles

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


async def download_file(user_id: int, url: str):
    async with httpx.AsyncClient() as client:
        file_name = f'media/{user_id}/{url.split("/")[-1]}'
        res = await client.get(url)
        async with aiofiles.open(file_name, 'wb+') as f:
            await f.write(res.read())


async def save_images(user_id: int, image_type: str, count: int):
    link_images = await search_image(image_type, count)
    await asyncio.gather(
        *(download_file(user_id, url) for url in link_images),
        return_exceptions=True
    )
    return link_images
