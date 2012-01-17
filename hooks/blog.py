def process_title_images(pages):
    ''' For every content page, process the `title_img_src` in the YAML header
    from Picasa Web Albums, if it exists, and create two new variables for use
    in the templates called `title_img_full` and `title_img_resized`
    '''
    pass

''' Old attempt using page.template.post hook

    # declare standard image width, in pixels, for title images
    IMG_WIDTH = 480

    try:
        # grab the Picasa Web Albums' title image source URL from the 
        # `title_img_src` variable in the page variables
        src = templ_vars['page']['title_img_src']
        src_split = src.split('/')

        # figure out URL portion before and after the 'size' property denoted 
        # by /s<number>/ in the source URL which should look something like
        # https://lh6.googleusercontent.com/foo/bar/herp/derp/s144/capture.png
        src_before_size = '/'.join(src_split[:-2])
        src_after_size = src_split[-1]

        # construct the resized and full versions of the original source URL
        src_resized = "%s/s%s/%s"%(src_before_size, IMG_WIDTH, src_after_size)
        src_full = '%s/%s'%(src_before_size, src_after_size)

        # insert the new variables for the template
        templ_vars['page']['title_img_full'] = src_full
        templ_vars['page']['title_img_resized'] = src_resized

    except KeyError:
        # ignore any page that doesn't have a `title_img_src` variable
        pass
'''
