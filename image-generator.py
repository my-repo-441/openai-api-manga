from openai import OpenAI
import requests

client = OpenAI()

print(client)

response = client.images.generate(
  model="dall-e-3",
  prompt ="This is the final frame of a 10-page battle shonen manga. Draw the final frame.",
  size="1024x1024",
  quality="standard",
  n=1,
)

image_url = response.data[0].url
print(image_url)

# 画像をダウンロードするためのリクエストを送信
response = requests.get(image_url)

i=1
# リクエストが成功した場合（HTTPステータスコード200）
if response.status_code == 200:
    # バイナリモードで画像ファイルを開き、内容を書き込む
    with open(f"downloaded_image{i}.png", "wb") as file:
        file.write(response.content)
    print("Image successfully downloaded and saved.")
else:
    print(f"Failed to download image. Status code: {response.status_code}")
