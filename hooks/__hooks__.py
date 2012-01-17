''' Attach functions to wok hooks '''

import blog

hooks = {
    'page.template.pre': [blog.process_title_image]
}
