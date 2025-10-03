import yt_dlp

def main():
    links = input("Вставьте ссылку(и) на видео из ютуб: ").split(',')

    links = [link.strip() for link in links if link.strip()]

    print("Выберете формат:")
    print("1. лучший по качеству (по умолчанию)")
    print("2. mp4 (Видео)")
    print("3. mp3 (только звук")
    format_choice = input("Введите число (1-3): ").strip()

    if format_choice == "2":
        ydl_opts = {'format': 'mp4'}
    elif format_choice == "3":
        ydl_opts = {
            'format': 'bestaudio/best',
            'postprocessors': [{
                'key': 'FFmpegExtractAudio',
                'preferredcodec': 'mp3',
                'preferredquality': '192',
            }],
        }
    else:
        ydl_opts = {'format': 'best'}

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        for link in links:
            try:
                ydl.download([link])
            except Exception as e:
                print(f"Ошибка установки {link}: {e}")

if __name__ == "__main__":
    main()