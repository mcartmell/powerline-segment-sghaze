from __future__ import absolute_import
from powerline.lib.threaded import ThreadedSegment
from powerline.theme import requires_segment_info
import urllib,json

def _haze(area='Central'):
   jsonurl = urllib.urlopen('http://sghaze.herokuapp.com')
   text = json.loads(jsonurl.read())
   c = text[area]
   return c

class SingaporeHazeSegment(ThreadedSegment):
  interval = 600

  def set_state(self, area='Central', **args):
    self.area = area
    super(SingaporeHazeSegment, self).set_state(**args)

  def update(self, old):
		return _haze(area=self.area)

  def render(self, c, **args):
    if not c:
      return None
    return [{
      'contents': '░ ' + str(c),
      'highlight_group': ['sghaze']
    }]

sghaze = SingaporeHazeSegment()
