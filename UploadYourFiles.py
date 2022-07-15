import os
import dropbox
from dropbox.files import WriteMode

class TransferData:
    def _init_(self, access_token):
        self.access_token = access_token

    def upload_file(self, file_from, file_to):
        dropbx = dropbox.Dropbox(self.access_token)

        for root, dirs, files in os.walk(file_from):

            for filename in files:

                local_path = os.path.join(root, filename)

                relative_path = os.path.relpath(local_path, file_from)
                dbx_path = os.path.join(file_to, relative_path)

                with open(local_path, 'rb') as f:
                    dropbx.files_upload(f.read(), dbx_path, mode = WriteMode('overwrite'))
   
def main():
    access_token='sl.BKA-GXaOqXF2Kv5-FRoKbmYxoGqKsvpRxFC1n8VA9uQsl07OkCJE3nxeVtoB3EZmXjHxonb-ZPZUplh8hyLgAPHNRduYi0CwydwcaNtJinoKiBxJh7ofpg2l7UHlQlbHfZvlvihwRzKH'
    transferData=TransferData(access_token)
    file_from=str(input("Enter the folder path to upload"))
    file_to=input('Enter the path to upload on dropbox')

    transferData.upload_file(file_from, file_to)
    print("File has been moved")
 
main()

    

