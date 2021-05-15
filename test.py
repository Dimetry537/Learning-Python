import matplotlib.pyplot as plt
import numpy as np

class TextResizer():
    def __init__(self, texts, fig=None, minimal=4):
        if not fig: fig = plt.gcf()
        self.fig=fig
        self.texts = texts
        self.fontsizes = [t.get_fontsize() for t in self.texts]
        _, self.windowheight = fig.get_size_inches()*fig.dpi
        self.minimal= minimal

    def __call__(self, event=None):
        scale = event.height / self.windowheight
        for i in range(len(self.texts)):
            newsize = np.max([int(self.fontsizes[i]*scale), self.minimal])
            self.texts[i].set_fontsize(newsize)

fontsize=11
text = plt.text(0.7, 0.6, "Some text", fontsize=fontsize,
                bbox={'facecolor':'skyblue', 'alpha':0.5, 'pad':10})

cid = plt.gcf().canvas.mpl_connect("resize_event", TextResizer([text]))

plt.show()