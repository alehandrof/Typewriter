Typewriter
==========

This plugin provides two typewriter-inspired modes for Sublime Text 2 & 3\*:

- **Typewriter Scrolling** keeps the view centered on the current line, when there is more than half a screenful of text, à la _iA Writer_, _WriteRoom_ and the like. This mode keeps you from craning your neck to look at the bottom of the screen for hours on end. (If you happen to write for hours on end.)

- **Typewriter Typing** moves your cursor to the end of the file and disabling your cursor keys and all bindings that move the cursor and/or select text, leaving you only with letters, numbers, symbols, <kbd>Backspace</kbd>, <kbd>Delete</kbd> and <kbd>Enter</kbd>. Stay in the flow of writing and don't let your inner editor stifle your verbiage ever again. (Also: experience the joy of not being able to go back and correct your typos.)

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

The typewriter modes are controlled by the `typewriter_mode_scrolling` and `typewriter_mode_typing` settings. Setting them to `true` enables the modes.

- See the files provided for ideas on how to use these in settings & keymap files.
- You can toggle the modes via the:
	- Command Palette -- search for `typewriter`


## Changelog & History

- **0.3.0** - The new version disables the mouse in both scrolling and typing mode. The typing mode is much more robust. Because he APIs used are only available for ST3, I will no longer be maintaining the much glitchier ST2 version. (It's still available, though.)
- **0.2.3** - Added offset option for Scrolling mode (requested by [Luis Martins](https://github.com/lmartins)), along with some small fixes & tweaks.
- **0.2.2** - Typing mode now supports OSX as well.
- **0.2.1** - Renamed settings to `typewriter_mode_scrolling` and `typewriter_mode_typing` so they won't conflict with BufferScroll.
- **0.2** - Added Typing mode for Windows & Linux. `typewriter_mode` renamed `typewriter_scrolling`.
- **0.1** - Initial release. Typewriter was created upon [my request](http://www.sublimetext.com/forum/viewtopic.php?f=6&t=4806) by [castles\_made\_of\_sand](https://github.com/sublimator/) & [facelessuser](https://github.com/facelessuser).


## Issues/Todo

- Neither mode is designed to work with multiple cursors, though nothing terribly is likely to happen. I need to do some more testing with cloned views as well.
- Add Markdown syntax (Current state: rough draft)
- Add color scheme designed for prose/long text (Current state: near complete)


## Alternatives

- [BufferScroll](https://github.com/SublimeText/BufferScroll) also provides a version of "typewriter scrolling" and many other features besides.
- [MarkdownEditing](https://github.com/SublimeText-Markdown/MarkdownEditing) has added typewriter scrolling among other more Markdown-specific features.
