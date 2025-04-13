from database.file_manager import FileManager

async def batch(files: list, client: Client):
    share_links = []
    for file_id in files:
        share_link = await FileManager.add_file(file_id, "document")
        share_links.append(share_link)

    combined_link = "_".join(share_links)
    share_url = f"https://t.me/{client.me.username}?start=batch_{combined_link}"
    return share_url
