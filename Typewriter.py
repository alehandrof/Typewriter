# http://www.sublimetext.com/forum/viewtopic.php?f=6&t=4806
# created by:
# + castles_made_of_sand
# + facelessuser

import sublime, sublime_plugin

class TypewriterScrolling(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        if view.settings().get('typewriter_scrolling') == 1:
            sel = view.sel()
            region = sel[0] if len(sel) == 1 else None
            if region != None:
                view.show_at_center(region)