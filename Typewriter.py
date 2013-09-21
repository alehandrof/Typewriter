# originally created by:
# + castles_made_of_sand
# + facelessuser
# http://www.sublimetext.com/forum/viewtopic.php?f=6&t=4806

import sublime, sublime_plugin


class TypewriterScrolling(sublime_plugin.EventListener):
    # def run (self, view):
        # self.center_view(view)

    # def on_deactivated(self, view):
        # self.center_view(view)

    def on_selection_modified(self, view):
        self.center_view(view)

    def center_view(self, view):
        if view.settings().get('typewriter_mode_scrolling') == 1:
            sel = view.sel()
            region = sel[0] if len(sel) == 1 else None
            if region != None:
                global offset
                offset = sublime.load_settings('Typewriter.sublime-settings').get('typewriter_mode_scrolling_offset', 0.0) * view.line_height()
                if offset != 0:
                    if offset > (view.viewport_extent()[1] / 2):
                        print("Typewriter Error: The cursor is outside the viewport! Use a smaller offset value.")
                    else:
                        region = sublime.Region(self.offset_point(view, region.a), self.offset_point(view, region.b))
                view.show_at_center(region)

    def offset_point(self, view, point):
        vector = list( view.text_to_layout(point) )
        vector[1] = vector[1] + offset
        return view.layout_to_text( tuple(vector) )
