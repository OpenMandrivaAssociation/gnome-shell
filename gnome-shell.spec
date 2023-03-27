%define _disable_rebuild_configure 1
%define url_ver %(echo %{version}|cut -d. -f1,2)
# To make GNOME Shell extensions load, we need to get rid of DT_RUNPATH on /usr/bin/gnome-shell
# (see glibc bug #13945, GNOME bug #670477, Mageia bug #4523)
%define _disable_ld_enable_new_dtags 1
#define debug_package %{nil}

%global systemd_units gnome-shell.service

Summary:	Next generation GNOME desktop shell
Name:		gnome-shell
Version:	44.0
Release:	1
License:	GPLv2+ and LGPLv2+
Group:		Graphical desktop/GNOME
Url:		http://live.gnome.org/GnomeShell
Source0:	http://ftp.gnome.org/pub/GNOME/sources/gnome-shell/%{url_ver}/%{name}-%{version}.tar.xz

# Mandriva patches
# Looks like it is still requires because soup3 is still pulled even when we compile g-s with soup2.
# Anyway no big issue right now, as we already (from gnome 42) have in repo soup3.
# https://gitlab.gnome.org/GNOME/gnome-shell/-/issues/4646
#Patch0:         gnome-shell-41.0-dirty-fix-for-stop-requiring-soup3-mandriva.patch

# From Fedora
Patch1:          gnome-shell-favourite-apps-firefox.patch

# Backported from upstream

BuildRequires:  a2x
BuildRequires:	gtk-doc
BuildRequires:  gjs
BuildRequires:	intltool >= 0.40
BuildRequires:	rootcerts
BuildRequires:	xsltproc
BuildRequires:	pkgconfig(caribou-1.0)
BuildRequires:	pkgconfig(clutter-1.0)
BuildRequires:	pkgconfig(clutter-glx-1.0) >= 1.7.5
BuildRequires:	pkgconfig(clutter-x11-1.0) >= 1.7.5
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:	pkgconfig(folks) >= 0.5.2
BuildRequires:	pkgconfig(dbus-glib-1)
BuildRequires:	pkgconfig(gcr-4)
BuildRequires:	pkgconfig(gdk-pixbuf-2.0)
BuildRequires:	pkgconfig(gdk-x11-3.0)
BuildRequires:	pkgconfig(gio-unix-2.0) >= 2.31.6
BuildRequires:	pkgconfig(gl)
BuildRequires:  pkgconfig(gnome-autoar-0)
BuildRequires:	pkgconfig(gnome-bluetooth-3.0)
BuildRequires:	pkgconfig(gnome-desktop-3.0)
BuildRequires:	pkgconfig(gnome-keyring-1)
# NOT READY YET
#BuildRequires:	pkgconfig(gnome-keybindings)
BuildRequires:	pkgconfig(gobject-2.0)
BuildRequires:	pkgconfig(gobject-introspection-1.0) >= 1.45.3
BuildRequires:	pkgconfig(gsettings-desktop-schemas)
BuildRequires:	pkgconfig(gstreamer-1.0) >= 0.11.92
BuildRequires:	pkgconfig(gstreamer-plugins-base-1.0)
BuildRequires:	pkgconfig(gtk4)
BuildRequires:	pkgconfig(gtk-doc)
BuildRequires:	pkgconfig(ibus-1.0)
BuildRequires:	pkgconfig(libcanberra)
BuildRequires:	pkgconfig(libecal-2.0)
BuildRequires:	pkgconfig(libedataserver-1.2) >= 1.2.0
BuildRequires:	pkgconfig(libgnome-menu-3.0) >= 3.6.0
BuildRequires:  pkgconfig(libmutter-11)
BuildRequires:  pkgconfig(mutter-clutter-11)
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(libpulse)
BuildRequires:	pkgconfig(libpulse-mainloop-glib)
BuildRequires:	pkgconfig(libsoup-3.0)
BuildRequires:	pkgconfig(libxml-2.0)
BuildRequires:  pkgconfig(libpipewire-0.3) 
BuildRequires:	pkgconfig(polkit-agent-1) >= 0.100
BuildRequires:	pkgconfig(polkit-gobject-1)
BuildRequires:	pkgconfig(systemd)
BuildRequires:	pkgconfig(telepathy-glib)
BuildRequires:	pkgconfig(telepathy-logger-0.2)
BuildRequires:	pkgconfig(x11)
BuildRequires:	pkgconfig(xfixes)
BuildRequires:	gettext-devel

BuildRequires:  meson
BuildRequires:  pkgconfig(ibus-1.0)
BuildRequires:  pkgconfig(gjs-1.0)
BuildRequires:  pkgconfig(python3)
BuildRequires:  pkgconfig(libcroco-0.6)
BuildRequires:  pkgconfig(libcanberra-gtk3)
BuildRequires:  pkgconfig(libstartup-notification-1.0)
BuildRequires:  pkgconfig(libnm)
BuildRequires:  sassc
BuildRequires:  egl-devel

Requires:	at-spi2-atk
Requires:	gjs
Requires:	glxinfo
Requires:	gnome-session
Requires:	adwaita-icon-theme
Requires:	gnome-settings-daemon
Requires:	gsettings-desktop-schemas
Requires:	packagekit-gtk3-module
Requires:	telepathy-mission-control
Requires:	gnome-control-center
Requires:	libgnomekbd-common
# Optional 
Recommends:	chrome-gnome-shell
Recommends: gnome-tweaks
Requires:	gdm
Requires:	unzip

Provides:	virtual-notification-daemon
Provides:	polkit-agent

Requires:	gtk+3.0
Requires:	json-glib
Requires:	librsvg
Requires:	mutter
Requires:	pipewire

# TYPELIBS #
# Looks like typelibs generator is broken for Cooker, so all needed gir packages should be added below
# omv bug https://issues.openmandriva.org/show_bug.cgi?id=2534

Requires:	typelib(AccountsService)
Requires:	typelib(Atk)
Requires:	typelib(Atspi)
Requires:	typelib(Cally)
Requires:	typelib(Clutter)
Requires:	typelib(ClutterX11)
Requires:	typelib(Cogl)
Requires:	typelib(CoglPango)
Requires:       typelib(DBus)
Requires:	typelib(GDesktopEnums)
Requires:	typelib(GL)
Requires:	typelib(GLib)
Requires:	typelib(GModule)
Requires:	typelib(GObject)
Requires:	typelib(GWeather)
Requires:	typelib(Gck)
Requires:	typelib(Gcr)
Requires:	typelib(Gdk)
Requires:	typelib(GdkPixbuf)
#Requires:      typelib(GdPrivate)
Requires:	typelib(Gdm)
Requires:	typelib(Geoclue)
Requires:	typelib(Gio)
Requires:	typelib(GnomeBluetooth)
Requires:	typelib(GnomeDesktop)
Requires:	typelib(Gtk)
Requires:       typelib(GtkClutter)
#Requires:	typelib(Gvc)
Requires:       typelib(Graphene)
Requires:	typelib(IBus)
Requires:	typelib(Json)
#Requires:	typelib(Meta)
Requires:	typelib(NM)
Requires:	typelib(NMA)
Requires:	typelib(Pango)
Requires:	typelib(PangoCairo)
Requires:	typelib(Polkit)
Requires:	typelib(PolkitAgent)
Requires:       typelib(Rsvg)
#Requires:	typelib(Shell)
Requires:	typelib(Soup)
#Requires:	typelib(St)
Requires:	typelib(TelepathyGLib)
Requires:	typelib(TelepathyLogger)
Requires:	typelib(UPowerGlib)
Requires:	typelib(cairo)
Requires:	typelib(xfixes)
Requires:	typelib(xlib)

#Dirty fix
Requires: %{_lib}handy-gir1

%description
The GNOME Shell redefines user interactions with the GNOME desktop. In
particular, it offers new paradigms for launching applications,
accessing documents, and organizing open windows in GNOME. Later, it
will introduce a new applets eco-system and offer new solutions for
other desktop features, such as notifications and contacts
management. The GNOME Shell is intended to replace functions handled
by the GNOME Panel and by the window manager in previous versions of
GNOME. The GNOME Shell has rich visual effects enabled by new
graphical technologies.

%package docs
Summary:	Documentation for %{name}
Group:		Books/Computer books
BuildArch:	noarch

%description docs
This package contains the documentation for %{name}.

%prep
%setup -q
%autopatch -p1

%build
%meson \
        -Dgtk_doc=true \
        -Dsoup2=false
%meson_build

%install
%meson_install

%find_lang %{name}

%post
%systemd_user_post %{systemd_units}

%files -f %{name}.lang
%doc README.md NEWS HACKING.md
%{_bindir}/*
#{_bindir}/gnome-extensions-app
%{_sysconfdir}/xdg/autostart/gnome-shell-overrides-migration.desktop
%{_libdir}/%{name}
%{_libexecdir}/gnome-shell-calendar-server
%{_libexecdir}/gnome-shell-hotplug-sniffer
%{_libexecdir}/gnome-shell-perf-helper
%{_libexecdir}/gnome-shell-portal-helper
%{_libexecdir}/gnome-shell-overrides-migration.sh
%{_datadir}/applications/org.gnome.Shell.desktop
%{_datadir}/applications/evolution-calendar.desktop
%{_datadir}/applications/org.gnome.Extensions.desktop
#{_datadir}/applications/gnome-shell-wayland.desktop
%{_datadir}/applications/org.gnome.Shell.PortalHelper.desktop
%{_datadir}/applications/org.gnome.Shell.Extensions.desktop
%{_datadir}/bash-completion/completions/gnome-extensions
%{_datadir}/dbus-1/services/org.gnome.Shell.PortalHelper.service
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.CalendarServer.service
%{_datadir}/dbus-1/services/org.gnome.Shell.HotplugSniffer.service
%{_datadir}/dbus-1/services/org.gnome.Extensions.service
%{_datadir}/dbus-1/services/org.gnome.Shell.Extensions.service
%{_datadir}/dbus-1/services/org.gnome.Shell.Notifications.service
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Introspect.xml
#{_datadir}/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screencast.xml
%{_datadir}/dbus-1/services/org.gnome.Shell.Screencast.service
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Screenshot.xml
#{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider.xml
%{_datadir}/dbus-1/interfaces/org.gnome.ShellSearchProvider2.xml
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.Extensions.xml
#{_datadir}/dbus-1/services/org.gnome.Shell.Screencast.service
%{_datadir}/dbus-1/services/org.gnome.ScreenSaver.service
#{_datadir}/GConf/gsettings/gnome-shell-overrides.convert
%{_datadir}/glib-2.0/schemas/org.gnome.shell.gschema.xml
%{_datadir}/glib-2.0/schemas/00_org.gnome.shell.gschema.override
%{_datadir}/dbus-1/interfaces/org.gnome.Shell.PadOsd.xml
%{_datadir}/gnome-control-center/keybindings/*%{name}*.xml
%{_datadir}/%{name}
%{_mandir}/man1/%{name}.1*
%{_mandir}/man1/gnome-extensions.1*
%{_datadir}/xdg-desktop-portal/portals/%{name}.portal
%{_userunitdir}/org.gnome.Shell-disable-extensions.service
%{_userunitdir}/org.gnome.Shell.target
%{_userunitdir}/org.gnome.Shell@wayland.service
%{_userunitdir}/org.gnome.Shell@x11.service

%{_datadir}/icons/hicolor/scalable/apps/org.gnome.Extensions*
%{_iconsdir}/hicolor/scalable/apps/org.gnome.Shell.Extensions.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Extensions-symbolic.svg
%{_iconsdir}/hicolor/symbolic/apps/org.gnome.Shell.Extensions-symbolic.svg
%{_datadir}/metainfo/org.gnome.Extensions.metainfo.xml

%files docs
%{_datadir}/gtk-doc/html/shell
%{_datadir}/gtk-doc/html/st
