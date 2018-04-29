import uuid
from os import path

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt
from wordcloud import WordCloud, STOPWORDS

from django.conf import settings


class GenerateWordCloud(object):
	"""
		docstring for GenerateWordCloud
	"""
	
	def execute(self, text):
		alice_mask = np.array(Image.open(path.join(settings.BASE_DIR, 'static/images/github_mask.png')))
		stopwords = set(STOPWORDS)
		stopwords.add("said")
		wc = WordCloud(background_color="white", max_words=2000, mask=alice_mask,
						stopwords=stopwords, contour_width=3, contour_color='#26dad2',
						font_path=path.join(settings.BASE_DIR, 'static/fonts/CabinSketch-Bold.ttf'))
		wc.generate(text)
		filename = str(uuid.uuid4()) + ".png"
		wc.to_file(path.join(settings.BASE_DIR, 'static/images/%s' % filename))
		return {
			"filename": filename
		}
