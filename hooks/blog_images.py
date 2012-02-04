''' Process Picasa Web Albums images in blog articles
'''

import re

# default image sizes
TITLE_IMG_SIZE = 719        # Size of the title image
THUMBNAIL_IMG_SIZE = 100    # Size of thumbnails
ARTICLE_IMG_SIZE = 480      # Size of article images

def process_picasaweb_images(pages):
    ''' Process Picasa Web Album images for each blog article
    '''

    def run():
        ''' Process images on all blog articles
        '''
        for page in pages:
            if 'blog' in page.meta['category']:
                process_title_image(page, TITLE_IMG_SIZE, THUMBNAIL_IMG_SIZE)
                process_article_images(page, ARTICLE_IMG_SIZE)


    def process_title_image(page, title_size, thumbnail_size):
        ''' For a single blog article in `page`, process the `title_img_src` 
        meta variable from Picasa Web Albums, if it exists, and create three 
        new meta variables for use in the templates:

            `title_img_full`:   Full-sized version of the image 
            `title_img_title`:  Title image-size version
            `title_img_thumb`:  Tiny version for use with thumbnails
        '''

        try:
            src = page.meta['title_img_src']
            src_full, src_title = split_picasaweb_src(src, title_size) 
            src_full, src_thumb = split_picasaweb_src(src, thumbnail_size)

            # insert the new variables for the template
            page.meta['title_img_full'] = src_full
            page.meta['title_img_title'] = src_title
            page.meta['title_img_thumb'] = src_thumb

        except KeyError:
            # ignore article that doesn't have a `title_img_src` variable
            pass


    def process_article_images(page, img_size):
        ''' Find all Picasa Web Album image source URLs in the given `page`,
        resize them according to `size`, and link them to the full version
        of the image.

        Picasa Web Album image source URLs should be denoted by 'picasa-img:'
        followed by the URL on their own line in the content file of the blog 
        article, e.g., 

            picasaweb-img: https://googleusercontent.com/foo/s144/bar.png

        Note that this is only tested for content written in Markdown
        '''

        # image tag find/replacement patterns
        PICASAWEB_IMG_FIND = r'^.*picasaweb-img:\s*(%s)<+?.*$'
        PICASAWEB_IMG_REPL = '''
            <div class='article-image'>
                <a href='%s'>
                    <img class='article-image' src='%s'>
                </a>
            </div>
            '''

        content = page.meta['content']

        # find all image tags and replace them with their prettified forms
        # defined in PICASAWEB_IMG_REPL
        matches = re.findall(PICASAWEB_IMG_FIND%('.*'), content, re.MULTILINE)
        for match in matches:
            src_full, src_resized = split_picasaweb_src(match, img_size)

            find = PICASAWEB_IMG_FIND%(match)
            replace = PICASAWEB_IMG_REPL%(src_full, src_resized)

            content = re.sub(find, replace, content, flags=re.MULTILINE) 

        # write the modified content back to the page
        page.meta['content'] = content


    def split_picasaweb_src(src, size):
        ''' Split a Picasa Web Album's image URL source into two sizes: full,
        and the specified `size`. 
        
        The source URL should look something like:
            
            https://googleusercontent.com/foo/s144/bar.png

        A tuple will be returned with the full and resized versions, e.g.,

            ('https://googleusercontent.com/foo/s0/bar.png',
            'https://googleusercontent.com/foo/s200/bar.png')
        '''

        src_split = src.split('/')

        # get the URL portion before and after the 'size' property 
        # denoted by /s<number>/ in the source URL
        src_before_size = '/'.join(src_split[:-2])
        src_after_size = src_split[-1]

        # construct the full and resized versions of the src URL
        src_full= "%s/s%s/%s"%(src_before_size, 0, src_after_size)
        src_resized = "%s/s%s/%s"%(src_before_size, size, src_after_size)

        # return the full and resized versions of the source URL 
        return (src_full, src_resized)


    # run all image processing functions
    run()
