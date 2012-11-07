''' Attach functions to wok hooks '''

from wok.contrib.hooks import compile_sass
import blog_images
import less

hooks = {
    'site.content.gather.post': [blog_images.process_picasaweb_images],
    'site.output.post':[less.compile]
}
