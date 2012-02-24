''' Attach functions to wok hooks '''

import blog_images
import sass

hooks = {
    'site.output.post':[sass.compile_css],
    'site.content.gather.post': [blog_images.process_picasaweb_images]
}
