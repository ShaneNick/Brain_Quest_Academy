from django.db import models

#Course model
class MakeCourse(models.Model):
    title = models.CharField(max_length = 100)
    course_desc = models.CharField(max_length = 500)


    def __str__(self):
        return self.title
    
class Section(models.Model):
    course = models.ForeignKey(MakeCourse, on_delete = models.CASCADE)
    title = models.CharField(max_length = 250)
    content = models.TextField()
    image = models.ImageField(upload_to= 'section_images/', blank = True, null = True)
    video = models.FileField(upload_to= 'section_videos/', blank = True, null = True)

    def __str__(self):
        return self.title
