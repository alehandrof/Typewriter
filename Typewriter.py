# http://www.sublimetext.com/forum/viewtopic.php?f=6&t=4806
# created by:
# + castles_made_of_sand
# + facelessuser

import sublime, sublime_plugin

class TypewriterScrolling(sublime_plugin.EventListener):
    def on_selection_modified(self, view):
        if view.settings().get('typewriter_mode_scrolling') == 1:
            sel = view.sel()
            region = sel[0] if len(sel) == 1 else None
            if region != None:
                view.show_at_center(region)
                offset = sublime.load_settings('Typewriter.sublime-settings').get('typewriter_mode_scrolling_offset', 0.0)
                if offset != 0:
                    cur_v = view.viewport_position()
                    new_v = (cur_v[0], cur_v[1] + (view.line_height() * offset) )
                    view.set_viewport_position(new_v)