''' Attach functions to wok hooks '''

from wok.contrib.hooks import compile_sass
import blog_images

hooks = {
    'site.content.gather.post': [blog_images.process_picasaweb_images]
}
