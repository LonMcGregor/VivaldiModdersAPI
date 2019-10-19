## Vivaldi Prefs
### vivaldi.address_bar.autocomplete.enabled
Type: `boolean`

Default: True

### vivaldi.address_bar.autocomplete.tld
Type: `string`

Default: com

### vivaldi.address_bar.autocomplete.prefer_bookmarks
Type: `boolean`

Default: True

### vivaldi.address_bar.extensions.show_toggle
Whether to display a toggle to show/hide extension buttons on the address bar.

Type: `boolean`

Default: False

### vivaldi.address_bar.extensions.visible
Whether extension buttons are shown on the address bar.

Type: `boolean`

Default: True

### vivaldi.address_bar.omnibox.cutcopy_encoded
URL encode the string passed to the clipboard from the url field

Type: `boolean`

Default: False

### vivaldi.address_bar.omnibox.enabled
Type: `boolean`

Default: True

### vivaldi.address_bar.omnibox.show_bookmarks
Type: `boolean`

Default: True

### vivaldi.address_bar.omnibox.show_typed_history
Type: `boolean`

Default: True

### vivaldi.address_bar.omnibox.show_top_sites
Type: `boolean`

Default: False

### vivaldi.address_bar.position
Type: `enum`

Enum|Notes
---|---
top|*Default*
bottom|

### vivaldi.address_bar.search.enabled
Type: `boolean`

Default: True

### vivaldi.address_bar.search.keep_selected
Keep last search engine selected in search field

Type: `boolean`

Default: False

### vivaldi.address_bar.search.suggest_enabled
Type: `boolean`

Default: False

### vivaldi.address_bar.search.typed_history_enabled
Type: `boolean`

Default: True

### vivaldi.address_bar.search.show_favicon
Type: `boolean`

Default: False

### vivaldi.address_bar.select_on_click
Select the content of the URL field when it gets activated

Type: `boolean`

Default: True

### vivaldi.address_bar.show_full_url
Type: `boolean`

Default: False

### vivaldi.address_bar.show_profile
Type: `boolean`

Default: True

### vivaldi.address_bar.show_progress
Type: `boolean`

Default: True

### vivaldi.address_bar.typed_history_enabled
Type: `boolean`

Default: True

### vivaldi.address_bar.url_open_shortcut
Which modifier key to use for opening the url in a new tab

Type: `enum`

Enum|Notes
---|---
alt|*Default*
shift|

### vivaldi.address_bar.visible
Type: `boolean`

Default: True

### vivaldi.bookmarks.bar.sorting
Type: `dictionary`

Default: {'sortOrder': 1, 'sortField': 'manually'}

### vivaldi.bookmarks.bar.display
Type: `enum`

Enum|Notes
---|---
default|*Default*
text|
icon|
iconexceptfolders|

### vivaldi.bookmarks.bar.folder_ids
Type: `list`

Default: ['1']

### vivaldi.bookmarks.bar.position
Type: `enum`

Enum|Notes
---|---
top|*Default*
bottom|

### vivaldi.bookmarks.bar.visible
Type: `boolean`

Default: False

### vivaldi.bookmarks.can_initialize
Test if initializing can be made possible if false

Type: `boolean`

Default: False

### vivaldi.bookmarks.confirm_opening
Ask before opening a number of bookmarks >= to  kBookmarksConfirmOpeningThreshold

Type: `boolean`

Default: True

### vivaldi.bookmarks.confirm_opening_threshold
Type: `integer`

Default: 20

### vivaldi.bookmarks.deleted_partners
Type: `list`

Default: []

### vivaldi.bookmarks.language
Set on first run. Upgrades will use this language when needed

Type: `string`

Default: ''

### vivaldi.bookmarks.manager.sorting
Type: `dictionary`

Default: {'sortOrder': 1, 'sortField': 'manually'}

### vivaldi.bookmarks.open_in_new_tab
Type: `boolean`

Default: False

### vivaldi.bookmarks.save_folder
Last Folder a bookmark was added to in url field

Type: `string`

Default: ''

### vivaldi.bookmarks.single_click_opens
Type: `boolean`

Default: False

### vivaldi.bookmarks.underline_menu_letter
Type: `boolean`

Default: False

### vivaldi.bookmarks.version
Type: `string`

Default: ''

### vivaldi.bookmarks.panel.sorting
Type: `dictionary`

Default: {'sortOrder': 1, 'sortField': 'manually'}

### vivaldi.biscuit.load_bookmarks
Type: `boolean`

Default: False

### vivaldi.biscuit.version
Type: `boolean`

Default: False

### vivaldi.calendar.date_format
Type: `enum`

Enum|Notes
---|---
language|*Default*
system|

### vivaldi.calendar.display_mode
Type: `enum`

Enum|Notes
---|---
day|
week|
multiweek|
month|*Default*
year|
agenda|

### vivaldi.calendar.show_day_sidebar
Type: `boolean`

Default: False

### vivaldi.calendar.default_calendar_id
Type: `string`

Default: ''

### vivaldi.clear_private_data.entries
Type: `dictionary`

Default: {}

### vivaldi.clear_private_data.range
Type: `enum`

Enum|Notes
---|---
past_hour|*Default*
past_day|
past_week|
past_4_weeks|
everything|

### vivaldi.contact.panel.sorting
Type: `dictionary`

Default: {'sortOrder': 1, 'sortField': 'manually'}

### vivaldi.dot_net.username
Type: `string`

Default: ''

### vivaldi.downloads.notify_on_complete
Type: `boolean`

Default: True

### vivaldi.downloads.open_panel_on_new
Opens the download panel when starting a new download

Type: `boolean`

Default: True

### vivaldi.downloads.panel.editor_height
Type: `integer`

Default: 180

### vivaldi.downloads.panel.sorting
Type: `dictionary`

Default: {'sortOrder': 2, 'sortField': 'startTime'}

### vivaldi.downloads.start_automatically
Automatically download files to the default download folder without asking the user

Type: `boolean`

Default: False

### vivaldi.downloads.update_default_download_when_saving_as
Update default download directory when setting download target via 'Save as...'

Type: `boolean`

Default: False

### vivaldi.homepage
Type: `string`

Default: https://vivaldi.com/

### vivaldi.homepage_cache
Cached custom homepage URL

Type: `string`

Default: https://vivaldi.com/

### vivaldi.history.days_to_keep_visits
Type: `integer`

Default: 91

### vivaldi.hue.bridge_ip
Hue Bridge IP

Type: `string`

Default: ''

### vivaldi.hue.enabled
Enable Hue Light integration

Type: `boolean`

Default: False

### vivaldi.hue.lights
List of selected light MAC addresses

Type: `list`

Default: []

### vivaldi.hue.username
Hue access token, called username in the API

Type: `string`

Default: ''

### vivaldi.razer_chroma.enabled
Enable Razer Chroma integration

Type: `boolean`

Default: False

### vivaldi.razer_chroma.devices
The devices we want to integrate with. Valid options: keyboard, mouse, mousemat, chromalink

Type: `list`

Default: ['keyboard', 'mouse', 'mousemat', 'chromalink']

### vivaldi.razer_chroma.has_shown_promotion
Has shown Razer Chroma promotion dialog.

Type: `boolean`

Default: False

### vivaldi.incognito.show_intro
Type: `boolean`

Default: True

### vivaldi.keyboard.shortcuts.alt_opens_menu
Pressing Alt opens the main menu

Type: `boolean`

Default: True

### vivaldi.keyboard.shortcuts.enable
Type: `boolean`

Default: True

### vivaldi.keyboard.shortcuts.enable_single_key
Type: `boolean`

Default: False

### vivaldi.keyboard.shortcuts.enable_single_key_for_mail
Type: `boolean`

Default: True

### vivaldi.keyboard.shortcuts.space_fast_forwards
Pressing space when a page is scrolled to the bottom will trigger fast-forward

Type: `boolean`

Default: True

### vivaldi.keyboard.tab_to_all
Whether the tab key allows reaching all controls or only text inputs and lists

Type: `integer`

Default: -1

### vivaldi.keyboard.tab_to_all_uses_system_default
Set tab_to_all based on the operating system configuration

Type: `boolean`

Default: False

### vivaldi.mail.accounts
Mail account credentials for each set up account

Type: `list`

Default: []

### vivaldi.mail.check_interval
How often to check for new mail, in minutes or false for manually

Type: `enum`

Enum|Notes
---|---
one_minute|
fifteen_minutes|*Default*
manual|

### vivaldi.mail.compose_headers_hidden
What header fields are hidden in mail message header when composing

Type: `list`

Default: []

### vivaldi.mail.contact_default_action
Selecting a contact can either view all messages or compose a message

Type: `enum`

Enum|Notes
---|---
compose|
viewAllMessages|*Default*

### vivaldi.mail.default_account
The one mail account that shall be the default account when sending mail

Type: `string`

Default: ''

### vivaldi.mail.imap_logs_on
Are imap actions logged in debug console or not?

Type: `boolean`

Default: False

### vivaldi.mail.is_turned_off
Is mail client turned on or off?

Type: `boolean`

Default: False

### vivaldi.mail.last_sent_from
The mail account that was most recently used to send from

Type: `string`

Default: ''

### vivaldi.mail.notifications
Should show mail notifications

Type: `boolean`

Default: True

### vivaldi.mail.notifications_sound_on
Have silent notifications

Type: `boolean`

Default: True

### vivaldi.mail.notifications_on_successfully_sent
Show a mail notification when a message is successfully sent

Type: `boolean`

Default: False

### vivaldi.mail.read_headers_hidden
What header fields are hidden in mail message header when reading

Type: `list`

Default: []

### vivaldi.mail.send_or_queue
Should button in Mail Composer Send directly or Queue to Outbox?

Type: `enum`

Enum|Notes
---|---
send|*Default*
queue|

### vivaldi.mail.search_ascending
Is mail list ordered ascending or descending?

Type: `boolean`

Default: True

### vivaldi.mail.search_threading
Is mail listed according to discussion threads?

Type: `boolean`

Default: True

### vivaldi.mail.single_click_tabs
Open mail tabs with single click

Type: `boolean`

Default: True

### vivaldi.mail.view_layout
Layout of mail client

Type: `enum`

Enum|Notes
---|---
horizontal|
vertical|*Default*
vertical_wide|

### vivaldi.mail.view_dimensions
Dimensions of mail list and detail view

Type: `dictionary`

Default: {'width': 400, 'width_wide': 600, 'height': 240}

### vivaldi.mouse_gestures.alt_gestures_enabled
Allow gestures using Alt key and left mouse button

Type: `boolean`

Default: False

### vivaldi.mouse_gestures.enabled
Type: `boolean`

Default: True

### vivaldi.mouse_gestures.stroke_tolerance
How many logical pixels the mouse has to travel before the mouse gesture move is detected. This is not syncable as it is a device-specific.

Type: `double`

Default: 20.0

### vivaldi.mouse_gestures.rocker_gestures.enabled
Type: `boolean`

Default: True

### vivaldi.mouse_gestures.double_click_menu.enabled
Type: `boolean`

Default: False

### vivaldi.mouse_wheel.page_zoom
Zoom pages with a mouse wheel or touchpad

Type: `boolean`

Default: True

### vivaldi.mouse_wheel.tab_switch
Switch tabs with a mouse wheel or touchpad

Type: `boolean`

Default: False

### vivaldi.notes.creation.add_screenshot
Automatically fetch a screenshot for new notes

Type: `boolean`

Default: True

### vivaldi.notes.creation.notify
Type: `boolean`

Default: True

### vivaldi.notes.creation.show_panel
Type: `boolean`

Default: False

### vivaldi.notes.panel.editor_height
Type: `integer`

Default: 300

### vivaldi.notes.panel.show_markdown
Display the notes text formattedusing mmarkdown

Type: `boolean`

Default: False

### vivaldi.notes.panel.sorting
Type: `dictionary`

Default: {'sortOrder': 1, 'sortField': 'manually'}

### vivaldi.page.search.in_background
Type: `boolean`

Default: False

### vivaldi.panels.as_overlay.auto_close
Type: `boolean`

Default: True

### vivaldi.panels.as_overlay.enabled
Enable floating panel

Type: `boolean`

Default: False

### vivaldi.panels.position
Type: `enum`

Enum|Notes
---|---
left|*Default*
right|

### vivaldi.panels.show_toggle
Show toggle button along the edge of the panel

Type: `boolean`

Default: False

### vivaldi.panels.window.show_unread
Type: `boolean`

Default: True

### vivaldi.popups.show_in_tab
Type: `boolean`

Default: False

### vivaldi.plugins.widevine.enabled
Type: `boolean`

Default: True

### vivaldi.privacy.autofill.server_assist
Use Google server-side assisted autofill.

Type: `boolean`

Default: True

### vivaldi.privacy.adverse_ad_block.enabled
Enables update and loading of the block-list.

Type: `boolean`

Default: True

### vivaldi.privacy.adverse_ad_block.last_update
Last time we did a successfull update of the block-list.

Type: `string`

Default: ''

### vivaldi.privacy.adverse_ad_block.block_list_url
URL to the most recent block-list.

Type: `string`

Default: https://downloads.vivaldi.com/blocklist/current.json

### vivaldi.privacy.adverse_ad_block.block_list_sha256_url
URL to a sha256 sum of the most recent block-list.

Type: `string`

Default: https://downloads.vivaldi.com/blocklist/current.sha256

### vivaldi.privacy.adverse_ad_block.update_interval
Time between the block-list download refresh in hours.

Type: `integer`

Default: 24

### vivaldi.quick_commands.open_url_in_new_tab
Open QC links in a new tab, overriding global setting

Type: `boolean`

Default: False

### vivaldi.quick_commands.match_nickname
Launch QC bookmark on its nickname match

Type: `boolean`

Default: False

### vivaldi.quick_commands.show_bookmarks
Include bookmarks in QC search results

Type: `boolean`

Default: True

### vivaldi.quick_commands.show_calculator
Include calculator in QC search results

Type: `boolean`

Default: True

### vivaldi.quick_commands.show_history
Include history in QC search results

Type: `boolean`

Default: True

### vivaldi.quick_commands.show_notes
Include notes in QC search results

Type: `boolean`

Default: True

### vivaldi.quick_commands.show_page_actions
Include page actions in QC search results

Type: `boolean`

Default: True

### vivaldi.quick_commands.limit_results
Limit number of QC search results to 20 per category

Type: `boolean`

Default: True

### vivaldi.quick_commands.search_english
Search in English translation term of command

Type: `boolean`

Default: True

### vivaldi.settings.size.width
Type: `integer`

Default: 960

### vivaldi.settings.size.height
Type: `integer`

Default: 800

### vivaldi.settings.size.top
Type: `integer`

Default: -1

### vivaldi.settings.size.left
Type: `integer`

Default: -1

### vivaldi.startpage.background.color
Background color or 'user_defined' reference

Type: `string`

Default: #cccccc

### vivaldi.startpage.background.color_custom
User-defined background color

Type: `string`

Default: #bfb8b0

### vivaldi.startpage.image.enable
Type: `boolean`

Default: True

### vivaldi.startpage.image.path
Start page image path, 'user_defined', or 'desktop_image' reference

Type: `file_path`

Default: ./../resources/bg.jpg

### vivaldi.startpage.image.path_custom
User-defined start page image path

Type: `file_path`

Default: ./../resources/bg.jpg

### vivaldi.startpage.image.repeat
Type: `boolean`

Default: False

### vivaldi.startpage.image.stretch
Type: `boolean`

Default: True

### vivaldi.startpage.speed_dial.add_button_visible
Type: `boolean`

Default: True

### vivaldi.startpage.speed_dial.allow_dnd
Allow Speed Dial entries reordering by drag & drop

Type: `boolean`

Default: True

### vivaldi.startpage.speed_dial.columns
Type: `integer`

Default: 6

### vivaldi.startpage.speed_dial.controls_visible
Type: `boolean`

Default: True

### vivaldi.startpage.speed_dial.delete_visible
Type: `boolean`

Default: True

### vivaldi.startpage.speed_dial.display_navigation
Controls Speed Dial navigation display in other Start Page components

Type: `boolean`

Default: False

### vivaldi.startpage.speed_dial.display_search
Display search field on Speed Dial page

Type: `boolean`

Default: True

### vivaldi.startpage.speed_dial.titles_visible
Type: `enum`

Enum|Notes
---|---
always|*Default*
hover|
never|

### vivaldi.startpage.speed_dial.width
Type: `integer`

Default: 220

### vivaldi.startup.check_is_default
Check if vivaldi is default on startup (not synced to allow people to have different default browser on different computers)

Type: `boolean`

Default: True

### vivaldi.startup.last_seen_version
Most recent version number seen on startup

Type: `string`

Default: ''

### vivaldi.startup.remember_full_screen
Re-open vivaldi in full-screen if it was closed in full-screen. Unofficial setting, not exposed in the UI for now.

Type: `boolean`

Default: False

### vivaldi.status_bar.display
Type: `enum`

Enum|Notes
---|---
on|*Default*
off|
overlay|

### vivaldi.sync.active
Type: `boolean`

Default: False

### vivaldi.sync.is_using_separate_encryption_password
Type: `enum`

Enum|Notes
---|---
unknown|*Default*
aye|
nay|

### vivaldi.sync.session_name
Type: `string`

Default: ''

### vivaldi.sync.username
Type: `string`

Default: ''

### vivaldi.tabs.activation.on_clone
Tab activation after clonning a tab

Type: `enum`

Enum|Notes
---|---
rightofcurrent|*Default*
alwayslast|

### vivaldi.tabs.activation.on_close
Tab activation after closing a tab

Type: `enum`

Enum|Notes
---|---
activation_order|*Default*
left|
right|

### vivaldi.tabs.activation.prefer_related
Always activate related tab

Type: `boolean`

Default: True

### vivaldi.tabs.active_min_size
Enforced minimum size of active tab

Type: `integer`

Default: 30

### vivaldi.tabs.align_next
Align close buttons with closed tab by freezing tab size for duration of hover

Type: `boolean`

Default: True

### vivaldi.tabs.always_load_pinned_after_restore
Type: `boolean`

Default: True

### vivaldi.tabs.at_edge
Remove vertical space around tab bar in fullscreen mode

Type: `boolean`

Default: False

### vivaldi.tabs.auto_muting
Rules for muting tabs

Type: `enum`

Enum|Notes
---|---
off|*Default*
onlyActive|
prioritizeActive|

### vivaldi.tabs.bar.width
Vertical Tab Bar width

Type: `integer`

Default: 180

### vivaldi.tabs.bar.height
Horizontal Tab Bar height

Type: `integer`

Default: 30

### vivaldi.tabs.bar.position
Type: `enum`

Enum|Notes
---|---
top|*Default*
left|
right|
bottom|

### vivaldi.tabs.close_pinned
Whether pinned tabs can be closed or buried

Type: `enum`

Enum|Notes
---|---
on|
off|*Default*
bury|

### vivaldi.tabs.counter_detection
Detect counter in webpage titles

Type: `boolean`

Default: True

### vivaldi.tabs.cycle_by_recent_order
Whether to cycle tabs by recently seen or linear order

Type: `boolean`

Default: True

### vivaldi.tabs.defer_loading_after_restore
Type: `boolean`

Default: True

### vivaldi.tabs.dim_hibernated
Dim favicon of hibernated pages

Type: `boolean`

Default: False

### vivaldi.tabs.double_click_close
Close tab on double-click

Type: `boolean`

Default: False

### vivaldi.tabs.page_load_info
Tab page loading progress display

Type: `enum`

Enum|Notes
---|---
none|
progress_bar|*Default*
progress_icon|
spinner|

### vivaldi.tabs.favicon_spinner.enabled
[DEPRECATED 2019/6]

Type: `boolean`

Default: False

### vivaldi.tabs.focus_webview
Focus webpage instead of address bar on new tab

Type: `boolean`

Default: False

### vivaldi.tabs.minimize
Click active tab to switch to previously active one

Type: `boolean`

Default: False

### vivaldi.tabs.never_close_last
Display tab popup tooltip preview

Type: `boolean`

Default: True

### vivaldi.tabs.new_page.link
New tab link type, one of NEW_PAGE_TYPE constant

Type: `enum`

Enum|Notes
---|---
startpage|*Default*
homepage|
blankpage|
extension|
custom|

### vivaldi.tabs.new_page.url
[DEPRECATED 2018-11] The actual URL for new tabs

Type: `string`

Default: ''

### vivaldi.tabs.new_page.custom_url
The URL set to be used when choosing a custom URL for new tabs

Type: `string`

Default: ''

### vivaldi.tabs.new_placement
Placement of a new tab

Type: `enum`

Enum|Notes
---|---
rightofcurrent|*Default*
directrightofcurrent|
alwayslast|
openintabstackwithrelated|

### vivaldi.tabs.selection.enabled
Enable tab selection

Type: `boolean`

Default: True

### vivaldi.tabs.selection.include_active
Include current tab in new selection

Type: `boolean`

Default: True

### vivaldi.tabs.show_close_button
Show tab close button

Type: `boolean`

Default: True

### vivaldi.tabs.stacking.allow_dnd
Allow tab stacking by drag & drop

Type: `boolean`

Default: True

### vivaldi.tabs.stacking.allow_rename
Allow tab stack renaming

Type: `boolean`

Default: False

### vivaldi.tabs.stacking.dnd_delay
Delay before triggering tab stacking by drag & drop

Type: `integer`

Default: 250

### vivaldi.tabs.stacking.mode
Enable tab stacking

Type: `enum`

Enum|Notes
---|---
off|
on|*Default*

### vivaldi.tabs.stacking.name_map
Keeps local track of tab stack name changes

Type: `dictionary`

Default: {}

### vivaldi.tabs.stacking.open_in_current
Open links within current tab stack

Type: `boolean`

Default: True

### vivaldi.tabs.thumbnails
Show page preview thumbnail within a tab

Type: `boolean`

Default: True

### vivaldi.tabs.tooltip
Display tab popup tooltip preview

Type: `boolean`

Default: True

### vivaldi.tabs.unread
Show unread page tab indicator

Type: `boolean`

Default: True

### vivaldi.tabs.visible
Whether to show the tab bar

Type: `boolean`

Default: True

### vivaldi.tabs.visual_switch.enable
Enable tab preview overlay when switching tabs

Type: `boolean`

Default: False

### vivaldi.tabs.visual_switch.list_layout
Show tab preview overlay as list

Type: `boolean`

Default: False

### vivaldi.appearance.css_ui_mods_directory
CSS modifications directory where *.css files will be injected from.

Type: `file_path`

Default: ''

### vivaldi.appearance.column_widths.entries
Type: `dictionary`

Default: {}

### vivaldi.theme.color_accent_saturation_limit
Type: `double`

Default: 1.0

### vivaldi.theme.contrast_minimum
Type: `double`

Default: 0.0

### vivaldi.theme.dim_blurred
Fade the colors of content that's not focused

Type: `boolean`

Default: False

### vivaldi.theme.window_background_accent_color_blend
Type: `boolean`

Default: True

### vivaldi.theme.window_background_image_url
Type: `string`

Default: ../resources/triangles_pattern_vivaldi.png

### vivaldi.theme.window_background_image_scaling
Type: `enum`

Enum|Notes
---|---
scale|
repeat|*Default*

### vivaldi.theme.window_background_image_enabled
Type: `boolean`

Default: False

### vivaldi.theme.use_animation
Type: `boolean`

Default: True

### vivaldi.toolbars.navigation
Type: `list`

Default: ['Back', 'Forward', 'Rewind', 'FastForward', 'Reload', 'Home']

### vivaldi.toolbars.status
Type: `list`

Default: ['PanelToggle', 'SyncStatus', 'StatusInfo', 'TaskList', 'VersionInfo', 'CaptureImages', 'TilingToggle', 'ImagesToggle', 'PageActions', 'Zoom']

### vivaldi.vivaldi_account.id
The actual username obtained from the server

Type: `string`

Default: ''

### vivaldi.vivaldi_account.refresh_token
Encrypted OAuth2 refresh token

Type: `string`

Default: ''

### vivaldi.vivaldi_account.username
The username as entered by the user

Type: `string`

Default: ''

### vivaldi.webpages.access_keys
Allows web pages to use access keys if turned on, otherwise blocks them.

Type: `boolean`

Default: True

### vivaldi.webpages.capture.directory
The location where captured pages are stored

Type: `file_path`

Default: None

### vivaldi.webpages.capture.compression_format
Type: `enum`

Enum|Notes
---|---
png|*Default*
jpg|

### vivaldi.webpages.capture.capture_mode
Type: `enum`

Enum|Notes
---|---
fullpage|*Default*
area|

### vivaldi.webpages.capture.save_location
Type: `enum`

Enum|Notes
---|---
file|*Default*
clipboard|

### vivaldi.webpages.capture.save_file_pattern
The file pattern used to contruct the filename.

Type: `string`

Default: $timestamp $host $shortid

### vivaldi.webpages.focus_trap
Controls keyboard TAB focus trapping within individual UI toolbars and/or a webpage.

Type: `boolean`

Default: False

### vivaldi.webpages.full_screen.hide_mouse
Type: `boolean`

Default: None

### vivaldi.webpages.full_screen.show_bubble
Show an info bubble telling the user to use Esc to exit full screen.

Type: `boolean`

Default: True

### vivaldi.webpages.smooth_scrolling.enabled
Type: `boolean`

Default: True

### vivaldi.webpages.spatial_navigation_method
Type: `enum`

Enum|Notes
---|---
none|*Default*
vivaldi|
blink|

### vivaldi.webpages.tab_focuses_links
Type: `boolean`

Default: False

### vivaldi.webpages.tab_zoom.enabled
Type: `boolean`

Default: True

### vivaldi.welcome.seen_pages
Welcome pages marked as seen

Type: `list`

Default: []

### vivaldi.welcome.read_pages
Welcome pages marked as consumed

Type: `list`

Default: []

### vivaldi.rss.settings
List of settings for RSS feeds

Type: `list`

Default: []

### vivaldi.rss.show_notifications
Should new feeds notifications be shown

Type: `boolean`

Default: True

### vivaldi.windows.linux_alt_controls
Type: `boolean`

Default: False

### vivaldi.windows.use_native_decoration
Type: `boolean`

Default: False

### vivaldi.windows.size_cache
Type: `dictionary`

Default: {'width': 1200, 'height': 700}

### vivaldi.windows.show_window_close_confirmation_dialog
Type: `boolean`

Default: True

### vivaldi.system.desktop_theme_color
Type: `enum`

Enum|Notes
---|---
light|*Default*
dark|

### vivaldi.system.has_desktop_wallpaper_protocol
Type: `boolean`

Default: None

### vivaldi.system.show_exit_confirmation_dialog
Type: `boolean`

Default: True

### vivaldi.system.mac.action_on_double_click
Type: `string`

Default: None

### vivaldi.system.mac.aqua_color_variant
Type: `integer`

Default: None

### vivaldi.system.mac.interface_style
Type: `integer`

Default: None

### vivaldi.system.mac.keyboard_ui_mode
Type: `integer`

Default: None

### vivaldi.system.mac.swipe_scroll_direction
Type: `boolean`

Default: None

## Chromium Prefs
### alternate_error_pages.enabled
Type: `boolean`

Internal key: *kAlternateErrorPagesEnabled*

### browser.allow_javascript_apple_events
Type: `boolean`

Internal key: *kAllowJavascriptAppleEvents*

### credentials_enable_service
Type: `boolean`

Internal key: *kCredentialsEnableService*

### download.default_directory
Type: `file_path`

Internal key: *kDownloadDefaultDirectory*

### enable_do_not_track
Type: `boolean`

Internal key: *kEnableDoNotTrack*

### extensions.chrome_url_overrides
Type: `dictionary`

Internal key: *kExtensionURLOverrides*

### plugins.always_open_pdf_externally
Type: `boolean`

Internal key: *kPluginsAlwaysOpenPdfExternally*

### safebrowsing.enabled
Type: `boolean`

Internal key: *kSafeBrowsingEnabled*

### session.startup_urls
Type: `list`

Internal key: *kURLsToRestoreOnStartup*

### webkit.webprefs.fonts.cursive.Zyyy
Type: `string`

Internal key: *kWebKitCursiveFontFamily*

### webkit.webprefs.fonts.fantasy.Zyyy
Type: `string`

Internal key: *kWebKitFantasyFontFamily*

### webkit.webprefs.fonts.fixed.Zyyy
Type: `string`

Internal key: *kWebKitFixedFontFamily*

### webkit.webprefs.minimum_font_size
Type: `string`

Internal key: *kWebKitMinimumFontSize*

### webkit.webprefs.fonts.sansserif.Zyyy
Type: `string`

Internal key: *kWebKitSansSerifFontFamily*

### webkit.webprefs.fonts.serif.Zyyy
Type: `string`

Internal key: *kWebKitSerifFontFamily*

### webkit.webprefs.fonts.standard.Zyyy
Type: `string`

Internal key: *kWebKitStandardFontFamily*

### webrtc.ip_handling_policy
Type: `string`

Internal key: *kWebRTCIPHandlingPolicy*

### browser.confirm_to_quit
Type: `boolean`

Internal key: *kConfirmToQuitEnabled*

### hardware_acceleration_mode.enabled
Type: `boolean`

Internal key: *kHardwareAccelerationModeEnabled*
