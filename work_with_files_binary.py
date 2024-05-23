import requests
url = 'https://static-assets.codecademy.com/assets/course-landing-page/meta/1x1/learn-typescript.jpg'
response = requests.get(url)
# print(response.text)

with open('ts.jpg', mode='wb') as file:
    file.write(response.content)

# url2 = '' ## .exe
# with open('ins.exe', mode='wb') as file:
#     file.write(requests.get(url2).content)

# url3 = '' ## .pdf
# with open('tut.pdf', mode='wb') as file:
#     file.write(requests.get(url3).content)


