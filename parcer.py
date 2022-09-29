from urllib import request
import requests
import aspose.words as aw


def download_docx(url):

    try:
        response = requests.get(url=url)

        with open('raspisanie.doc', 'wb') as file:
            file.write(response.content)

        doc = aw.Document('raspisanie.doc')
        doc.save('raspisanie.docx')

    except Exception as ex:
        return 'Что-то пошло не так'
