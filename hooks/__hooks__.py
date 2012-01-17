''' Attach functions to wok hooks '''

import blog

hooks = {
    'site.content.gather.post': [blog.process_title_images]
}
