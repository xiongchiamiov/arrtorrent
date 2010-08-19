On open, we start off with one window, showing the buffer `clients01`.

Calling `:filter` allows you to filter the results by any of `Client`'s
attributes. I'm not sure if multiple calls would override previous ones, or
build on them.

Toggle selection of a client with space. Visual mode can be used to hilight a
number of rows, and then space toggles selection.

With some non-zero rows selected, `:torrents` creates a buffer named
`torrents01`, containing all torrents that match our selection, and displays it
in the current window. `:sbuffer clients01` will reopen the original buffer in a
split window. If the `torrents01` buffer already exists, it is updated. If it
exists and is in an open window, it is updated and focus is moved to that
window.

This window can create, in a similar fashion, buffers, with `:peers`, `:files`,
`:trackers`, `:chunks`, `:transfers`.

`:o[pen]` opens a new client buffer (`clients02` and so on) in the current
window; `:tabo[pen]` does the same, but in a new window, in a new tab.
