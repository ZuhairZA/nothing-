"""
media
	article_audio

	article_images
		insta
		newspaperImages
		twitter
		ETC

	background 		#dont touch

	cleanedImages

	videoChunks

	videos
		insta
		normal
		twitter

"""

import os
import shutil

media = ['article_images/insta', 'article_images/newspaperImages' ,'article_images/twitter' , 'article_audio', 'cleanedImages', 'videoChunks', 'videos/insta', 'videos/twitter', 'videos/normal']


def fFlush():
	shutil.rmtree('media')
	for i in media:
		os.makedirs('media/'+i)


fFlush()