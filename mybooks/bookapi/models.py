from django.db import models 
from pathlib import Path

def determine_file_path(instance, filename):
    fileExt = Path(filename).suffix
    directoryName = 'document/'
    if (fileExt == '.pdf'):
        directoryName = 'pdf/'
    elif (fileExt == '.epub'):
        directoryName = 'epub/'
    
    return '{0}/{1}'.format(directoryName, filename)

def determine_file_type(file):
    print(file)
    fileExt = Path(file).suffix
    fileType = 'unknown'
    if (fileExt == '.pdf'):
        fileType = 'pdf'
    elif (fileExt == '.epub'):
        fileType = 'epub'
    return fileType

class BooksModel(models.Model):
    book_title = models.CharField(max_length=255, blank=True)
    file = models.FileField(blank=False, null=False, upload_to=determine_file_path)
    book_type = models.CharField(max_length=10, blank=True)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    owner = models.ForeignKey('auth.User', on_delete=models.CASCADE)

    def __str__(self):
        return self.file.name

    def remove_on_image_update(self):
        try:
            # is the object in the database yet?
            obj = BooksModel.objects.get(id=self.id)
        except BooksModel.DoesNotExist:
            # object is not in db, nothing to worry about
            return
        # is the save due to an update of the actual image file?
        if obj.file and self.file and (obj.file != self.file):
            # delete the old image file from the storage in favor of the new file
            obj.file.delete()

    def delete(self, *args, **kwargs):
        # object is being removed from db, remove the file from storage first
        self.file.delete()
        return super(BooksModel, self).delete(*args, **kwargs)

    def save(self, *args, **kwargs):
        if self.file:
            self.book_type = determine_file_type(self.file.name)
        # object is possibly being updated, if so, clean up.
        self.remove_on_image_update()
        super(BooksModel, self).save(*args, **kwargs) # Call the "real" save() method.
