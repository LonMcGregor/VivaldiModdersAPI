### vivaldi.accessKeys.action()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`string`|id|


### vivaldi.accessKeys.getAccessKeysForPage()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`function`|callback|


### vivaldi.autoUpdate.checkForUpdates()
Type | Argument | Notes
---|---|---
`boolean`|withUi|


### vivaldi.autoUpdate.disableUpdateNotifier()
Unknown arguments


### vivaldi.autoUpdate.enableUpdateNotifier()
Unknown arguments


### vivaldi.autoUpdate.isUpdateNotifierEnabled()
Type | Argument | Notes
---|---|---
`function`|callback|


### [Listener] vivaldi.bookmarkContextMenu.onClose



### [Listener] vivaldi.bookmarkContextMenu.onOpen



### vivaldi.bookmarkContextMenu.show()
Type | Argument | Notes
---|---|---
`object`|properties|
`function`|callback|


### [Enum] vivaldi.bookmarkContextMenu.SortField
Value | Notes
---|---
`DATEADDED`|
`DESCRIPTION`|
`NICKNAME`|
`TITLE`|
`URL`|


### [Enum] vivaldi.bookmarkContextMenu.SortOrder
Value | Notes
---|---
`ASCENDING`|
`DESCENDING`|


### [Listener] vivaldi.bookmarksPrivate.onMetaInfoChanged



### [Listener] vivaldi.bookmarksPrivate.onFaviconChanged



### vivaldi.bookmarksPrivate.emptyTrash()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.bookmarksPrivate.isCustomThumbnail()
Type | Argument | Notes
---|---|---
`string`|bookmarkId|
`function`|callback|


### vivaldi.bookmarksPrivate.updateSpeedDialsForWindowsJumplist()
Type | Argument | Notes
---|---|---
`array`|speedDials|


### vivaldi.bookmarksPrivate.upgradePartner()
Type | Argument | Notes
---|---|---
`string`|id|
`object`|changes|
`function`|callback|*(Optional)*


### [Listener] vivaldi.calendar.onCalendarChanged



### [Listener] vivaldi.calendar.onCalendarRemoved



### [Listener] vivaldi.calendar.onCalendarCreated



### [Listener] vivaldi.calendar.onEventTypeChanged



### [Listener] vivaldi.calendar.onEventTypeRemoved



### [Listener] vivaldi.calendar.onEventTypeCreated



### [Listener] vivaldi.calendar.onEventChanged



### [Listener] vivaldi.calendar.onEventRemoved



### [Listener] vivaldi.calendar.onEventCreated



### vivaldi.calendar.create()
Type | Argument | Notes
---|---|---
`calendar.CreateCalendarDetails`|calendar|
`function`|callback|*(Optional)*


### vivaldi.calendar.createEventException()
Type | Argument | Notes
---|---|---
`string`|parent_event_id|
`string`|exception_event_id|*(Optional)*
`boolean`|cancelled|
`number`|date|*(Optional)*
`function`|callback|*(Optional)*


### vivaldi.calendar.delete()
Type | Argument | Notes
---|---|---
`string`|id|
`function`|callback|*(Optional)*


### vivaldi.calendar.deleteEvent()
Type | Argument | Notes
---|---|---
`string`|id|
`function`|callback|*(Optional)*


### vivaldi.calendar.deleteEventType()
Type | Argument | Notes
---|---|---
`string`|id|
`function`|callback|*(Optional)*


### vivaldi.calendar.eventCreate()
Type | Argument | Notes
---|---|---
`calendar.CreateDetails`|event|
`function`|callback|*(Optional)*


### vivaldi.calendar.eventTypeCreate()
Type | Argument | Notes
---|---|---
`calendar.CreateEventType`|event|
`function`|callback|*(Optional)*


### vivaldi.calendar.eventTypeUpdate()
Type | Argument | Notes
---|---|---
`string`|id|
`object`|changes|


### vivaldi.calendar.eventsCreate()
Type | Argument | Notes
---|---|---
`array`|eventsList|
`function`|callback|*(Optional)*


### vivaldi.calendar.getAll()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.calendar.getAllEventTypes()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.calendar.getAllEvents()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.calendar.update()
Type | Argument | Notes
---|---|---
`string`|id|
`object`|changes|


### vivaldi.calendar.updateEvent()
Type | Argument | Notes
---|---|---
`string`|id|
`object`|changes|
`function`|callback|*(Optional)*


### [Enum] vivaldi.calendar.OccurrenceFrequency
Value | Notes
---|---
``|
`DAYS`|
`MONTHS`|
`WEEKS`|
`YEARS`|


### [Listener] vivaldi.contacts.onContactChanged



### [Listener] vivaldi.contacts.onContactRemoved



### [Listener] vivaldi.contacts.onContactCreated



### vivaldi.contacts.addEmailAddress()
Type | Argument | Notes
---|---|---
`contacts.EmailAddressAddUpdate`|emailToAdd|
`function`|callback|*(Optional)*


### vivaldi.contacts.addPropertyItem()
Type | Argument | Notes
---|---|---
`contacts.AddPropertyDetails`|propertyToAdd|
`function`|callback|*(Optional)*


### vivaldi.contacts.create()
Type | Argument | Notes
---|---|---
`contacts.CreateUpdateDetails`|contact|
`function`|callback|*(Optional)*


### vivaldi.contacts.createMany()
Type | Argument | Notes
---|---|---
`array`|contactList|
`function`|callback|*(Optional)*


### vivaldi.contacts.delete()
Type | Argument | Notes
---|---|---
`string`|id|
`function`|callback|*(Optional)*


### vivaldi.contacts.getAll()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.contacts.getAllEmailAddresses()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.contacts.removePropertyItem()
Type | Argument | Notes
---|---|---
`contacts.RemovePropertyDetails`|propertyToRemove|
`function`|callback|*(Optional)*


### vivaldi.contacts.update()
Type | Argument | Notes
---|---|---
`string`|id|
`contacts.CreateUpdateDetails`|changes|
`function`|callback|*(Optional)*


### vivaldi.contacts.updateEmailAddress()
Type | Argument | Notes
---|---|---
`string`|emailAddressId|
`contacts.EmailAddressAddUpdate`|emailToUpdate|
`function`|callback|*(Optional)*


### vivaldi.contacts.updatePropertyItem()
Type | Argument | Notes
---|---|---
`contacts.UpdatePropertyDetails`|propertyToUpdate|
`function`|callback|*(Optional)*


### [Enum] vivaldi.contacts.ContactPropertyName
Value | Notes
---|---
`PHONE_NUMBER`|
`POSTAL_ADDRESS`|


### vivaldi.contextMenu.show()
Type | Argument | Notes
---|---|---
`object`|properties|
`function`|callback|


### [Enum] vivaldi.contextMenu.ExpandType
Value | Notes
---|---
`PWA`|


### [Enum] vivaldi.contextMenu.Origin
Value | Notes
---|---
`BOTTOM_LEFT`|
`BOTTOM_RIGHT`|
`POINTER`|
`TOP_LEFT`|
`TOP_RIGHT`|


### [Listener] vivaldi.devtoolsPrivate.onDevtoolsUndocked



### [Listener] vivaldi.devtoolsPrivate.onClosed



### [Listener] vivaldi.devtoolsPrivate.onDockingSizesChanged



### [Listener] vivaldi.devtoolsPrivate.onDockingStateChanged



### vivaldi.devtoolsPrivate.closeDevtools()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`integer`|windowId|*(Optional)*
`function`|callback|


### vivaldi.devtoolsPrivate.getDockingStateSizes()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`function`|callback|


### vivaldi.devtoolsPrivate.toggleDevtools()
Type | Argument | Notes
---|---|---
`devtoolsPrivate.PanelType`|panelType|


### [Enum] vivaldi.devtoolsPrivate.PanelType
Value | Notes
---|---
`CONSOLE`|
`DEFAULT`|
`INSPECT`|


### [Listener] vivaldi.extensionActionUtils.onIconLoaded



### [Listener] vivaldi.extensionActionUtils.onCommandRemoved



### [Listener] vivaldi.extensionActionUtils.onCommandAdded



### [Listener] vivaldi.extensionActionUtils.onUpdated



### [Listener] vivaldi.extensionActionUtils.onRemoved



### [Listener] vivaldi.extensionActionUtils.onAdded



### vivaldi.extensionActionUtils.executeExtensionAction()
Type | Argument | Notes
---|---|---
`string`|extensionId|
`integer`|windowId|
`function`|showPopup|


### vivaldi.extensionActionUtils.getToolbarExtensions()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.extensionActionUtils.removeExtension()
Type | Argument | Notes
---|---|---
`string`|extensionId|
`integer`|windowId|


### vivaldi.extensionActionUtils.showExtensionOptions()
Type | Argument | Notes
---|---|---
`string`|extensionId|
`integer`|windowId|


### vivaldi.extensionActionUtils.toggleBrowserActionVisibility()
Type | Argument | Notes
---|---|---
`string`|extensionId|


### [Enum] vivaldi.extensionActionUtils.ActionType
Value | Notes
---|---
`BROWSER`|
`PAGE`|


### [Enum] vivaldi.extensionActionUtils.ExtensionType
Value | Notes
---|---
`COMPONENT_ACTION`|
`EXTENSION_ACTION`|


### [Listener] vivaldi.historyPrivate.onVisitModified



### vivaldi.historyPrivate.dbSearch()
Type | Argument | Notes
---|---|---
`object`|query|
`function`|callback|


### vivaldi.historyPrivate.deleteAllSearchTermsForKeyword()
Type | Argument | Notes
---|---|---
`integer`|keywordId|


### vivaldi.historyPrivate.deleteVisits()
Type | Argument | Notes
---|---|---
`object`|details|
`function`|callback|*(Optional)*


### vivaldi.historyPrivate.getTopUrlsPerDay()
Type | Argument | Notes
---|---|---
`number`|maxTopUrlResults|
`function`|callback|


### vivaldi.historyPrivate.getTypedHistory()
Type | Argument | Notes
---|---|---
`string`|query|
`integer`|prefixKeywordId|
`integer`|max_results|
`function`|callback|


### vivaldi.historyPrivate.migrateOldTypedUrl()
Type | Argument | Notes
---|---|---
`string`|url|
`number`|time|
`historyPrivate.TransitionType`|transitionType|


### vivaldi.historyPrivate.search()
Type | Argument | Notes
---|---|---
`object`|query|
`function`|callback|


### vivaldi.historyPrivate.setKeywordSearchTermsForURL()
Type | Argument | Notes
---|---|---
`string`|url|
`integer`|keywordId|
`string`|searchTerms|


### vivaldi.historyPrivate.visitSearch()
Type | Argument | Notes
---|---|---
`object`|query|
`function`|callback|


### [Enum] vivaldi.historyPrivate.HistoryResultSetGrouping
Value | Notes
---|---
`KEEP_ALL_DUPLICATES`|
`REMOVE_ALL_DUPLICATES`|
`REMOVE_DUPLICATES_PER_DAY`|


### [Enum] vivaldi.historyPrivate.TransitionType
Value | Notes
---|---
`AUTO_BOOKMARK`|
`AUTO_SUBFRAME`|
`AUTO_TOPLEVEL`|
`FORM_SUBMIT`|
`GENERATED`|
`KEYWORD`|
`KEYWORD_GENERATED`|
`LINK`|
`MANUAL_SUBFRAME`|
`RELOAD`|
`TYPED`|


### [Listener] vivaldi.importData.onImportItemFailed



### [Listener] vivaldi.importData.onImportItemEnded



### [Listener] vivaldi.importData.onImportItemStarted



### [Listener] vivaldi.importData.onImportEnded



### [Listener] vivaldi.importData.onImportStarted



### vivaldi.importData.getProfiles()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.importData.startImport()
Type | Argument | Notes
---|---|---
`array`|itemsToImport|
`string`|masterPassword|*(Optional)*
`function`|callback|


### [Listener] vivaldi.infobars.onInfobarRemoved



### [Listener] vivaldi.infobars.onInfobarCreated



### vivaldi.infobars.sendButtonAction()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`integer`|identifier|
`string`|action|


### [Enum] vivaldi.infobars.ButtonAction
Value | Notes
---|---
`ACCEPT`|
`CANCEL`|
`DISMISS`|
`LINK`|


### vivaldi.mailPrivate.createDataDirectory()
Type | Argument | Notes
---|---|---
`string`|hashedAccountId|
`function`|callback|*(Optional)*


### vivaldi.mailPrivate.delete()
Type | Argument | Notes
---|---|---
`array`|paths|
`string`|fileName|
`function`|callback|*(Optional)*


### vivaldi.mailPrivate.getDataDirectory()
Type | Argument | Notes
---|---|---
`string`|hashedAccountId|
`function`|callback|*(Optional)*


### vivaldi.mailPrivate.getPaths()
Type | Argument | Notes
---|---|---
`array`|paths|
`function`|callback|*(Optional)*


### vivaldi.mailPrivate.read()
Type | Argument | Notes
---|---|---
`array`|paths|
`string`|fileName|
`function`|callback|*(Optional)*


### vivaldi.mailPrivate.readBuffer()
Type | Argument | Notes
---|---|---
`array`|paths|
`string`|fileName|
`function`|callback|*(Optional)*


### vivaldi.mailPrivate.readFile()
Type | Argument | Notes
---|---|---
`string`|path|
`function`|callback|*(Optional)*


### vivaldi.mailPrivate.rename()
Type | Argument | Notes
---|---|---
`array`|paths|
`string`|fileName|
`string`|newFileName|
`function`|callback|*(Optional)*


### vivaldi.mailPrivate.save()
Type | Argument | Notes
---|---|---
`array`|paths|
`string`|fileName|
`string`|raw|
`function`|callback|*(Optional)*


### vivaldi.mailPrivate.saveBuffer()
Type | Argument | Notes
---|---|---
`array`|paths|
`string`|fileName|
`binary`|raw|
`function`|callback|*(Optional)*


### [Listener] vivaldi.menubar.onActivated



### vivaldi.menubar.setup()
Type | Argument | Notes
---|---|---
`array`|items|
`menubar.Mode`|mode|


### [Enum] vivaldi.menubar.Mode
Value | Notes
---|---
`ALL`|
`TABS`|
`UPDATE`|


### [Listener] vivaldi.menubarMenu.onError



### [Listener] vivaldi.menubarMenu.onHover



### [Listener] vivaldi.menubarMenu.onBookmarkAction



### [Listener] vivaldi.menubarMenu.onOpenBookmark



### [Listener] vivaldi.menubarMenu.onAction



### [Listener] vivaldi.menubarMenu.onClose



### [Listener] vivaldi.menubarMenu.onOpen



### vivaldi.menubarMenu.show()
Type | Argument | Notes
---|---|---
`object`|properties|
`function`|callback|


### [Enum] vivaldi.menubarMenu.BookmarkCommand
Value | Notes
---|---
`ADDACTIVETAB`|
`ADDBOOKMARK`|
`ADDFOLDER`|
`COPY`|
`CUT`|
`EDIT`|
`PASTE`|


### [Enum] vivaldi.menubarMenu.ContainerType
Value | Notes
---|---
`BOOKMARKS`|
`HISTORY`|


### [Enum] vivaldi.menubarMenu.Disposition
Value | Notes
---|---
`CURRENT`|
`NEW_PRIVATE_WINDOW`|
`NEW_TAB`|
`NEW_WINDOW`|
`SETTING`|


### [Enum] vivaldi.menubarMenu.ItemType
Value | Notes
---|---
`CHECKBOX`|
`NORMAL`|
`RADIOBUTTON`|


### [Enum] vivaldi.menubarMenu.SortField
Value | Notes
---|---
`DATEADDED`|
`DESCRIPTION`|
`NICKNAME`|
`TITLE`|
`URL`|


### [Enum] vivaldi.menubarMenu.SortOrder
Value | Notes
---|---
`ASCENDING`|
`DESCENDING`|


### [Listener] vivaldi.notes.onImportEnded



### [Listener] vivaldi.notes.onImportBegan



### [Listener] vivaldi.notes.onMoved



### [Listener] vivaldi.notes.onChanged



### [Listener] vivaldi.notes.onRemoved



### [Listener] vivaldi.notes.onCreated



### vivaldi.notes.create()
Type | Argument | Notes
---|---|---
`notes.CreateDetails`|note|
`function`|callback|*(Optional)*


### vivaldi.notes.emptyTrash()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.notes.get()
Type | Argument | Notes
---|---|---
`[string|array]`|idOrIdList|
`function`|callback|


### vivaldi.notes.getTree()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.notes.move()
Type | Argument | Notes
---|---|---
`string`|id|
`object`|destination|
`function`|callback|*(Optional)*


### vivaldi.notes.remove()
Type | Argument | Notes
---|---|---
`string`|id|
`function`|callback|*(Optional)*


### vivaldi.notes.search()
Type | Argument | Notes
---|---|---
`string`|query|
`function`|callback|


### vivaldi.notes.update()
Type | Argument | Notes
---|---|---
`string`|id|
`object`|changes|
`function`|callback|*(Optional)*


### [Listener] vivaldi.prefs.onChanged



### vivaldi.prefs.get()
Type | Argument | Notes
---|---|---
`string`|path|
`function`|callback|


### vivaldi.prefs.getForCache()
Type | Argument | Notes
---|---|---
`array`|paths|
`function`|callback|*(Optional)*


### vivaldi.prefs.reset()
Type | Argument | Notes
---|---|---
`string`|path|
`function`|callback|


### vivaldi.prefs.set()
Type | Argument | Notes
---|---|---
`prefs.PreferenceValue`|newValue|


### [Listener] vivaldi.runtimePrivate.onProfilesUpdated



### vivaldi.runtimePrivate.closeActiveProfile()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.runtimePrivate.closeGuestSession()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.runtimePrivate.createProfile()
Type | Argument | Notes
---|---|---
`string`|name|
`string`|avatarUrl|
`boolean`|createDesktopIcon|
`function`|callback|


### vivaldi.runtimePrivate.deleteProfile()
Type | Argument | Notes
---|---|---
`string`|profilePath|
`function`|callback|


### vivaldi.runtimePrivate.exit()
Quits Vivaldi


### vivaldi.runtimePrivate.getAllFeatureFlags()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.runtimePrivate.getProfileDefaults()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.runtimePrivate.getProfileStatistics()
Type | Argument | Notes
---|---|---
`string`|profilePath|
`function`|callback|


### vivaldi.runtimePrivate.getUserProfileImages()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.runtimePrivate.getUserProfiles()
Type | Argument | Notes
---|---|---
`integer`|avatarWidth|
`integer`|avatarHeight|
`function`|callback|


### vivaldi.runtimePrivate.hasDesktopShortcut()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.runtimePrivate.hasGuestSession()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.runtimePrivate.isGuestSession()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.runtimePrivate.openNamedProfile()
Type | Argument | Notes
---|---|---
`string`|profilePath|
`function`|callback|


### vivaldi.runtimePrivate.openProfileSelectionWindow()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.runtimePrivate.setFeatureEnabled()
Type | Argument | Notes
---|---|---
`string`|featureName|
`boolean`|enable|
`function`|callback|


### vivaldi.runtimePrivate.switchToGuestSession()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.runtimePrivate.updateActiveProfile()
Type | Argument | Notes
---|---|---
`string`|name|
`integer`|avatarIndex|
`boolean`|createDesktopIcon|*(Optional)*
`function`|callback|


### vivaldi.savedpasswords.add()
Type | Argument | Notes
---|---|---
`boolean`|isExplicit|
`savedpasswords.PasswordForm`|passwordForm|


### vivaldi.savedpasswords.authenticate()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.savedpasswords.delete()
Type | Argument | Notes
---|---|---
`boolean`|isExplicit|
`savedpasswords.PasswordForm`|passwordForm|


### vivaldi.savedpasswords.get()
Type | Argument | Notes
---|---|---
`boolean`|isExplicit|
`savedpasswords.PasswordForm`|passwordForm|
`function`|callback|


### vivaldi.savedpasswords.getList()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.savedpasswords.remove()
Type | Argument | Notes
---|---|---
`string`|id|
`function`|callback|*(Optional)*


### vivaldi.sessionsPrivate.delete()
Type | Argument | Notes
---|---|---
`string`|name|
`function`|callback|


### vivaldi.sessionsPrivate.getAll()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.sessionsPrivate.open()
Type | Argument | Notes
---|---|---
`string`|name|
`sessionsPrivate.SessionOpenOptions`|options|*(Optional)*
`function`|callback|*(Optional)*


### vivaldi.sessionsPrivate.saveOpenTabs()
Type | Argument | Notes
---|---|---
`string`|name|
`sessionsPrivate.SessionSaveOptions`|options|
`function`|callback|


### vivaldi.settings.setContentSetting()
Type | Argument | Notes
---|---|---
`settings.ContentSettingItem`|settingsItem|


### [Enum] vivaldi.settings.ContentSettingEnum
Value | Notes
---|---
`ALLOW`|
`ASK`|
`BLOCK`|
`DETECT_IMPORTANT_CONTENT`|
`NUM_SETTINGS`|
`SESSION_ONLY`|


### [Enum] vivaldi.settings.ContentSettingsTypeEnum
Value | Notes
---|---
`GEOLOCATION`|
`NOTIFICATIONS`|
`PLUGINS`|
`POPUPS`|


### [Listener] vivaldi.sync.onCycleCompleted



### [Listener] vivaldi.sync.onEngineStateChanged



### vivaldi.sync.clearData()
Unknown arguments


### vivaldi.sync.getDefaultSessionName()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.sync.getEngineState()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.sync.getLastCycleState()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.sync.notificationReceived()
Type | Argument | Notes
---|---|---
`string`|client_id|
`string`|notification_type|
`string`|version|


### vivaldi.sync.setEncryptionPassword()
Type | Argument | Notes
---|---|---
`string`|password|*(Optional)*
`function`|callback|


### vivaldi.sync.setTypes()
Type | Argument | Notes
---|---|---
`boolean`|syncEverything|
`array`|types|


### vivaldi.sync.setupComplete()
Unknown arguments


### vivaldi.sync.start()
Unknown arguments


### vivaldi.sync.stop()
Unknown arguments


### vivaldi.sync.updateNotificationClientStatus()
Type | Argument | Notes
---|---|---
`sync.SyncNotificationClientStatus`|status|


### [Enum] vivaldi.sync.ClientAction
Value | Notes
---|---
`DISABLE_SYNC_ON_CLIENT`|
`RESET_LOCAL_SYNC_DATA`|
`STOP_SYNC_FOR_DISABLED_ACCOUNT`|
`UNKNOWN`|
`UPGRADE_CLIENT`|


### [Enum] vivaldi.sync.DataType
Value | Notes
---|---
`AUTOFILL`|
`BOOKMARKS`|
`EXTENSIONS`|
`NOTES`|
`PASSWORDS`|
`PREFERENCES`|
`TYPED_URLS`|


### [Enum] vivaldi.sync.DisableReason
Value | Notes
---|---
`ENTERPRISE_POLICY`|
`FLAG`|
`NOT_SIGNED_IN`|
`PLATFORM_OVERRIDE`|
`UNRECOVERABLE_ERROR`|
`USER_CHOICE`|


### [Enum] vivaldi.sync.EngineState
Value | Notes
---|---
`CLEARING_DATA`|
`CONFIGURATION_PENDING`|
`FAILED`|
`STARTED`|
`STARTING`|
`STARTING_SERVER_ERROR`|
`STOPPED`|


### [Enum] vivaldi.sync.ProtocolErrorType
Value | Notes
---|---
`CLEAR_PENDING`|
`CLIENT_DATA_OBSOLETE`|
`DISABLED_BY_ADMIN`|
`MIGRATION_DONE`|
`NOT_MY_BIRTHDAY`|
`PARTIAL_FAILURE`|
`SUCCESS`|
`THROTTLED`|
`TRANSIENT_ERROR`|
`UNKNOWN`|


### [Enum] vivaldi.sync.SyncNotificationClientStatus
Value | Notes
---|---
`CONNECTED`|
`DISCONNECTED`|


### [Enum] vivaldi.sync.SyncerError
Value | Notes
---|---
`CANNOT_DO_WORK`|
`DATATYPE_TRIGGERED_RETRY`|
`NETWORK_CONNECTION_UNAVAILABLE`|
`NETWORK_IO_ERROR`|
`SERVER_MORE_TO_DOWNLOAD`|
`SERVER_RESPONSE_VALIDATION_FAILED`|
`SERVER_RETURN_CLEAR_PENDING`|
`SERVER_RETURN_CLIENT_DATA_OBSOLETE`|
`SERVER_RETURN_CONFLICT`|
`SERVER_RETURN_DISABLED_BY_ADMIN`|
`SERVER_RETURN_INVALID_CREDENTIAL`|
`SERVER_RETURN_MIGRATION_DONE`|
`SERVER_RETURN_NOT_MY_BIRTHDAY`|
`SERVER_RETURN_PARTIAL_FAILURE`|
`SERVER_RETURN_THROTTLED`|
`SERVER_RETURN_TRANSIENT_ERROR`|
`SERVER_RETURN_UNKNOWN_ERROR`|
`SERVER_RETURN_USER_ROLLBACK`|
`SYNC_AUTH_ERROR`|
`SYNC_SERVER_ERROR`|
`SYNCER_OK`|
`UNSET`|


### [Listener] vivaldi.tabsPrivate.onPageZoom



### [Listener] vivaldi.tabsPrivate.onWebviewClickCheck



### [Listener] vivaldi.tabsPrivate.onRockerGesture



### [Listener] vivaldi.tabsPrivate.onTabSwitchEnd



### [Listener] vivaldi.tabsPrivate.onMouseGesture



### [Listener] vivaldi.tabsPrivate.onMouseGestureDetection



### [Listener] vivaldi.tabsPrivate.onTabIsAttached



### [Listener] vivaldi.tabsPrivate.onTabIsDetached



### [Listener] vivaldi.tabsPrivate.onKeyboardShortcut



### [Listener] vivaldi.tabsPrivate.onKeyboardChanged



### [Listener] vivaldi.tabsPrivate.onPermissionAccessed



### [Listener] vivaldi.tabsPrivate.onDragEnd



### [Listener] vivaldi.tabsPrivate.onTabUpdated



### [Listener] vivaldi.tabsPrivate.onThemeColorChanged



### [Listener] vivaldi.tabsPrivate.onMediaStateChanged



### vivaldi.tabsPrivate.get()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`function`|callback|*(Optional)*


### vivaldi.tabsPrivate.insertText()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`string`|text|


### vivaldi.tabsPrivate.scrollPage()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`string`|scrollType|
`function`|callback|


### vivaldi.tabsPrivate.startDrag()
Type | Argument | Notes
---|---|---
`tabsPrivate.DragData`|dragData|


### vivaldi.tabsPrivate.update()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`tabsPrivate.UpdateTabInfo`|tabInfo|


### [Enum] vivaldi.tabsPrivate.MediaType
Value | Notes
---|---
`BLUETOOTH`|
`CAPTURING`|
`DESKTOP_CAPTURING`|
`EMPTY`|
`MUTING`|
`PIP`|
`PLAYING`|
`RECORDING`|
`SERIAL_CONNECTED`|
`USB`|
`VR_PRESENTING_IN_HEADSET`|


### vivaldi.thumbnails.captureTab()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`thumbnails.CaptureTabParams`|params|
`function`|callback|


### vivaldi.thumbnails.captureUI()
Type | Argument | Notes
---|---|---
`thumbnails.CaptureUIParams`|params|
`function`|callback|


### vivaldi.thumbnails.captureUrl()
Type | Argument | Notes
---|---|---
`thumbnails.CaptureUrlParams`|params|
`function`|callback|


### [Listener] vivaldi.utilities.onRazerChromaReady



### [Listener] vivaldi.utilities.onDownloadManagerReady



### [Listener] vivaldi.utilities.onPasswordIconStatusChanged



### [Listener] vivaldi.utilities.onResume



### [Listener] vivaldi.utilities.onSuspend



### [Listener] vivaldi.utilities.onSharedDataUpdated



### [Listener] vivaldi.utilities.onScroll



### vivaldi.utilities.canShowWelcomePage()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.canShowWhatsNewPage()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.clearAllRecentlyClosedSessions()
Unknown arguments


### vivaldi.utilities.getBlockThirdPartyCookies()
Type | Argument | Notes
---|---|---
`function`|blockThirdParty|


### vivaldi.utilities.getDefaultContentSettings()
Type | Argument | Notes
---|---|---
`string`|contentSetting|
`function`|callback|


### vivaldi.utilities.getLanguage()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.getSelectedText()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`function`|callback|


### vivaldi.utilities.getSharedData()
Type | Argument | Notes
---|---|---
`utilities.SharedDataValue`|keyValuePair|
`function`|callback|*(Optional)*


### vivaldi.utilities.getStartupAction()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.getSystemDateFormat()
Unknown arguments


### vivaldi.utilities.getUniqueUserId()
Type | Argument | Notes
---|---|---
`string`|legacyUserId|
`function`|callback|


### vivaldi.utilities.getVersion()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.isDownloadManagerReady()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.isRazerChromaAvailable()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.isRazerChromaReady()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.isTabInLastSession()
Type | Argument | Notes
---|---|---
`integer`|tabId|
`function`|callback|


### vivaldi.utilities.isUrlValid()
Type | Argument | Notes
---|---|---
`string`|url|
`function`|callback|


### vivaldi.utilities.isVivaldiDefaultBrowser()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.launchNetworkSettings()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.openPage()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.openTaskManager()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.print()
Type | Argument | Notes
---|---|---
`integer`|tabId|


### vivaldi.utilities.savePage()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.selectFile()
Type | Argument | Notes
---|---|---
`array`|accepts|*(Optional)*
`string`|title|*(Optional)*
`utilities.SelectFileDialogType`|type|
`function`|callback|


### vivaldi.utilities.selectLocalImage()
Type | Argument | Notes
---|---|---
`utilities.SelectLocalImageParams`|params|
`function`|callback|*(Optional)*


### vivaldi.utilities.setBlockThirdPartyCookies()
Type | Argument | Notes
---|---|---
`boolean`|block3rdParty|
`function`|callback|


### vivaldi.utilities.setDefaultContentSettings()
Type | Argument | Notes
---|---|---
`string`|contentSetting|
`string`|value|
`function`|callback|


### vivaldi.utilities.setDialogPosition()
Type | Argument | Notes
---|---|---
`utilities.DialogName`|dialogName|
`integer`|windowId|
`object`|position|
`utilities.FlowDirection`|flowDirection|
`function`|callback|


### vivaldi.utilities.setLanguage()
Type | Argument | Notes
---|---|---
`string`|locale|
`function`|callback|


### vivaldi.utilities.setRazerChromaColor()
Type | Argument | Notes
---|---|---
`array`|colors|
`function`|callback|


### vivaldi.utilities.setSharedData()
Type | Argument | Notes
---|---|---
`utilities.SharedDataValue`|keyValuePair|
`function`|callback|*(Optional)*


### vivaldi.utilities.setStartupAction()
Type | Argument | Notes
---|---|---
`string`|startup|
`array`|urls|
`function`|callback|


### vivaldi.utilities.setVivaldiAsDefaultBrowser()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.utilities.showPasswordDialog()
Invokes OS Password Authenticator


### [Enum] vivaldi.utilities.DialogName
Value | Notes
---|---
`CHROMECAST`|
`PASSWORD`|


### [Enum] vivaldi.utilities.FlowDirection
Value | Notes
---|---
`DOWN`|
`UP`|


### [Enum] vivaldi.utilities.SelectFileDialogType
Value | Notes
---|---
`FILE`|
`FOLDER`|


### [Listener] vivaldi.vivaldiAccount.onAccountStateChanged



### vivaldi.vivaldiAccount.getState()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.vivaldiAccount.login()
Type | Argument | Notes
---|---|---
`string`|username|
`string`|password|
`boolean`|savePassword|


### vivaldi.vivaldiAccount.logout()
Unknown arguments


### [Enum] vivaldi.vivaldiAccount.FetchErrorType
Value | Notes
---|---
`INVALID_CREDENTIALS`|
`NETWORK_ERROR`|
`NO_ERROR`|
`SERVER_ERROR`|


### [Listener] vivaldi.windowPrivate.onActiveTabStatusText



### [Listener] vivaldi.windowPrivate.onWindowClosed



### [Listener] vivaldi.windowPrivate.onWindowCreated



### [Listener] vivaldi.windowPrivate.onBeforeUnloadDialogOpened



### [Listener] vivaldi.windowPrivate.onWindowCloseCancelled



### [Listener] vivaldi.windowPrivate.onFullscreenMenubarChanged



### [Listener] vivaldi.windowPrivate.onFullscreen



### [Listener] vivaldi.windowPrivate.onActivated



### [Listener] vivaldi.windowPrivate.onPositionChanged



### [Listener] vivaldi.windowPrivate.onMaximized



### [Listener] vivaldi.windowPrivate.onMinimized



### vivaldi.windowPrivate.create()
Type | Argument | Notes
---|---|---
`string`|url|
`windowPrivate.CreateWindowOptions`|options|
`windowPrivate.WindowType`|type|*(Optional)*
`function`|callback|*(Optional)*


### vivaldi.windowPrivate.getCurrentId()
Type | Argument | Notes
---|---|---
`function`|callback|


### vivaldi.windowPrivate.setState()
Type | Argument | Notes
---|---|---
`integer`|windowId|
`windowPrivate.WindowState`|state|


### [Enum] vivaldi.windowPrivate.WindowState
Value | Notes
---|---
`FULLSCREEN`|
`MAXIMIZED`|
`MINIMIZED`|
`NORMAL`|


### [Enum] vivaldi.windowPrivate.WindowType
Value | Notes
---|---
`NORMAL`|
`SETTINGS`|


### [Listener] vivaldi.zoom.onUIZoomChanged



### [Listener] vivaldi.zoom.onDefaultZoomChanged



### vivaldi.zoom.getDefaultZoom()
Type | Argument | Notes
---|---|---
`function`|zoomLevel|


### vivaldi.zoom.getVivaldiUIZoom()
Type | Argument | Notes
---|---|---
`function`|zoomLevel|


### vivaldi.zoom.setDefaultZoom()
Type | Argument | Notes
---|---|---
`number`|zoomFactor|
`function`|callback|*(Optional)*


### vivaldi.zoom.setVivaldiUIZoom()
Type | Argument | Notes
---|---|---
`number`|zoomFactor|
`function`|callback|*(Optional)*
