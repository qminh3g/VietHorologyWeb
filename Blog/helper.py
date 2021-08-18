from django.template.defaultfilters import slugify
import random
import string
def slug_random(N):
    res = ''.join(random.choice(string.ascii_uppercase + string.digits)
                                                  for i in range(N))
    return res
def generate_slug(text):
    new_slug = slugify(text)
    from Blog.models import BlogModel
    if BlogModel.objects.filter(slug = new_slug).exists():
        return generate_slug(text +'-' +slug_random(5))
    return new_slug