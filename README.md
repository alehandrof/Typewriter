Typewriter
==========

This plugin provides two typewriter-inspired modes for Sublime Text 2 & 3\*:

- **Typewriter Scrolling** keeps the view centered on the current line, when there is more than half a screenful of text, à la _iA Writer_, _WriteRoom_ and the like.

	This mode keeps you from craning your neck to look at the bottom of the screen for hours on end. (If you happen to write for hours on end.)

- **Typewriter Typing** moves your cursor to the end of the file and disables all commands that move the cursor and/or select text, leaving you only with letters, numbers, symbols, Backspace, Delete and Enter.

	Stay in the flow of writing and don't let your inner editor stifle your verbiage ever again. (Also: experience the joy of not being able to go back and correct your typos.)

\* _The ST3 version is much more robust than the ST2 version, which is no longer being maintained._


## Installation

This plugin is available through [Package Control](https://sublime.wbond.net/).

Select the `Package Control: Install Package` command via the palette and choose the `Typewriter` package.

### Manual Install

1. Download the latest release from here: <https://github.com/alehandrof/Typewriter/releases/>
2. Extract it in your Packages folder. (You can find out its location by clicking the `Preferences > Browse Packages…` menu inside Sublime Text.)

-- _or_ --

Clone the repository in your Packages folder: `git clone https://github.com/alehandrof/Typewriter.git`


## Usage

The typewriter modes can be toggled via the command palette. Just search for `typewriter`. There are three commands: one to toggle each mode and one to toggle both modes together.

You can use the `typewriter_mode_scrolling` setting to enable or disable the Scrolling mode. For example, I have `"typewriter_mode_scrolling" : true,` in my Distraction Free settings.

The Typing mode needs to be triggered by the `typewriter_typing_toggle` command. In earlier versions, you could also toggle this mode via a setting, but this doesn't work well in the current version.

### Warnings

- Mouse clicking is disabled in both modes, but you can use the scroll wheel.
- For best results in Scrolling mode you should set `"scroll_past_end": true`. (By default it is set to `true` in Windows and Linux, but `false` in OSX.)

## Changelog & History

- **0.3.1** - Expanded usage warnings
- **0.3.0** - The mouse is now disabled in both Scrolling and Typing mode. The Typing mode now moves the cursor to the end of the file and is much more robust in general. Because the APIs used are only available for ST3, I will no longer be maintaining the much glitchier ST2 version. (It's still available, though.)
- **0.2.3** - Added offset option for Scrolling mode (requested by [Luis Martins](https://github.com/lmartins)), along with some small fixes & tweaks.
- **0.2.2** - Typing mode now supports OSX as well.
- **0.2.1** - Renamed settings to `typewriter_mode_scrolling` and `typewriter_mode_typing` so they won't conflict with BufferScroll.
- **0.2** - Added Typing mode for Windows & Linux. `typewriter_mode` renamed `typewriter_scrolling`.
- **0.1** - Initial release. Typewriter was created upon [my request](http://www.sublimetext.com/forum/viewtopic.php?f=6&t=4806) by [castles\_made\_of\_sand](https://github.com/sublimator/) & [facelessuser](https://github.com/facelessuser).


## Issues/Todo

- Neither mode is designed to work with multiple cursors, though nothing terrible is likely to happen. I need to do some more testing with cloned views as well.
- Figure out how to toggle Typing mode via setting correctly.
- Per [Issue #6](https://github.com/alehandrof/Typewriter/issues/6), change Scrolling mode to a command that can toggle `scroll_past_end` if needed. 
- Add Markdown syntax (Current state: rough draft)
- ~~Add color scheme designed for prose/long text (Current state: near complete)~~ See: [Writerly](https://github.com/alehandrof/Writerly)


## Alternatives

- [BufferScroll](https://github.com/SublimeText/BufferScroll) also provides a version of "typewriter scrolling" and many other features besides.
- [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing) has added typewriter scrolling among other more Markdown-specific features.
