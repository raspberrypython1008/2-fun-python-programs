from requests import get
goturl=get(input('URL: '))
exec(goturl.content)
