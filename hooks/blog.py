''' Blog-processing functions '''

import re

def process_images(pages):
    ''' Process images on each blog article '''

    TITLE_IMG_WIDTH = 480
    DEFAULT_IMG_WIDTH = 480

    def process_title_image(page):
        ''' For every content page, process the `title_img_src` in the YAML header
        from Picasa Web Albums, if it exists, and create two new variables for use
        in the templates called `title_img_full` and `title_img_resized`
        '''

        try:
            # grab the Picasa Web Albums' title image source URL from the 
            # 'title_img_src' variable in the page's meta data
            src = page.meta['title_img_src']
            src_split = src.split('/')

            # figure out URL portion before and after the 'size' property 
            # denoted by /s<number>/ in the source URL which should look 
            # something like
            # https://googleusercontent.com/foo/bar/herp/derp/s144/capture.png
            src_before_size = '/'.join(src_split[:-2])
            src_after_size = src_split[-1]

            # construct the resized/full versions of the src URL
            src_resized = "%s/s%s/%s"%(src_before_size, TITLE_IMG_WIDTH,\
                    src_after_size)
            src_full= "%s/s%s/%s"%(src_before_size, 0, src_after_size)

            # insert the new variables for the template
            page.meta['title_img_full'] = src_full
            page.meta['title_img_resized'] = src_resized

        except KeyError:
            # ignore any page that doesn't have a `title_img_src` variable
            pass

    def split_picasaweb_src(src, size):

        src_split = src.split('/')

        # figure out URL portion before and after the 'size' property 
        # denoted by /s<number>/ in the source URL which should look 
        # something like
        # https://googleusercontent.com/foo/bar/herp/derp/s144/capture.png
        src_before_size = '/'.join(src_split[:-2])
        src_after_size = src_split[-1]

        # construct the resized/full versions of the src URL
        src_resized = "%s/s%s/%s"%(src_before_size, size,
                src_after_size)
        src_full= "%s/s%s/%s"%(src_before_size, 0, src_after_size)

        return (src_resized, src_full)

    def process_article_images(page):

        PICASAWEB_IMG_FIND = r'^.*picasaweb-img:\s*(%s)<+?.*$'
        PICASAWEB_IMG_REPL = '''
            <div class='article-image'>
                <a href='%s'>
                    <img class='article-image' src='%s'>
                </a>
            </div>
            '''

        content = page.meta['content']
        matches = re.findall(PICASAWEB_IMG_FIND%('.*'), content, re.MULTILINE)

        print "Matches: " + str(matches)
        for match in matches:

            print "Current match: " + match

            src_resized, src_full = split_picasaweb_src(match, 
                    DEFAULT_IMG_WIDTH)

            find = PICASAWEB_IMG_FIND%(match)
            replace = PICASAWEB_IMG_REPL%(src_full, src_resized)

            content = re.sub(find, replace, content, flags=re.MULTILINE) 

        page.meta['content'] = content

        '''
        processed_content, nr_replaced = re.subn(PICASAWEB_IMG_FIND, 
                PICASAWEB_IMG_REPL, content, flags = re.M)

        if nr_replaced > 0:
            print "OK! "
            page.meta['content'] = processed_content
        else:
            print "Fail"
        print
        '''

    # run image processors on each blog article
    for page in pages:
        if 'blog' in page.meta['category']:
            process_title_image(page)
            process_article_images(page)

