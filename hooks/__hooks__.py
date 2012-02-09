''' Attach functions to wok hooks '''

import blog_images

hooks = {
    'site.content.gather.post': [blog_images.process_picasaweb_images]
}
