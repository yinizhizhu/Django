from django.db import models

class blog_lee(models.Model):
    """
    	this is for each blogs
    		content:
    			class_blog		the class of the blog
    			tag_blog 		the tag of the blog
    			link_blog		the link of the blog
                index_blog      the content of index
    			state_blog 		the state of the blog
    			date_blog		the publishdate of the blog
    """
    title_blog = models.CharField(max_length = 45)
    class_blog = models.CharField(max_length = 45)
    tag_blog = models.CharField(max_length = 45)
    link_blog = models.CharField(max_length = 45)
    index_blog = models.CharField(max_length = 300)
    state_blog = models.BooleanField(default = False)  #to judge the first time and get the record.
    date_blog = models.DateTimeField(auto_now = True)

    def __unicode__(self):
        return self.date_blog